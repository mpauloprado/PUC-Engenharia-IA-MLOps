# Configuração do Claude Code

## rules/
Regras persistentes ou contextuais do projeto.

## agents/
Subagentes especializados. Os arquivos usam frontmatter YAML com `name` e `description`, conforme a estrutura esperada pelo Claude Code.

## skills/
Fluxos reutilizáveis invocáveis diretamente:
- `/ingest-material`
- `/study-session`
- `/review-activity`
- `/exam-prep`
- `/weekly-review`
- `/inspect-document` — triagem defensiva de documentos e prompt injection

Os fluxos acadêmicos mais longos ficam em skills para evitar aumentar desnecessariamente o `CLAUDE.md`.
