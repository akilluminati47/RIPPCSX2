<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <b>Português (Brasil)</b> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.it.md">Italiano</a> |
  <a href="README.nl.md">Nederlands</a> |
  <a href="README.da.md">Dansk</a> |
  <a href="README.sv.md">Svenska</a> |
  <a href="README.pl.md">Polski</a> |
  <a href="README.cs.md">Čeština</a> |
  <a href="README.hr.md">Hrvatski</a> |
  <a href="README.sr.md">Srpski</a> |
  <a href="README.bg.md">Български</a> |
  <a href="README.ru.md">Русский</a> |
  <a href="README.el.md">Ελληνικά</a> |
  <a href="README.hu.md">Magyar</a> |
  <a href="README.ro.md">Română</a> |
  <a href="README.gl.md">Galego</a> |
  <a href="README.sq.md">Shqip</a> |
  <a href="README.tr.md">Türkçe</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fa.md">فارسی</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Tradução do README em inglês; se diferirem, vale o inglês. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Baixar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Um emulador de PlayStation 2 para testar e desenvolver homebrew, feito para ser controlado por você ou por um agente de IA.**

O RIPPCSX2 é o PCSX2 v2.9.96 com as mudanças de que um desenvolvedor de homebrew de PS2 precisa para ver a coisa real: modos de vídeo HD exibidos, gravados e capturados do jeito que uma TV HD os mostra, e o breakpoint de dados por hardware do EE, para que menus dentro do jogo e ferramentas de modo de vídeo que interceptam os registradores do GS (o GSM do Open PS2 Loader, o menu dentro do jogo do RIPPS2) funcionem como num console. Todo o resto é PCSX2 puro. Ele nasceu como o laboratório de testes do front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) e é feito para quem cria homebrew, temas ou ferramentas para PS2.

