<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <b>Português</b> |
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

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Transferir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Tipos de letra</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Um emulador de PlayStation 2 para testar e desenvolver homebrew, feito para ser conduzido por si ou por um agente de IA.**

O RIPPCSX2 é o PCSX2 v2.9.96 com as alterações de que um programador de homebrew da PS2 precisa para ver a coisa real: modos de vídeo HD mostrados, gravados e capturados como uma TV HD os mostra, e o ponto de paragem de dados por hardware do EE, para que os menus dentro do jogo e as ferramentas de modo de vídeo que se ligam aos registos do GS (o GSM do Open PS2 Loader, o menu dentro do jogo do RIPPS2) funcionem como numa consola. Tudo o resto é PCSX2 puro. Nasceu como o laboratório de testes do front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) e destina-se a quem faz homebrew, temas ou ferramentas para a PS2.

**[Vê o site](https://akilluminati47.github.io/RIPPCSX2/)**: desmonta uma PS2 ou fá-la explodir, com tudo sobre o RIPPCSX2 no painel Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Transferir o RIPPCSX2 (zip para Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ou 11, x64, um processador com AVX2. Descompacte onde quiser, abra `pcsx2-qtx64-avx2.exe` e indique o seu próprio dump de BIOS. O zip traz um `portable.txt` vazio junto ao exe, por isso o RIPPCSX2 guarda todas as definições e ficheiros na sua própria pasta: um PCSX2 que já tenha instalado mantém as suas definições, intactas. A versão contém sempre a compilação mais recente ([a sua página](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); os clips abaixo estão em [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Transferir o RIPPCSX2 (AppImage para Linux)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, um CPU com AVX2. Torna-o executável e inicia-o. É novo nesta versão e é compilado pelo mesmo fluxo do zip do Windows, mas ainda não foi executado numa máquina Linux: diz-nos como correu. O botão da barra de tarefas para execuções ocultas é só do Windows.

**Executa programas `.elf` para testes:** System > Start File, ou `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, e o programa arranca como arrancaria a partir de um cartão de memória ou de uma pen USB numa PS2. **Comporta-se como hardware real**: um ELF que lança outro ELF entrega-lhe a máquina e desaparece, um menu dentro do jogo que se liga ao GS desenha por cima da imagem real do jogo, e desligar fecha a VM como uma consola a desligar-se.

<a id="see-it-work"></a>

## Veja-o a funcionar

Cada clip é uma execução real do laboratório nesta compilação, cortada para menos de 12 segundos.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Um agente de IA a testar um ELF.** Gravado a partir do canto inferior direito do ecrã do utilizador (barra de tarefas, parte da sessão do Claude): o Claude arranca o `RIPPS2.elf` no RIPPCSX2 num ambiente de trabalho oculto, lança Aqua Teen Hunger Force a partir da imagem do HDD e abre por cima o menu dentro do jogo do RIPPS2. O pequeno painel é a única coisa no ecrã; o utilizador mantém o teclado e o rato.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**O menu dentro do jogo, todas as funções.** L1+L2+R1+R2+SELECT+START sobre um jogo a correr: ACHIEVEMENTS, RESUME (o jogo continua), o menu outra vez sobre uma imagem posterior, depois POWER OFF, que fecha a VM. O menu sabe sobre que imagem desenhar porque o RIPPCSX2 emula o ponto de paragem de escrita de dados do EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Um ELF a lançar um ELF, como uma PS2 real.** O Memory Files do RIPPS2 abre `mc0:/RIPPS2/RIPPS2.ELF` (a compilação mais recente, copiada para o cartão) e executa-o. O RIPPS2 em execução passa a vez e desaparece; o novo carrega a partir do cartão e arranca na sua lista de jogos.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## O que ganha face ao PCSX2 v2.9.96 original

- **Um menu RIPPCSX2** entre Debug e Help: Run ELF e Run Last ELF, um Lab Monitor em direto, Test Steps, um Compatibility Report, os interruptores do fork e as pastas onde tudo fica.
- **RIPART,** nesse menu: a base de dados de arte do OPL Manager, 16.313 jogos lidos por intervalos de bytes da cópia de segurança em archive.org. Entradas de jogo falsas para avaliar um tema numa lista real sem jogos na unidade, uma lista de caixas de verificação com cada peça da arte de um jogo para manter ou deixar de fora, uma procura dos jogos de uma unidade sem capa, e uma pasta ART ou um `art.tar` para guardar tudo. As entradas falsas aparecem no OPL e no RIPPS2 e não arrancam; um ficheiro que já existe nunca é substituído. akilluminati47 ajudou a trazer para essa base de dados a arte PNG de 8 bits e os ícones de disco de 128 x 128.
- **O OPL original arranca jogos.** Um dispositivo `host` que um programa regista por si próprio recebe agora as suas próprias aberturas, por isso o reinício do IOP do OPL funciona. O original para em `file 'host0:' can't open`.
- **EXIT GAME chega ao navegador.** Perdia-se uma interrupção do SIO2 num reinício do IOP, o que deixava o OSDSYS à espera do cartão de memória com o ecrã preto.
- **Um botão na barra de tarefas para execuções ocultas.** Um PCSX2 iniciado num ambiente de trabalho oculto coloca um botão na tua barra de tarefas, para que um misturador de volume ou um mod de volume por aplicação o alcance como a qualquer outro programa.
- **Os modos HD aparecem corretos.** 720p e 1080i são mostrados em 16:9 (o original desenha-os em 4:3), em qualquer definição de proporção exceto Stretch.
- **Gravações e capturas em HD.** F11 grava 720p a 1280 x 720 e 1080i a 1920 x 1080 (ou isso vezes o aumento de resolução), marcados como 16:9; F8 guarda capturas nos mesmos tamanhos. O original dá 640 x 480 ou o buffer bruto com 640 de largura.
- **Uma mudança de modo a meio da gravação** continua num ficheiro novo com o novo tamanho, em vez de se espremer no primeiro.
- **1080i no sítio certo.** O original sobe uma imagem 1080i 42 linhas (corte em cima, faixa preta em baixo); o RIPPCSX2 começa-a na linha 40, onde começa a temporização da própria consola.
- **Ponto de paragem de escrita de dados do EE** (novo no rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funciona: uma escrita num endereço vigiado lança a exceção de depuração de nível 2 em `0x80000100` antes de ser executada, no interpretador e no recompilador. O GSM do OPL e o menu dentro do jogo do RIPPS2 precisam dele para saber que imagem um jogo mostra.
- **Linhas de registo do modo de vídeo.** Cada mudança de modo regista a temporização de sincronismo e os registos de ecrã (`RIPPCSX2: video mode ...` em `logs/emulog.txt`).
- **Sem ofertas do atualizador automático.** As etiquetas de versão mantêm desligado o atualizador do PCSX2, por isso nunca o "atualiza" de volta para o original.
- A definição padrão fica intocada: as capturas em 480i são idênticas byte a byte às do original. `HDTVOutput = false` em `[EmuCore/GS]` no `inis/PCSX2.ini` repõe o comportamento HD original para comparar lado a lado.

<a id="what-it-is-for"></a>

## Para que serve

- **Criadores de temas** (Open PS2 Loader, RiptOPL, RIPPS2): avalie um tema em 720p e 1080i como uma TV o mostra, e faça pré-visualizações em tamanho real e vídeos de apresentação.
- **Programadores de homebrew:** teste ELF que mudam de modo de vídeo, se ligam ao GS ou usam os registos de depuração do EE, e leia no registo os valores exatos de ecrã que um modo define.
- **Menus dentro do jogo e ferramentas do GS:** o GSM do OPL, o menu dentro do jogo do RIPPS2 e tudo o resto assente no ponto de paragem de escrita de dados funcionam no emulador e não só no hardware.
- **Jogos de PS1:** executa o Ember e os seus jogos de PS1 a partir de uma unidade virtual para testar o arranque e as listas de PS1, com a tua própria BIOS de PS1 na unidade.
- **Testes automatizados e assistidos por IA:** execuções com guião num ambiente de trabalho oculto, com capturas, gravações, estados guardados e leituras de memória por PINE, sem tomar conta do seu PC.

<a id="the-end-goal-the-whole-library"></a>

## O objetivo final: a biblioteca inteira

O maior trabalho pela frente é testar jogos de PS2 pelo próprio caminho de código do Open PS2 Loader, tal como uma consola os executa, e registar o que cada um precisa: ELFs, KELFs, aplicações homebrew e jogos num ambiente isolado do OPL, com os seus modos de compatibilidade testados automaticamente. Alguém poderá usar isto para pôr a biblioteca inteira a funcionar um dia. Esse é o objetivo final do RIPPCSX2.

O Compatibility Report é o primeiro passo: o resultado de um jogo, os modos do OPL usados e o estado da máquina, guardados em `reports/` como um ficheiro e uma linha em `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para agentes de IA, LLM e os seus utilizadores

Este repositório está escrito para que um agente consiga configurar tudo ao utilizador só com a ligação. Dê ao seu assistente `https://github.com/akilluminati47/RIPPCSX2` e peça-lhe que instale o RIPPCSX2; tudo aquilo de que precisa está aqui:

1. **Obtenha a compilação:** `RIPPCSX2-windows-x64-avx2.zip` da versão contínua ([ligação direta](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ou `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Descompacte-o numa pasta só sua; o `portable.txt` já está junto ao exe, por isso nunca toca nas definições de um PCSX2 instalado.
2. **BIOS:** o utilizador fornece o dump de BIOS da sua própria consola (nunca descarregue um): coloque-o na pasta `bios` junto ao exe (ou aponte `[Folders] Bios` em `inis/PCSX2.ini` para ele) e escolha-o no assistente da primeira execução (`[Filenames] BIOS`).
3. **Execute algo:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ou `-- <game.iso>`. As definições são INI simples em `inis/PCSX2.ini`; os registos vão para `logs/emulog.txt` (`[Logging] EnableEEConsole = true` acrescenta o printf do EE).
4. **Controle-o e observe-o:** F8 captura de ecrã (`snaps/`), F11 gravação (`videos/`), F1 estado guardado (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) para ler e escrever a memória da PS2 a partir de um script.
5. **Teste sem roubar o ecrã:** [`ripps2-lab/`](ripps2-lab/README.md) descreve uma instalação de laboratório (`install-lab.ps1` coloca uma compilação numa pasta portátil e mantém os seus cartões, definições e gravações), e o `tools/dev/ps2bg.ps1` do repositório do RIPPS2 executa listas de passos (botões, esperas, capturas, gravações) num ambiente de trabalho oculto com um painel na barra de tarefas que o utilizador pode ver, parar ou assumir.

O que mudou e porquê, ficheiro a ficheiro: **[RIPPCSX2.md](RIPPCSX2.md)**. Agentes que trabalhem no código deste fork: nunca abram pull requests, issues nem comentários no projeto PCSX2 (o seu `AGENTS.md` proíbe contribuições feitas por IA); o RIPPCSX2 continua a ser um fork.

**Sem ligação à equipa do PCSX2.** GPL-3.0 como o PCSX2. Comunique problemas do RIPPCSX2 ao RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nunca ao PCSX2. Segue-se o README do próprio PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

O PCSX2 é um emulador de PlayStation 2 (PS2) livre e de código aberto. O seu objetivo é emular o hardware da PS2 usando uma combinação de [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) de CPU MIPS, [Recompiladores](https://en.wikipedia.org/wiki/Dynamic_recompilation) e uma [Máquina Virtual](https://en.wikipedia.org/wiki/Virtual_machine) que gere os estados do hardware e a memória do sistema da PS2. Isto permite-lhe jogar jogos da PS2 no seu PC, com muitas funcionalidades e vantagens adicionais.

<a id="project-details"></a>

## Detalhes do projeto

O PCSX2 está em desenvolvimento há mais de 20 anos. As versões antigas só corriam umas poucas demos de domínio público, mas as mais recentes correm a maioria dos jogos à velocidade total, incluindo títulos populares como Final Fantasy X e Devil May Cry 3. Visite a [lista de compatibilidade do PCSX2](https://pcsx2.net/compat/) para ver o estado de compatibilidade mais recente dos jogos (com mais de 2500 títulos testados).

Os instaladores e binários das versões estáveis e nightly estão disponíveis no [nosso site](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Requisitos do sistema

O PCSX2 suporta Windows, Linux e Mac. A nossa [página de documentação de configuração](https://pcsx2.net/docs/setup/requirements) tem mais detalhes sobre requisitos de software e hardware.

Tenha em atenção que, para usar o emulador, é necessário um dump de BIOS de uma consola PS2 adquirida legitimamente. Para mais informações, visite [esta página](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuir / Compilar

O PCSX2 suporta tradução para outras línguas através do [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Consulte o [Guia de contribuição](https://pcsx2.net/docs/contributing/) para saber mais sobre como contribuir.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Transferir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Tipos de letra</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

