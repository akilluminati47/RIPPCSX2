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
  <b>Filipino</b> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Salin ng README sa Ingles; kung magkaiba, ang Ingles ang masusunod. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Mga font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Isang PlayStation 2 emulator para sa pag-test at pagbuo ng homebrew, ginawa para ikaw o isang AI agent ang magpatakbo.**

Ang RIPPCSX2 ay PCSX2 v2.9.96 na may mga pagbabagong kailangan ng isang PS2 homebrew developer para makita ang totoo: ipinapakita, nire-record at kinukunan ng screenshot ang mga HD video mode gaya ng pagpapakita ng HD TV, kasama ang hardware data breakpoint ng EE, para gumana ang mga in-game menu at video mode tool na kumakabit sa mga GS register (ang GSM ng Open PS2 Loader, ang in-game menu ng RIPPS2) gaya sa console. Ang lahat ng iba pa ay karaniwang PCSX2. Nagsimula ito bilang test lab ng front end na [RIPPS2](https://github.com/akilluminati47/RIPPS2) at para ito sa sinumang gumagawa ng homebrew, theme o tool para sa PS2.

**[Tingnan ang website](https://akilluminati47.github.io/RIPPCSX2/)**: kalasin ang isang PS2 o pasabugin ito, at nasa Info panel ang lahat tungkol sa RIPPCSX2.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [I-download ang RIPPCSX2 (Windows zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 o 11, x64, CPU na may AVX2. I-unzip kahit saan, patakbuhin ang `pcsx2-qtx64-avx2.exe`, at ituro ito sa sarili mong BIOS dump. May walang lamang `portable.txt` ang zip sa tabi ng exe, kaya iniimbak ng RIPPCSX2 ang lahat ng setting at file nito sa sarili nitong folder: ang PCSX2 na naka-install na ay mananatili sa sarili nitong mga setting, hindi nagagalaw. Ang release ay laging ang pinakabagong build ([ang page nito](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); nasa [docs/videos](docs/videos) ang mga clip sa ibaba.

**Nagpapatakbo ng mga `.elf` program para sa pag-test:** System > Start File, o `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, at magbo-boot ang program gaya ng pag-boot nito mula sa memory card o USB stick sa PS2. **Kumikilos ito gaya ng tunay na hardware**: ang ELF na naglulunsad ng ibang ELF ay ipinapasa ang makina rito at umaalis, ang in-game menu na kumakabit sa GS ay gumuguhit sa ibabaw ng tunay na frame ng laro, at ang pag-power off ay nagsasara sa VM gaya ng console na pinatay.

<a id="see-it-work"></a>

## Panoorin itong gumagana

Bawat clip ay tunay na lab run sa build na ito, pinaikli sa ilalim ng 12 segundo.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Isang AI agent na nagte-test ng ELF.** Ni-record mula sa kanang-ibabang sulok ng screen ng user (ang taskbar, bahagi ng Claude session): inilulunsad ni Claude ang `RIPPS2.elf` sa RIPPCSX2 sa isang nakatagong desktop, inilulunsad ang Aqua Teen Hunger Force mula sa HDD image at binubuksan sa ibabaw nito ang in-game menu ng RIPPS2. Ang maliit na panel lang ang nasa screen; nananatili sa user ang keyboard at mouse.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Ang in-game menu, bawat function.** L1+L2+R1+R2+SELECT+START sa ibabaw ng tumatakbong laro: ACHIEVEMENTS, RESUME (tuloy ang laro), ang menu ulit sa isang mas huling frame, tapos POWER OFF na nagsasara sa VM. Alam ng menu kung aling frame ang guguhitan dahil ine-emulate ng RIPPCSX2 ang data write breakpoint ng EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF na naglulunsad ng ELF, gaya ng tunay na PS2.** Binubuksan at pinapatakbo ng Memory Files ng RIPPS2 ang `mc0:/RIPPS2/RIPPS2.ELF` (ang pinakabagong build, kinopya sa card). Ipinapasa ito ng tumatakbong RIPPS2 at nawawala; nilo-load mula sa card ang bago at nagbo-boot hanggang sa listahan ng mga laro nito.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Ano ang makukuha mo kumpara sa karaniwang PCSX2 v2.9.96

- **Isang RIPPCSX2 menu** sa pagitan ng Debug at Help: Run ELF at Run Last ELF, live na Lab Monitor, Test Steps, Compatibility Report, ang mga switch ng fork, at ang mga folder kung saan napupunta ang lahat.
- **Isang taskbar button para sa mga nakatagong run.** Ang PCSX2 na sinimulan sa nakatagong desktop ay naglalagay ng button sa taskbar mo, kaya naaabot ito ng volume mixer o per-app volume mod tulad ng ibang programa.
- **Tama ang itsura ng HD modes.** Ang 720p at 1080i ay ipinapakita sa 16:9 (4:3 ang guhit ng orihinal), sa bawat aspect setting maliban sa Stretch.
- **HD na recording at screenshot.** Nire-record ng F11 ang 720p sa 1280 x 720 at ang 1080i sa 1920 x 1080 (o isang upscale multiple nito), naka-tag na 16:9; nagse-save ang F8 ng screenshot sa parehong laki. Ang orihinal ay nagbibigay ng 640 x 480 o ng raw buffer na 640 ang lapad.
- **Ang pagpalit ng mode habang nagre-record** ay nagpapatuloy sa bagong file sa bagong laki sa halip na isiksik sa unang file.
- **Nasa tamang puwesto ang 1080i.** Itinataas ng orihinal ang 1080i na larawan nang 42 linya (putol ang itaas, itim na guhit sa ibaba); sinisimulan ito ng RIPPCSX2 sa linya 40 gaya ng sariling timing ng console.
- **Data write breakpoint ng EE** (bago sa rippcsx2.2). Gumagana ang COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...): ang pagsulat sa binabantayang address ay nagti-trigger ng level 2 debug exception sa `0x80000100` bago ito tumakbo, sa interpreter at sa recompiler. Kailangan ito ng GSM ng OPL at ng in-game menu ng RIPPS2 para malaman kung aling frame ang ipinapakita ng laro.
- **Mga log line ng video mode.** Bawat pagpalit ng mode ay nagla-log ng sync timing at mga display register (`RIPPCSX2: video mode ...` sa `logs/emulog.txt`).
- **Walang alok ng auto-updater.** Pinapanatiling patay ng mga release tag ang updater ng PCSX2, kaya hindi ka nito kailanman "ia-update" pabalik sa orihinal.
- Hindi ginalaw ang standard definition: magkapareho byte por byte ang mga 480i screenshot sa orihinal. Ibinabalik ng `HDTVOutput = false` sa ilalim ng `[EmuCore/GS]` sa `inis/PCSX2.ini` ang orihinal na HD behavior para sa magkatabing paghahambing.

<a id="what-it-is-for"></a>

## Para saan ito

- **Mga gumagawa ng theme** (Open PS2 Loader, RiptOPL, RIPPS2): suriin ang theme sa 720p at 1080i gaya ng pagpapakita ng TV, at gumawa ng mga preview na tunay ang laki at mga tour video.
- **Mga homebrew developer:** i-test ang mga ELF na nagpapalit ng video mode, kumakabit sa GS o gumagamit ng mga debug register ng EE, at basahin sa log ang eksaktong display register na itinatakda ng isang mode.
- **Mga in-game menu at GS tool:** tumatakbo sa emulator ang GSM ng OPL, ang in-game menu ng RIPPS2 at anumang nakabatay sa data write breakpoint, hindi lang sa hardware.
- **Automated at AI-assisted na pag-test:** mga scripted run sa nakatagong desktop na may screenshot, recording, save state at pagbasa ng memory sa pamamagitan ng PINE, nang hindi inaagaw ang iyong computer.

<a id="the-end-goal-the-whole-library"></a>

## Ang huling layunin: ang buong library

Ang pinakamalaking trabaho sa hinaharap ay ang pagsubok ng mga larong PS2 sa mismong code path ng Open PS2 Loader, gaya ng pagpapatakbo ng console, at ang pagsusulat ng kailangan ng bawat isa: mga ELF, KELF, homebrew app at laro sa isang OPL sandbox, na awtomatikong sinusubukan ang mga compatibility mode nito. Balang araw, magagamit ito ng isang tao para mapatakbo ang buong library. Iyan ang huling layunin ng RIPPCSX2.

Ang Compatibility Report ang unang hakbang: ang resulta ng isang laro, ang mga OPL mode na ginamit at ang estado ng makina, na naka-save sa `reports/` bilang file at isang row sa `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Para sa mga AI agent, LLM at sa mga user nila

Isinulat ang repo na ito para maihanda ng isang agent ang lahat para sa user mula sa link lang. Ibigay sa iyong assistant ang `https://github.com/akilluminati47/RIPPCSX2` at hilingin na i-install ang RIPPCSX2; narito ang lahat ng kailangan nito:

1. **Kunin ang build:** `RIPPCSX2-windows-x64-avx2.zip` mula sa rolling release ([direktang link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), o `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). I-unzip ito sa sarili nitong folder; nasa tabi na ng exe ang `portable.txt` nito, kaya hindi nito kailanman gagalawin ang mga setting ng naka-install na PCSX2.
2. **BIOS:** ang user ang nagbibigay ng BIOS dump mula sa sarili nilang console (huwag kailanman mag-download ng isa): ilagay ito sa `bios` folder sa tabi ng exe (o ituro roon ang `[Folders] Bios` sa `inis/PCSX2.ini`) at piliin ito sa first-run wizard (`[Filenames] BIOS`).
3. **Magpatakbo ng kahit ano:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, o `-- <game.iso>`. Simpleng INI ang mga setting sa `inis/PCSX2.ini`; napupunta ang mga log sa `logs/emulog.txt` (idinadagdag ng `[Logging] EnableEEConsole = true` ang printf ng EE).
4. **Patakbuhin at obserbahan:** F8 screenshot (`snaps/`), F11 record (`videos/`), F1 save state (`sstates/`), at PINE (`[EmuCore] EnablePINE`, `PINESlot`) para basahin at sulatan ang PS2 memory mula sa isang script.
5. **Mag-test nang hindi inaagaw ang screen:** inilalarawan ng [`ripps2-lab/`](ripps2-lab/README.md) ang lab install (inilalagay ng `install-lab.ps1` ang isang build sa portable folder at iniingatan ang mga card, setting at recording nito), at pinapatakbo ng `tools/dev/ps2bg.ps1` sa RIPPS2 repo ang mga listahan ng hakbang (button, paghihintay, screenshot, recording) sa nakatagong desktop, may taskbar panel na maaaring panoorin, ihinto o kunin ng user.

Ano ang nagbago at bakit, bawat file: **[RIPPCSX2.md](RIPPCSX2.md)**. Mga agent na gumagawa sa code ng fork na ito: huwag kailanman magbukas ng pull request, issue o comment sa proyekto ng PCSX2 (ipinagbabawal ng `AGENTS.md` nito ang mga kontribusyong gawa ng AI); mananatiling fork ang RIPPCSX2.

**Walang kaugnayan sa PCSX2 team.** GPL-3.0 gaya ng PCSX2. I-report ang mga isyu ng RIPPCSX2 sa RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), huwag kailanman sa PCSX2. Kasunod ang sariling README ng PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

Ang PCSX2 ay isang libre at open-source na PlayStation 2 (PS2) emulator. Layunin nitong i-emulate ang hardware ng PS2, gamit ang kumbinasyon ng [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) ng MIPS CPU, [Mga Recompiler](https://en.wikipedia.org/wiki/Dynamic_recompilation) at isang [Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) na namamahala sa mga hardware state at sa system memory ng PS2. Pinapayagan ka nitong maglaro ng mga PS2 game sa iyong PC, na may maraming dagdag na feature at benepisyo.

<a id="project-details"></a>

## Mga detalye ng proyekto

Mahigit 20 taon nang dine-develop ang PCSX2. Ilang public domain game demo lang ang kayang patakbuhin ng mga lumang bersyon, pero kaya ng mga bagong bersyon na patakbuhin ang karamihan ng laro nang full speed, kasama ang mga sikat na pamagat gaya ng Final Fantasy X at Devil May Cry 3. Bisitahin ang [PCSX2 compatibility list](https://pcsx2.net/compat/) para sa pinakabagong compatibility status ng mga laro (mahigit 2500 pamagat ang na-test).

Makukuha ang mga installer at binary ng stable at nightly build sa [aming website](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Mga kailangan ng system

Sinusuportahan ng PCSX2 ang Windows, Linux at Mac. May dagdag na detalye tungkol sa mga kailangang software at hardware ang aming [setup documentation page](https://pcsx2.net/docs/setup/requirements).

Pakitandaan na kailangan ang BIOS dump mula sa legal na pag-aaring PS2 console para magamit ang emulator. Para sa higit pang impormasyon, bisitahin ang [page na ito](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Pag-ambag / Pag-build

Maaaring isalin ang PCSX2 sa ibang mga wika sa pamamagitan ng [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Tingnan ang [Gabay sa Pag-ambag](https://pcsx2.net/docs/contributing/) para malaman kung paano mag-ambag.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">I-download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Mga tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Mga font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

