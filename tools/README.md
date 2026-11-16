# Ferramentas locais

## document_forensics.py
Triagem defensiva de documentos acadêmicos.

Exemplo:
```bash
python tools/document_forensics.py "caminho/arquivo.pdf"
```

Gerar JSON:
```bash
python tools/document_forensics.py "caminho/arquivo.pdf" --json-out "relatorio.json"
```

### O que verifica
- SHA-256;
- metadados;
- indicadores estruturais de PDF;
- links;
- texto minúsculo/branco/fora de página quando PyMuPDF estiver disponível;
- prompt injection e Unicode invisível;
- macros/custom XML/comentários e alguns itens ocultos em Office;
- dados após IEND/EOI em PNG/JPEG;
- metadados de imagem quando Pillow estiver disponível.

### Limite
Não existe teste universal que prove ausência de esteganografia.
A ferramenta é uma triagem e deve ser combinada com inspeção visual e,
quando houver suspeita real, ferramentas forenses especializadas.

## puc_sync/ — sincronização com o Canvas

Baixa materiais, atividades, prazos e avisos do Canvas (somente leitura). Detalhes e
regras de uso: `.claude/rules/canvas-sync.md`.

```bash
python3 tools/puc_sync/puc_sync.py --listar-cursos   # cursos e mapeamento
python3 tools/puc_sync/puc_sync.py --dry-run         # simula
python3 tools/puc_sync/puc_sync.py                   # sincroniza
```

Automação (Kali): `~/.local/bin/puc-sync` + `puc-sync.timer` (scripts versionados em `ambiente-claude`).
O token fica em `~/.config/puc-sync/` (fora do repositório).

## painel/ — painel de acompanhamento

Gera `00_ADMIN/painel/painel.html` (HTML único, sem dependências externas, tema claro/escuro):
próxima entrega com contagem regressiva, pendentes, progresso pelos checklists de
`disciplinas/*/03_atividades/enunciado/*.md`, materiais por disciplina, itens a inspecionar,
avisos e validade dos tokens.

```bash
python3 tools/painel/gerar_painel.py
```

- Regenerado automaticamente pelo `puc-sync` a cada sincronização.
- Kali: `puc-painel` (ou "Painel PUC" no menu) regenera e abre.
- Windows: abrir `00_ADMIN\painel\painel.html` na pasta do projeto (atualiza com o `git pull`).
- Para o progresso aparecer, marque `- [x]` nos checklists dos enunciados.
