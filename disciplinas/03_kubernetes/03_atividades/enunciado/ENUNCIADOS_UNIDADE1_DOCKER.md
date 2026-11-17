# Enunciados — Unidade 1 Docker

> Fonte: API do Canvas, curso 279168, lida em 15/11/2026 `[CANVAS]` `[PUC-ATIVIDADE]`.
> A avaliação da unidade é a nota do Teste de Fixação + Trabalho prático `[PUC-AULA: Orientações de Estudo]`.

## 1. Teste Fixação unidade 1 Docker

| Campo | Valor |
|---|---|
| Prazo | 24/11/2026 23:59 |
| Pontos | 15 |
| Tipo | Ferramenta externa (questionário) — sem descrição pela API |
| Link | https://pucminas.instructure.com/courses/279168/assignments/1469916 |

Número de questões, tempo e tentativas: **NÃO CONFIRMADO**. Revisão: `05_revisao/RESUMO_UNIDADE1_DOCKER.md`.

## 2. Trabalho prático Unidade 1 Docker

| Campo | Valor |
|---|---|
| Prazo | 01/12/2026 23:59 |
| Pontos | 35 |
| Entrega | URL (repositório GitHub) |
| Link | https://pucminas.instructure.com/courses/279168/assignments/1457600 |

### Texto do enunciado (transcrição)

**Desafio: Implementação de Estrutura com Docker Compose**

Objetivo: Utilizando o jogo demo disponível em https://github.com/fams/guess_game, implementar uma estrutura com Docker Compose com:
- um container para o backend em Python (Flask);
- um container para o banco de dados Postgres;
- um container NGINX atuando como proxy reverso e servindo as páginas do frontend React.

Requisitos:
- **Backend e Frontend:** o backend executa a aplicação Flask do jogo; o NGINX é proxy reverso, **balanceando a carga entre instâncias do backend**, e serve o frontend React.
- **Postgres:** armazena os dados do jogo, em **volume separado** para persistência.
- **Resiliência:** se algum container falhar, deve ser **reiniciado automaticamente**.
- **Balanceamento:** NGINX balanceando entre **múltiplos containers** do backend.
- **Facilidade de atualização:** atualizar qualquer componente apenas **trocando a versão do container**.

Entrega — repositório no GitHub com:
- `docker-compose.yml`;
- Dockerfile do backend Python;
- Dockerfile do frontend React (servido via NGINX);
- configuração do NGINX (proxy reverso + balanceamento);
- `README.md`: decisões de design (serviços, volumes, redes, estratégia de balanceamento), instruções de instalação/execução/atualização e como atualizar cada componente trocando a versão da imagem.

Critérios de avaliação:
- **Funcionamento correto:** containers se comunicando, resiliência a falhas. **Informar a URL a usar após o `docker-compose up`. Trabalhos que não funcionam recebem automaticamente 0.**
- **Facilidade de atualização** sem mudanças complexas no código.
- **Documentação completa e clara.**
- **Ater-se ao objetivo:** as aplicações não são alvo; **mudanças no fonte dos programas serão penalizadas**.

Observações do professor:
- Sistema desenvolvido em **Node 18** e **Python 3.12**; alterações de versão são desencorajadas.
- Atenção ao `.gitignore`: no original ele **não envia** `Dockerfile` e `docker-compose.yaml` (ajustar para que sejam versionados).

### Checklist

- [x] Fork/clone de `fams/guess_game` sem alterar o código da aplicação
- [x] Dockerfile backend (python:3.12)
- [x] Dockerfile frontend (build node:18 → nginx)
- [x] `nginx.conf` com `upstream` de ≥2 backends
- [x] Postgres com volume nomeado
- [x] `restart:` em todos os serviços
- [x] Versões de imagem parametrizadas (`${BACKEND_TAG:-...}`)
- [x] `.gitignore` corrigido
- [x] README completo + URL de acesso
- [x] Testado de verdade: `docker compose up`, jogar, derrubar um backend, reiniciar, dados persistem

### Status da implementação (17/11/2026)

- Código: https://github.com/mpauloprado/guess_game (fork público de `fams/guess_game`, commit `0cc6b44`, publicado em 17/11/2026);
  no projeto: submódulo em `../entrega/guess_game/` (rodar no Kali).
- Código do jogo inalterado (verificado com `git diff` em `guess/`, `repository/`, `run.py`,
  `requirements*.txt`, `frontend/src`, `frontend/package*.json`, `tests/`).
- Escolhas: 3 réplicas do backend (gunicorn) atrás do NGINX com `upstream ... resolve` (round-robin,
  DNS do Docker); frontend com `REACT_APP_BACKEND_URL=/api`; rede `app` interna; volume `db-data`;
  `restart: unless-stopped`; versões em `BACKEND_VERSION`/`FRONTEND_VERSION`/`POSTGRES_VERSION`.
- Achado: o backend usa uma conexão única com o Postgres e não reconecta (após reinício do banco,
  HTTP 500 permanente). Resolvido só com infraestrutura: healthcheck que joga uma partida de
  monitoramento e reinicia o container quando a aplicação perdeu a conexão.
- Evidências de execução real no Kali (Docker 28.5.2 / Compose 2.40.3):
  - jogo via NGINX (`/api/create`, `/api/guess`) e rotas `/`, `/maker`, `/breaker` com HTTP 200;
  - balanceamento 4/4/4 em 12 requisições (cabeçalho `X-Upstream`);
  - queda de backend (SIGTERM no PID 1): reinício automático, 40/40 jogadas OK durante a queda;
  - `docker kill` não reinicia (parada manual, comportamento do Docker) — documentado no README;
  - persistência após `down`/`up`; reinício do banco: jogadas voltaram em ~4 s; queda do banco
    (`pg_ctl stop -m immediate`): ~5 s;
  - atualização 1.0.0 → 1.0.1 só recriou os backends; rollback OK;
  - clone limpo + `docker compose up -d --build` sem `.env`: 5 containers healthy, jogo OK.
- Pendente: testar o frontend no navegador e postar o link no Canvas.
