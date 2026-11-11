<div align="center">

<img width="4726" height="1350" alt="logo (10)" src="https://github.com/user-attachments/assets/67b7d3c8-21b5-4d1e-8af2-d1b4a41a5b53" />

# UNIVERSIDADE DE SÃO PAULO — USP
## ESCOLA DE ENGENHARIA DE SÃO CARLOS
### DEPARTAMENTO DE ENGENHARIA ELÉTRICA E DE COMPUTAÇÃO — SEL

**SEL0337 — Projetos em Sistemas Embarcados**

---

### **Prática 5: Personalização de Serviços de Inicialização de S.O.**

**Docente:** Prof. Pedro de Oliveira Conceição Junior  

**Discentes:**  
- Gabriel Aparecido Lacerda Ambrosio (N° USP 16228848)  
- Érico Antônio Cabreira Paes Leme (N° USP 14746206)  

*São Carlos — 2026*

</div>

---

## 1. Introdução

Esta prática teve como objetivo explorar o processo de inicialização (*boot*) do sistema operacional Linux Embarcado na Raspberry Pi 3B+ e a automação de programas por meio do **systemd** (*Init System*). Em sistemas embarcados comerciais, é fundamental que as aplicações sejam inicializadas automaticamente no *power-on*, dispensando a necessidade de login manual de um usuário.

Além disso, abordou-se a utilização do **Git** e do **GitHub** como ferramentas essenciais de Controle de Versão (*VCS - Version Control System*) e documentação técnica diretamente a partir do ambiente embarcado.

---

## 2. Checkpoint 1 — Configuração do SystemD

No Checkpoint 1, analisaram-se as etapas de *boot* da Raspberry Pi (desde a inicialização da GPU via Bootloader até o carregamento do Kernel e montagem do *rootfs*) e criou-se uma unidade de serviço personalizada (*unit file*) para o **systemd**.

* **Desenvolvimento de Programa:** Além do programa egab_blink1.py, usado em práticas anteriores, para mudar o estado de um LED com um botão, fora feito um programa parada.py, para ser usado como ponto de parada do programa principal.
* **Criação do Unit File (`.service`):** Estruturou-se um arquivo de serviço contendo os blocos `[Unit]`, `[Service]` e `[Install]`.
  * **`ExecStart=`**: Responsável por invocar o interpretador Python e executar a aplicação principal durante o *boot*.
  * **`ExecStop=`**: Responsável por chamar um script de encerramento/interrupção caso o serviço seja pausado.
* **Gerenciamento de Serviço (`systemctl`):**
  * O arquivo `.service` foi copiado para o diretório `/lib/systemd/system/`.
  * Foram testados os comandos `sudo systemctl start`, `stop`, `status` e `enable`.
  * Com o serviço habilitado via `systemctl enable`, a aplicação foi executada automaticamente após a reinicialização da Raspberry Pi.

<div align="center">

<img width="1000" height="500" alt="WhatsApp Image 2026-11-11 at 20 06 06" src="https://github.com/user-attachments/assets/d5274994-c419-4c19-af36-b99aef6b4b58" />
*Figura 1: Montagem do circuito utilizado no Checkpoint 1.*

</div>

---

## 3. Checkpoint 2 — Git e GitHub

No Checkpoint 2, foi realizada a configuração do **Git** diretamente na Raspberry Pi para gerenciar o versionamento do projeto e sincronizar as alterações com o repositório remoto no **GitHub**.

* **Configuração de Usuário e Credenciais:**
  * Definição das variáveis globais `user.name` e `user.email`.
  * Configuração de autenticação segura através de *Personal Access Token* (PAT) gerado no GitHub.
* **Fluxo de Versionamento:**
  * Clonagem do repositório remoto na Raspberry Pi (`git clone`).
  * Adição dos scripts desenvolvidos (`.py`), do arquivo de serviço (`.service`).
  * Realização de commits (`git commit -m`).
  * Envio das atualizações para a nuvem (`git push origin main`).
* **Histórico de Commits:**
  * O histórico de alterações foi inspecionado através do comando `git log` e salvo no arquivo `historico_git.txt` para comprovação do fluxo de trabalho.


