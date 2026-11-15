# Manifesto de Arquivos

Registro de integridade dos arquivos do projeto `PUC-Engenharia-IA-MLOps`.

## Geração
- Data e hora: 16/09/2026 15:43 UTC (12:43 no horário de Brasília, UTC-3). ISO 8601: `2026-09-16T15:43:37Z`.
- Algoritmo: SHA-256, calculado sobre o conteúdo binário de cada arquivo (64 caracteres hexadecimais, em minúsculas).
- Arquivos listados: 310.
- Tamanho total dos arquivos listados: 24698813 bytes.
- Gerado por: Claude (Cowork), por solicitação do aluno.

## Regra de escopo
- Raiz: a pasta `PUC-Engenharia-IA-MLOps/`.
- Inclui todos os arquivos da raiz e de todas as subpastas, inclusive arquivos ocultos ou de controle (`.claude/`, `.gitignore`, `.gitkeep`), a cópia histórica em `00_ADMIN/historico/` e a pasta `Claude outputs/`.
- Exclui somente este arquivo, `00_ADMIN/MANIFESTO_ARQUIVOS.md`, porque o próprio hash mudaria ao ser gravado (autorreferência).
- Pastas não são listadas; pastas vazias não aparecem.
- Caminhos relativos à raiz, com `/` como separador, em ordem crescente de código Unicode.
- O manifesto retrata a pasta na data e hora acima. Qualquer arquivo incluído, alterado, movido ou excluído depois disso exige nova geração.

## Método
1. Listagem recursiva da pasta vinculada.
2. Cópia de cada arquivo para o ambiente da sessão, com conferência do tamanho em bytes em relação à listagem.
3. Cálculo do SHA-256 sobre cada cópia.
4. Nova listagem depois de gravar a cópia histórica, para confirmar que nenhum outro arquivo foi incluído, alterado ou removido.

## Como conferir um arquivo
- Windows (PowerShell): `Get-FileHash -Algorithm SHA256 -LiteralPath "caminho\do\arquivo"`. O PowerShell mostra o hash em maiúsculas; a comparação não depende de maiúsculas ou minúsculas.
- Linux: `sha256sum "caminho/do/arquivo"`. macOS: `shasum -a 256 "caminho/do/arquivo"`.

## Versão anterior
- Preservada byte a byte em `00_ADMIN/historico/MANIFESTO_ARQUIVOS_2026-09-16_anterior.md` (28376 bytes; SHA-256 `a173f7d0a58dcd74c59fa4c37d73d721a2e885e71aa144f064fc5b84aa97e34e`). Essa cópia também consta da tabela abaixo.
- A versão anterior não informava data, algoritmo nem escopo. Ela listava 226 arquivos: 215 com o mesmo hash atual; 10 com hash diferente, por terem sido editados depois da geração dela (entre eles `CLAUDE.md`, que já divergia na auditoria inicial de 16/09/2026); e `PROMPT_INICIAL_CLAUDE.md`, que não existe mais na pasta e foi retirado desta versão.
- Arquivos desta versão que não constavam da anterior: 85.

## Conferência dos originais
- Os 89 arquivos binários de materiais da PUC e de evidências (PDF, DOCX, imagens e ZIP) têm o mesmo SHA-256 medido na auditoria inicial de 16/09/2026. Nenhum foi alterado.

## Observações
- `00_ADMIN/COWORK_WRITE_TEST.txt`: arquivo do teste controlado de escrita de 16/09/2026.
- `Claude outputs/`: pasta surgida em 16/09/2026, logo após o envio de dois rascunhos como anexos no chat; o conteúdo é idêntico a esses rascunhos, inclusive `integridade-academica-ia.md`, que o aluno decidiu não adotar. Esses arquivos não são regras ativas (as regras ativas ficam em `.claude/rules/`). A pasta foi mantida porque nenhuma exclusão foi autorizada.

## Resumo por pasta
| Pasta | Arquivos | Bytes |
|---|---:|---:|
| (raiz) | 3 | 19277 |
| `.claude/` | 18 | 14431 |
| `00_ADMIN/` | 48 | 14315765 |
| `01_FONTES/` | 7 | 665376 |
| `Claude outputs/` | 2 | 2400 |
| `conhecimento/` | 5 | 1592 |
| `disciplinas/01_pipeline_dados/` | 66 | 9638762 |
| `disciplinas/02_cloud_computing/` | 11 | 2068 |
| `disciplinas/03_kubernetes/` | 11 | 2110 |
| `disciplinas/04_apis_modelos_ia/` | 11 | 2054 |
| `disciplinas/05_testes_modelos_ia/` | 11 | 2040 |
| `disciplinas/06_orquestracao_workflows/` | 11 | 1956 |
| `disciplinas/07_cicd/` | 11 | 2040 |
| `disciplinas/08_performance/` | 11 | 1956 |
| `disciplinas/09_seguranca_governanca/` | 11 | 1977 |
| `disciplinas/10_finops/` | 11 | 1935 |
| `disciplinas/11_agentes_ia/` | 11 | 2019 |
| `disciplinas/12_projeto_engenharia_ia/` | 11 | 1956 |
| `disciplinas/13_monitoramento_observabilidade/` | 11 | 1984 |
| `disciplinas/14_mlops_dataops/` | 11 | 2082 |
| `disciplinas/15_arquitetura_governanca/` | 11 | 2082 |
| `provas/` | 5 | 620 |
| `tools/` | 2 | 12331 |
| **Total** | **310** | **24698813** |