**[Veja o site](https://akilluminati47.github.io/RIPPCSX2/)**: desmonte um PS2 ou exploda um, com tudo sobre o RIPPCSX2 no painel Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Baixar o RIPPCSX2 (zip para Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ou 11, x64, uma CPU com AVX2. Descompacte onde quiser, abra `pcsx2-qtx64-avx2.exe` e aponte para o seu próprio dump de BIOS. O zip traz um `portable.txt` vazio ao lado do exe, então o RIPPCSX2 guarda todas as configurações e arquivos na própria pasta: um PCSX2 que você já tenha instalado mantém as configurações dele, intactas. O release sempre tem a build mais nova ([a página dele](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); os clipes abaixo estão em [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Baixar o RIPPCSX2 (AppImage para Linux)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, uma CPU com AVX2. Torne-o executável e inicie-o. É novo nesta versão e é compilado pelo mesmo fluxo do zip do Windows, mas ainda não foi executado em uma máquina Linux: conte para nós como foi. O botão da barra de tarefas para execuções ocultas é só do Windows.

**Ele roda programas `.elf` para teste:** System > Start File, ou `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, e o programa inicia como iniciaria de um memory card ou pendrive num PS2. Ele **se comporta como hardware real**: um ELF que inicia outro ELF passa a máquina adiante e some, um menu dentro do jogo que intercepta o GS desenha sobre o quadro real do jogo, e desligar fecha a VM como um console sendo desligado.

<a id="see-it-work"></a>

## Veja funcionando

Cada clipe é uma execução real do laboratório nesta build, cortada para menos de 12 segundos.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Um agente de IA testando um ELF.** Gravado do canto inferior direito da tela do usuário (barra de tarefas, parte da sessão do Claude): o Claude inicia o `RIPPS2.elf` no RIPPCSX2 numa área de trabalho oculta, inicia Aqua Teen Hunger Force pela imagem do HDD e abre por cima o menu dentro do jogo do RIPPS2. O painelzinho é a única coisa na tela; o usuário continua com o teclado e o mouse.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**O menu dentro do jogo, todas as funções.** L1+L2+R1+R2+SELECT+START sobre um jogo rodando: ACHIEVEMENTS, RESUME (o jogo continua), o menu de novo sobre um quadro posterior, depois POWER OFF, que fecha a VM. O menu sabe sobre qual quadro desenhar porque o RIPPCSX2 emula o breakpoint de escrita de dados do EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Um ELF iniciando um ELF, como num PS2 real.** O Memory Files do RIPPS2 abre `mc0:/RIPPS2/RIPPS2.ELF` (a build mais nova, copiada para o cartão) e o executa. O RIPPS2 em execução passa a vez e some; o novo carrega do cartão e inicia na lista de jogos.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## O que você ganha em relação ao PCSX2 v2.9.96 puro

- **Um menu RIPPCSX2** entre Debug e Help: Run ELF e Run Last ELF, um Lab Monitor ao vivo, Test Steps, um Compatibility Report, os interruptores do fork e as pastas onde tudo fica.
- **RIPART,** nesse menu: o banco de dados de arte do OPL Manager, 16.313 jogos lidos por intervalos de bytes do backup em archive.org. Entradas de jogo falsas para avaliar um tema em uma lista real sem jogos na unidade, uma lista de caixas de seleção com cada peça da arte de um jogo para manter ou deixar de fora, uma busca pelos jogos de uma unidade sem capa, e uma pasta ART ou um `art.tar` para guardar tudo. As entradas falsas aparecem no OPL e no RIPPS2 e não iniciam; um arquivo que já existe nunca é substituído. akilluminati47 ajudou a trazer para esse banco de dados a arte PNG de 8 bits e os ícones de disco de 128 x 128.
- **O OPL original inicia jogos.** Um dispositivo `host` que um programa registra por conta própria agora recebe suas próprias aberturas, então o reboot do IOP do OPL funciona. O original para em `file 'host0:' can't open`.
- **EXIT GAME chega ao navegador.** Uma interrupção do SIO2 se perdia em um reboot do IOP, o que deixava o OSDSYS esperando o cartão de memória com a tela preta.
- **Um botão na barra de tarefas para execuções ocultas.** Um PCSX2 iniciado em uma área de trabalho oculta coloca um botão na sua barra de tarefas, assim um mixer de volume ou um mod de volume por aplicativo o alcança como qualquer outro programa.
- **Modos HD aparecem certos.** 720p e 1080i são exibidos em 16:9 (o original desenha em 4:3), em qualquer configuração de proporção exceto Stretch.
- **Gravações e capturas em HD.** F11 grava 720p em 1280 x 720 e 1080i em 1920 x 1080 (ou isso vezes o upscale), marcado como 16:9; F8 salva capturas nos mesmos tamanhos. O original dá 640 x 480 ou o buffer bruto de 640 de largura.
- **Uma troca de modo no meio da gravação** continua num arquivo novo no novo tamanho, em vez de se espremer no primeiro.
- **1080i no lugar certo.** O original sobe uma imagem 1080i em 42 linhas (corte em cima, faixa preta embaixo); o RIPPCSX2 a começa na linha 40, onde a própria temporização do console começa.
- **Breakpoint de escrita de dados do EE** (novo no rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funciona: uma escrita num endereço vigiado dispara a exceção de depuração de nível 2 em `0x80000100` antes de executar, no interpretador e no recompilador. O GSM do OPL e o menu dentro do jogo do RIPPS2 precisam disso para saber qual quadro um jogo mostra.
- **Linhas de log de modo de vídeo.** Toda troca de modo registra a temporização de sincronia e os registradores de exibição (`RIPPCSX2: video mode ...` em `logs/emulog.txt`).
- **Sem ofertas do atualizador automático.** As tags de release mantêm o atualizador do PCSX2 desligado, então ele nunca te "atualiza" de volta para o original.
- A definição padrão fica intocada: capturas em 480i são idênticas byte a byte às do original. `HDTVOutput = false` em `[EmuCore/GS]` no `inis/PCSX2.ini` traz de volta o comportamento HD original para comparar lado a lado.

<a id="what-it-is-for"></a>

## Para que serve

- **Criadores de temas** (Open PS2 Loader, RiptOPL, RIPPS2): avalie um tema em 720p e 1080i como uma TV mostra, e faça prévias em tamanho real e vídeos de demonstração.
- **Desenvolvedores de homebrew:** teste ELFs que trocam de modo de vídeo, interceptam o GS ou usam os registradores de depuração do EE, e leia no log os registradores de exibição exatos que um modo define.
- **Menus dentro do jogo e ferramentas de GS:** o GSM do OPL, o menu dentro do jogo do RIPPS2 e qualquer outra coisa baseada no breakpoint de escrita de dados rodam no emulador, não só no hardware.
- **Jogos de PS1:** rode o Ember e seus jogos de PS1 a partir de uma unidade virtual para testar a inicialização e as listas de PS1, com a sua própria BIOS de PS1 na unidade.
- **Testes automatizados e assistidos por IA:** execuções roteirizadas numa área de trabalho oculta com capturas, gravações, save states e leituras de memória por PINE, sem tomar conta do seu PC.

<a id="the-end-goal-the-whole-library"></a>

## O objetivo final: a biblioteca inteira

O maior trabalho pela frente é testar jogos de PS2 pelo próprio caminho de código do Open PS2 Loader, do jeito que um console os roda, e registrar o que cada um precisa: ELFs, KELFs, aplicativos homebrew e jogos em um ambiente isolado do OPL, com seus modos de compatibilidade testados automaticamente. Alguém poderia usar isto para fazer a biblioteca inteira rodar um dia. Esse é o objetivo final do RIPPCSX2.

O Compatibility Report é o primeiro passo: o resultado de um jogo, os modos do OPL usados e o estado da máquina, salvos em `reports/` como um arquivo e uma linha em `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para agentes de IA, LLMs e seus usuários

Este repositório foi escrito para que um agente consiga configurar tudo para o usuário só com o link. Dê ao seu assistente `https://github.com/akilluminati47/RIPPCSX2` e peça para instalar o RIPPCSX2; tudo de que ele precisa está aqui:

1. **Pegue a build:** `RIPPCSX2-windows-x64-avx2.zip` do release contínuo ([link direto](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ou `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Descompacte numa pasta só dele; o `portable.txt` já está ao lado do exe, então ele nunca mexe nas configurações de um PCSX2 instalado.
2. **BIOS:** o usuário fornece o dump de BIOS do próprio console (nunca baixe um): coloque na pasta `bios` ao lado do exe (ou aponte `[Folders] Bios` em `inis/PCSX2.ini` para ela) e escolha no assistente de primeira execução (`[Filenames] BIOS`).
3. **Rode alguma coisa:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ou `-- <game.iso>`. As configurações são INI simples em `inis/PCSX2.ini`; os logs vão para `logs/emulog.txt` (`[Logging] EnableEEConsole = true` acrescenta o printf do EE).
4. **Controle e observe:** F8 captura de tela (`snaps/`), F11 gravação (`videos/`), F1 save state (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) para ler e escrever a memória do PS2 por script.
5. **Teste sem roubar a tela:** [`ripps2-lab/`](ripps2-lab/README.md) descreve uma instalação de laboratório (`install-lab.ps1` coloca uma build numa pasta portátil e mantém cartões, configurações e gravações), e o `tools/dev/ps2bg.ps1` do repositório do RIPPS2 roda listas de passos (botões, esperas, capturas, gravações) numa área de trabalho oculta com um painel na barra de tarefas que o usuário pode acompanhar, parar ou assumir.

O que mudou e por quê, arquivo por arquivo: **[RIPPCSX2.md](RIPPCSX2.md)**. Agentes que trabalham no código deste fork: nunca abram pull requests, issues ou comentários no projeto PCSX2 (o `AGENTS.md` dele proíbe contribuições feitas por IA); o RIPPCSX2 continua sendo um fork.

**Sem ligação com a equipe do PCSX2.** GPL-3.0 como o PCSX2. Relate problemas do RIPPCSX2 ao RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nunca ao PCSX2. A seguir, o README do próprio PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

O PCSX2 é um emulador de PlayStation 2 (PS2) livre e de código aberto. Seu objetivo é emular o hardware do PS2 usando uma combinação de [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) de CPU MIPS, [Recompiladores](https://en.wikipedia.org/wiki/Dynamic_recompilation) e uma [Máquina Virtual](https://en.wikipedia.org/wiki/Virtual_machine) que gerencia os estados do hardware e a memória do sistema do PS2. Assim você pode jogar jogos de PS2 no seu PC, com muitos recursos e vantagens extras.

<a id="project-details"></a>

## Detalhes do projeto

O PCSX2 está em desenvolvimento há mais de 20 anos. Versões antigas só rodavam algumas demos de domínio público, mas as mais novas rodam a maioria dos jogos em velocidade total, incluindo títulos populares como Final Fantasy X e Devil May Cry 3. Visite a [lista de compatibilidade do PCSX2](https://pcsx2.net/compat/) para ver o status de compatibilidade mais recente dos jogos (com mais de 2500 títulos testados).

Instaladores e binários das builds estáveis e nightly estão disponíveis no [nosso site](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Requisitos do sistema

O PCSX2 roda em Windows, Linux e Mac. Nossa [página de documentação de instalação](https://pcsx2.net/docs/setup/requirements) tem mais detalhes sobre requisitos de software e hardware.

Observe que é necessário um dump de BIOS de um console PS2 obtido legalmente para usar o emulador. Para mais informações, visite [esta página](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuir / Compilar

O PCSX2 permite tradução para outros idiomas pelo [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Veja o [Guia de contribuição](https://pcsx2.net/docs/contributing/) para saber mais sobre como contribuir.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Baixar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

