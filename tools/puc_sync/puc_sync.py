#!/usr/bin/env python3
"""puc-sync: sincroniza o Canvas da PUC Minas com o projeto (somente leitura no Canvas).

O que faz:
- baixa arquivos novos dos módulos (e da aba Arquivos, quando liberada) para
  <pasta da disciplina>/00_original/canvas/<módulo>/;
- salva páginas do Canvas (HTML original) no mesmo lugar;
- não duplica arquivos que já existam em 00_original (comparação por SHA-256);
- nunca sobrescreve: se o professor alterar um arquivo ou página, salva uma nova versão datada;
- gera 00_ADMIN/canvas/PRAZOS.md, AVISOS.md e NOVIDADES.md;
- registra tudo em 00_ADMIN/canvas/estado.json.

Uso:
  python3 tools/puc_sync/puc_sync.py            # sincroniza
  python3 tools/puc_sync/puc_sync.py --dry-run  # só mostra o que faria
  python3 tools/puc_sync/puc_sync.py --listar-cursos

O token do Canvas NUNCA fica no repositório (ver config.json).
"""
import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CFG = json.loads((Path(__file__).parent / "config.json").read_text(encoding="utf-8"))
SAIDA = RAIZ / "00_ADMIN" / "canvas"
ESTADO_ARQ = SAIDA / "estado.json"
TZ = dt.timezone(dt.timedelta(hours=-3))  # horário de Brasília
AGORA = dt.datetime.now(TZ)


class TokenInvalido(Exception):
    pass


def ler(p):
    return Path(os.path.expanduser(p)).read_text().strip()


BASE = ler(CFG["canvas_base_url_arquivo"]).rstrip("/")
TOKEN = ler(CFG["canvas_token_arquivo"])


# ---------------------------------------------------------------- Canvas API
def requisicao(url, bruto=False):
    if url.startswith("/"):
        url = BASE + url
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + TOKEN,
                                               "User-Agent": "puc-sync/1.0"})
    for tentativa in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                corpo = r.read()
                link = r.headers.get("Link", "")
                return (corpo if bruto else json.loads(corpo)), link
        except urllib.error.HTTPError as e:
            if e.code == 401:
                raise TokenInvalido()
            if e.code in (403, 404):
                return None, ""
            if e.code in (429, 500, 502, 503) and tentativa < 2:
                time.sleep(5 * (tentativa + 1))
                continue
            raise
        except urllib.error.URLError:
            if tentativa < 2:
                time.sleep(5)
                continue
            raise


def paginado(caminho):
    url, itens = caminho, []
    while url:
        dados, link = requisicao(url)
        if dados is None:
            return None
        itens.extend(dados if isinstance(dados, list) else [dados])
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    return itens


# ---------------------------------------------------------------- utilidades
PROIBIDOS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
SUFIXO_TURMA = re.compile(r"_?\s*\[IEC_[^\]]*\].*?(?=\.[A-Za-z0-9]{2,5}$|$)")


def nome_seguro(nome, limite=90):
    """Nome válido no Windows e no Linux, sem o sufixo longo da turma e com tamanho limitado
    (no Windows o prefixo G:\\Meu Drive\\... já consome boa parte dos 260 caracteres)."""
    nome = SUFIXO_TURMA.sub("", nome).strip()
    nome = PROIBIDOS.sub("_", nome).strip(" .") or "sem_nome"
    if len(nome) > limite:
        base, ext = os.path.splitext(nome)
        nome = base[: limite - len(ext)].rstrip(" ._") + ext
    return nome


def sha256(dados):
    return hashlib.sha256(dados).hexdigest()


