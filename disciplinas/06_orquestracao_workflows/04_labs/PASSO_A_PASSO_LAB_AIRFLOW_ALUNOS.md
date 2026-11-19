# Passo a passo — subir o `lab-airflow-Alunos` (Aula 2 de Orquestração de Workflows)

> Executado no Kali em 18/11/2026, durante a aula. Fonte do lab:
> `00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/lab-airflow-Alunos.zip`
> (SHA-256 `c6b96ee247634a014be870aabd285cdb75bfc0c090359cf0856f820fc56039ac`) `[PUC-AULA]`.
> Os comentários do `docker-compose.yml` do professor são a melhor leitura complementar:
> eles explicam cada serviço linha a linha.

## Visão geral: o que sobe

| Container | Papel | Porta no seu PC |
|---|---|---|
| `airflow-meta-db` (postgres-meta) | Banco **interno** do Airflow (runs, estados, XComs, usuários, connections) | não exposta |
| `airflow-lab-db` (postgres-lab) | Banco **de destino** do ETL (tabelas `clima`, `etl_log`) | 5433 |
| `airflow-init` | Roda uma vez: `db migrate`, cria usuário admin e a connection `postgres_lab`. Termina com `Exited (0)` | — |
| `airflow-scheduler` | O "cérebro": lê `./dags`, agenda e executa tasks (LocalExecutor) | — |
| `airflow-webserver` | Interface web | 8080 |
| `fake-api` | API instável (FastAPI) para estudar retries | 5001 |

---

## Passo 0 — Não trabalhar em cima do original

Arquivo em `00_original/` é fonte primária: não se descompacta por cima nem se roda lá dentro
(o Airflow escreveria `logs/` no meio do material do professor). Extraí uma **cópia de trabalho**:

```bash
cd disciplinas/06_orquestracao_workflows/04_labs
unzip "../00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/lab-airflow-Alunos.zip" -d .
cd lab-airflow-Alunos
```

Para conferir o que tem no zip antes de extrair: `unzip -l arquivo.zip`.

> Curiosidade: o zip traz uma pasta chamada literalmente `{dags,scripts,sql}`. É resto de um
> `mkdir {dags,scripts,sql}` rodado num shell sem *brace expansion* (ex.: `sh` ou PowerShell).
> Pode ignorar.

## Passo 1 — Inspeção rápida (segurança)

Antes de rodar código de terceiros, li o `docker-compose.yml`, o `Dockerfile` e o `app.py` da
fake-api e procurei chamadas perigosas (`subprocess`, `os.system`, `eval`, downloads) e Unicode
invisível. **Nenhum indício encontrado pelos testes executados.**

## Passo 2 — Verificar pré-requisitos e conflitos de porta

```bash
docker ps -a            # o que já está rodando?
ss -ltnp | grep 8080    # quem está usando a porta 8080?
```

**Problema real encontrado:** o meu projeto `shopbrasil-airflow` (Atividade 01) estava no ar
usando as portas **8080** e **5433**, as mesmas do lab. Dois containers não podem publicar a
mesma porta do host → o `up` falharia com `port is already allocated`.

Duas saídas possíveis:
1. Pausar o outro projeto (escolhida — mantém o lab idêntico ao da aula):
   ```bash
   docker compose -p shopbrasil-airflow stop     # para, mas NÃO apaga containers nem volumes
   ```
2. Mudar a porta do lado do host no compose do lab (ex.: `"8081:8080"`). Só o número da
   **esquerda** muda; o da direita é a porta dentro do container.

`stop` ≠ `down`: `stop` só para os containers; `down` remove containers e rede (volumes
continuam, a não ser com `-v`).

> **No Kali o meu usuário não está no grupo `docker`**, por isso cada comando foi rodado com
> `sudo docker ...`. (Alternativa permanente: `sudo usermod -aG docker $USER` + novo login.)

## Passo 3 — Preparar a pasta de logs (Linux)

```bash
mkdir -p logs && chmod -R 777 logs
```

