# Status do Projeto

## Fase atual
Fase 1 — Estruturação e ingestão inicial.

## Critério para avançar
Avançar para a Fase 2 quando:
- materiais iniciais de pelo menos uma disciplina estiverem em `00_original/`;
- cronograma mínimo estiver confirmado;
- enunciados disponíveis estiverem preservados;
- pendências críticas estiverem registradas.

## Próxima fase
Fase 2 — Ingestão, classificação e criação de mapa de conhecimento por disciplina.

## Diário de sessões

> Entradas mais recentes no topo. Veja `.claude/rules/multiplas-maquinas.md`.

### 2026-11-15 (noite) — Kali (Claude Code, terminal)
- E-mail PUC (M365): leitura via Microsoft Graph **bloqueada** (exige aprovação do administrador). Pedido de aprovação enviado pelo aluno; aguardando. Encaminhamento para Gmail não testado.
- Triagem forense do material de Kubernetes e Orquestração (32 arquivos): nenhum indício suspeito (`00_ADMIN/RELATORIOS_FORENSES/2026-11-15_lote_canvas_docker_orquestracao.md`). 39 itens marcados `[x]` em `NOVIDADES.md`.
- Baixado o PDF da Atividade 01 de Orquestração (estava só linkado na descrição da atividade).
- Enunciados transcritos com checklist: `03_kubernetes/03_atividades/enunciado/ENUNCIADOS_UNIDADE1_DOCKER.md` e `06_orquestracao_workflows/03_atividades/enunciado/ATIVIDADE_01_AIRFLOW.md`.
- Resumo de revisão + autoteste: `03_kubernetes/05_revisao/RESUMO_UNIDADE1_DOCKER.md`.
- Painel de acompanhamento: `tools/painel/` → `00_ADMIN/painel/painel.html`.
- Ambiente: Docker **não instalado** no Kali; Docker Desktop instalado no Windows, mas parado.
- Próximos passos: estudar para o Teste de Fixação (24/11); Atividade 01 Airflow (25/11); trabalho prático Docker Compose (01/12); decidir onde rodar Docker.

### 2026-11-15 — Kali (Claude Code, terminal)
- Projeto versionado no Git e publicado no GitHub privado (`mpauloprado/PUC-Engenharia-IA-MLOps`).
- Windows: repositório Git em `C:\git\` (fora do Google Drive); `core.longpaths` ativado.
- Kali: clone em `~/projetos/`; acesso ao Drive via rclone; SSH Kali→Windows por chave.
- `.gitignore` ampliado (inclui anotações com credenciais de laboratório) e `.gitattributes` criado.
- Próximos passos: montagem automática do Drive no Kali; credencial própria do rclone (Google Cloud).
