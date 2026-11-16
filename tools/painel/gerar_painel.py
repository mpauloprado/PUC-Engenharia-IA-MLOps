#!/usr/bin/env python3
"""
Gera 00_ADMIN/painel/painel.html — painel de acompanhamento do curso.

Fontes (somente leitura):
- 00_ADMIN/canvas/PRAZOS.md        atividades, disciplina, link e situação [CANVAS]
- 00_ADMIN/canvas/estado.json      avisos e materiais baixados
- 00_ADMIN/canvas/NOVIDADES.md     itens inspecionados [x] / pendentes [ ]
- disciplinas/*/03_atividades/enunciado/*.md   checklists "- [ ]" / "- [x]" (progresso)
- ~/.config/puc-sync/canvas_token_expira, ~/.config/rclone/gdrive-auth-date (se existirem)

Saída determinística (sem horário de geração): contagens regressivas são calculadas no
navegador, então o arquivo só muda quando os dados mudam. Sem recursos externos.

Uso: python3 tools/painel/gerar_painel.py
"""
from __future__ import annotations
import json, re, html, os
from pathlib import Path
from datetime import datetime, timedelta

RAIZ = Path(__file__).resolve().parents[2]
CANVAS = RAIZ / "00_ADMIN" / "canvas"
SAIDA = RAIZ / "00_ADMIN" / "painel" / "painel.html"

ABREV = {
    "Pipeline de Dados: Integração, Qualidade e Automação": "Pipeline de Dados",
    "Cloud Computing para IA e Ciência de Dados": "Cloud Computing",
    "Conteinerização e Orquestração com Kubernetes": "Kubernetes",
    "Orquestração de Workflows": "Orquestração de Workflows",
    "Espaço Coordenação": "Coordenação",
}
PASTA_NOME = {
    "01_pipeline_dados": "Pipeline de Dados",
    "02_cloud_computing": "Cloud Computing",
    "03_kubernetes": "Kubernetes",
    "06_orquestracao_workflows": "Orquestração de Workflows",
    "00_ADMIN": "Coordenação",
}


def br_para_iso(s: str) -> str | None:
    m = re.match(r"(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})", s.strip())
    if not m:
        return None
    d, mo, a, h, mi = m.groups()
    return f"{a}-{mo}-{d}T{h}:{mi}:00-03:00"


def atividades():
    out = []
    txt = (CANVAS / "PRAZOS.md").read_text(encoding="utf-8")
    secao = txt.split("## Atividades", 1)[1].split("## ", 1)[0]
    for linha in secao.splitlines():
        cols = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cols) != 4 or cols[0] in ("Prazo", "---"):
            continue
        prazo, curso, ativ, situ = cols
        m = re.match(r"\[(.*)\]\((.*)\)", ativ)
        nome, url = (m.group(1), m.group(2)) if m else (ativ, "")
        out.append({
            "prazo": br_para_iso(prazo), "disciplina": ABREV.get(curso, curso), "nome": nome, "url": url,
            "entregue": "entregue" in situ, "encerrada": "encerrado" in situ,
        })
    return out


GENERICOS = ("requisitos", "checklist", "opcionais", "entrega", "contexto", "materiais")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"^\d+\.\s*", "", s)).strip().lower()


def checklists(ativs):
    """Conta "- [ ]"/"- [x]" dos enunciados derivados e associa à atividade do Canvas pelo nome.
    Itens sob um "## Opcionais" contam à parte."""
    prog = {}
    for arq in sorted(RAIZ.glob("disciplinas/*/03_atividades/enunciado/*.md")):
        h1 = h2 = ""
        opcional = False
        for l in arq.read_text(encoding="utf-8").splitlines():
            if l.startswith("# "):
                h1 = l[2:].strip()
            elif l.startswith("## "):
                t = l[3:].strip()
                opcional = t.lower().startswith("opcionais")
                if not t.lower().startswith(GENERICOS):
                    h2 = t
            m = re.match(r"- \[( |x|X)\] ", l)
            if not m:
                continue
            titulo = h2 or h1
            p = prog.setdefault((str(arq.relative_to(RAIZ)), titulo),
                                {"arquivo": str(arq.relative_to(RAIZ)), "titulo": titulo, "h1": h1,
                                 "feitos": 0, "total": 0, "opc_feitos": 0, "opc_total": 0})
            k = "opc_" if opcional else ""
            p[k + "total"] += 1
            if m.group(1) != " ":
                p[k + "feitos"] += 1
    for p in prog.values():
        alvo = norm(p["titulo"]) + " | " + norm(p["h1"])
        for a in ativs:
            if norm(a["nome"]) in alvo:
                a["checklist"] = {k: p[k] for k in ("arquivo", "feitos", "total", "opc_feitos", "opc_total")}
                break
    return list(prog.values())


def novidades():
    txt = (CANVAS / "NOVIDADES.md").read_text(encoding="utf-8")
    pend, feitos = {}, {}
    for l in txt.splitlines():
        m = re.match(r"- \[( |x)\] \*\*(.+?)\*\* — (.+?):", l)
        if not m:
            continue
        disc = ABREV.get(m.group(3), m.group(3))
        alvo = pend if m.group(1) == " " else feitos
        alvo[disc] = alvo.get(disc, 0) + 1
    ult = re.findall(r"### Sincronização de (\d{2}/\d{2}/\d{4} \d{2}:\d{2})", txt)
    return pend, feitos, (br_para_iso(ult[0]) if ult else None)


def estado():
    e = json.loads((CANVAS / "estado.json").read_text(encoding="utf-8"))
    mats = {}
    for f in e.get("arquivos", {}).values():
        partes = f.get("caminho", "").split("/")
        chave = partes[1] if partes[0] == "disciplinas" and len(partes) > 1 else partes[0]
        if chave not in PASTA_NOME:
            continue  # arquivos fora das pastas mapeadas (ex.: 01_FONTES) não entram no painel
        nome = PASTA_NOME[chave]
        mats[nome] = mats.get(nome, 0) + 1
    avisos = sorted(({"titulo": a.get("titulo"), "data": a.get("data"), "curso": ABREV.get(a.get("curso"), a.get("curso")),
                      "url": a.get("url")} for a in e.get("avisos", {}).values()),
                    key=lambda x: x["data"] or "", reverse=True)[:6]
    return mats, avisos, len(e.get("paginas", {}))


def sistema():
    s = {}
    p = Path.home() / ".config/puc-sync/canvas_token_expira"
    if p.exists():
        s["canvas_token"] = p.read_text().strip()[:10]
    p = Path.home() / ".config/rclone/gdrive-auth-date"
    if p.exists():
        try:
            d = datetime.fromisoformat(p.read_text().strip()[:10])
            s["gdrive"] = (d + timedelta(days=7)).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return s


def main():
    pend, feitos, ult_sync = novidades()
    mats, avisos, paginas = estado()
    ativs = atividades()
    checklists(ativs)
    dados = {
        "atividades": ativs, "novidades_pend": pend, "novidades_ok": feitos,
        "ultima_novidade": ult_sync, "materiais": mats, "paginas": paginas, "avisos": avisos, "sistema": sistema(),
    }
    tpl = (Path(__file__).parent / "template.html").read_text(encoding="utf-8")
    js = json.dumps(dados, ensure_ascii=False, sort_keys=True).replace("</", "<\\/")
    out = tpl.replace("/*__DADOS__*/null", js)
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != out:
        SAIDA.write_text(out, encoding="utf-8")
        print(f"painel atualizado: {SAIDA.relative_to(RAIZ)}")
    else:
        print("painel sem mudanças")


if __name__ == "__main__":
    main()
