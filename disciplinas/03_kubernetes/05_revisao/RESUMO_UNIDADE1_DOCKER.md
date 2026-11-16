# Resumo de revisão — Unidade 1: Docker

> Preparação para o **Teste Fixação unidade 1 Docker** (prazo 24/11/2026 23:59, 15 pts) `[CANVAS]`.
> Fonte principal: slides da Unidade 1 (`00_original/canvas/03 - Unidade 1 - Docker/`), prof. Fernando Augusto Medeiros Silva.
> Marcação: `[PUC-AULA: arquivo, slide N]` = conteúdo dos slides; `[OFICIAL]`/`[INFERÊNCIA]` = complemento externo, não está nos slides.
> Material inspecionado em 15/11/2026 (triagem forense sem achados relevantes; ver `00_ADMIN/RELATORIOS_FORENSES/2026-11-15_lote_canvas_docker_orquestracao.md`).
> Bibliografia indicada: POULTON, *Docker Deep Dive* (2020); NEMETH et al., *Unix and Linux System Administration Handbook*; LOONYCORN, *Introduction to Docker and the DCA Certification* (2018) `[PUC-AULA: Orientações de Estudo]`.

---

## 1. Por que containers

- Desafios que motivam: bibliotecas, scripts, configuração, código, logs e runtime diferentes entre ambientes. Lema **Build, Ship, Run** `[PUC-AULA: Introdução aos containers, 3–5]`.
- **Vantagens** `[PUC-AULA: Introdução aos containers, 9–13]`:
  - *Escalabilidade*: fáceis de copiar, instalar, rápidos para iniciar → escalabilidade **horizontal**.
  - *Eficiência*: compactos, gestão de recursos simples, *right sizing*.
  - *Portabilidade*: **build once, run in more places**; executa em mais de um SO — *"not really"* (o container usa o kernel do host); **infraestrutura imutável** DEV → UAT → PRD.
  - *Isolamento*: cada container vê seu próprio **userland**, filesystem, processos e recursos.
- **VM × Container** `[PUC-AULA: slide 8, fonte Docker Deep Dive]`: VM virtualiza hardware e tem SO completo; container compartilha o **kernel do host** e isola só o userland → mais leve e rápido. `[INFERÊNCIA]`
- Casos reais: **Netflix** (velocidade, desenvolvimento local, gestão de recursos; batch e serviços; Spinnaker CI/CD) e uso em **CI/CD** (ambientes de teste e build) `[PUC-AULA: 14–18]`.
- Automação do desenvolvimento: setup inicial, versão do ambiente, compilador, banco, webserver, cache `[PUC-AULA: 19]`.

## 2. Origem e evolução (linha do tempo — cai muito em teste)

| Ano | Marco | Ideia-chave |
|---|---|---|
| 1979 | **chroot** (Unix V7) | Muda o diretório raiz dos processos filhos; 1º isolamento |
| 2000 | **FreeBSD Jails** | Cada jail com IP próprio; isola usuários e root |
| 2001 | **Linux VServer** | Isola processos, CPU/memória, rede; kernel modificado; COW |
| 2003 | **CKRM** | Tentativa de portar o WLM do AIX; base conceitual dos cgroups |
| 2004 | **Solaris Containers (Zones)** | Isola FS, rede, recursos; alternativa leve às LPAR da IBM |
| 2005 | **OpenVZ** | Similar ao VServer, kernel modificado |
| 2006 | **Process Containers → cgroups** (Google) | Controle de recursos por processo; aceito no kernel vanilla |
| 2008 | **LXC** | namespaces + chroot + cgroups com kernel **vanilla** |
| 2011 | **Warden** (Cloud Foundry) | |
| 2013 | **LMCTFY** (Google) | Biblioteca padronizada sobre cgroups |
| 2013 | **Docker** | Baseado no LXC; CLI simples estilo Git (pull/push/tag), **Dockerfile**, **Registry**; dotCloud vira Docker |
| 2014 | **Kubernetes** | Baseado no **Borg** (Google, 2003); open source |
| 2015 | **OCI** (Linux Foundation, jun/2015), **CNCF**, **Helm** | OCI padroniza imagem e runtime; **runc** = implementação de referência |
| 2017 | **OCI 1.0** | |
| 2018 | Kubernetes *mainstream* | Padrão de fato; 1º projeto da CNCF |