## Arquivos
| # | Arquivo | Bytes | SHA-256 |
|---:|---|---:|---|
| 1 | `.claude/README.md` | 576 | `895853f2b5cffadb07e90cf49156a72f0194586e7c5cbace746ed1a6017064bb` |
| 2 | `.claude/agents/exam-coach.md` | 550 | `a695f811b21e8874bf59a14c311dea988610cd2ec62e010e3a5dfbd5934ebd2d` |
| 3 | `.claude/agents/lab-engineer.md` | 768 | `e572c41685cf1e41d127b9d5ffba5f72290473c81829a37c401d9601521e8aa8` |
| 4 | `.claude/agents/revisor-academico.md` | 648 | `df59ad39170ca40af8e84c28b88b6afcf9ea0cca844c95c14dde140e09433958` |
| 5 | `.claude/agents/source-verifier.md` | 606 | `9e87dbeeefcf3fe79b9f32b426c023d913bce3af0693db9941a82830496eeb4c` |
| 6 | `.claude/agents/tutor.md` | 972 | `25a7ed514fd2987019e528dc02669977df2f3add7aa4c1d525b578639b1d481f` |
| 7 | `.claude/rules/atividades-academicas.md` | 2243 | `fac31d28e74915429994f6f60790f426d1662a743b18f6d40b360fa634acee5a` |
| 8 | `.claude/rules/document-forensics.md` | 1341 | `3a86cd2a2f5413cf7c7951e8aacc77eb1fdb500b43bae2b7e2dc78f1079b445e` |
| 9 | `.claude/rules/fontes-e-evidencias.md` | 465 | `0eb25068206b8e0dd29b482b1217dbb0c37f7a9f930182b1ad80b29771af711d` |
| 10 | `.claude/rules/laboratorios-codigo.md` | 457 | `a9fcf2af4a8eb55d527de747aa042c960a171864d3827ab9c019a473f96adb9d` |
| 11 | `.claude/rules/metodologia-estudo.md` | 371 | `687788f4114612b54a19033867ed73b75f960aa0c62e69206437095993c5658a` |
| 12 | `.claude/rules/provas-e-revisoes.md` | 373 | `005da145230b37d1bca90c141bb6f21912b92c907747e45a76105a33005bc1f6` |
| 13 | `.claude/skills/exam-prep/SKILL.md` | 738 | `f8eeb006786d6552d74c003015750ece006a3a2146f8bec87edeac96421d9f74` |
| 14 | `.claude/skills/ingest-material/SKILL.md` | 901 | `897bf71326d7e10875381dd0c9a9e33aa4311e7a4a4f52a410661674af6f7bb5` |
| 15 | `.claude/skills/inspect-document/SKILL.md` | 1331 | `e73db5d75c5582a449ff1e9c9eb54683234017c7caa8a8c4f193b58566052715` |
| 16 | `.claude/skills/review-activity/SKILL.md` | 800 | `330c2e8dc87680a98dfcd8fc6af80857fc444c3b3feaad3c23d226606bd9d36c` |
| 17 | `.claude/skills/study-session/SKILL.md` | 759 | `3a83b63e451d510f3497cabda4ae38630a61f27356ad585c1c246536430726ed` |
| 18 | `.claude/skills/weekly-review/SKILL.md` | 532 | `af30dd02923a2983ce2a3f922a71f4255089b2647fdabdb13542c7655dd93be0` |
| 19 | `.gitignore` | 149 | `bc294e7439b3f54f63e1a91fc55baee4387c3f4afb4b9bccf54554666bf22eb1` |
| 20 | `00_ADMIN/CALENDARIO_ACADEMICO.md` | 4458 | `19fcb0286973f24f0c123129dac130f02063abbf09c3565239944d3b3ddfffa9` |
| 21 | `00_ADMIN/COWORK_WRITE_TEST.txt` | 126 | `6024fcaccbaf33fa130fb30c4b9d4be64c119a9cb8bbdfe18128a23c7c1c9795` |
| 22 | `00_ADMIN/FONTES_PARA_BAIXAR.md` | 3803 | `e1df598c84513860ab71126997eb13ca26dcd6f6f33e34de9d9d33b5edb7e269` |
| 23 | `00_ADMIN/MATRIZ_CURRICULAR.md` | 3819 | `12c60b7f56b02f38e6682df53ab0d7d3ed08fc6de7c597b4bdda7971280868b6` |
| 24 | `00_ADMIN/PENDENCIAS.md` | 5104 | `91ae4518177aa3574847186e4bbfaa74935f4e20bab4491ecbbad7f03b24dce6` |
| 25 | `00_ADMIN/POLITICA_INTEGRIDADE_DOCUMENTAL.md` | 2692 | `9125e2e60f468d40bc919834d715703af0da0dbabee56a383533c33b03960a35` |
| 26 | `00_ADMIN/PROGRESSO_GERAL.md` | 2482 | `7a1673710dcedf592bb1522ad321c3607e7884da07083978311d341cbe5c5a24` |
| 27 | `00_ADMIN/README_ADMIN.md` | 275 | `34463f9b598429c5ac78c5c51640b2d7509b6aa3c0d214ce0b7327985cc08595` |
| 28 | `00_ADMIN/RELATORIOS_FORENSES/Painel_de_controle_inicial.forensics.json` | 1261 | `2ad34d7339648c18811d7df9281c126c194f6b487ae11639ba8f435060ee8b9b` |
| 29 | `00_ADMIN/RELATORIOS_FORENSES/Painel_de_controle_inicial.md` | 1267 | `7fb6abfccbb8371d970bd24f3d0ef8fd3bb5ad0a69b0a942760bd0d429798864` |
| 30 | `00_ADMIN/RELATORIOS_FORENSES/README.md` | 300 | `c16478e7f907e7b712af44e151d27b093b15b1927b6db1debd92df4f4ffcfa42` |
| 31 | `00_ADMIN/STATUS_DO_PROJETO.md` | 465 | `b2c5e5a869300aa8ced12805d63e5304d17a39e08cee96676ffaea6687e5c59d` |
| 32 | `00_ADMIN/avisos_canvas/Jornada 2s2026.jpg` | 87707 | `76cdd7fdaee1b1918288617b1e6acb71ac455224dc7cc62b20666029cec4fb0e` |
| 33 | `00_ADMIN/avisos_canvas/Jornada da Pós 2s2026_Feed - Perdeu a Live - IEC.jpg` | 352147 | `e4d55c93d91aaa588cdd71b217cb27653746ec42cec0c81f59803d4663bf3222` |
| 34 | `00_ADMIN/avisos_canvas/Painel_de_controle_inicial.pdf` | 208061 | `b1e5c83feee4942b4c2b5307c640f9380f840977c31724fc5fe51c3f82e14048` |
| 35 | `00_ADMIN/avisos_canvas/README.md` | 179 | `909fd46458936570bee7a13ee0f955d741346124b9bf494ee528fc97443e2365` |
| 36 | `00_ADMIN/calendario_e_grade/SisIEC - Grade Horária - Engenharia de Inteligência Artificial E MLOps - EAD com aulas ao vivo 1.1 (2_2026).pdf` | 536908 | `ab631034a3700fff3c51d2e8a77744599598b5f0d73a9b1935791561a818b8b5` |
| 37 | `00_ADMIN/contatos/Apoio_Academico.png` | 43428 | `dfcebd43f3284b7083e84abf5c8e2b85389e3037e0e3e995e25c60aaab92ee05` |
| 38 | `00_ADMIN/coordenacao_canvas/00_original/-Espa-o-Coordena-o---ENGENHARIA-DE-INTELIG-NCIA-ARTIFICIAL-E-MLOPS---EAD-com-aulas-ao-vivo---Oferta-1---Turma-1--2026-Sep-16_00-33-56-607.zip` | 4608668 | `bae66cd0b17c0f2623d0faf33223cc00bcbc3912ced1490a4d6daf5348980e57` |
| 39 | `00_ADMIN/coordenacao_canvas/01_extraido/Abertura de chamados de serviços financeiros_Aluno-1.pdf` | 296859 | `2e015c1d05c385158df8b9b960348ad309963fad7ce01ddb74319788152891c8` |
| 40 | `00_ADMIN/coordenacao_canvas/01_extraido/Abertura de chamados de serviços financeiros_Aluno.pdf` | 285004 | `1a7153e58ee8688c60a048bbca91cf659236898b38c5b88a66bd6c97b390fcfc` |
| 41 | `00_ADMIN/coordenacao_canvas/01_extraido/Abertura de chamados de suporte técnico_Aluno-1.pdf` | 403337 | `cdcdc47feb1172f300a2cfa7972c91410392de06300cfbae9bbb7fb4f5883a89` |
| 42 | `00_ADMIN/coordenacao_canvas/01_extraido/Abertura de chamados de suporte técnico_Aluno.pdf` | 238089 | `0153de4e416d7bdf1a94e292ba1682905d024fdcbba39c622adabf15d9a4e539` |
| 43 | `00_ADMIN/coordenacao_canvas/01_extraido/GUIA DO ALUNO_IEC PUC MINAS_cursos sincronos.pdf` | 421227 | `b585a4c65d36c9613cfe54e87c8eed7a1afbd4c5cf5e7c3a9740683225ee9ed6` |
| 44 | `00_ADMIN/coordenacao_canvas/01_extraido/Jornada da Pós 2s2026_Feed - Perdeu a Live - IEC.jpg` | 352147 | `e4d55c93d91aaa588cdd71b217cb27653746ec42cec0c81f59803d4663bf3222` |
| 45 | `00_ADMIN/coordenacao_canvas/01_extraido/ORIENTAÇÕES ESTÁGIO.pdf` | 56262 | `94874c34e648e03d0ef9dff5a2c1652b5db7081c9f4ba3087472a8df2ac982ef` |
| 46 | `00_ADMIN/coordenacao_canvas/01_extraido/Revisão de nota .png` | 191362 | `0825e3ad8ab8ceb38d9a688543fac92463aedf5c9f8ba3a8592742373464dbca` |
| 47 | `00_ADMIN/coordenacao_canvas/01_extraido/SisIEC - Grade Horária - Engenharia de Inteligência Artificial E MLOps - EAD com aulas ao vivo 1.1 (2_2026).pdf` | 536908 | `ab631034a3700fff3c51d2e8a77744599598b5f0d73a9b1935791561a818b8b5` |
| 48 | `00_ADMIN/coordenacao_canvas/01_extraido/TRABALHO DE CONCLUSÃO DE CURSO.png` | 541958 | `e3819a149cdf076a15dd4c14d1bf2fbd438f3d30a9155e58d566f8e7964ede10` |
| 49 | `00_ADMIN/coordenacao_canvas/01_extraido/Tutorial Sistemas Acadêmicos Aluno 2s26.pdf` | 1047172 | `d6a0ab2e8acff7cf4af023d2180fb5532c8165a1579e1d37e02e3381aa85f60a` |
| 50 | `00_ADMIN/evidencias_iniciais/README.md` | 292 | `70fa1ad4cd457fd17f26ea85d9145c76f412fbfe28ab1573f74046f3d01091b0` |
| 51 | `00_ADMIN/evidencias_iniciais/captura_inicial_01.png` | 143843 | `92f38054757f038ccb2d07e873dbc3ff2483e563a3799c34948b16d7205e3065` |
| 52 | `00_ADMIN/evidencias_iniciais/captura_inicial_02.png` | 105609 | `efa77f26ee46cabf66e981f67c8eeb111054157c8bdb2f59f9ae6697439da84f` |
| 53 | `00_ADMIN/evidencias_iniciais/captura_inicial_03.png` | 128258 | `c636db8b19f95a665b14737f713ccf9b74eb84a91ea33c2036d60984eedc8d77` |
| 54 | `00_ADMIN/evidencias_iniciais/captura_inicial_04.png` | 124614 | `9a863e0a06f758887c22051265533468a9800129005f2a054ef64aaa284c6364` |
| 55 | `00_ADMIN/evidencias_iniciais/captura_inicial_05.png` | 61395 | `9a8370775c6b46beaf1e8cb5d6be48c00dddb7323da18429d25b62cfbbdc3557` |
| 56 | `00_ADMIN/evidencias_iniciais/captura_inicial_06.png` | 179678 | `0541e8606aebc89ae9b24ec78dfa89040d5cdc4999ae5d02591ce4fd78c74b59` |
| 57 | `00_ADMIN/evidencias_iniciais/captura_inicial_07.png` | 84740 | `ed6cc23e8c45dd6346f953c902353d1f9cd27143c7644b93ff059cc55bcccc20` |
| 58 | `00_ADMIN/evidencias_iniciais/captura_inicial_08.png` | 165442 | `48ce6cf48e9893645ceda207cab316fec2c1c7f85f9f27e8def7884f1a9a24a5` |
| 59 | `00_ADMIN/guias_sistemas/Abertura de chamados de serviços financeiros_Aluno-1.pdf` | 296859 | `2e015c1d05c385158df8b9b960348ad309963fad7ce01ddb74319788152891c8` |
| 60 | `00_ADMIN/guias_sistemas/Abertura de chamados de serviços financeiros_Aluno.pdf` | 285004 | `1a7153e58ee8688c60a048bbca91cf659236898b38c5b88a66bd6c97b390fcfc` |
| 61 | `00_ADMIN/guias_sistemas/Abertura de chamados de suporte técnico_Aluno-1.pdf` | 403337 | `cdcdc47feb1172f300a2cfa7972c91410392de06300cfbae9bbb7fb4f5883a89` |
| 62 | `00_ADMIN/guias_sistemas/Abertura de chamados de suporte técnico_Aluno.pdf` | 238089 | `0153de4e416d7bdf1a94e292ba1682905d024fdcbba39c622adabf15d9a4e539` |
| 63 | `00_ADMIN/guias_sistemas/Tutorial Sistemas Acadêmicos Aluno 2s26.pdf` | 1047172 | `d6a0ab2e8acff7cf4af023d2180fb5532c8165a1579e1d37e02e3381aa85f60a` |
| 64 | `00_ADMIN/historico/MANIFESTO_ARQUIVOS_2026-09-16_anterior.md` | 28376 | `a173f7d0a58dcd74c59fa4c37d73d721a2e885e71aa144f064fc5b84aa97e34e` |
| 65 | `00_ADMIN/regulamentos/ORIENTAÇÕES ESTÁGIO.pdf` | 56262 | `94874c34e648e03d0ef9dff5a2c1652b5db7081c9f4ba3087472a8df2ac982ef` |
| 66 | `00_ADMIN/regulamentos/Revisão de nota .png` | 191362 | `0825e3ad8ab8ceb38d9a688543fac92463aedf5c9f8ba3a8592742373464dbca` |
| 67 | `00_ADMIN/regulamentos/TRABALHO DE CONCLUSÃO DE CURSO.png` | 541958 | `e3819a149cdf076a15dd4c14d1bf2fbd438f3d30a9155e58d566f8e7964ede10` |
| 68 | `01_FONTES/README.md` | 396 | `f728526b29802083dd845a44c7cd8e0bbf7be1cb42826c673eb5c51c5c96cad5` |
| 69 | `01_FONTES/artigos_cientificos/REFERENCIAS.md` | 168 | `a0dee479e8b12b682453130f7c43c27b34073d0af1824aa2ea3120577bc62901` |
| 70 | `01_FONTES/documentacao_tecnica/REFERENCIAS.md` | 205 | `8b8f5161dcbe81b901a6374820c5efe2645f91532df3499d3e0f7ed4044c4d49` |
| 71 | `01_FONTES/puc_oficial/REFERENCIAS.md` | 241 | `683d9dc841fc0809642f23b9f4416892c3e97d85ff2546e32a63e1232f36c22f` |
| 72 | `01_FONTES/puc_oficial/curso_atual/Ementas.pdf` | 91055 | `bf1163e8faadb01aaa15e6a297412f1794ca4526260c330d66d4305031e79ca2` |
| 73 | `01_FONTES/puc_oficial/curso_atual/SAL - Plano de Estudo.pdf` | 152084 | `fe548d327229a6cf883d018489e627f2f8962f8df7a6f3c5870e0550653c5248` |
| 74 | `01_FONTES/puc_oficial/institucional/GUIA DO ALUNO_IEC PUC MINAS_cursos sincronos.pdf` | 421227 | `b585a4c65d36c9613cfe54e87c8eed7a1afbd4c5cf5e7c3a9740683225ee9ed6` |
| 75 | `CLAUDE.md` | 16298 | `b582044aaea2a677fd4873b0c1af13c3603533ba5269ead9b9b6670a833de12b` |
| 76 | `Claude outputs/atividades-academicas.md` | 996 | `e7eae476668f26b51dbfcb34c965fd676e9e2a7fb1c7e0e02f0b32095c24900a` |
| 77 | `Claude outputs/integridade-academica-ia.md` | 1404 | `d44b75ac97cefae33d64002e7999bf852248dab4e153a0316dd8fe6d6251d95c` |
| 78 | `README.md` | 2830 | `49eb4991f56ba9e45a91241c4a9c1421ece9fb790dec6da3b10051d29bcc2ecb` |
| 79 | `conhecimento/ERROS_E_LACUNAS.md` | 276 | `be5628bf6a1c54f409b14dda69b6c163848ac98aedefee00d38420be351acc16` |
| 80 | `conhecimento/GLOSSARIO.md` | 506 | `51434a7db1c2260becaea5677973bda75cbd0849a9820a8617984f8d1b9fb95b` |
| 81 | `conhecimento/MAPA_DE_CONCEITOS.md` | 383 | `a25d86602ff579ef5b4a6ed305b9246108acc603d6a9aa0a407a37d7548f9bc8` |
| 82 | `conhecimento/REFERENCIAS.md` | 198 | `6ad72111964994b7837fbf8b7c2b899bb60fe982208a04812a0c6e028cb94572` |
| 83 | `conhecimento/TECNOLOGIAS.md` | 229 | `f3c91b84a2ff7349e4e26beb59b3ad0680e8020c72a23d005b21b07818ce94cc` |
| 84 | `disciplinas/01_pipeline_dados/00_original/Aula 1 - Arquiteturas e fundamentos de pipelines de dados/Apresentação/Aula 1 - Arquiteturas e fundamentos de pipelines de dados.pdf` | 2470619 | `ede0253851e93d1fe157e6076d3762b73b09d8ed333404155902d26110bce36e` |
| 85 | `disciplinas/01_pipeline_dados/00_original/Aula 1 - Arquiteturas e fundamentos de pipelines de dados/Exercícios/Exercício 1 - Arquitetura e ferramentas administrativas do SQL Server.docx` | 49432 | `b70eb282c8965ef2824f163228774d1aafb2f9853eaa16c85214837e53128a43` |
| 86 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/icone-ativiidade-aberta.png` | 6988 | `314d6a1582ddbf4b1d4594edbd3ff9488b0ada6910c39c7c4b214961e8478d59` |
| 87 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/importancia sustentabilidade.pdf` | 347716 | `0c954b1513de3f1aa999641610d65d18cdf27d07ef3c21bf4297f49a032f7ffa` |
| 88 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/info 2.jpg` | 59973 | `d5d0e57928a8d07248e2fe08f5d156a318dd924a50aab6140c278d924edb89ef` |
| 89 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/sust e des sustentavel.pdf` | 1390169 | `93d1c1ffa228a7375ecfb7134b966476b0d5ba107516d8c354099aec1918b859` |
| 90 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/sustentabilidade.png` | 813455 | `b489ed8096945b48f7fec9948eed2fc650eaf631e8b769ad4aab097f43bb61c5` |
| 91 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/tree-silhouette.png` | 16356 | `784f5b80a530cda94f7744816318229015fc91e49360582916d08e7e6b967f70` |
| 92 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/unidade 1 capacitacao.png` | 727654 | `cb09870b548506311dd03eaae8e0253f87dbe6b410726a1eafb2032ae5bde9e1` |
| 93 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/unidade 1 capacitacao_.png` | 727293 | `b4d348f3b5e19fc3b4ad5ac26b2587673ac6f71698efdb062cbcd09ecdb6017a` |
| 94 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/video.png` | 347444 | `be36d858ef15dc1fb9d92349bde080a38415b57873b0924fa3c97c1e2603b3af` |
| 95 | `disciplinas/01_pipeline_dados/00_original/Layout/Exemplo/video1.png` | 341917 | `470cdb7cf2f734ec53e0bfd03b12bb896af5fa1bcc04b89539441aad7dde5679` |
| 96 | `disciplinas/01_pipeline_dados/00_original/Layout/Imagem1prof.png` | 373269 | `afd51f096a6affa2adc24a49bd97f395f4991d1273aae588b479d2613b394069` |
| 97 | `disciplinas/01_pipeline_dados/00_original/Layout/Leitura.png` | 42543 | `a5cf041a03f2e09136e3446971d78264ac713b5e3461a5d649e38543d885cd80` |
| 98 | `disciplinas/01_pipeline_dados/00_original/Layout/Play.png` | 44060 | `56aeb1cbbaa5f1dfde0a3b5c8eb598c4c2f4343d22a00c75e346ff878432a3da` |
| 99 | `disciplinas/01_pipeline_dados/00_original/Layout/alvo (2).png` | 51647 | `10315d7435e820d2400e1d27c8170036862ead096ee3ba6f1d6bea178de4f62d` |
| 100 | `disciplinas/01_pipeline_dados/00_original/Layout/arrow.png` | 6496 | `e4c4756d336db4b62be775bd9bfc4772bbde764a68ccaf1e71e963cec0932e47` |
| 101 | `disciplinas/01_pipeline_dados/00_original/Layout/banner-pos-2022.jpg` | 746527 | `7e3c322970addd4f9c94734c07d905be7da2b03b2ab0248e6a39ad2ec8b1e190` |
| 102 | `disciplinas/01_pipeline_dados/00_original/Layout/bussola.png` | 80984 | `bb7e004b4ea9bd56945d0606b1f9bcb350ab30bc2214467ea84d537b652401db` |
| 103 | `disciplinas/01_pipeline_dados/00_original/Layout/clip.png` | 8517 | `b679a186817b9b820169bdea998dda919a0a946e4f239a0b917905e706bc8514` |
| 104 | `disciplinas/01_pipeline_dados/00_original/Layout/course_image/thumbnail-pos.jpg` | 69401 | `e065df632c57b015e8461b30a2b0a64254171e8954facc631c2e163549a7e5b9` |
| 105 | `disciplinas/01_pipeline_dados/00_original/Layout/elearning-1.png` | 12797 | `36a9d86276bab3f5cc05c852db3b17e804536c9749b2358543f07584fa4ceaf1` |
| 106 | `disciplinas/01_pipeline_dados/00_original/Layout/elearning.png` | 20728 | `3cd1c5d3a4c1b4d68c3bdd9ab61ad52386bbbc6ceb8af455904985db53db860a` |
| 107 | `disciplinas/01_pipeline_dados/00_original/Layout/elearning1.png` | 42841 | `4e2d0382582ada5544f3c85ca231412ef7341b5fc96f161dbe5c52b4c1804d10` |
| 108 | `disciplinas/01_pipeline_dados/00_original/Layout/elearning_.png` | 13709 | `6e9a6ca044c4fbd480186b06cf1d29f16bf349b2e450eb3624ae661964176469` |
| 109 | `disciplinas/01_pipeline_dados/00_original/Layout/google-docs (1).png` | 6291 | `bde9338ea0ce482530dbc4704d292bc5a8f871ecfcef769577b6b685c74d6c10` |
| 110 | `disciplinas/01_pipeline_dados/00_original/Layout/google-docs.png` | 16583 | `84e1fc4ae209f70d085d30408fb1efe166fe02b2c5923a8d0830088bb8121ecc` |
| 111 | `disciplinas/01_pipeline_dados/00_original/Layout/google-docs_azul.png` | 5190 | `9696f7c822319ec9d0fc9b9bb1c9a4efcd6888be41ceb74103aea24abb2d29a7` |
| 112 | `disciplinas/01_pipeline_dados/00_original/Layout/home (4).png` | 6708 | `1769509905a30716a7721690666ed2d27c8b479006891a949b6ada4dc611adc4` |
| 113 | `disciplinas/01_pipeline_dados/00_original/Layout/home.png` | 10459 | `96d4fdb883abd0f5ec18b0169fa72c2ccf03196ed08cd2e616e7b81524c9108f` |
| 114 | `disciplinas/01_pipeline_dados/00_original/Layout/icone-bussola.png` | 9439 | `eb2210b0fe0043e4ee23d76025972cb88ea04fc9e8d9ee341b48dc193e6d63ac` |
| 115 | `disciplinas/01_pipeline_dados/00_original/Layout/icone-coruja.png` | 10640 | `c6378f63f71ffea766153bad6309d19c36f1c64ae74399fd94cd2e082ca0adc0` |
| 116 | `disciplinas/01_pipeline_dados/00_original/Layout/icone-lampada.png` | 7901 | `d79998f86c690140224192254080e8f7850e2d9b676b0a4916d16e5cba1124d3` |
| 117 | `disciplinas/01_pipeline_dados/00_original/Layout/icone-preto.png` | 190981 | `36575576152acbe47955c78cf3b9356ff9401fc0e730e90ba27461b03e1d19be` |
| 118 | `disciplinas/01_pipeline_dados/00_original/Layout/info-1.png` | 23891 | `1f55d5591148092e63f779d4801e97380250eb82f211900791af273880cc06f6` |
| 119 | `disciplinas/01_pipeline_dados/00_original/Layout/info2.png` | 20967 | `41f2d3b54b2b82dfbe118d719f254feee460124818bb63d0d3743ecacc71ce13` |
| 120 | `disciplinas/01_pipeline_dados/00_original/Layout/lamp (1).png` | 40346 | `f9e37e1874a5c55c2b74ed75982dae0b8384a754ff446469efaddc7be94d97cc` |
| 121 | `disciplinas/01_pipeline_dados/00_original/Layout/lamp-1.png` | 12444 | `5a2156c06f7559fa5dd05de296b7e3fef3a06cfd24fc72bc03629e55e4800b0b` |
| 122 | `disciplinas/01_pipeline_dados/00_original/Layout/lamp.png` | 21254 | `a173b7f013557bed2bae295479de6537646cf70ff66c612fe844fe4e0b083064` |
| 123 | `disciplinas/01_pipeline_dados/00_original/Layout/laptop.png` | 11694 | `b70209a4ccf7f1c89ad82882c2eaa747a98ae84923b704c4ae15ba55b1e2d596` |
| 124 | `disciplinas/01_pipeline_dados/00_original/Layout/material-b.png` | 15586 | `415aeeaba2eaa66965af1ac44912d57f3ab30623a65b5dddf95af8607c0dc215` |
| 125 | `disciplinas/01_pipeline_dados/00_original/Layout/material.png` | 31955 | `9a240b8ccafcf2501ce4666c98e147efae3757f21008fa07d14faa061fb7a09d` |
| 126 | `disciplinas/01_pipeline_dados/00_original/Layout/online-class (1).png` | 40333 | `baa42d9fd5ed5038efa618667691afffc98b81198d35186adc9e139cf629f9b7` |
| 127 | `disciplinas/01_pipeline_dados/00_original/Layout/page.png` | 18979 | `fef2f8417874e55ccd84fb8e447d6c72fa516dc11a27da4ede0dadc12067491f` |
| 128 | `disciplinas/01_pipeline_dados/00_original/Layout/puzzle-2.png` | 10904 | `c3c6dab8c8ca9522b50ab7307e9311b454615a5659204abea29aa27f3fbb6eef` |
| 129 | `disciplinas/01_pipeline_dados/00_original/Layout/puzzle.png` | 10904 | `c3c6dab8c8ca9522b50ab7307e9311b454615a5659204abea29aa27f3fbb6eef` |
| 130 | `disciplinas/01_pipeline_dados/00_original/Layout/rocket.png` | 31338 | `4c969eadb89ea98c762cf78a14b10c5c4f427a157677757cbdb82edc66b0801b` |
| 131 | `disciplinas/01_pipeline_dados/00_original/Layout/rocket1.png` | 62277 | `21b5ab8560b36c2b18bfe776140eaa8f66af3ad571a715f77e89e4ebbd1821d4` |
| 132 | `disciplinas/01_pipeline_dados/00_original/Layout/seta.png` | 40182 | `2ce1730bac818bc222f90c7189c5e320ccb9c0839d76b6802c4bb8ee63e8f0b0` |
| 133 | `disciplinas/01_pipeline_dados/00_original/README.md` | 207 | `e737a3d161679dde39ce7eaa906a47c5204138958522929f474197ba695baf0b` |
| 134 | `disciplinas/01_pipeline_dados/00_original/Unidade 1/Unidade 1.png` | 40182 | `2ce1730bac818bc222f90c7189c5e320ccb9c0839d76b6802c4bb8ee63e8f0b0` |
| 135 | `disciplinas/01_pipeline_dados/00_original/Unidade 2/Unidade 2.png` | 40182 | `2ce1730bac818bc222f90c7189c5e320ccb9c0839d76b6802c4bb8ee63e8f0b0` |
| 136 | `disciplinas/01_pipeline_dados/00_original/Unidade 3/Unidade 3.png` | 40182 | `2ce1730bac818bc222f90c7189c5e320ccb9c0839d76b6802c4bb8ee63e8f0b0` |
| 137 | `disciplinas/01_pipeline_dados/00_original/Unidade 4/Unidade 4.png` | 40182 | `2ce1730bac818bc222f90c7189c5e320ccb9c0839d76b6802c4bb8ee63e8f0b0` |
| 138 | `disciplinas/01_pipeline_dados/01_aulas/ESTRUTURA_VISIVEL_NO_CANVAS.md` | 1311 | `a485e0f30d30e18bf33a4c1aaeb7c55efbc4460ee374c2d0e2070f6506da9953` |
| 139 | `disciplinas/01_pipeline_dados/01_aulas/INVENTARIO_00_ORIGINAL.md` | 3558 | `e2503160bfcf4f6e839d4dd1cf50a7c4efeb785273c3a28f6eb9b89456378c13` |
| 140 | `disciplinas/01_pipeline_dados/01_aulas/README.md` | 242 | `74702bf980cb668d3b05f9dfda8c693b8a1433b1712ec663c5e326416a714416` |
| 141 | `disciplinas/01_pipeline_dados/02_notas/NOTAS_MESTRE.md` | 224 | `9a423a19a08469e0c4f6f79bd679aaea52d8ae4184417864b295d228a713d612` |
| 142 | `disciplinas/01_pipeline_dados/03_atividades/README.md` | 192 | `b9a107496e93c128256392acd0be6c6a637048ab4f0d2423896127ff94823fc6` |
| 143 | `disciplinas/01_pipeline_dados/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 144 | `disciplinas/01_pipeline_dados/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 145 | `disciplinas/01_pipeline_dados/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 146 | `disciplinas/01_pipeline_dados/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 147 | `disciplinas/01_pipeline_dados/04_labs/README.md` | 262 | `9294d47e3f0fe9f24b8302f1bd0c5df7f3aa2c92fa33e1879d9ec4821f1ca13f` |
| 148 | `disciplinas/01_pipeline_dados/05_revisao/README.md` | 272 | `55425b78d133ec0392a392843885ad8cfa66d65ed297275d4d552608e567e703` |
| 149 | `disciplinas/01_pipeline_dados/README.md` | 1981 | `d26ac5bcf6aae6c2e89bb8bdedfaee63a1394ba42b841d98c66bce202a1fd067` |
| 150 | `disciplinas/02_cloud_computing/00_original/README.md` | 194 | `91a392678bf47f8a81a65d649fd228536c738b7b1e939ef2055c76d20fdd5a4a` |
| 151 | `disciplinas/02_cloud_computing/01_aulas/README.md` | 229 | `1aa9a6cf7d78af1c062178fc879a2210d1c1a4146027358027c2558aa32b85e5` |
| 152 | `disciplinas/02_cloud_computing/02_notas/NOTAS_MESTRE.md` | 211 | `fc2418c2cf32acbc48bf11375234af7aa14ad38c2b2e556e51310839a3905d9d` |
| 153 | `disciplinas/02_cloud_computing/03_atividades/README.md` | 179 | `be8168170a41d3273cf5e9667d964abf50dea1ba44d534c77e513443c36b9bc3` |
| 154 | `disciplinas/02_cloud_computing/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 155 | `disciplinas/02_cloud_computing/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 156 | `disciplinas/02_cloud_computing/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 157 | `disciplinas/02_cloud_computing/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 158 | `disciplinas/02_cloud_computing/04_labs/README.md` | 249 | `0bb8d542de3e48fe89a67d8f5e3a5037c0e247c13d7c2f0ac2057164ca84f945` |
| 159 | `disciplinas/02_cloud_computing/05_revisao/README.md` | 259 | `3a92851bbb7192fddf214c32471f98ba76c3f07da669ba46ee06b4e7857ee66d` |
| 160 | `disciplinas/02_cloud_computing/README.md` | 743 | `0039e3242748107ceb3b4ad0bbea2efbbf0efd4c953aa5d799d0671950cd2d75` |
| 161 | `disciplinas/03_kubernetes/00_original/README.md` | 200 | `c599e49f393738a84a20218a9d2db48c9a1e77e62a0d41ba005b8a3c268e1dc1` |
| 162 | `disciplinas/03_kubernetes/01_aulas/README.md` | 235 | `314b39f1afe1a98327bbdb721be13d444ddcca8906c3d4d944ed0a17af880a64` |
| 163 | `disciplinas/03_kubernetes/02_notas/NOTAS_MESTRE.md` | 217 | `90144adf7145ced3fcee1f69bd20ff8ca72b85ebef185cd77dd278cef51f09d8` |
| 164 | `disciplinas/03_kubernetes/03_atividades/README.md` | 185 | `6db28c7bb6dab74804e2d27f7a998d3d86436dd86d794301917a452dd789b1d7` |
| 165 | `disciplinas/03_kubernetes/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 166 | `disciplinas/03_kubernetes/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 167 | `disciplinas/03_kubernetes/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 168 | `disciplinas/03_kubernetes/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 169 | `disciplinas/03_kubernetes/04_labs/README.md` | 255 | `8b82a9096524525a01bc4329d1532ba2a4687b968baf7145bcf74ee845a063b7` |
| 170 | `disciplinas/03_kubernetes/05_revisao/README.md` | 265 | `46c9c4683c6fbef25ba666e50fa4807249f906a4380e1b083ba405656f086a2e` |
| 171 | `disciplinas/03_kubernetes/README.md` | 749 | `083676b4a13943f34ca46f7100725062ded144a4c83d86b43236268b489f84a3` |
| 172 | `disciplinas/04_apis_modelos_ia/00_original/README.md` | 192 | `639762171dade8dfba36a4e8f90674c937cf459b37f5dca4c8c6baccec543a91` |
| 173 | `disciplinas/04_apis_modelos_ia/01_aulas/README.md` | 227 | `a22ddda7f01981bfa505bf1d2cefcfaca7bb47cb8dfce676f6015acd17366384` |
| 174 | `disciplinas/04_apis_modelos_ia/02_notas/NOTAS_MESTRE.md` | 209 | `39ef40640ac3c85e0e7fafa5daa8aff4f710fa4f26613c15bba9cc221ac8b61d` |
| 175 | `disciplinas/04_apis_modelos_ia/03_atividades/README.md` | 177 | `a06aab85f2f45675a14d0d3c3e7f3c9e83f2c295b8d018589e9bdf196bdfcb88` |
| 176 | `disciplinas/04_apis_modelos_ia/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 177 | `disciplinas/04_apis_modelos_ia/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 178 | `disciplinas/04_apis_modelos_ia/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 179 | `disciplinas/04_apis_modelos_ia/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 180 | `disciplinas/04_apis_modelos_ia/04_labs/README.md` | 247 | `8c41a7d6243e13263df29a0e4cb3d61a9fef11829a9379a33784ac318c885a44` |
| 181 | `disciplinas/04_apis_modelos_ia/05_revisao/README.md` | 257 | `6741b518230c8116d50d9fdf6b183f3e705970aac0c20a5b2ffbc8c0820d9b01` |
| 182 | `disciplinas/04_apis_modelos_ia/README.md` | 741 | `a319fb5b0805d99617a9350d8c977d01b350853a0656708bbfb41984f24345be` |
| 183 | `disciplinas/05_testes_modelos_ia/00_original/README.md` | 190 | `653eef6002262ace936e651803c9e46c2f2c95ff08ff93fd0daeb9933722752f` |
| 184 | `disciplinas/05_testes_modelos_ia/01_aulas/README.md` | 225 | `065f30e3eb8be9624d299107710c644b3bbb366a3886f4f64191c11bdba85739` |
| 185 | `disciplinas/05_testes_modelos_ia/02_notas/NOTAS_MESTRE.md` | 207 | `cddf04b7f5240821388002f1dbb6d6b1a06b410af07efe4a82ddb5156c4fa468` |
| 186 | `disciplinas/05_testes_modelos_ia/03_atividades/README.md` | 175 | `b9c06bdc90f786706ae7b01497e52e4825ce2b418d9a44b490e456aaef7ff5ca` |
| 187 | `disciplinas/05_testes_modelos_ia/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 188 | `disciplinas/05_testes_modelos_ia/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 189 | `disciplinas/05_testes_modelos_ia/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 190 | `disciplinas/05_testes_modelos_ia/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 191 | `disciplinas/05_testes_modelos_ia/04_labs/README.md` | 245 | `97a6825af220fc6457df6c07763edcd7284ab7fbba8218b4ad6006214ff4c842` |
| 192 | `disciplinas/05_testes_modelos_ia/05_revisao/README.md` | 255 | `0b4e0ae33458616b24d90203fb27c08ef20aa8688573e59586429bb8c927ef91` |
| 193 | `disciplinas/05_testes_modelos_ia/README.md` | 739 | `0740d20a728572c9e2e90cce12fae0aeca019e8eee1d1307b24d9c11b1d2994b` |
| 194 | `disciplinas/06_orquestracao_workflows/00_original/README.md` | 178 | `a71fcc6552a0e0089c92cfe772b2db08454ba7639cfb97299ba97cdcc7b8ba47` |
| 195 | `disciplinas/06_orquestracao_workflows/01_aulas/README.md` | 213 | `3d02007616461a9e981a7189d62218628328ed62b2251d4658756c6e33935e1c` |
| 196 | `disciplinas/06_orquestracao_workflows/02_notas/NOTAS_MESTRE.md` | 195 | `24b5fb220b758f256911b68a8dce1cce418898fcb2bb7945e53f9b539e984d92` |
| 197 | `disciplinas/06_orquestracao_workflows/03_atividades/README.md` | 163 | `2ee3f0464dcd8e3eacf3808b01c53f83fc03e8c1c1779911657cf1bed50a196e` |
| 198 | `disciplinas/06_orquestracao_workflows/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 199 | `disciplinas/06_orquestracao_workflows/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 200 | `disciplinas/06_orquestracao_workflows/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 201 | `disciplinas/06_orquestracao_workflows/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 202 | `disciplinas/06_orquestracao_workflows/04_labs/README.md` | 233 | `d74ff23723fac6dfbdaac8ca299d52e7991a93480374c86e6ea0c348650cd1e8` |
| 203 | `disciplinas/06_orquestracao_workflows/05_revisao/README.md` | 243 | `a3162ed50f7aac63802ca0501f7b3a3fdfc8b761b9bd9090403b54089b3d0929` |
| 204 | `disciplinas/06_orquestracao_workflows/README.md` | 727 | `c703cf31b0a1b4f86291deae4597c6fc25d34e06a49435c9da7431123e77d65f` |
| 205 | `disciplinas/07_cicd/00_original/README.md` | 190 | `578cfb318268be3f6d80e44c3574a052b996da95f94fd034edae9065e60e52d7` |
| 206 | `disciplinas/07_cicd/01_aulas/README.md` | 225 | `14ab17582066764cd1739c65dc84467304d53551330e8f0e3a8e17d2618d0032` |
| 207 | `disciplinas/07_cicd/02_notas/NOTAS_MESTRE.md` | 207 | `5ec9a0d30771630c97bf4a5e04a3bd5c14c34424893c3e4d1d9eb65b1a5ccaf0` |
| 208 | `disciplinas/07_cicd/03_atividades/README.md` | 175 | `3910a715b644b829c82ec2de7b64858bceb8df052b77b28700a48c9951eb6af1` |
| 209 | `disciplinas/07_cicd/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 210 | `disciplinas/07_cicd/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 211 | `disciplinas/07_cicd/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 212 | `disciplinas/07_cicd/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 213 | `disciplinas/07_cicd/04_labs/README.md` | 245 | `8679406fb5bf5d855ea7ba7519359453ae3b30d37911cd9b4c505041d801f1de` |
| 214 | `disciplinas/07_cicd/05_revisao/README.md` | 255 | `a9a36d4b08af7519cb046cc15e8f48f3b87433b7a64084f4f0fecef86da0b599` |
| 215 | `disciplinas/07_cicd/README.md` | 739 | `f70b51d0e94a9d089732b72861d3c4d3c8f8ef0d1baf99ce57ad4e5d90964ea8` |
| 216 | `disciplinas/08_performance/00_original/README.md` | 178 | `c5420e3953b616b9252f53f8e043850f0909de55de44f6656b5306ca1cfb10c6` |
| 217 | `disciplinas/08_performance/01_aulas/README.md` | 213 | `1053db08a5e731f3c310db9b732a9d73ac3c9075b308c9638239c54fc6cc720d` |
| 218 | `disciplinas/08_performance/02_notas/NOTAS_MESTRE.md` | 195 | `211a84a69b807b82edb60b98966ad134d4e028e86b2b04f5cd51f01121e16a80` |
| 219 | `disciplinas/08_performance/03_atividades/README.md` | 163 | `7f6ba043017f577e29271b2464a448925db86ffcf01c7aeb6e367b50285ed311` |
| 220 | `disciplinas/08_performance/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 221 | `disciplinas/08_performance/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 222 | `disciplinas/08_performance/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 223 | `disciplinas/08_performance/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 224 | `disciplinas/08_performance/04_labs/README.md` | 233 | `abaa11ea33d535696cfa1523487ebcfe61d7d10305d2ab8bee495dd57020b4de` |
| 225 | `disciplinas/08_performance/05_revisao/README.md` | 243 | `14a787b6df2d592c80f1b1868311e83e6eaae87ca8dce734f307f1ded2b3ccf0` |
| 226 | `disciplinas/08_performance/README.md` | 727 | `3eaace697598e8e70e5427a39d917f01908ce7b70f9078e25cac8f0700ca616f` |
| 227 | `disciplinas/09_seguranca_governanca/00_original/README.md` | 181 | `3ae77b98400e6d55d85c7dd05509aea3b7d93681edfa37c7fe12610ca63e8b3b` |
| 228 | `disciplinas/09_seguranca_governanca/01_aulas/README.md` | 216 | `79021195d1f74faa04110f4cc12d2b4cf723e9a44682d56fdc14bb08aeb67102` |
| 229 | `disciplinas/09_seguranca_governanca/02_notas/NOTAS_MESTRE.md` | 198 | `582cdc434565ca1203065b194f26d5019d1ac5f6fedbe31d438de807aa804fee` |
| 230 | `disciplinas/09_seguranca_governanca/03_atividades/README.md` | 166 | `e447cd0ba3632e28efeffc09e7ce2814c601713dac0469a5ecf9813a03223a8a` |
| 231 | `disciplinas/09_seguranca_governanca/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 232 | `disciplinas/09_seguranca_governanca/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 233 | `disciplinas/09_seguranca_governanca/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 234 | `disciplinas/09_seguranca_governanca/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 235 | `disciplinas/09_seguranca_governanca/04_labs/README.md` | 236 | `464d4f334eae61aa5b31060ea510d5eec43639aa635306fd38ecb29cfd8a4456` |
| 236 | `disciplinas/09_seguranca_governanca/05_revisao/README.md` | 246 | `0aebdacd6f7fe93291e63af8a4decbb64c32556defdad8ecd559b506587f813b` |
| 237 | `disciplinas/09_seguranca_governanca/README.md` | 730 | `1b768ab00e04c98de7b12a3d3a7af5c59e423fdab9560bddc51e26481aee9600` |
| 238 | `disciplinas/10_finops/00_original/README.md` | 175 | `9a28cbcf2552a3be8ee3a32c3b6399e265cfeb689f4f5537fb86132215d4f45f` |
| 239 | `disciplinas/10_finops/01_aulas/README.md` | 210 | `5e84041fcac3ef2ef4858950f40a561312e20e2d7853ac2b382bc8a1e5ac9ddd` |
| 240 | `disciplinas/10_finops/02_notas/NOTAS_MESTRE.md` | 192 | `398ec197ae5acadef408d09264fd4dabd10c2469f4d0ae47e5615abd59aa07bd` |
| 241 | `disciplinas/10_finops/03_atividades/README.md` | 160 | `89faae3cd6847fa1be8ab2c7357f63185aca23cf953aaacf5d00b1e04da8eb5d` |
| 242 | `disciplinas/10_finops/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 243 | `disciplinas/10_finops/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 244 | `disciplinas/10_finops/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 245 | `disciplinas/10_finops/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 246 | `disciplinas/10_finops/04_labs/README.md` | 230 | `c774e91ebd37fc90c2edd55193435188cbdce40ea7b36781c7c3309bbe51b9ad` |
| 247 | `disciplinas/10_finops/05_revisao/README.md` | 240 | `13b92e05d8726fc2dabbefac26c92574fab9184edd283df3bfe0e7624cd24087` |
| 248 | `disciplinas/10_finops/README.md` | 724 | `fa2f0c6986beb952d2d917ecb5196fff79072d9046395e07dd86b05cbf0405a9` |
| 249 | `disciplinas/11_agentes_ia/00_original/README.md` | 187 | `1cf94046b3661f03e9cce155f6cfea91072497c4830db741ab849e0763a5db30` |
| 250 | `disciplinas/11_agentes_ia/01_aulas/README.md` | 222 | `fe03f7977f8e4e79f77e5434a8043337d78c3e1cec9bc0c59ddf5d1ad04661bb` |
| 251 | `disciplinas/11_agentes_ia/02_notas/NOTAS_MESTRE.md` | 204 | `7f9f341c274c2defb73f00765be8f618ef5c6db9391881d8e2d762a34bc55b30` |
| 252 | `disciplinas/11_agentes_ia/03_atividades/README.md` | 172 | `516455b55f8d03b002f8c1dff052bf3f8a5d451436ff1900f4aca6f5b29320e9` |
| 253 | `disciplinas/11_agentes_ia/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 254 | `disciplinas/11_agentes_ia/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 255 | `disciplinas/11_agentes_ia/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 256 | `disciplinas/11_agentes_ia/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 257 | `disciplinas/11_agentes_ia/04_labs/README.md` | 242 | `4f189353dd1f5e9c46723256b34e0a726042c13444466a7b65a2fcb70fecfc36` |
| 258 | `disciplinas/11_agentes_ia/05_revisao/README.md` | 252 | `6b2ea54f3d65013055c51039e22d19c01cdc157dab1b440fdbd18b335e009492` |
| 259 | `disciplinas/11_agentes_ia/README.md` | 736 | `38a824196ae74a81fe940c9b50f264c40657bd75da7f9db862a116e0da6f3606` |
| 260 | `disciplinas/12_projeto_engenharia_ia/00_original/README.md` | 178 | `2c6dc64e56837786da2f75571b8dfc450be74dc62075ad0e72e45dfaf3317014` |
| 261 | `disciplinas/12_projeto_engenharia_ia/01_aulas/README.md` | 213 | `e62edf4c38274dfbd3a8675c8cb833d8ea61245a75639b695905e85d7cdf1620` |
| 262 | `disciplinas/12_projeto_engenharia_ia/02_notas/NOTAS_MESTRE.md` | 195 | `eb32f3d3b2f35fe5d0267e39aad9e9848306a3b89a616f36e0fb2fdcb031e045` |
| 263 | `disciplinas/12_projeto_engenharia_ia/03_atividades/README.md` | 163 | `3804242692cef3c1fa23b1f8a2cae8beb0910b720e91c970665950c0447379d9` |
| 264 | `disciplinas/12_projeto_engenharia_ia/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 265 | `disciplinas/12_projeto_engenharia_ia/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 266 | `disciplinas/12_projeto_engenharia_ia/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 267 | `disciplinas/12_projeto_engenharia_ia/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 268 | `disciplinas/12_projeto_engenharia_ia/04_labs/README.md` | 233 | `2dc3f24791f95640937d223e09c4eec56bbf0c6543f81d57064da914ae12760d` |
| 269 | `disciplinas/12_projeto_engenharia_ia/05_revisao/README.md` | 243 | `140ed1d0e150e4ca469cc2c163fe4f7a51f0ed1cb07698864cd4de124727c469` |
| 270 | `disciplinas/12_projeto_engenharia_ia/README.md` | 727 | `97250e370752e3cac8fcaf6883dc5b5a549b11eded6279ad8b0801b5c1434661` |
| 271 | `disciplinas/13_monitoramento_observabilidade/00_original/README.md` | 182 | `47fe7835e81266bc782346dd93442c6d28bda2cd217ee60f4f3d3a2b938fef39` |
| 272 | `disciplinas/13_monitoramento_observabilidade/01_aulas/README.md` | 217 | `333629ac8eabb785dcbd9335a28156be81f096ebdea6538ded4bfafb86f9e88c` |
| 273 | `disciplinas/13_monitoramento_observabilidade/02_notas/NOTAS_MESTRE.md` | 199 | `ecc5e16ac5b2115e0dca8d8e35d6b5591229a7cae8e9eca8d5bfb03f86469ee7` |
| 274 | `disciplinas/13_monitoramento_observabilidade/03_atividades/README.md` | 167 | `a3228d539f457b915fa12dfd19a86f3e954c8f91304febf585d4c47c65a60b72` |
| 275 | `disciplinas/13_monitoramento_observabilidade/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 276 | `disciplinas/13_monitoramento_observabilidade/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 277 | `disciplinas/13_monitoramento_observabilidade/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 278 | `disciplinas/13_monitoramento_observabilidade/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 279 | `disciplinas/13_monitoramento_observabilidade/04_labs/README.md` | 237 | `91f42bc995ae57653ea18b66672d1cd0ff4d413e8b2746d602df9c415496de62` |
| 280 | `disciplinas/13_monitoramento_observabilidade/05_revisao/README.md` | 247 | `e2537ebed7a557af8f64dc9591b60e3878cec1d6b20ba7e621e542670cf003ef` |
| 281 | `disciplinas/13_monitoramento_observabilidade/README.md` | 731 | `5e4bc4e1f029c83fd1e395831ae46c638ecbd06f5163ea4904413af3e884570a` |
| 282 | `disciplinas/14_mlops_dataops/00_original/README.md` | 196 | `eebb569233f678bcb720b957d9f0163b8f498d1fa7ecfaf89cfb3d6b1595daad` |
| 283 | `disciplinas/14_mlops_dataops/01_aulas/README.md` | 231 | `e99104c70854b9f5bdf57d34e51e5ab552f69f8ec4e9aab28ad5ee31013f69b5` |
| 284 | `disciplinas/14_mlops_dataops/02_notas/NOTAS_MESTRE.md` | 213 | `968b0f5de99f7de0ce0ef27ef1793b193cda41b1c37e9ca5bcfcd81bb5e7fbcf` |
| 285 | `disciplinas/14_mlops_dataops/03_atividades/README.md` | 181 | `65f9138c79855edcb52cac06e662d8e92cfb3d36c6e21cb92c793744a3725137` |
| 286 | `disciplinas/14_mlops_dataops/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 287 | `disciplinas/14_mlops_dataops/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 288 | `disciplinas/14_mlops_dataops/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 289 | `disciplinas/14_mlops_dataops/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 290 | `disciplinas/14_mlops_dataops/04_labs/README.md` | 251 | `0b17af1405f6c5df717bfbfdf402f31d7b62ad5b25bb4c3b1792592e6650682f` |
| 291 | `disciplinas/14_mlops_dataops/05_revisao/README.md` | 261 | `cd85f6caf388a7a2a11189df40e89016cd0d0a2bb6d6bdf0a21e5e847d5e9cfe` |
| 292 | `disciplinas/14_mlops_dataops/README.md` | 745 | `08d09d5c5975f015a73cafa303d0a8859cb256493c8096933662347c50126ba7` |
| 293 | `disciplinas/15_arquitetura_governanca/00_original/README.md` | 196 | `cb803b268e74dad5418bc7343c2c197eb6f58b3c8e20ace29f137915b9658ac2` |
| 294 | `disciplinas/15_arquitetura_governanca/01_aulas/README.md` | 231 | `12551e73feca2cf92be5a765c444900f00b4949817b0b50f4d2450f1b53b260a` |
| 295 | `disciplinas/15_arquitetura_governanca/02_notas/NOTAS_MESTRE.md` | 213 | `010f02751cb73aeffdd89dfa3dc36deee984d15da5675055491f40e46cbffff6` |
| 296 | `disciplinas/15_arquitetura_governanca/03_atividades/README.md` | 181 | `44e1d18c039c487882782e9fd172ab7c8b500e57bde78e83a23ccd31f7da1f1e` |
| 297 | `disciplinas/15_arquitetura_governanca/03_atividades/entrega/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 298 | `disciplinas/15_arquitetura_governanca/03_atividades/enunciado/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 299 | `disciplinas/15_arquitetura_governanca/03_atividades/feedback/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 300 | `disciplinas/15_arquitetura_governanca/03_atividades/rascunho/.gitkeep` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| 301 | `disciplinas/15_arquitetura_governanca/04_labs/README.md` | 251 | `f484ec00e19cb82ed4a845a6391ad222c67046591b65b67b6007c33e3642c8cb` |
| 302 | `disciplinas/15_arquitetura_governanca/05_revisao/README.md` | 261 | `d9008eb65af5c3d4406818aa4854f914e24671c1ac3d52ab9c233c61c1166ed1` |
| 303 | `disciplinas/15_arquitetura_governanca/README.md` | 745 | `a6c9bb95d3e817fa3e4b231cb5c68bd46a13b47d9e0b0e716c4ee3453f5624a9` |
| 304 | `provas/README.md` | 296 | `009ff54c9910f818251e3127830c750b5ddcbdf76a50b6a048b46b589bf7c8f3` |
| 305 | `provas/banco_questoes/README.md` | 92 | `d0be52ab6dc6d91a7eb482e6a96b052fc421cf8f8ec7cd1250998798dc28c68a` |
| 306 | `provas/erros_simulados/README.md` | 83 | `d70d28cc359c4ccd82a8660ec196cb0ebbf920c561987f08379431a2654dc78b` |
| 307 | `provas/revisoes/README.md` | 72 | `8d85f6ac1cb5dfbe2ade749b979e73f2456aca6a564aaf76a7d315d41a0e02a0` |
| 308 | `provas/simulados/README.md` | 77 | `7f2c5e4d70ef3295d9cea74209d3bfed2386713c8550659de64cc711a8cbb2d9` |
| 309 | `tools/README.md` | 866 | `16c1d7a73d8bb64d9c51a4e90633b62f6535e9e720562729c2633a051defbe4c` |
| 310 | `tools/document_forensics.py` | 11465 | `b5274cb781e2945a893f2098760af0408301770d9e496d7b49af6c495d623d33` |