def sha256_arquivo(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def destino_livre(p: Path):
    """Nunca sobrescreve: se já existe, acrescenta a data."""
    if not p.exists():
        return p
    carimbo = AGORA.strftime("%Y-%m-%d_%H%M")
    return p.with_name(f"{p.stem} (versao {carimbo}){p.suffix}")


def fmt_data(iso):
    if not iso:
        return "sem data"
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(TZ)
    return d.strftime("%d/%m/%Y %H:%M")


def texto_html(h, limite=600):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h or "", flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= limite else t[:limite].rstrip() + "…"


# ---------------------------------------------------------------- sincronização
class Sync:
    def __init__(self, dry):
        self.dry = dry
        self.estado = json.loads(ESTADO_ARQ.read_text(encoding="utf-8")) if ESTADO_ARQ.exists() else {
            "arquivos": {}, "paginas": {}, "avisos": {}, "atividades": {}}
        self.novidades = []
        self.hashes_locais = {}

    # ---- índice de hashes de TODO o projeto (evita duplicar o que já foi baixado à mão, em qualquer pasta)
    def hashes_de(self, _pasta=None):
        if not self.hashes_locais:
            for p in RAIZ.rglob("*"):
                if p.is_file() and ".git" not in p.parts and p.name != ".gitkeep":
                    self.hashes_locais.setdefault(sha256_arquivo(p), p)
        return self.hashes_locais

    def novidade(self, curso, tipo, titulo, detalhe=""):
        self.novidades.append({"quando": AGORA.isoformat(timespec="minutes"), "curso": curso,
                               "tipo": tipo, "titulo": titulo, "detalhe": detalhe})
        print(f"  [{tipo}] {titulo} {detalhe}")

    # ---- arquivo
    def arquivo(self, cid, cfg, file_id, modulo):
        meta, _ = requisicao(f"/api/v1/courses/{cid}/files/{file_id}")
        if not meta:
            meta, _ = requisicao(f"/api/v1/files/{file_id}")
        if not meta or meta.get("locked_for_user"):
            return
        chave = str(file_id)
        anterior = self.estado["arquivos"].get(chave)
        if anterior and anterior.get("updated_at") == meta.get("updated_at"):
            return  # sem alteração
        nome = meta.get("display_name") or meta.get("filename") or f"arquivo_{file_id}"
        mb = (meta.get("size") or 0) / 1e6
        if mb > CFG["tamanho_maximo_mb"]:
            if not anterior:
                self.novidade(cfg["nome"], "ARQUIVO GRANDE (não baixado)", nome,
                              f"{mb:.0f} MB — {BASE}/courses/{cid}/files/{file_id}")
                self.estado["arquivos"][chave] = {"nome": nome, "updated_at": meta.get("updated_at"),
                                                  "grande": True}
            return
        if self.dry:
            print(f"  (dry-run) baixaria: {modulo}/{nome} ({mb:.1f} MB)")
            return
        dados, _ = requisicao(meta["url"], bruto=True)
        if dados is None:
            return
        h = sha256(dados)
        existente = self.hashes_de(cfg["pasta"]).get(h)
        if existente:
            rel = existente.relative_to(RAIZ).as_posix()
            self.estado["arquivos"][chave] = {"nome": nome, "updated_at": meta.get("updated_at"),
                                              "sha256": h, "caminho": rel, "ja_existia": True}
            return
        pasta = RAIZ / cfg["pasta"] / "00_original" / "canvas" / nome_seguro(modulo, 50)
        pasta.mkdir(parents=True, exist_ok=True)
        dest = destino_livre(pasta / nome_seguro(nome))
        dest.write_bytes(dados)
        self.hashes_de(cfg["pasta"])[h] = dest
        rel = dest.relative_to(RAIZ).as_posix()
        self.estado["arquivos"][chave] = {"nome": nome, "updated_at": meta.get("updated_at"),
                                          "sha256": h, "caminho": rel, "baixado_em": AGORA.isoformat()}
        tipo = "ARQUIVO ATUALIZADO (nova versão salva)" if anterior else "ARQUIVO NOVO"
        self.novidade(cfg["nome"], tipo, f"`{rel}`", f"sha256 {h[:16]}…")
        time.sleep(0.5)

    # ---- página
    def pagina(self, cid, cfg, url_pagina, modulo):
        p, _ = requisicao(f"/api/v1/courses/{cid}/pages/{url_pagina}")
        if not p or p.get("locked_for_user"):
            return
        corpo = p.get("body") or ""
        h = sha256(corpo.encode())
        chave = f"{cid}:{url_pagina}"
        anterior = self.estado["paginas"].get(chave)
        if anterior and anterior.get("sha256") == h:
            return
        if self.dry:
            print(f"  (dry-run) salvaria página: {modulo}/{p.get('title')}")
            return
        pasta = RAIZ / cfg["pasta"] / "00_original" / "canvas" / nome_seguro(modulo, 50)
        pasta.mkdir(parents=True, exist_ok=True)
        dest = destino_livre(pasta / nome_seguro(f"Página - {p.get('title', url_pagina)}.html"))
        doc = (f"<!-- Origem: {BASE}/courses/{cid}/pages/{url_pagina} | atualizada no Canvas em "
               f"{p.get('updated_at')} | capturada por puc-sync em {AGORA.isoformat()} -->\n"
               f"<meta charset=\"utf-8\"><h1>{html.escape(p.get('title', ''))}</h1>\n{corpo}\n")
        dest.write_text(doc, encoding="utf-8")
        rel = dest.relative_to(RAIZ).as_posix()
        self.estado["paginas"][chave] = {"titulo": p.get("title"), "sha256": h, "caminho": rel}
        tipo = "PÁGINA ALTERADA (nova versão salva)" if anterior else "PÁGINA NOVA"
        self.novidade(cfg["nome"], tipo, f"`{rel}`")
        for fid in set(re.findall(r"/files/(\d+)", corpo)):  # arquivos linkados dentro da página
            self.arquivo(cid, cfg, fid, modulo)

    # ---- curso
    def curso(self, cid, cfg):
        print(f"\n== {cfg['nome']}")
        modulos = paginado(f"/api/v1/courses/{cid}/modules?per_page=100&include[]=items") or []
        for m in modulos:
            nome_mod = f"{m.get('position', 0):02d} - {m.get('name', 'modulo')}"
            for it in m.get("items", []):
                t = it.get("type")
                if t == "File":
                    self.arquivo(cid, cfg, it["content_id"], nome_mod)
                elif t == "Page":
                    self.pagina(cid, cfg, it["page_url"], nome_mod)
                elif t == "ExternalUrl":
                    chave = f"{cid}:url:{it['id']}"
                    if chave not in self.estado["arquivos"]:
                        self.estado["arquivos"][chave] = {"nome": it.get("title"), "url": it.get("external_url")}
                        self.novidade(cfg["nome"], "LINK EXTERNO", it.get("title", ""), it.get("external_url", ""))
        # aba Arquivos, quando o professor deixou liberada
        for f in paginado(f"/api/v1/courses/{cid}/files?per_page=100") or []:
            self.arquivo(cid, cfg, f["id"], "00 - Aba Arquivos")

    # ---- atividades, avisos, calendário
    def atividades(self):
        linhas = []
        for cid, cfg in CFG["cursos"].items():
            for a in paginado(f"/api/v1/courses/{cid}/assignments?per_page=100&include[]=submission") or []:
                sub = a.get("submission") or {}
                entregue = sub.get("workflow_state") in ("submitted", "graded") or bool(sub.get("submitted_at"))
                linhas.append((a.get("due_at") or "9999", cfg["nome"], a))
                chave = str(a["id"])
                anterior = self.estado["atividades"].get(chave)
                if anterior is None:
                    self.novidade(cfg["nome"], "ATIVIDADE NOVA", a.get("name", ""), f"prazo {fmt_data(a.get('due_at'))}")
                elif anterior.get("due_at") != a.get("due_at"):
                    self.novidade(cfg["nome"], "PRAZO ALTERADO", a.get("name", ""),
                                  f"{fmt_data(anterior.get('due_at'))} → {fmt_data(a.get('due_at'))}")
                self.estado["atividades"][chave] = {"nome": a.get("name"), "due_at": a.get("due_at"),
                                                    "entregue": entregue}
        eventos = paginado("/api/v1/calendar_events?type=event&per_page=100&start_date="
                           + (AGORA - dt.timedelta(days=7)).date().isoformat() + "&end_date="
                           + (AGORA + dt.timedelta(days=120)).date().isoformat() + "&"
                           + "&".join(f"context_codes[]=course_{c}" for c in CFG["cursos"])) or []
        return linhas, eventos

    def avisos(self):
        ctx = "&".join(f"context_codes[]=course_{c}" for c in CFG["cursos"])
        lista = paginado(f"/api/v1/announcements?per_page=50&{ctx}&start_date=2026-09-01") or []
        nomes = {f"course_{c}": v["nome"] for c, v in CFG["cursos"].items()}
        for a in lista:
            chave = str(a["id"])
            if chave not in self.estado["avisos"]:
                curso = nomes.get(a.get("context_code"), "?")
                self.estado["avisos"][chave] = {"titulo": a.get("title"), "data": a.get("posted_at"),
                                                "curso": curso, "texto": texto_html(a.get("message"), 1500),
                                                "url": a.get("html_url")}
                self.novidade(curso, "AVISO NOVO", a.get("title", ""), fmt_data(a.get("posted_at")))

    # ---- relatórios
    def escrever(self, linhas, eventos):
        SAIDA.mkdir(parents=True, exist_ok=True)
        cab = (f"> Gerado automaticamente por `tools/puc_sync` em {AGORA.strftime('%d/%m/%Y %H:%M')} "
               f"(horário de Brasília). Fonte: Canvas `[CANVAS]`. Não edite à mão.\n\n")
        # PRAZOS
        out = ["# Prazos e compromissos — Canvas\n", cab, "## Atividades\n",
               "| Prazo | Disciplina | Atividade | Situação |", "|---|---|---|---|"]
        for due, curso, a in sorted(linhas, key=lambda x: x[0]):
            st = self.estado["atividades"][str(a["id"])]
            situ = "✅ entregue" if st["entregue"] else ("⚠️ pendente" if due != "9999" and due >= AGORA.isoformat() else
                                                        ("sem prazo" if due == "9999" else "❌ prazo encerrado, não entregue"))
            out.append(f"| {fmt_data(a.get('due_at'))} | {curso} | [{a.get('name')}]({a.get('html_url')}) | {situ} |")
        out += ["\n## Eventos do calendário (próximos 120 dias)\n", "| Início | Fim | Evento | Local/Link |", "|---|---|---|---|"]
        for e in sorted(eventos, key=lambda x: x.get("start_at") or ""):
            out.append(f"| {fmt_data(e.get('start_at'))} | {fmt_data(e.get('end_at'))} | {e.get('title')} | "
                       f"{e.get('location_name') or ''} {e.get('html_url') or ''} |")
        (SAIDA / "PRAZOS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
        # AVISOS
        out = ["# Avisos do Canvas\n", cab]
        for a in sorted(self.estado["avisos"].values(), key=lambda x: x.get("data") or "", reverse=True):
            out += [f"## {a['titulo']}", f"*{a['curso']} — {fmt_data(a['data'])}* — [abrir no Canvas]({a['url']})\n",
                    a["texto"] + "\n"]
        (SAIDA / "AVISOS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
        # NOVIDADES (acumulativo, mais recentes no topo)
        arq = SAIDA / "NOVIDADES.md"
        antigo = arq.read_text(encoding="utf-8").split("<!-- entradas -->", 1)[1] if arq.exists() else "\n"
        novo = ""
        if self.novidades:
            novo = f"\n### Sincronização de {AGORA.strftime('%d/%m/%Y %H:%M')}\n\n"
            novo += "\n".join(f"- [ ] **{n['tipo']}** — {n['curso']}: {n['titulo']} {n['detalhe']}" for n in self.novidades)
            novo += "\n"
        topo = ("# Novidades do Canvas\n\n"
                "Itens marcados `[ ]` ainda **não foram inspecionados**. Antes de usar um material novo em\n"
                "atividade, rodar `/inspect-document` e `/ingest-material` (regras do projeto) e marcar `[x]`.\n\n"
                "<!-- entradas -->")
        arq.write_text(topo + novo + antigo, encoding="utf-8")
        ESTADO_ARQ.write_text(json.dumps(self.estado, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--listar-cursos", action="store_true")
    a = ap.parse_args()
    try:
        if a.listar_cursos:
            for c in paginado("/api/v1/courses?per_page=100&enrollment_state=active") or []:
                if "name" in c:
                    marca = "MAPEADO " if str(c["id"]) in CFG["cursos"] else (
                        "IGNORADO" if str(c["id"]) in CFG["cursos_ignorados"] else "NOVO!   ")
                    print(f"{marca} {c['id']}  {c['name']}")
            return 0
        s = Sync(a.dry_run)
        for cid, cfg in CFG["cursos"].items():
            s.curso(cid, cfg)
        ativ, ev = s.atividades()
        s.avisos()
        # disciplinas novas no Canvas ainda não mapeadas
        for c in paginado("/api/v1/courses?per_page=100&enrollment_state=active") or []:
            if "name" in c and str(c["id"]) not in CFG["cursos"] and str(c["id"]) not in CFG["cursos_ignorados"]:
                s.novidade(c["name"], "DISCIPLINA NOVA NO CANVAS (mapear em config.json)", str(c["id"]))
        if not a.dry_run:
            s.escrever(ativ, ev)
        print(f"\nRESUMO: {len(s.novidades)} novidade(s)")
        Path(os.path.expanduser("~/.config/puc-sync/ultimo_resumo.json")).write_text(
            json.dumps(s.novidades, ensure_ascii=False))
        return 0
    except TokenInvalido:
        print("ERRO: token do Canvas inválido ou expirado. Rode: renovar-canvas-token", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