`[PUC-AULA: Origem Evolução, 4–15]`

- Concorrentes/alternativas: **Podman Desktop** (Red Hat, múltiplos runtimes), **Rancher Desktop** (SUSE) `[PUC-AULA: 19]`.
- Gartner 2024: até 2029 >95% das organizações com containers em produção (vs <50% em 2023); 35% das apps empresariais em containers (vs <15%); >80% dos COTS em container (vs <30%); até 2028, 80% do software na borda em containers (vs 10%). Casos de uso: microsserviços, DevOps, portabilidade, modernização de legado `[PUC-AULA: 22–24]`.

## 3. Imagem, container, registry e ciclo de vida

- **Imagem**: conjunto de instruções/camadas **somente leitura** sobrepostas, geradas pelo Dockerfile. **Container** = imagem + **camada gravável** do container `[PUC-AULA: Criando containers, 5]`.
- **Registry**: armazena imagens; nome `[Host[:PORT]/][Namespace/]Repository:TAG`; `latest` = último gerado `[PUC-AULA: Criando containers, 12]`.
- **Anatomia**: `docker [subcomando] -[opções] imagem [cmd/args]` (ex.: `run` = `container run`, `images` = `image ls`) `[PUC-AULA: Ciclo de vida, 3]`.

| Comando | Faz |
|---|---|
| `run` | cria **e** executa |
| `exec` | executa comando em container em execução |
| `ps` / `ps -a` | lista em execução / todos |
| `build` | constrói imagem |
| `pull` / `push` | baixa / envia imagem ao registry |
| `images` | lista imagens |
| `login` / `logout` / `search` / `version` / `info` | |

`[PUC-AULA: Ciclo de vida, 4]`

- **Estados**: `Created → Running ⇄ Paused → Stopped → Deleted`
  - `create` → Created; `start` → Running; `pause`/`unpause`; `stop` → Stopped; `start` volta a Running; `rm` → Deleted `[PUC-AULA: Ciclo de vida, 6–8]`.
  - `docker run` = `pull` (se preciso) + `create` + `start`.
- Opções de lab que caem em pergunta `[PUC-AULA: Ciclo de vida, 9–21]`:
  - `-it` interativo + TTY; `docker start -ai` inicia anexado; **Ctrl+P Ctrl+Q** = *detach* sem parar; `docker attach` reanexa.
  - `--rm` remove ao terminar; `-d` desanexado (background); `-e VAR=valor` variável de ambiente; `--name`.
  - `-v ./dir:/dir` monta diretório do host; arquivos criados no `/tmp` do container **não** aparecem no host.
  - Sem `-p`, a porta 80 do nginx fica só no container (`80/tcp`); `--publish 8080:80` → host:8080 → container:80.

## 4. Dockerfile e build

```dockerfile
FROM ubuntu:22.04
LABEL mantainer=fams@linuxplace.com.br
RUN apt-get update -y && apt-get install --no-install-recommends python3 -y
COPY ./www/ /var/www/html
EXPOSE 8080
WORKDIR /var/www/html
ENTRYPOINT [ "python3", "-m", "http.server", "8080" ]
```
`[PUC-AULA: Criando containers, 3 e 18 — versão otimizada]`

| Instrução | Função |
|---|---|
| `FROM` | imagem de origem |
| `COPY` | copia do host para a camada |
| `ADD` | como COPY, mas aceita **URL remota** e **descompacta tar.gz** |
| `RUN` | executa comando na camada corrente |
| `ENTRYPOINT` | comando executado na criação do container |
| `CMD` | **parâmetros** para o ENTRYPOINT |
| `LABEL` | metadados (MAINTAINER é uso comum) |
| `EXPOSE` | portas que **podem** ser liberadas (documenta; não publica) |
| `ENV` | variáveis de ambiente |
| `USER` | usuário a partir dali |
| `WORKDIR` | diretório corrente a partir dali |
| `SHELL` | shell usado em RUN, CMD e ENTRYPOINT |

