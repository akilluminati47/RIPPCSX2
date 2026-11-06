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
  <b>Cebuano</b>
</p>
<!-- /i18n -->

<p align="center"><sub>Hubad sa README nga Iningles; kung lahi, ang Iningles ang sundon. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Mga font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Usa ka PlayStation 2 emulator para sa pag-test ug paghimo og homebrew, gihimo aron ikaw o usa ka AI agent ang modagan niini.**

Ang RIPPCSX2 mao ang PCSX2 v2.9.96 nga adunay mga kausaban nga kinahanglan sa usa ka PS2 homebrew developer aron makita ang tinuod: ang mga HD video mode gipakita, gi-record ug gikuhaan og screenshot sama sa pagpakita sa HD TV, uban ang hardware data breakpoint sa EE, aron ang mga in-game menu ug video mode tool nga mokabit sa mga GS register (ang GSM sa Open PS2 Loader, ang in-game menu sa RIPPS2) molihok sama sa console. Ang tanan nga uban kay yanong PCSX2. Nagsugod kini isip test lab sa front end nga [RIPPS2](https://github.com/akilluminati47/RIPPS2) ug para kini sa bisan kinsa nga naghimo og homebrew, theme o tool para sa PS2.

**[Tan-awa ang website](https://akilluminati47.github.io/RIPPCSX2/)**: buaga ang usa ka PS2 o pabuthon kini, ug naa sa Info panel ang tanan bahin sa RIPPCSX2.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [I-download ang RIPPCSX2 (Windows zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 o 11, x64, CPU nga adunay AVX2. I-unzip bisan asa, padagana ang `pcsx2-qtx64-avx2.exe`, ug itudlo kini sa imong kaugalingong BIOS dump. Ang zip adunay walay sulod nga `portable.txt` tupad sa exe, mao nga gitipigan sa RIPPCSX2 ang tanan niyang setting ug file sa kaugalingon niyang folder: ang PCSX2 nga na-install na nimo magpabilin sa kaugalingon niyang mga setting, wala matandog. Ang release kanunay ang pinakabag-o nga build ([ang page niini](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); ang mga clip sa ubos naa sa [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [I-download ang RIPPCSX2 (Linux AppImage)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, CPU nga adunay AVX2. Himoa kining executable ug sugdi. Bag-o kini sa kini nga release ug gitukod sa samang workflow sa Windows zip, apan wala pa kini mapadagan sa Linux nga makina: palihug isulti kanamo kung giunsa kini. Ang taskbar button alang sa mga tinago nga run alang ra sa Windows.

**Nagpadagan og mga `.elf` program para sa pag-test:** System > Start File, o `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, ug ang program mo-boot sama sa pag-boot niini gikan sa memory card o USB stick sa PS2. **Molihok kini sama sa tinuod nga hardware**: ang ELF nga molansad og laing ELF motugyan sa makina niini ug mobiya, ang in-game menu nga mokabit sa GS modrowing ibabaw sa tinuod nga frame sa dula, ug ang pag-power off mosira sa VM sama sa console nga gipalong.

<a id="see-it-work"></a>

## Tan-awa kini nga molihok

Ang matag clip usa ka tinuod nga lab run niini nga build, giputol ngadto sa ubos sa 12 segundos.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Usa ka AI agent nga nag-test og ELF.** Gi-record gikan sa tuo-ubos nga suok sa screen sa user (ang taskbar, bahin sa Claude session): gilansad ni Claude ang `RIPPS2.elf` sa RIPPCSX2 sa usa ka tinago nga desktop, gilansad ang Aqua Teen Hunger Force gikan sa HDD image ug giablihan ibabaw niini ang in-game menu sa RIPPS2. Ang gamay nga panel ra ang naa sa screen; ang keyboard ug mouse magpabilin sa user.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Ang in-game menu, matag function.** L1+L2+R1+R2+SELECT+START ibabaw sa nagdagan nga dula: ACHIEVEMENTS, RESUME (padayon ang dula), ang menu pag-usab ibabaw sa ulahi nga frame, dayon POWER OFF nga mosira sa VM. Nahibal-an sa menu kung asang frame ang drowingan kay gi-emulate sa RIPPCSX2 ang data write breakpoint sa EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF nga molansad og ELF, sama sa tinuod nga PS2.** Giablihan ug gipadagan sa Memory Files sa RIPPS2 ang `mc0:/RIPPS2/RIPPS2.ELF` (ang pinakabag-o nga build, gikopya sa card). Ang nagdagan nga RIPPS2 motugyan ug mawala; ang bag-o i-load gikan sa card ug mo-boot hangtod sa listahan sa iyang mga dula.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Unsa ang imong makuha kumpara sa yanong PCSX2 v2.9.96

- **Usa ka RIPPCSX2 menu** taliwala sa Debug ug Help: Run ELF ug Run Last ELF, live nga Lab Monitor, Test Steps, Compatibility Report, ang mga switch sa fork, ug ang mga folder diin moadto ang tanan.
- **RIPART,** niana nga menu: ang art database sa OPL Manager, 16,313 ka dula nga gibasa pinaagi sa byte range gikan sa backup niini sa archive.org. Mga paon nga entry sa dula aron masusi ang tema sa tinuod nga lista nga walay dula sa drive, lista sa checkbox nga adunay matag piraso sa art sa dula aron itipig o biyaan, pagpangita sa mga dula sa drive nga walay cover, ug ART folder o `art.tar` nga butangan sa tanan. Ang mga paon makita sa OPL ug RIPPS2 ug dili magsugod; ang file nga anaa na dili gayud pulihan. Mitabang si akilluminati47 sa pagdala sa 8-bit PNG art ug sa 128 x 128 nga disc icon niana nga database.
- **Ang stock OPL makasugod og mga dula.** Ang `host` device nga ang programa mismo ang nagrehistro makadawat na karon sa kaugalingon niini nga mga open, busa molihok ang IOP reboot sa OPL. Ang orihinal mohunong sa `file 'host0:' can't open`.
- **Ang EXIT GAME makaabot sa browser.** Nawala ang usa ka SIO2 interrupt sa IOP reboot, mao nga naghulat ang OSDSYS sa memory card nga itom ang screen.
- **Usa ka taskbar button para sa mga tinago nga run.** Ang PCSX2 nga gisugdan sa tinago nga desktop magbutang og button sa imong taskbar, busa maabot kini sa volume mixer o per-app volume mod sama sa bisan unsang programa.
- **Husto ang hitsura sa HD modes.** Ang 720p ug 1080i gipakita sa 16:9 (4:3 ang drowing sa orihinal), sa matag aspect setting gawas sa Stretch.
- **HD nga recording ug screenshot.** Ang F11 mo-record sa 720p sa 1280 x 720 ug sa 1080i sa 1920 x 1080 (o usa ka upscale multiple niini), naka-tag og 16:9; ang F8 mo-save og screenshot sa parehas nga gidak-on. Ang orihinal mohatag og 640 x 480 o sa raw buffer nga 640 ang gilapdon.
- **Ang pag-ilis og mode samtang nag-record** mopadayon sa bag-ong file sa bag-ong gidak-on imbes nga isiksik sa unang file.
- **Ang 1080i naa sa hustong dapit.** Gipataas sa orihinal ang 1080i nga hulagway og 42 ka linya (putol ang ibabaw, itom nga gilis sa ubos); gisugdan kini sa RIPPCSX2 sa linya 40 sama sa kaugalingong timing sa console.
- **Data write breakpoint sa EE** (bag-o sa rippcsx2.2). Molihok ang COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...): ang pagsulat sa gibantayan nga address mo-trigger og level 2 debug exception sa `0x80000100` sa dili pa kini modagan, sa interpreter ug sa recompiler. Kinahanglan kini sa GSM sa OPL ug sa in-game menu sa RIPPS2 aron mahibal-an kung asang frame ang gipakita sa dula.
- **Mga log line sa video mode.** Ang matag pag-ilis og mode mo-log sa sync timing ug sa mga display register (`RIPPCSX2: video mode ...` sa `logs/emulog.txt`).
- **Walay tanyag sa auto-updater.** Ang mga release tag nagpabilin nga patay sa updater sa PCSX2, mao nga dili ka niini "i-update" pabalik sa orihinal.
- Wala gitandog ang standard definition: ang mga 480i screenshot parehas byte matag byte sa orihinal. Ang `HDTVOutput = false` ilalom sa `[EmuCore/GS]` sa `inis/PCSX2.ini` mobalik sa orihinal nga HD behavior para sa magtupad nga pagkumpara.

<a id="what-it-is-for"></a>

## Para asa kini

- **Mga naghimo og theme** (Open PS2 Loader, RiptOPL, RIPPS2): timbanga ang theme sa 720p ug 1080i sama sa pagpakita sa TV, ug paghimo og mga preview nga tinuod ang gidak-on ug mga tour video.
- **Mga homebrew developer:** i-test ang mga ELF nga moilis og video mode, mokabit sa GS o mogamit sa mga debug register sa EE, ug basaha sa log ang eksaktong display register nga gitakda sa usa ka mode.
- **Mga in-game menu ug GS tool:** ang GSM sa OPL, ang in-game menu sa RIPPS2 ug bisan unsa nga gitukod sa data write breakpoint modagan sa emulator, dili lang sa hardware.
- **Mga dula sa PS1:** padagana ang Ember ug ang mga dula niini sa PS1 gikan sa virtual drive aron sulayan ang pag-launch ug mga lista sa PS1, uban ang imong kaugalingong PS1 BIOS sa drive.
- **Automated ug AI-assisted nga pag-test:** mga scripted run sa tinago nga desktop nga adunay screenshot, recording, save state ug pagbasa sa memory pinaagi sa PINE, nga dili moilog sa imong computer.

<a id="the-end-goal-the-whole-library"></a>

## Ang kataposang tumong: ang tibuok library

Ang pinakadakong buluhaton sa unahan mao ang pagsulay sa mga dula sa PS2 pinaagi sa kaugalingong code path sa Open PS2 Loader, sama sa pagpadagan sa console, ug ang pagsulat kung unsa ang gikinahanglan sa matag usa: mga ELF, KELF, homebrew app ug dula sa usa ka OPL sandbox, nga awtomatikong sulayan ang mga compatibility mode niini. Usa ka adlaw, magamit kini sa usa ka tawo aron mapadagan ang tibuok library. Mao kana ang kataposang tumong sa RIPPCSX2.

Ang Compatibility Report mao ang unang lakang: ang resulta sa usa ka dula, ang mga OPL mode nga gigamit ug ang kahimtang sa makina, nga gitipigan sa `reports/` isip file ug usa ka row sa `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para sa mga AI agent, LLM ug sa ilang mga user

Gisulat kini nga repo aron ang usa ka agent makapahimutang sa tanan para sa user gikan sa link ra. Ihatag sa imong assistant ang `https://github.com/akilluminati47/RIPPCSX2` ug hangyoa nga i-install ang RIPPCSX2; ania ang tanan nga kinahanglan niini:

1. **Kuhaa ang build:** `RIPPCSX2-windows-x64-avx2.zip` gikan sa rolling release ([direktang link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), o `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). I-unzip kini sa kaugalingon niyang folder; ang `portable.txt` niini naa na tupad sa exe, mao nga dili gyud niini tandugon ang mga setting sa na-install nga PCSX2.
2. **BIOS:** ang user ang mohatag sa BIOS dump gikan sa ilang kaugalingong console (ayaw gyud pag-download og usa): ibutang kini sa `bios` folder tupad sa exe (o itudlo didto ang `[Folders] Bios` sa `inis/PCSX2.ini`) ug pilia kini sa first-run wizard (`[Filenames] BIOS`).
3. **Padagana ang bisan unsa:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, o `-- <game.iso>`. Yanong INI ang mga setting sa `inis/PCSX2.ini`; ang mga log moadto sa `logs/emulog.txt` (ang `[Logging] EnableEEConsole = true` modugang sa printf sa EE).
4. **Padagana ug obserbahi:** F8 screenshot (`snaps/`), F11 record (`videos/`), F1 save state (`sstates/`), ug PINE (`[EmuCore] EnablePINE`, `PINESlot`) aron basahon ug sulatan ang PS2 memory gikan sa usa ka script.
5. **Pag-test nga dili moilog sa screen:** gihulagway sa [`ripps2-lab/`](ripps2-lab/README.md) ang lab install (ang `install-lab.ps1` mobutang og build sa portable folder ug motipig sa mga card, setting ug recording niini), ug ang `tools/dev/ps2bg.ps1` sa RIPPS2 repo modagan sa mga listahan sa lakang (button, paghulat, screenshot, recording) sa tinago nga desktop, uban ang taskbar panel nga mahimong tan-awon, hunongon o kuhaon sa user.

Unsa ang nausab ug ngano, matag file: **[RIPPCSX2.md](RIPPCSX2.md)**. Mga agent nga nagtrabaho sa code niini nga fork: ayaw gyud pag-abli og pull request, issue o comment sa proyekto sa PCSX2 (gidili sa `AGENTS.md` niini ang mga kontribusyon nga gihimo sa AI); magpabilin nga fork ang RIPPCSX2.

**Walay kalabotan sa PCSX2 team.** GPL-3.0 sama sa PCSX2. I-report ang mga isyu sa RIPPCSX2 ngadto sa RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), ayaw gyud ngadto sa PCSX2. Sunod ang kaugalingong README sa PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

Ang PCSX2 usa ka libre ug open-source nga PlayStation 2 (PS2) emulator. Ang tumong niini mao ang pag-emulate sa hardware sa PS2, gamit ang kombinasyon sa [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) sa MIPS CPU, [Mga Recompiler](https://en.wikipedia.org/wiki/Dynamic_recompilation) ug usa ka [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) nga nagdumala sa mga hardware state ug sa system memory sa PS2. Tugotan ka niini nga magdula og mga PS2 game sa imong PC, uban ang daghang dugang nga feature ug benepisyo.

<a id="project-details"></a>

## Mga detalye sa proyekto

Kapin na sa 20 ka tuig nga gi-develop ang PCSX2. Pipila ra ka public domain game demo ang kaya padaganon sa mga daan nga bersyon, apan kaya sa mga bag-ong bersyon nga padaganon ang kadaghanan sa mga dula nga full speed, lakip ang mga sikat nga titulo sama sa Final Fantasy X ug Devil May Cry 3. Bisitaha ang [PCSX2 compatibility list](https://pcsx2.net/compat/) para sa pinakabag-o nga compatibility status sa mga dula (kapin sa 2500 ka titulo ang na-test).

Ang mga installer ug binary sa stable ug nightly build anaa sa [among website](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Mga kinahanglanon sa system

Gisuportahan sa PCSX2 ang Windows, Linux ug Mac. Ang among [setup documentation page](https://pcsx2.net/docs/setup/requirements) adunay dugang nga detalye bahin sa mga kinahanglanon sa software ug hardware.

Palihug timan-i nga kinahanglan ang BIOS dump gikan sa legal nga gipanag-iya nga PS2 console aron magamit ang emulator. Para sa dugang impormasyon, bisitaha [kini nga page](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Pag-amot / Pag-build

Ang PCSX2 mahimong ihubad ngadto sa ubang mga pinulongan pinaagi sa [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Tan-awa ang [Giya sa Pag-amot](https://pcsx2.net/docs/contributing/) aron mahibal-an kung unsaon pag-amot.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Mga font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

