# Atividades — Orquestração de Workflows

Para cada atividade, criar:
- `enunciado/`
- `rascunho/`
- `entrega/`
- `feedback/`

Preservar o enunciado original.

## Projetos de código entregues como repositório

Quando a entrega é um repositório próprio (ex.: Atividade 01 — Airflow), ele fica em
`entrega/<nome>/` como **submódulo git**: o repositório público continua independente
para o professor, e aqui aparece a mesma versão.

- Clonar/atualizar: `git submodule update --init` (com `submodule.recurse=true`, o
  `git pull` já atualiza).
- Rodar Docker só no Kali; no Windows a pasta está no Google Drive (logs sincronizariam).
- Alterações no projeto: commit/push dentro do submódulo e, depois, registrar a nova
  versão aqui (`git add entrega/<nome>`).