`[PUC-AULA: Criando containers, 8–10]`

- **Camadas**: criadas por instruções que alteram o filesystem — `FROM`, `COPY`, `ADD`, `RUN` (se gerar alteração). `ENV`, `USER`, `WORKDIR`, `SHELL` alteram metadados e **invalidam o cache** `[PUC-AULA: 11]`.
- **Otimização** (lab 7, passo 5): colocar o `RUN apt-get install` **antes** do `COPY` do conteúdo → mudar o site não invalida a camada pesada de pacotes `[PUC-AULA: 18]`.
- Build: `docker build . -t myapp` (contexto = diretório) `[PUC-AULA: 4]`. Imagem derivada: `FROM py-web:04` + `COPY` (lab 8) `[PUC-AULA: 21]`.
- Publicar: `docker tag`, `docker login`, `docker push` — aviso: senha guardada **sem criptografia** em `~/.docker/config.json` `[PUC-AULA: 22]`.

## 5. Internals: "não existem containers no kernel"

Container = junção de **namespaces + cgroups + capabilities + pivot_root** `[PUC-AULA: Conteiner Internals, 2]`.

| Namespace | Isola |
|---|---|
| **Mount** | pontos de montagem |
| **PID** | árvore de processos; o 1º processo vira **PID 1** |
| **Network** | pilha IP, rotas, firewall, interfaces |
| **UTS** | hostname (indispensável para nomes de containers) |
| **IPC** | SysV IPC: memória compartilhada, semáforos, filas |
| **User** | usuários/UIDs e privilégios |

`[PUC-AULA: 19, 25–29]`

- **pivot_root**: muda a raiz do sistema para um novo diretório (diferente de chroot: troca a raiz do mount namespace e permite desmontar a antiga). Demo: `docker export $(docker create busybox) | tar -C rootfs -xf -`, `unshare -m`, `mount --bind`, `pivot_root . old_root`, `umount -l /old_root` `[PUC-AULA: 20–24]`.
- `unshare` cria namespaces e executa comando; `nsenter` executa comando em namespace existente `[PUC-AULA: 16]`.
- **cgroups** (Google 2006, *process groups*): controle de recursos dividido em *controllers* — cpu, memory, io; expostos via VFS `[PUC-AULA: 31]`.
- Recap Linux: kernel × userland × distribuição; VFS; PID/fork/clone; bridge e **veth** (interface virtual que conecta namespaces); netfilter; uid/gid em `/etc/passwd` e `/etc/group` `[PUC-AULA: 4–13]`.

## 6. Volumes e redes

- **Storage driver** monta as camadas: **overlay2** (padrão), BTRFS, ZFS `[PUC-AULA: Volumes And Network, 5]`.
- **Volumes não são camadas**: não armazene dados nem logs no container; semelhante a host mount; tipos **local, tmpfs, plugins (NFS, iSCSI)** `[PUC-AULA: 7]`.
- `docker volume create --label <nome>`; `--driver <driver> --opt` `[PUC-AULA: 9]`.
- Rede padrão: bridge **docker0**; container recebe IP, sai por **NAT** do host; containers na mesma rede se acessam **sem `-p`**; `-p <addr:porta_local>:<porta_container>` publica `[PUC-AULA: 15]`.
- Comandos: `docker network ls | inspect | create --driver | connect | disconnect` `[PUC-AULA: 16]`.

| Driver | Uso |
|---|---|
| **bridge** | padrão |
| **host** | remove isolamento de rede entre host e container |
| **none** | isola o container (sem rede) |
| **overlay** | conexão **entre hosts** |
| **ipvlan** | controle total do endereçamento |
| **macvlan** | MAC próprio na placa física |

`[PUC-AULA: 17]`

## 7. Docker Engine e OCI

