<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <b>Español</b> |
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

<p align="center"><sub>Traducción del README en inglés; si difieren, vale el inglés. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fuentes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Un emulador de PlayStation 2 para probar y desarrollar homebrew, hecho para que lo manejes tú o un agente de IA.**

RIPPCSX2 es PCSX2 v2.9.96 con los cambios que un desarrollador de homebrew de PS2 necesita para ver lo real: los modos de vídeo HD mostrados, capturados y fotografiados como los muestra un televisor HD, y el punto de interrupción de datos por hardware del EE, para que los menús dentro del juego y las herramientas de modo de vídeo que enganchan los registros del GS (el GSM de Open PS2 Loader, el menú dentro del juego de RIPPS2) funcionen como en una consola. Todo lo demás es PCSX2 normal. Nació como el laboratorio de pruebas del front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) y está pensado para cualquiera que haga homebrew, temas o herramientas para PS2.

**[Ver el sitio web](https://akilluminati47.github.io/RIPPCSX2/)**: desmonta una PS2 o hazla estallar, con todo sobre RIPPCSX2 en su panel Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Descargar RIPPCSX2 (zip para Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 u 11, x64, una CPU con AVX2. Descomprímelo donde quieras, abre `pcsx2-qtx64-avx2.exe` e indícale tu propio volcado de BIOS. El zip trae un `portable.txt` vacío junto al exe, así que RIPPCSX2 guarda todos sus ajustes y archivos en su propia carpeta: un PCSX2 que ya tengas instalado conserva sus ajustes, intactos. La versión siempre contiene la compilación más nueva ([su página](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); los clips de abajo están en [docs/videos](docs/videos).

**Ejecuta programas `.elf` para probarlos:** System > Start File, o `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, y el programa arranca como lo haría desde una tarjeta de memoria o un USB en una PS2. **Se comporta como el hardware real**: un ELF que lanza otro ELF le cede la máquina y desaparece, un menú dentro del juego que engancha el GS se dibuja sobre el fotograma real del juego, y apagar cierra la VM como una consola que se apaga.

<a id="see-it-work"></a>

## Míralo funcionar

Cada clip es una ejecución real del laboratorio con esta compilación, recortada a menos de 12 segundos.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Un agente de IA probando un ELF.** Grabado desde la esquina inferior derecha de la pantalla del usuario (barra de tareas, parte de la sesión de Claude): Claude arranca `RIPPS2.elf` en RIPPCSX2 en un escritorio oculto, lanza Aqua Teen Hunger Force desde la imagen del HDD y abre encima el menú dentro del juego de RIPPS2. El pequeño panel es lo único en pantalla; el usuario conserva el teclado y el ratón.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**El menú dentro del juego, todas sus funciones.** L1+L2+R1+R2+SELECT+START sobre un juego en marcha: ACHIEVEMENTS, RESUME (el juego sigue), el menú otra vez sobre un fotograma posterior, y luego POWER OFF, que cierra la VM. El menú sabe sobre qué fotograma dibujar porque RIPPCSX2 emula el punto de interrupción de escritura de datos del EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Un ELF lanzando un ELF, como una PS2 real.** Memory Files de RIPPS2 abre `mc0:/RIPPS2/RIPPS2.ELF` (la compilación más nueva, copiada a la tarjeta) y la ejecuta. El RIPPS2 en marcha cede el control y desaparece; el nuevo carga desde la tarjeta y arranca en su lista de juegos.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Lo que obtienes frente al PCSX2 v2.9.96 normal

- **Un menú RIPPCSX2** entre Debug y Help: Run ELF y Run Last ELF, un Lab Monitor en vivo, Test Steps, un Compatibility Report, los interruptores del fork y las carpetas donde queda todo.
- **Un botón en la barra de tareas para las ejecuciones ocultas.** Un PCSX2 iniciado en un escritorio oculto pone un botón en tu barra de tareas, así un mezclador de volumen o un mod de volumen por aplicación lo alcanza como a cualquier otro programa.
- **Los modos HD se ven bien.** 720p y 1080i se muestran en 16:9 (el original los dibuja en 4:3), con cualquier ajuste de aspecto salvo Stretch.
- **Capturas y fotos en HD.** F11 graba 720p a 1280 x 720 y 1080i a 1920 x 1080 (o eso por el escalado), marcado como 16:9; F8 guarda capturas a los mismos tamaños. El original da 640 x 480 o el búfer crudo de 640 de ancho.
- **Un cambio de modo a mitad de grabación** sigue en un archivo nuevo con el nuevo tamaño, en vez de encajarse en el primero.
- **1080i en su sitio.** El original sube una imagen 1080i 42 líneas (cortada arriba, banda negra abajo); RIPPCSX2 la empieza en la línea 40, donde lo hace la temporización de la propia consola.
- **Punto de interrupción de escritura de datos del EE** (nuevo en rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funciona: una escritura a una dirección vigilada lanza la excepción de depuración de nivel 2 en `0x80000100` antes de ejecutarse, en el intérprete y en el recompilador. El GSM de OPL y el menú dentro del juego de RIPPS2 lo necesitan para saber qué fotograma muestra un juego.
- **Líneas de registro del modo de vídeo.** Cada cambio de modo registra la temporización de sincronía y los registros de pantalla (`RIPPCSX2: video mode ...` en `logs/emulog.txt`).
- **Sin ofertas del actualizador automático.** Las etiquetas de versión mantienen apagado el actualizador de PCSX2, así que nunca te "actualiza" de vuelta al original.
- La definición estándar queda intacta: las capturas a 480i son idénticas byte a byte a las del original. `HDTVOutput = false` bajo `[EmuCore/GS]` en `inis/PCSX2.ini` devuelve el comportamiento HD original para comparar.

<a id="what-it-is-for"></a>

## Para qué sirve

- **Creadores de temas** (Open PS2 Loader, RiptOPL, RIPPS2): juzga un tema en 720p y 1080i como lo muestra un televisor, y haz vistas previas a tamaño real y vídeos de recorrido.
- **Desarrolladores de homebrew:** prueba ELF que cambian de modo de vídeo, enganchan el GS o usan los registros de depuración del EE, y lee en el registro los valores exactos de pantalla que fija un modo.
- **Menús dentro del juego y herramientas del GS:** el GSM de OPL, el menú dentro del juego de RIPPS2 y cualquier otra cosa basada en el punto de interrupción de escritura de datos funcionan en el emulador y no solo en el hardware.
- **Pruebas automatizadas y asistidas por IA:** ejecuciones guionizadas en un escritorio oculto con capturas, grabaciones, estados guardados y lecturas de memoria por PINE, sin adueñarse de tu PC.

<a id="the-end-goal-the-whole-library"></a>

## El objetivo final: toda la biblioteca

El mayor trabajo pendiente es probar juegos de PS2 por el propio camino de código de Open PS2 Loader, como los ejecuta una consola, y anotar lo que necesita cada uno: ELF, KELF, aplicaciones homebrew y juegos en un entorno aislado de OPL, probando sus modos de compatibilidad automáticamente. Alguien podría usar esto para hacer funcionar toda la biblioteca algún día. Ese es el objetivo final de RIPPCSX2.

El Compatibility Report es su primer paso: el resultado de un juego, los modos de OPL usados y el estado de la máquina, guardados en `reports/` como un archivo y una fila en `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para agentes de IA, LLM y sus usuarios

Este repositorio está escrito para que un agente pueda configurar a un usuario solo con el enlace. Dale a tu asistente `https://github.com/akilluminati47/RIPPCSX2` y pídele que instale RIPPCSX2; todo lo que necesita está aquí:

1. **Consigue la compilación:** `RIPPCSX2-windows-x64-avx2.zip` de la versión continua ([enlace directo](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), o `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Descomprímelo en una carpeta propia; su `portable.txt` ya está junto al exe, así que nunca toca los ajustes de un PCSX2 instalado.
2. **BIOS:** el usuario aporta el volcado de BIOS de su propia consola (nunca lo descargues): ponlo en la carpeta `bios` junto al exe (o apunta `[Folders] Bios` en `inis/PCSX2.ini` hacia él) y elígelo en el asistente del primer arranque (`[Filenames] BIOS`).
3. **Ejecuta algo:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, o `-- <game.iso>`. Los ajustes son INI plano en `inis/PCSX2.ini`; los registros van a `logs/emulog.txt` (`[Logging] EnableEEConsole = true` añade el printf del EE).
4. **Manéjalo y obsérvalo:** F8 captura (`snaps/`), F11 grabación (`videos/`), F1 estado guardado (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) para leer y escribir la memoria de la PS2 desde un script.
5. **Prueba sin robar la pantalla:** [`ripps2-lab/`](ripps2-lab/README.md) describe una instalación de laboratorio (`install-lab.ps1` pone una compilación en una carpeta portátil y conserva sus tarjetas, ajustes y grabaciones), y `tools/dev/ps2bg.ps1` del repositorio de RIPPS2 ejecuta listas de pasos (botones, esperas, capturas, grabaciones) en un escritorio oculto con un panel en la barra de tareas que el usuario puede mirar, detener o tomar.

Qué cambió y por qué, archivo por archivo: **[RIPPCSX2.md](RIPPCSX2.md)**. Agentes que trabajen en el código de este fork: nunca abráis pull requests, issues ni comentarios en el proyecto PCSX2 (su `AGENTS.md` prohíbe las contribuciones hechas por IA); RIPPCSX2 sigue siendo un fork.

**Sin relación con el equipo de PCSX2.** GPL-3.0 como PCSX2. Informa de los problemas de RIPPCSX2 a RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nunca a PCSX2. Sigue el README propio de PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 es un emulador de PlayStation 2 (PS2) libre y de código abierto. Su propósito es emular el hardware de la PS2 usando una combinación de [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) de CPU MIPS, [Recompiladores](https://en.wikipedia.org/wiki/Dynamic_recompilation) y una [Máquina virtual](https://en.wikipedia.org/wiki/Virtual_machine) que gestiona los estados del hardware y la memoria del sistema de la PS2. Esto te permite jugar a juegos de PS2 en tu PC, con muchas funciones y ventajas adicionales.

<a id="project-details"></a>

## Detalles del proyecto

PCSX2 lleva más de 20 años en desarrollo. Las versiones antiguas solo podían ejecutar unas pocas demos de dominio público, pero las nuevas ejecutan la mayoría de los juegos a velocidad completa, incluidos títulos populares como Final Fantasy X y Devil May Cry 3. Visita la [lista de compatibilidad de PCSX2](https://pcsx2.net/compat/) para ver el estado de compatibilidad más reciente de los juegos (con más de 2500 títulos probados).

Los instaladores y binarios de las versiones estables y nightly están en [nuestra web](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Requisitos del sistema

PCSX2 funciona en Windows, Linux y Mac. Nuestra [página de documentación de configuración](https://pcsx2.net/docs/setup/requirements) tiene más detalles sobre los requisitos de software y hardware.

Ten en cuenta que para usar el emulador se necesita un volcado de BIOS de una consola PS2 adquirida legítimamente. Para más información, visita [esta página](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuir / Compilar

PCSX2 admite traducción a otros idiomas mediante [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Consulta la [Guía de contribución](https://pcsx2.net/docs/contributing/) para saber más sobre cómo contribuir.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descargar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temas</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fuentes</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

