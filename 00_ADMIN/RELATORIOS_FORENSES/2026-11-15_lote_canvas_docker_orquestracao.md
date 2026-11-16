# Relatório forense — lote Canvas: Kubernetes e Orquestração de Workflows

- Data: 15/11/2026 (Kali)
- Ferramenta: `tools/document_forensics.py` (biblioteca padrão; **sem PyMuPDF** — PDFs sem inspeção profunda de camadas/renderização)
- Arquivos: 35
- Resultado geral: **nenhum indício suspeito**. Itens de 'atenção' explicados abaixo como elementos normais do formato.

| Arquivo | SHA-256 (16) | Severidade | Achado |
|---|---|---|---|
| `disciplinas/03_kubernetes/00_original/canvas/02 - Apresentação da disciplina/Apresentação da disciplina-2.pptx` | `a13c4d90b1ac62d1` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Introdução ao Kubernetes-2.pptx` | `bc48bb52d6d05a1b` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Network E Storage-2.pptx` | `f76a9b05df0c3767` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Conteiner Internals.pptx` | `4fb142a761c7db6e` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Segurança.pptx` | `2f44bc0aa83341e0` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Introdução aos containers-1.pptx` | `c0c65199ce8eb95e` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Introdução-1.pptx` | `931c6ddd5519b3ea` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Ciclo de vida.pptx` | `2651397b5de8865d` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Criando containers.pptx` | `e8e1d62f21f3c399` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Docker Engines.pptx` | `bc1e0f8a3bd315c7` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Instalando Docker.pptx` | `933ef4ac86594e03` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/02 - Apresentação da disciplina/Plano de Ensino.docx` | `a6d758fb0c295089` | attention | customXml = metadados de biblioteca do SharePoint (contentType 'Documento'); relationships sem destino http externo. Elemento normal do formato. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Página - 1 - Orientações de Estudo.html` | `955b9ce0a9cb765f` | attention | Strings hex longas = parâmetro x-goog-signature de URL assinada do Google Cloud Storage (link da VM OVA). Elemento normal. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Docker Registry.pptx` | `ae1591fdbf159161` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Docker Compose.pptx` | `4df354910756da53` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Origem Evolução.pptx` | `8beb2853b596faad` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/DevContainers.pptx` | `bb2bd20286a24835` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Docker Logs.pptx` | `eba51e751314f3fc` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/Docker Volumes And Network-1.pptx` | `0fcde09716782cf0` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/03 - Unidade 1 - Docker/linux-basics.pdf` | `457cec3686ecd1b6` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/Encontro 02 - Orquestração de Workflow.pdf` | `f5982d862dd1b5bb` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/05 - UNIDADE 2 - TÍTULO DA UNIDADE/lab-airflow-11-01-2026.zip` | `aaa3dfe555f7aeae` | attention | 1 ZERO WIDTH JOINER em texto do ZIP; típico de emoji composto. Sem frases suspeitas. |
| `disciplinas/03_kubernetes/00_original/canvas/02 - Apresentação da disciplina/Página - Referências Bibliográficas.html` | `b9e2825c24a25f71` | attention | 1 ZERO WIDTH NON-JOINER; artefato comum de editor HTML. Sem frases suspeitas. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/09 - ATIVIDADES AVALIATIVAS/TRABALHO_FINAL_ORQUESTRACAO.pdf` | `b8258a4f6f9945bd` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/03 - MATERIAL COMPLEMENTAR/Material_Completo - [Python].zip` | `8210d2e36fd21912` | attention | Caracteres de controle bidirecional (LRE/LRO/FSI) em texto dentro do ZIP; comuns em textos copiados de editores. Nenhuma frase de prompt injection detectada. Revisar ao extrair o código (risco teórico de 'Trojan Source' em código-fonte). |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/03 - MATERIAL COMPLEMENTAR/preparacao_ambiente [Python].pdf` | `0b76cf77c049abfc` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/02 - APRESENTAÇÃO/Página - Apresentação da Disciplina.html` | `8c936f191383b2dc` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/02 - APRESENTAÇÃO/Página - Plano de Ensino.html` | `389415980dc785e1` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/AutoScale-1.pptx` | `fffb6d64e11ff419` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Arquitetura Kubernetes-2.pptx` | `a4b039401050ae89` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Helm-2.pptx` | `32304802017fb881` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Intoducao a orquestracao-2.pptx` | `4f8db7a4461c8264` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/Gerenciamento de aplicações-2.pptx` | `80ffb6c9afd3fad2` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/03_kubernetes/00_original/canvas/04 - Orquestração/segurança-2.pptx` | `91bba1cfb98e48b2` | informational | Nenhum indício encontrado pelos testes executados. |
| `disciplinas/06_orquestracao_workflows/00_original/canvas/09 - ATIVIDADES AVALIATIVAS/Atividade 01 - Descrição.pdf` | `01124f9957b0627c` | informational | Nenhum indício encontrado pelos testes executados. |

## Limitações
- Sem comparação visual texto × renderização dos PDFs (PyMuPDF ausente).
- Ausência de achados não prova ausência de esteganografia.
- Conteúdo interno dos ZIPs só foi varrido como texto; o código será revisado antes de executar.

## Recomendação
Material liberado para uso acadêmico. Ao extrair `Material_Completo - [Python].zip`, conferir os caracteres bidirecionais nos arquivos-fonte.