- Original: client `docker` → daemon `dockerd` → registry. 2015: plugins (libnetwork, VolumeAPI, AuthZ), docker-machine, compose, swarm, Docker Trust. **2017**: `dockerd` → **containerd** → **containerd-shim** → **runc** `[PUC-AULA: Docker Engines, 3–6]`.
- Papéis `[PUC-AULA: 8]`:
  - **dockerd**: expõe APIs, gerencia volumes, imagens, rede.
  - **containerd**: ciclo de vida; download do registry.
  - **runc**: runtime padrão OCI (low-level); monta e executa o container.
  - **shim**: pai dos processos do container; permite o containerd sair/reiniciar sem matar containers.
- Runtimes alternativos sob o containerd: **gVisor**, **Kata** `[PUC-AULA: 7]`.
- **OCI** (2015): **image-spec**, **runtime-spec**, **distribution-spec**; runc `[PUC-AULA: 9]`.

## 8. Registry

- Registry local: `docker run -d -p 5000:5000 --name registry registry:2.8.3`; `docker tag myimage localhost:5000/myimage:latest`; `docker push ...` `[PUC-AULA: Docker Registry, 3]`. Config em `/etc/docker/registry/config.yml`, dados em `/var/lib/registry` `[PUC-AULA: 4–5]`.
- **Docker Hub**: oficial, público/privado, Docker Trust, scan, build remoto; recursos avançados pagos.
- **ECR (AWS)**: IAM, **tags imutáveis**, scanner, custo de S3, menor integração ao cliente docker.
- **GCR (GCP)**: IAM do GCP, público/privado, scanner, exige ferramentas do GCP. Outros: **Harbor** `[PUC-AULA: 2, 6–10]`.

## 9. Logs

- Gerenciados pelo **daemon**; capturam **STDOUT e STDERR** (e STDIN) do **primeiro processo e seus filhos** `[PUC-AULA: Docker Logs, 2]`.
- Config global em **`/etc/docker/daemon.json`**: `"log-driver": "json-file"`, `"log-opts": {"max-size": "10m", "max-file": "3"}` `[PUC-AULA: 5]`.
- `docker logs <id>` com `--details`, `--since`, `--until`, `-f/--follow`, `-n` `[PUC-AULA: 6–7]`; por container: `docker run --log-driver <driver>` `[PUC-AULA: 8]`.
- Pegadinhas `[PUC-AULA: 9]`: mudança no daemon.json vale só para **novos containers após restart do daemon**; serviço remoto de log indisponível pode causar instabilidade; **`docker logs` só funciona com dados locais** (desabilitar o cache tira essa possibilidade).

## 10. Segurança

- Mesmas regras de sempre: defesa em profundidade, **processo e não projeto**, **menor privilégio**, preocupação maior com comunicação `[PUC-AULA: Segurança, 2]`.
- Camadas do kernel: namespaces, cgroups, **capabilities**, **seccomp**, **LSM** (SELinux/AppArmor) `[PUC-AULA: 3]`.
- **Build / Ship / Run** `[PUC-AULA: 4]`: build (imagem, software, workstation) · ship (assinatura de imagens, TLS, registry) · run (container, host, daemon, rede).
- Imagem: bases seguras, de preferência **from scratch**; scan (Clair, quay.io, Aqua, Container Analysis) `[PUC-AULA: 6]`. Imagens confiáveis: **Notary, cosign** `[PUC-AULA: 8]`.
- Menor privilégio: **não executar como root**, remover capabilities, perfis seccomp, SELinux `[PUC-AULA: 7]`.
- Host: hardening, OS mínimo (**Bottlerocket, RancherOS, Alpine**) — "menos binários, menos problemas" `[PUC-AULA: 10–12]`.
- **Docker Content Trust**: `export DOCKER_CONTENT_TRUST=1` → push/pull só de imagens assinadas `[PUC-AULA: 13]`.
- Capabilities padrão do Docker (14): CHOWN, DAC_OVERRIDE, FSETID, FOWNER, MKNOD, NET_RAW, SETGID, SETUID, SETFCAP, SETPCAP, NET_BIND_SERVICE, SYS_CHROOT, KILL, AUDIT_WRITE `[PUC-AULA: 14]`.

