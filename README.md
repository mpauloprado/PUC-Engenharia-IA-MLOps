# PUC-Engenharia-IA-MLOps

Ambiente de estudo e execução acadêmica para a Pós-graduação em Engenharia de Inteligência Artificial e MLOps da PUC Minas (Oferta 1, Turma 1).

## Ambiente de uso
Este projeto é usado como um Project do Claude Cowork vinculado a esta pasta local.

- `CLAUDE.md` e `.claude/rules/` são a base documental de instruções do projeto.
- Neste projeto Cowork, os arquivos de `.claude/skills/` e `.claude/agents/` são playbooks e referências especializadas, usados quando forem úteis.
- Não presuma que skills ou agentes aparecem como slash commands nativos no Cowork.
- Não oriente o uso de `/inspect-document` se esse comando não estiver disponível na interface atual.
- A inspeção documental pode ser feita seguindo o procedimento de `.claude/skills/inspect-document/SKILL.md` e/ou executando `tools/document_forensics.py`.

## Como usar
1. Leia `CLAUDE.md` e `.claude/rules/`.
2. Consulte `00_ADMIN/PENDENCIAS.md`, `00_ADMIN/CALENDARIO_ACADEMICO.md` e `00_ADMIN/PROGRESSO_GERAL.md`.
3. Coloque materiais originais de cada disciplina em `disciplinas/<disciplina>/00_original/`.
4. Nunca edite, mova ou renomeie o material original.
5. Produza notas em `02_notas/`, atividades em `03_atividades/`, laboratórios em `04_labs/` e revisões em `05_revisao/`.
6. Mantenha progresso, pendências e `00_ADMIN/MANIFESTO_ARQUIVOS.md` atualizados.

## Estrutura
- `00_ADMIN/`: matriz, calendário, progresso, pendências, manifesto e evidências administrativas.
- `01_FONTES/`: fontes oficiais (incluindo as fontes canônicas do curso) e referências.
- `disciplinas/`: conteúdo separado por disciplina.
- `conhecimento/`: base transversal e consolidada.
- `provas/`: simulados, revisões e banco de questões.
- `tools/`: ferramentas locais, como `document_forensics.py`.
- `.claude/rules/`: regras operacionais.
- `.claude/agents/` e `.claude/skills/`: playbooks especializados.

## Playbooks disponíveis
Procedimentos descritos em `.claude/skills/`, que podem ser pedidos pelo nome na conversa:
- `ingest-material`: classificar novos materiais;
- `study-session`: conduzir uma sessão de estudo;
- `review-activity`: revisar uma entrega;
- `exam-prep`: preparar revisão ou simulado;
- `weekly-review`: consolidar a semana;
- `inspect-document`: triagem defensiva de documentos.

## Vocabulários de status
O projeto usa duas escalas diferentes, que não se contradizem:
- status epistemológico (CLAUDE.md): CONFIRMADO / PROVÁVEL / HIPÓTESE / NÃO CONFIRMADO / DIVERGENTE. Indica quanto uma informação está comprovada.
- severidade forense (inspeção documental): informativo / atenção / suspeito / confirmado. Indica o grau de preocupação com um achado técnico em um documento.

## Regra de ouro
Se uma informação não estiver confirmada, registre a lacuna em vez de assumir.