Por quê: dentro do container o Airflow roda como o usuário `airflow` (UID 50000), que não é o
seu usuário do Kali. Como `./logs` é um *bind mount*, sem permissão de escrita as tasks falham
ao gravar log. No Windows/Docker Desktop isso não é necessário.

Também criei um `.gitignore` com `logs/` dentro da cópia, para os logs não irem para o Git.

## Passo 4 — Validar e subir

```bash
docker compose config --quiet    # valida a sintaxe do YAML (sem saída = OK)
docker compose up -d             # sobe tudo em segundo plano
```

O que acontece, em ordem (graças aos `depends_on` + `healthcheck`):
1. sobem `postgres-meta`, `postgres-lab` e `fake-api` (esta é *buildada* a partir de `./fake-api`);
2. quando `postgres-meta` fica **healthy**, sobem `scheduler` e `webserver`;
3. quando os **dois** bancos ficam healthy, roda o `airflow-init`;
4. na primeira subida, cada container do Airflow instala os pacotes de
   `_PIP_ADDITIONAL_REQUIREMENTS` (provider Postgres, pandas, requests) — por isso demora.

## Passo 5 — Acompanhar até ficar pronto

```bash
docker compose ps                     # esperar (healthy) no scheduler e webserver
docker compose logs -f airflow-init   # ver o init terminar (Ctrl+C sai)
curl http://localhost:8080/health     # webserver respondendo
```

O `airflow-init` aparecer como `Exited (0)` é o **esperado**: ele termina depois de preparar tudo.

**Resultado observado (18/11/2026, ~20h, Kali, Docker 28.5.2):**
- `airflow-init` → `Exited (0)`, com as mensagens `Successfully added conn_id=postgres_lab` e
  `=== Airflow inicializado ===`;
- bancos `healthy` em menos de 1 min; webserver respondendo em ~3 min (tempo gasto no `pip install`);
- `/health`: `metadatabase: healthy`, `scheduler: healthy` (`triggerer`/`dag_processor` nulos
  porque esses componentes não existem neste compose — normal);
- API REST (`curl -u admin:admin http://localhost:8080/api/v1/dags`): **8 DAGs carregadas,
  0 erros de importação** (`/api/v1/importErrors`);
- fake-api respondendo em `http://localhost:5001/reset`.

## Passo 6 — Usar

| O quê | Onde |
|---|---|
| Airflow UI | http://localhost:8080 (usuário e senha de lab: ver comentário no topo do `docker-compose.yml`) |
| Fake API (Swagger) | http://localhost:5001/docs |
| Banco do lab | `localhost:5433`, banco `labdb` (credenciais no `docker-compose.yml`) |

Na UI: toda DAG nova aparece **pausada** (`DAGS_ARE_PAUSED_AT_CREATION=true`). Ligue o toggle e
clique em ▶ (Trigger DAG). Veja Grid, Graph, Logs de cada task e Admin → Connections
(`postgres_lab`, criada pelo init).

DAGs do lab: `clima_etl`, `pipeline_clima_monolitico`, `pipeline_clima_taskgroup`,
`retry_simples`, `retry_backoff`, `callbacks_example`, `process_files_hardcoded`,
`process_files_dynamic`.

Conferir dados gravados direto no banco:
```bash
docker exec -it airflow-lab-db psql -U lab -d labdb -c "SELECT * FROM v_clima_resumo;"
```

## Passo 7 — Desligar e voltar ao projeto da Atividade 01

```bash
docker compose down                         # para o lab (dados dos bancos ficam nos volumes)
docker compose down -v                      # idem, mas APAGA os bancos (recomeça do zero)
docker compose -p shopbrasil-airflow start  # religa o shopbrasil
```

Pegadinha: o `init.sql` só roda quando o volume do banco é **criado**. Se mudar o SQL, precisa de
`down -v` para ele rodar de novo.

## Resumo para memorizar

`ler o compose → checar portas → logs com permissão → config → up -d → ps/logs até healthy → UI`