## 11. Desenvolvimento e Docker Compose

- Dev com containers: backends locais, testes, toolchain; **devcontainers** integrados ao VS Code/JetBrains; **LocalStack** simula serviços de nuvem `[PUC-AULA: DevContainers, 2–9]`.
- **Compose**: gerencia múltiplos containers (serviços, rede, storage) via **YAML** `[PUC-AULA: Docker Compose, 2]`; nomes aceitos: `compose.yaml`, `compose.yml`, `docker-compose.yaml`, `docker-compose.yml`; usa o **diretório corrente**; spec em compose-spec `[PUC-AULA: 6]`.
- Top level: `name`, `services`, `volumes`, `configs` (montado na raiz), `secrets` (montado em **`/var/run/secrets`**), `networks`; configs/secrets comuns no Swarm `[PUC-AULA: 11]`.
- Em `services`: `image`, `environment`, **`expose`** (porta para **outros containers**), **`ports`** (para o **host**), `logging`, `links` (*deprecated*), `networks`, `volumes`, **`depends_on`** (ordem de inicialização), `build` (`context`; usado com `image` quando a imagem não existe) `[PUC-AULA: 12, 18]`.
- Redes: conectividade externa por padrão; `internal: true` bloqueia acesso ao mundo; DNS por nome do serviço **só dentro da rede** `[PUC-AULA: 14–15]`.
- Variáveis: `${VAR}` e default `${VAR:-default}` `[PUC-AULA: 17]`.
- Cheat-sheet: `up`, `up -d`, `down` (para **e remove** containers), `start/stop [serviço]`, `logs <serviço>` `[PUC-AULA: 19]`.

---

## Autoteste (respostas no fim)

1. Qual instrução do Dockerfile aceita URL remota e descompacta tar.gz?
2. Qual a diferença entre `EXPOSE` e `-p`/`ports`?
3. Quais instruções criam camadas? Quais só invalidam o cache?
4. Qual namespace permite que o container tenha hostname próprio?
5. Qual componente permite reiniciar o containerd sem derrubar os containers?
6. Qual o runtime de referência da OCI, e quais as três especificações OCI?
7. Qual driver de rede conecta containers em hosts diferentes?
8. Uma mudança de `log-driver` no `daemon.json` afeta os containers já existentes?
9. Em que ano e em que sistema surgiu o chroot? E as Jails?
10. Kubernetes foi inspirado em qual sistema do Google?
11. Qual sequência sai de um container interativo sem pará-lo?
12. `docker compose down` faz o quê, além de parar os containers?
13. Onde são montados os `secrets` do Compose?
14. Qual variável ativa o Docker Content Trust?
15. Qual o storage driver padrão?

<details><summary>Respostas</summary>

1. `ADD`. 2. `EXPOSE` só documenta/declara; `-p`/`ports` publica no host. 3. Criam: FROM, COPY, ADD, RUN; invalidam cache: ENV, USER, WORKDIR, SHELL. 4. UTS. 5. containerd-shim. 6. runc; image-spec, runtime-spec, distribution-spec. 7. overlay. 8. Não: só novos containers após restart do daemon. 9. 1979, Unix V7; Jails em 2000, FreeBSD 4.0. 10. Borg. 11. Ctrl+P Ctrl+Q. 12. Remove os containers (e a rede padrão do projeto `[OFICIAL]`). 13. `/var/run/secrets`. 14. `DOCKER_CONTENT_TRUST=1`. 15. overlay2.
</details>

## Lacunas

- O teste é uma ferramenta externa (`external_tool`) no Canvas: número de questões, tempo e tentativas **não confirmados** pela API.
- Slides com imagem sem texto (ex.: "Instalando Docker", diagramas de rede) não foram cobertos; a videoaula de instalação (68 MB) não foi baixada.
- Exercícios práticos do professor: https://github.com/fams/cursodocker (não clonado ainda).
