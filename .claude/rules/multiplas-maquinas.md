# Regra — Trabalho em múltiplas máquinas e plataformas

Este projeto é usado pelo Claude Code em dois computadores e em várias interfaces
(terminal, extensão do VS Code, aba Code do app, claude.ai/code). O histórico de
conversas e a memória automática NÃO são compartilhados entre elas. A continuidade
depende do Git e de `00_ADMIN/STATUS_DO_PROJETO.md`.

## Onde fica o projeto

| Máquina | Cópia de trabalho | Observação |
|---|---|---|
| Windows (SUPORTE-NOCTEL2) | `G:\Meu Drive\DOCUMENTOS VIVOBOOK\PUC-Engenharia-IA-MLOps` | Repositório Git em `C:\git\PUC-Engenharia-IA-MLOps` (fora do Drive) |
| Kali | `~/projetos/PUC-Engenharia-IA-MLOps` | Clone normal do GitHub |
| GitHub | `git@github.com:mpauloprado/PUC-Engenharia-IA-MLOps.git` | Privado. Fonte da verdade |

No Kali, `~/gdrive/PUC-Engenharia-IA-MLOps` é a pasta do Drive (cópia do Windows),
montada via rclone. Use-a só para leitura ou para arquivos que não vão para o Git.
Não edite arquivos versionados por ali, porque isso cria alterações não commitadas
no Windows.

## Início de sessão

1. `git pull`
2. Ler a seção "Diário de sessões" de `00_ADMIN/STATUS_DO_PROJETO.md`.

## Fim de sessão (ou quando o aluno pedir "encerrar", "salvar" ou "sincronizar")

1. Acrescentar uma entrada no topo do "Diário de sessões": data, máquina/plataforma,
   o que foi feito, decisões e próximos passos.
2. `git add` dos arquivos alterados, commit com mensagem descritiva e `git push`.

## Cuidados

- Usar caminhos relativos ao projeto. Nunca usar `G:\...` ou `/home/kali/...` em código ou notas.
- Nunca versionar credenciais. Anotações de laboratório com senha ficam fora do Git
  (veja o `.gitignore`).
- Datasets grandes, embeddings e índices de RAG não vão para o Git.
- Se `git pull` apontar conflito, parar e mostrar ao aluno antes de resolver.
