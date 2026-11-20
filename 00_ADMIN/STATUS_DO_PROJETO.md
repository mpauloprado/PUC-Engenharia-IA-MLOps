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

### 2026-11-20 — Kali (Claude Code, aba Code do app)
- Atividade 01 Airflow revisada contra o enunciado, simplificada (estilo dos DAGs do lab do professor) e republicada com commit único sem assinatura de IA (force push; backup local na branch `backup-antes-revisao` do submódulo). Testada em clone limpo: subida, run automática, pytest, idempotência e API fora do ar. Detalhes em `06_orquestracao_workflows/03_atividades/enunciado/ATIVIDADE_01_AIRFLOW.md`.
- Encontrado no Canvas o enunciado do Projeto Final de Orquestração (`TRABALHO_FINAL_ORQUESTRACAO.pdf`, 50 pts, com pitch em vídeo); prazo ainda não publicado.
- Ambiente: usuário `kali` adicionado ao grupo `docker` (vale após logout/login). Até lá, `sg docker -c "..."` roda Docker sem senha.
- E-mail M365: a API do Canvas não cobre o e-mail institucional; pedido de consentimento do admin segue pendente (ver `PENDENCIAS.md`).
- Próximos passos: postar o link da Atividade 01 no Canvas (até 25/11); Teste de Fixação Docker (24/11); testar frontend e postar link do trabalho Docker (01/12).

### 2026-11-18 (noite) — Kali (Claude Code, aba Code do app)
- Retomada do contexto. Registro tardio de 16–17/11: Atividade 01 Airflow (`shopbrasil-airflow`) e trabalho Docker Compose (`guess_game`) publicados no GitHub e ligados como submódulos; falta postar os links no Canvas e testar o frontend do guess_game no navegador.
- Aula 2 de Orquestração: `lab-airflow-Alunos.zip` (chegou pelo puc-sync em 18/11) extraído como cópia de trabalho em `06_orquestracao_workflows/04_labs/lab-airflow-Alunos/` (`logs/` fora do Git) e rodando no Kali: 6 containers, 8 DAGs, 0 erros de importação.
- Passo a passo para estudo: `06_orquestracao_workflows/04_labs/PASSO_A_PASSO_LAB_AIRFLOW_ALUNOS.md`.
- Decisão: `shopbrasil-airflow` **pausado** (`docker compose -p shopbrasil-airflow stop`) por conflito de portas 8080/5433. Religar com `start` após a aula (sem ele, a run diária das 06:00 não acontece).
- Observação: no Drive foi extraído o zip **antigo** (`lab-airflow-11-01-2026`) dentro de `00_original/`; tirar de lá no Windows.
- Pendente: inspeção formal (`/inspect-document`) de `Modulo 02 - Orquestração de Workflow.pdf` e do zip do lab; itens seguem `[ ]` em `NOVIDADES.md`.
- Próximos passos: Teste de Fixação Docker (24/11); postar link da Atividade 01 (25/11); testar frontend e postar link do trabalho Docker (01/12).

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
