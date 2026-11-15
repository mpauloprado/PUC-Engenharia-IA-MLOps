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
