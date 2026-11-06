<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
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
  <b>Galego</b> |
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

<p align="center"><sub>Tradución do README en inglés; se difiren, vale o inglés. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Un emulador de PlayStation 2 para probar e desenvolver homebrew, feito para que o manexes ti ou un axente de IA.**

RIPPCSX2 é PCSX2 v2.9.96 cos cambios que un desenvolvedor de homebrew de PS2 precisa para ver o real: os modos de vídeo HD amosados, gravados e capturados como os amosa un televisor HD, e o punto de interrupción de datos por hardware do EE, para que os menús dentro do xogo e as ferramentas de modo de vídeo que enganchan os rexistros do GS (o GSM de Open PS2 Loader, o menú dentro do xogo de RIPPS2) funcionen coma nunha consola. Todo o demais é PCSX2 normal. Naceu coma o laboratorio de probas do front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) e está pensado para calquera que faga homebrew, temas ou ferramentas para PS2.

**[Ver o sitio web](https://akilluminati47.github.io/RIPPCSX2/)**: desmonta unha PS2 ou faina estoupar, con todo sobre RIPPCSX2 no seu panel Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Descargar RIPPCSX2 (zip para Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ou 11, x64, unha CPU con AVX2. Descomprímeo onde queiras, abre `pcsx2-qtx64-avx2.exe` e indícalle o teu propio volcado de BIOS. O zip trae un `portable.txt` baleiro xunto ao exe, así que RIPPCSX2 garda todos os seus axustes e ficheiros no seu propio cartafol: un PCSX2 que xa teñas instalado conserva os seus axustes, intactos. A versión contén sempre a compilación máis nova ([a súa páxina](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); os clips de abaixo están en [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Descargar RIPPCSX2 (AppImage para Linux)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, unha CPU con AVX2. Faino executable e iníciao. É novo nesta versión e compílase co mesmo fluxo ca o zip de Windows, pero aínda non se executou nunha máquina Linux: cóntanos como che vai. O botón da barra de tarefas para as execucións ocultas é só para Windows.

**Executa programas `.elf` para probalos:** System > Start File, ou `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, e o programa arrinca coma o faría dende unha tarxeta de memoria ou un USB nunha PS2. **Compórtase coma o hardware real**: un ELF que lanza outro ELF cédelle a máquina e desaparece, un menú dentro do xogo que engancha o GS debúxase sobre o fotograma real do xogo, e apagar pecha a VM coma unha consola que se apaga.

<a id="see-it-work"></a>

## Véxao funcionar

Cada clip é unha execución real do laboratorio con esta compilación, recortada a menos de 12 segundos.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Un axente de IA probando un ELF.** Gravado dende a esquina inferior dereita da pantalla do usuario (barra de tarefas, parte da sesión de Claude): Claude arrinca `RIPPS2.elf` en RIPPCSX2 nun escritorio oculto, lanza Aqua Teen Hunger Force dende a imaxe do HDD e abre enriba o menú dentro do xogo de RIPPS2. O pequeno panel é o único en pantalla; o usuario conserva o teclado e o rato.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**O menú dentro do xogo, todas as súas funcións.** L1+L2+R1+R2+SELECT+START sobre un xogo en marcha: ACHIEVEMENTS, RESUME (o xogo segue), o menú outra vez sobre un fotograma posterior, e logo POWER OFF, que pecha a VM. O menú sabe sobre que fotograma debuxar porque RIPPCSX2 emula o punto de interrupción de escritura de datos do EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Un ELF lanzando un ELF, coma unha PS2 real.** Memory Files de RIPPS2 abre `mc0:/RIPPS2/RIPPS2.ELF` (a compilación máis nova, copiada á tarxeta) e execútaa. O RIPPS2 en marcha cede o control e desaparece; o novo carga dende a tarxeta e arrinca na súa lista de xogos.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## O que obtés fronte ao PCSX2 v2.9.96 normal

- **Un menú RIPPCSX2** entre Debug e Help: Run ELF e Run Last ELF, un Lab Monitor en directo, Test Steps, un Compatibility Report, os interruptores do fork e os cartafoles onde queda todo.
- **RIPART,** nese menú: a base de datos de arte de OPL Manager, 16.313 xogos lidos por intervalos de bytes desde a súa copia de seguranza en archive.org. Entradas de xogo chamariz para xulgar un tema nunha lista real sen xogos na unidade, unha lista de caixas con cada peza da arte dun xogo para conservala ou deixala fóra, unha busca dos xogos dunha unidade sen portada, e un cartafol ART ou un `art.tar` onde gardalo todo. Os chamarices aparecen en OPL e RIPPS2 e non arrincan; nunca se substitúe un ficheiro que xa existe. akilluminati47 axudou a levar a esa base de datos a súa arte PNG de 8 bits e as súas iconas de disco de 128 x 128.
- **OPL orixinal arrinca xogos.** Un dispositivo `host` que un programa rexistra por si mesmo recibe agora as súas propias aperturas, así que o reinicio do IOP de OPL funciona. O orixinal detense en `file 'host0:' can't open`.
- **EXIT GAME chega ao navegador.** Perdíase unha interrupción de SIO2 nun reinicio do IOP, e OSDSYS quedaba esperando a tarxeta de memoria coa pantalla en negro.
- **Un botón na barra de tarefas para as execucións ocultas.** Un PCSX2 iniciado nun escritorio oculto pon un botón na túa barra de tarefas, así un mesturador de volume ou un mod de volume por aplicación chégalle como a calquera outro programa.
- **Os modos HD vense ben.** 720p e 1080i amósanse en 16:9 (o orixinal debúxaos en 4:3), con calquera axuste de aspecto agás Stretch.
- **Gravacións e capturas en HD.** F11 grava 720p a 1280 x 720 e 1080i a 1920 x 1080 (ou iso polo escalado), marcado coma 16:9; F8 garda capturas aos mesmos tamaños. O orixinal dá 640 x 480 ou o búfer cru de 640 de ancho.
- **Un cambio de modo a metade da gravación** segue nun ficheiro novo co novo tamaño, no canto de encaixarse no primeiro.
- **1080i no seu sitio.** O orixinal sobe unha imaxe 1080i 42 liñas (cortada arriba, banda negra abaixo); RIPPCSX2 comézaa na liña 40, onde o fai a temporización da propia consola.
- **Punto de interrupción de escritura de datos do EE** (novo en rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funciona: unha escritura nun enderezo vixiado lanza a excepción de depuración de nivel 2 en `0x80000100` antes de executarse, no intérprete e no recompilador. O GSM de OPL e o menú dentro do xogo de RIPPS2 precísano para saber que fotograma amosa un xogo.
- **Liñas de rexistro do modo de vídeo.** Cada cambio de modo rexistra a temporización de sincronía e os rexistros de pantalla (`RIPPCSX2: video mode ...` en `logs/emulog.txt`).
- **Sen ofertas do actualizador automático.** As etiquetas de versión manteñen apagado o actualizador de PCSX2, así que nunca te "actualiza" de volta ao orixinal.
- A definición estándar queda intacta: as capturas a 480i son idénticas byte a byte ás do orixinal. `HDTVOutput = false` baixo `[EmuCore/GS]` en `inis/PCSX2.ini` devolve o comportamento HD orixinal para comparar.

<a id="what-it-is-for"></a>

## Para que serve

- **Creadores de temas** (Open PS2 Loader, RiptOPL, RIPPS2): xulga un tema en 720p e 1080i coma o amosa un televisor, e fai vistas previas a tamaño real e vídeos de percorrido.
- **Desenvolvedores de homebrew:** proba ELF que cambian de modo de vídeo, enganchan o GS ou usan os rexistros de depuración do EE, e le no rexistro os valores exactos de pantalla que fixa un modo.
- **Menús dentro do xogo e ferramentas do GS:** o GSM de OPL, o menú dentro do xogo de RIPPS2 e calquera outra cousa baseada no punto de interrupción de escritura de datos funcionan no emulador e non só no hardware.
- **Xogos de PS1:** executa Ember e os seus xogos de PS1 desde unha unidade virtual para probar o arranque e as listas de PS1, coa túa propia BIOS de PS1 na unidade.
- **Probas automatizadas e asistidas por IA:** execucións con guión nun escritorio oculto con capturas, gravacións, estados gardados e lecturas de memoria por PINE, sen apropiarse do teu PC.

<a id="the-end-goal-the-whole-library"></a>

## O obxectivo final: toda a biblioteca

O maior traballo pendente é probar xogos de PS2 polo propio camiño de código de Open PS2 Loader, tal como os executa unha consola, e anotar o que precisa cada un: ELF, KELF, aplicacións homebrew e xogos nun espazo illado de OPL, probando os seus modos de compatibilidade automaticamente. Alguén podería usar isto para facer funcionar toda a biblioteca algún día. Ese é o obxectivo final de RIPPCSX2.

O Compatibility Report é o seu primeiro paso: o resultado dun xogo, os modos de OPL usados e o estado da máquina, gardados en `reports/` como un ficheiro e unha fila en `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para axentes de IA, LLM e os seus usuarios

Este repositorio está escrito para que un axente poida configurarlle todo a un usuario só co ligazón. Dálle ao teu asistente `https://github.com/akilluminati47/RIPPCSX2` e pídelle que instale RIPPCSX2; todo o que precisa está aquí:

1. **Consegue a compilación:** `RIPPCSX2-windows-x64-avx2.zip` da versión continua ([ligazón directa](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ou `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Descomprímeo nun cartafol propio; o seu `portable.txt` xa está xunto ao exe, así que nunca toca os axustes dun PCSX2 instalado.
2. **BIOS:** o usuario achega o volcado de BIOS da súa propia consola (nunca o descargues): pono no cartafol `bios` xunto ao exe (ou apunta `[Folders] Bios` en `inis/PCSX2.ini` cara a el) e escólleo no asistente do primeiro arranque (`[Filenames] BIOS`).
3. **Executa algo:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ou `-- <game.iso>`. Os axustes son INI simple en `inis/PCSX2.ini`; os rexistros van a `logs/emulog.txt` (`[Logging] EnableEEConsole = true` engade o printf do EE).
4. **Manéxao e obsérvao:** F8 captura (`snaps/`), F11 gravación (`videos/`), F1 estado gardado (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) para ler e escribir a memoria da PS2 dende un script.
5. **Proba sen roubar a pantalla:** [`ripps2-lab/`](ripps2-lab/README.md) describe unha instalación de laboratorio (`install-lab.ps1` pon unha compilación nun cartafol portátil e conserva as súas tarxetas, axustes e gravacións), e `tools/dev/ps2bg.ps1` do repositorio de RIPPS2 executa listas de pasos (botóns, esperas, capturas, gravacións) nun escritorio oculto cun panel na barra de tarefas que o usuario pode mirar, deter ou tomar.

Que cambiou e por que, ficheiro a ficheiro: **[RIPPCSX2.md](RIPPCSX2.md)**. Axentes que traballen no código deste fork: nunca abrades pull requests, issues nin comentarios no proxecto PCSX2 (o seu `AGENTS.md` prohibe as contribucións feitas por IA); RIPPCSX2 segue sendo un fork.

**Sen relación co equipo de PCSX2.** GPL-3.0 coma PCSX2. Informa dos problemas de RIPPCSX2 a RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nunca a PCSX2. Segue o README propio de PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 é un emulador de PlayStation 2 (PS2) libre e de código aberto. O seu propósito é emular o hardware da PS2 usando unha combinación de [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) de CPU MIPS, [Recompiladores](https://en.wikipedia.org/wiki/Dynamic_recompilation) e unha [Máquina virtual](https://en.wikipedia.org/wiki/Virtual_machine) que xestiona os estados do hardware e a memoria do sistema da PS2. Isto permíteche xogar a xogos de PS2 no teu PC, con moitas funcións e vantaxes adicionais.

<a id="project-details"></a>

## Detalles do proxecto

PCSX2 leva máis de 20 anos en desenvolvemento. As versións antigas só podían executar unhas poucas demos de dominio público, pero as novas executan a maioría dos xogos a velocidade completa, incluídos títulos populares coma Final Fantasy X e Devil May Cry 3. Visita a [lista de compatibilidade de PCSX2](https://pcsx2.net/compat/) para ver o estado de compatibilidade máis recente dos xogos (con máis de 2500 títulos probados).

Os instaladores e binarios das versións estables e nightly están dispoñibles na [nosa web](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Requisitos do sistema

PCSX2 funciona en Windows, Linux e Mac. A nosa [páxina de documentación de configuración](https://pcsx2.net/docs/setup/requirements) ten máis detalles sobre os requisitos de software e hardware.

Ten en conta que para usar o emulador precísase un volcado de BIOS dunha consola PS2 adquirida legalmente. Para máis información, visita [esta páxina](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuír / Compilar

PCSX2 admite tradución a outras linguas mediante [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Consulta a [Guía de contribución](https://pcsx2.net/docs/contributing/) para saber máis sobre como contribuír.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

