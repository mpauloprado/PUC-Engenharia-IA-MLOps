# Atividade 01 — Airflow (Orquestração de Workflows)

> Fonte: `00_original/canvas/09 - ATIVIDADES AVALIATIVAS/Atividade 01 - Descrição.pdf`
> (SHA-256 `01124f99…20f5e`, baixado da descrição da atividade no Canvas em 15/11/2026) `[PUC-ATIVIDADE]`.

| Campo | Valor |
|---|---|
| Prazo | 25/11/2026 23:59 (fecha 25/11 23:59 BRT) `[CANVAS]` |
| Pontos | 10 |
| Entrega | texto online ou URL |
| Escopo | temas dos Encontros 01 e 02 |
| Link | https://pucminas.instructure.com/courses/279171/assignments/1472100 |

## Contexto

Tech lead do time de dados da **ShopBrasil** (marketplace). Painel diário de preços por categoria (preço médio, mínimo, máximo e quantidade de produtos) alimentado hoje por script Python via cron que: falha silenciosamente quando a API oscila; duplica dados ao ser rodado de novo; exige editar código a cada nova categoria.

Missão: pipeline no **Apache Airflow** que colete produtos da **FakeStore API** (https://fakestoreapi.com/docs), calcule métricas por categoria e grave em **PostgreSQL**.

## Requisitos obrigatórios (checklist)

- [x] Roda todo dia às **06:00 America/Sao_Paulo** (`pendulum`), com `start_date` e `catchup=False`
- [x] **TaskFlow API** (`@dag`/`@task`); dependências pela chamada das funções
- [x] XComs automáticos via `return` (só dados pequenos)
- [x] Topologias identificáveis: **linear**, **fan-out** (mapeamento por categoria) e **fan-in** (consolidação)
- [x] Task "Buscar Produtos" com **retry + exponential backoff**
- [x] `try/except` + `raise` para acionar o retry
- [x] Callbacks na task crítica: `on_failure_callback`, `on_retry_callback`, `on_success_callback`
- [x] Métricas por categoria com **Dynamic Task Mapping** (`.expand(...)`)
- [x] **Pool `ecommerce_pool` com 2 slots** limitando as tasks mapeadas
- [x] **≥ 2 TaskGroups** (ex.: ingestão e análise)
- [x] Task de persistência com **PostgresHook** + **Connection** do Airflow
- [x] Gravação **idempotente**: re-rodar a mesma run não duplica linhas

## Opcionais

- [x] `ValidarProdutosOperator(BaseOperator)` validando schema dos produtos
- [x] 2ª tabela de histórico em **append** com data da execução
- [x] SLA ou `on_failure_callback` simulando alerta

## Entrega

- Repositório (GitHub/GitLab) com **acesso de visualização liberado**
- Todo o pipeline em projeto **dockerizado**
- Postar o link no Canvas

## Materiais relacionados

- `00_original/Encontro 01 - Orquestração de Workflow.pdf`
- `00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/Encontro 02 - Orquestração de Workflow.pdf`
- `00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/lab-airflow-11-01-2026.zip`
- `00_original/lab_01-airflow/`

## Revisão final (20/11/2026)

- Enunciado original relido. Canvas: entrega por texto ou URL, 10 pts, prazo 25/11 23:59; sem orientação extra do professor nos avisos ou na Inbox `[CANVAS]`.
- Projeto simplificado no estilo dos DAGs do lab do professor, mantendo todos os requisitos: sem tabela de alertas (o alerta simulado vai para o log), sem SLA, operador e callbacks mais curtos, README mais direto.
- Reprodução: logs em volume nomeado (sem precisar de `.env`/`AIRFLOW_UID` no Linux) e sem publicar a porta 5433, que conflitava com o lab da disciplina.
- Histórico do repositório: um commit único, sem a linha `Co-Authored-By` (branch local `entrega`; o histórico antigo está guardado na branch local `backup-antes-revisao`).
- Testado num clone limpo, só com `docker compose up -d` e sem `.env` (Kali, Docker 28.5.2):
  - init cria usuário, Connection e Pool `ecommerce_pool` (2 slots); 0 erros de importação;
  - run agendada automática com sucesso: 4 categorias, 4 tasks mapeadas;
  - `pytest`: 4 passed;
  - Clear da mesma run: continua com 4 linhas no snapshot e 4 no histórico;
  - API fora do ar: 5 tentativas, retries com espera crescente, `[ALERTA SIMULADO]` no fim, demais tasks em `upstream_failed`;
  - run manual depois disso com sucesso: snapshot com 4 linhas; histórico com +4 linhas (append).
- Ajuste depois do teste: no texto do retry, o número da tentativa foi corrigido (`try_number - 1`). Só checagem de sintaxe, sem nova execução.
- Publicado em 20/11/2026 (force push, commit `fe73dee`). Clone anônimo pelo HTTPS idêntico ao local (mesma árvore `04042f33`).
- Pendente: postar o link https://github.com/mpauloprado/shopbrasil-airflow na Atividade 01 do Canvas.

## Status da implementação (16/11/2026)

- Código: https://github.com/mpauloprado/shopbrasil-airflow (público, publicado em 17/11/2026). No projeto: submódulo em `../entrega/shopbrasil-airflow/` (rodar no Kali; no Windows só leitura, pois a pasta fica no Google Drive).
- Base técnica igual ao lab da disciplina: Airflow 2.9.3, Python 3.11, provider Postgres 5.11.0, PostgreSQL 16.
- Evidências de execução real no Kali (Docker 28.5.2):
  - 6 testes (pytest) passando: integridade do DAG, agendamento, topologia, retries, pool e operador.
  - Run completa com sucesso: 4 categorias mapeadas, snapshot em `metricas_categoria` (data_referencia 2026-11-16).
  - Idempotência: run agendada + run manual + clear da mesma run → snapshot com 4 linhas; histórico com 4 linhas por run, sem duplicar.
  - API fora do ar (`fakestore_base_url` inválida): 4 retries com intervalos crescentes (~52s, 72s, 182s, 331s), alertas `RETRY` e `FALHA` gravados em `alertas_pipeline`; tasks seguintes em `upstream_failed`, nada gravado.
- Run agendada real em 17/11/2026 06:00: sucesso, 4 categorias gravadas (data_referencia 2026-11-17).
- Pendente: postar o link do repositório na Atividade 01 do Canvas.
