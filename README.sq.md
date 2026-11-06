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
  <b>Shqip</b> |
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

<p align="center"><sub>Përkthim i README-së në anglisht; nëse ndryshojnë, vlen anglishtja. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Shkarko</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temat</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontet</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Faqja</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Një emulator PlayStation 2 për testimin dhe zhvillimin e homebrew-ve, i bërë që ta drejtosh ti ose një agjent IA.**

RIPPCSX2 është PCSX2 v2.9.96 me ndryshimet që i duhen një zhvilluesi homebrew-sh për PS2 për të parë gjënë e vërtetë: mënyrat video HD të shfaqura, të regjistruara dhe të fotografuara ashtu si i tregon një televizor HD, dhe pika e ndërprerjes së të dhënave në harduer e EE-së, që menytë brenda lojës dhe mjetet e mënyrave video që kapen pas regjistrave të GS-së (GSM e Open PS2 Loader, menyja brenda lojës e RIPPS2) të punojnë si në konsolë. Gjithçka tjetër është PCSX2 i pastër. Nisi si laboratori i testimit i front end-it [RIPPS2](https://github.com/akilluminati47/RIPPS2) dhe është menduar për këdo që ndërton homebrew, tema ose mjete për PS2.

**[Shiko faqen e internetit](https://akilluminati47.github.io/RIPPCSX2/)**: çmonto një PS2 ose hidhe në erë, me gjithçka rreth RIPPCSX2 në panelin Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Shkarko RIPPCSX2 (zip për Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ose 11, x64, një procesor me AVX2. Shpaketoje kudo, nis `pcsx2-qtx64-avx2.exe` dhe drejtoje te dump-i yt i BIOS-it. Zip-i ka një `portable.txt` bosh pranë exe-së, ndaj RIPPCSX2 i mban të gjitha cilësimet dhe skedarët në dosjen e vet: një PCSX2 që e ke tashmë të instaluar i ruan cilësimet e veta, të paprekura. Botimi mban gjithmonë build-in më të ri ([faqja e tij](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klipet më poshtë janë te [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Shkarko RIPPCSX2 (Linux AppImage)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, një CPU me AVX2. Bëje të ekzekutueshëm dhe nise. Është i ri në këtë version dhe ndërtohet nga i njëjti workflow si zip-i i Windows, por ende nuk është nisur në një makinë Linux: na trego si shkon. Butoni i shiritit të detyrave për nisjet e fshehura është vetëm për Windows.

**Ekzekuton programe `.elf` për testim:** System > Start File, ose `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, dhe programi niset ashtu si do të nisej nga një kartë memorieje ose USB në një PS2. **Sillet si harduer i vërtetë**: një ELF që nis një ELF tjetër i dorëzon makinën dhe zhduket, një meny brenda lojës që kapet pas GS-së vizatohet mbi kuadrin e vërtetë të lojës, dhe fikja mbyll VM-në si një konsolë që fiket.

<a id="see-it-work"></a>

## Shikoje në punë

Çdo klip është një ekzekutim i vërtetë në laborator me këtë build, i shkurtuar nën 12 sekonda.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Një agjent IA që teston një ELF.** I regjistruar nga këndi i poshtëm djathtas i ekranit të përdoruesit (shiriti i detyrave, pjesë e seancës së Claude): Claude nis `RIPPS2.elf` në RIPPCSX2 në një desktop të fshehur, nis Aqua Teen Hunger Force nga imazhi i HDD-së dhe hap mbi të menynë brenda lojës të RIPPS2. Paneli i vogël është e vetmja gjë në ekran; përdoruesi e mban tastierën dhe miun.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menyja brenda lojës, çdo funksion.** L1+L2+R1+R2+SELECT+START mbi një lojë që po luhet: ACHIEVEMENTS, RESUME (loja vazhdon), sërish menyja mbi një kuadër më të vonshëm, pastaj POWER OFF, që mbyll VM-në. Menyja e di mbi cilin kuadër të vizatojë sepse RIPPCSX2 emulon pikën e ndërprerjes për shkrimin e të dhënave të EE-së.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Një ELF që nis një ELF, si një PS2 e vërtetë.** Memory Files e RIPPS2 hap `mc0:/RIPPS2/RIPPS2.ELF` (build-in më të ri, të kopjuar në kartë) dhe e ekzekuton. RIPPS2 që po punonte e dorëzon dhe zhduket; i riu ngarkohet nga karta dhe niset deri te lista e tij e lojërave.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Çfarë fiton krahasuar me PCSX2 v2.9.96 të zakonshëm

- **Një menu RIPPCSX2** midis Debug dhe Help: Run ELF dhe Run Last ELF, një Lab Monitor i drejtpërdrejtë, Test Steps, një Compatibility Report, çelësat e fork-ut dhe dosjet ku përfundon gjithçka.
- **RIPART,** në atë meny: baza e të dhënave të artit të OPL Manager, 16.313 lojëra të lexuara me rende bajtesh nga kopja e saj rezervë në archive.org. Hyrje lojërash karrem për të gjykuar një temë në një listë të vërtetë pa lojëra në disk, një listë me kuti zgjedhjeje me çdo pjesë të artit të një loje për ta mbajtur ose për ta lënë jashtë, një kërkim për lojërat në një disk pa kopertinë, dhe një dosje ART ose një `art.tar` për të vënë gjithçka. Karremat shfaqen në OPL dhe RIPPS2 dhe nuk nisen; një skedar që ekziston nuk zëvendësohet kurrë. akilluminati47 ndihmoi që kjo bazë të dhënash të marrë artin PNG 8-bit dhe ikonat e diskut 128 x 128.
- **OPL-i origjinal nis lojëra.** Një pajisje `host` që një program e regjistron vetë tani merr hapjet e veta, kështu që rinisja e IOP-it të OPL funksionon. Origjinali ndalon te `file 'host0:' can't open`.
- **EXIT GAME arrin te shfletuesi.** Një ndërprerje SIO2 humbiste gjatë një rinisjeje të IOP-it, gjë që e linte OSDSYS të priste kartën e kujtesës me ekran të zi.
- **Një buton në shiritin e detyrave për ekzekutimet e fshehura.** Një PCSX2 i nisur në një desktop të fshehur vendos një buton në shiritin tënd të detyrave, kështu që një përzierës volumi ose një mod volumi për aplikacion e arrin si çdo program tjetër.
- **Mënyrat HD duken si duhet.** 720p dhe 1080i shfaqen në 16:9 (origjinali i vizaton në 4:3), me çdo cilësim proporcioni përveç Stretch.
- **Regjistrime dhe pamje ekrani HD.** F11 regjistron 720p në 1280 x 720 dhe 1080i në 1920 x 1080 (ose kjo herë shkallëzimin), të shënuara 16:9; F8 ruan pamje ekrani në të njëjtat madhësi. Origjinali jep 640 x 480 ose buffer-in e papërpunuar 640 të gjerë.
- **Një ndërrim mënyre gjatë regjistrimit** vazhdon në një skedar të ri në madhësinë e re, në vend që të shtrydhet në të parin.
- **1080i në vendin e duhur.** Origjinali e ngre një figurë 1080i 42 rreshta lart (e prerë sipër, brez i zi poshtë); RIPPCSX2 e nis në rreshtin 40, aty ku e nis edhe kohëzimi i vetë konsolës.
- **Pika e ndërprerjes për shkrimin e të dhënave të EE-së** (e re në rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) punon: një shkrim në një adresë të vëzhguar ngre përjashtimin e korrigjimit të nivelit 2 në `0x80000100` para se të ekzekutohet, në interpretues dhe në rikompilues. GSM e OPL dhe menyja brenda lojës e RIPPS2 kanë nevojë për të për të ditur cilin kuadër tregon një lojë.
- **Rreshta regjistri për mënyrën video.** Çdo ndërrim mënyre regjistron kohëzimin e sinkronizimit dhe regjistrat e ekranit (`RIPPCSX2: video mode ...` në `logs/emulog.txt`).
- **Pa oferta të përditësuesit automatik.** Etiketat e botimit e mbajnë të fikur përditësuesin e PCSX2, ndaj nuk të "përditëson" kurrë mbrapsht te origjinali.
- Rezolucioni standard mbetet i paprekur: pamjet e ekranit në 480i janë bajt për bajt të njëjta me të origjinalit. `HDTVOutput = false` nën `[EmuCore/GS]` në `inis/PCSX2.ini` sjell sërish sjelljen origjinale HD për krahasim.

<a id="what-it-is-for"></a>

## Për çfarë shërben

- **Krijuesit e temave** (Open PS2 Loader, RiptOPL, RIPPS2): gjyko një temë në 720p dhe 1080i ashtu si e tregon një televizor, dhe bëj parapamje në madhësi reale dhe video prezantuese.
- **Zhvilluesit e homebrew-ve:** testo ELF që ndërrojnë mënyrën video, kapen pas GS-së ose përdorin regjistrat e korrigjimit të EE-së, dhe lexo në regjistër regjistrat e saktë të ekranit që vendos një mënyrë.
- **Menytë brenda lojës dhe mjetet e GS-së:** GSM e OPL, menyja brenda lojës e RIPPS2 dhe gjithçka tjetër e ndërtuar mbi pikën e ndërprerjes për shkrimin e të dhënave punojnë në emulator dhe jo vetëm në harduer.
- **Lojëra PS1:** nis Ember dhe lojërat e tij PS1 nga një disk virtual për të testuar nisjen dhe listat PS1, me BIOS-in tënd PS1 në disk.
- **Neutrino dhe POPStarter:** Neutrino i ekzekuton lojërat me shpejtësi të plotë përmes RIPPS2. POPStarter i nis lojërat PS1 vetëm me rikompiluesin EE të fikur, tani për tani rreth gjysmë shpejtësie dhe me grafikë të dëmtuar; me rikompiluesin mbetet në ekran të zi.
- **Testim i automatizuar dhe i ndihmuar nga IA:** ekzekutime me skript në një desktop të fshehur me pamje ekrani, regjistrime, gjendje të ruajtura dhe lexime memorieje përmes PINE, pa ta marrë kompjuterin.

<a id="the-end-goal-the-whole-library"></a>

## Qëllimi përfundimtar: e gjithë biblioteka

Puna më e madhe përpara është testimi i lojërave PS2 përmes rrugës së vetë kodit të Open PS2 Loader, ashtu siç i ekzekuton një konsolë, dhe shënimi i asaj që i duhet secilës: ELF, KELF, aplikacione homebrew dhe lojëra në një sandbox OPL, me mënyrat e përputhshmërisë të provuara automatikisht. Dikush mund ta përdorë këtë për ta bërë të gjithë bibliotekën të funksionojë një ditë. Ky është qëllimi përfundimtar i RIPPCSX2.

Compatibility Report është hapi i parë: rezultati i një loje, mënyrat OPL të përdorura dhe gjendja e makinës, të ruajtura në `reports/` si skedar dhe si rresht në `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Për agjentët IA, LLM-të dhe përdoruesit e tyre

Ky depo është shkruar që një agjent të mund të përgatisë gjithçka për një përdorues vetëm nga lidhja. Jepi asistentit tënd `https://github.com/akilluminati47/RIPPCSX2` dhe kërkoji të instalojë RIPPCSX2; gjithçka që i duhet është këtu:

1. **Merr build-in:** `RIPPCSX2-windows-x64-avx2.zip` nga botimi i vazhdueshëm ([lidhje e drejtpërdrejtë](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ose `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Shpaketoje në një dosje më vete; `portable.txt` i tij është tashmë pranë exe-së, ndaj nuk i prek kurrë cilësimet e një PCSX2 të instaluar.
2. **BIOS:** përdoruesi jep dump-in e BIOS-it të konsolës së vet (mos shkarko kurrë një): vendose në dosjen `bios` pranë exe-së (ose drejtoje `[Folders] Bios` në `inis/PCSX2.ini` drejt saj) dhe zgjidhe te magjistari i nisjes së parë (`[Filenames] BIOS`).
3. **Ekzekuto diçka:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ose `-- <game.iso>`. Cilësimet janë INI e thjeshtë në `inis/PCSX2.ini`; regjistrat shkojnë te `logs/emulog.txt` (`[Logging] EnableEEConsole = true` shton printf-in e EE-së).
4. **Drejtoje dhe vëzhgoje:** F8 pamje ekrani (`snaps/`), F11 regjistrim (`videos/`), F1 gjendje e ruajtur (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) për të lexuar dhe shkruar memorien e PS2 nga një skript.
5. **Testo pa vjedhur ekranin:** [`ripps2-lab/`](ripps2-lab/README.md) përshkruan një instalim laboratori (`install-lab.ps1` vendos një build në një dosje të lëvizshme dhe ruan kartat, cilësimet dhe regjistrimet e tij), dhe `tools/dev/ps2bg.ps1` i depos së RIPPS2 ekzekuton lista hapash (butona, pritje, pamje ekrani, regjistrime) në një desktop të fshehur me një panel në shiritin e detyrave që përdoruesi mund ta shohë, ta ndalë ose ta marrë në dorë.

Çfarë ndryshoi dhe pse, skedar pas skedari: **[RIPPCSX2.md](RIPPCSX2.md)**. Agjentë që punoni në kodin e këtij fork-u: mos hapni kurrë pull request, issue ose komente në projektin PCSX2 (`AGENTS.md` i tij i ndalon kontributet e bëra nga IA); RIPPCSX2 mbetet fork.

**Pa lidhje me ekipin e PCSX2.** GPL-3.0 si PCSX2. Raportoji problemet e RIPPCSX2 te RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), kurrë te PCSX2. Vijon README-ja e vetë PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 është një emulator PlayStation 2 (PS2) falas dhe me kod të hapur. Qëllimi i tij është të emulojë harduerin e PS2 duke përdorur një kombinim [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) për procesorin MIPS, [Rikompiluesish](https://en.wikipedia.org/wiki/Dynamic_recompilation) dhe një [Makine virtuale](https://en.wikipedia.org/wiki/Virtual_machine) që menaxhon gjendjet e harduerit dhe memorien e sistemit të PS2. Kjo të lejon të luash lojëra PS2 në kompjuter, me shumë veçori dhe përfitime shtesë.

<a id="project-details"></a>

## Detaje të projektit

PCSX2 është në zhvillim prej më shumë se 20 vitesh. Versionet e kaluara mund të ekzekutonin vetëm pak demo lojërash të domenit publik, por versionet e reja ekzekutojnë shumicën e lojërave me shpejtësi të plotë, përfshirë tituj të njohur si Final Fantasy X dhe Devil May Cry 3. Vizito [listën e përputhshmërisë së PCSX2](https://pcsx2.net/compat/) për gjendjen më të fundit të përputhshmërisë së lojërave (me më shumë se 2500 tituj të testuar).

Instaluesit dhe binarët për build-et e qëndrueshme dhe nightly gjenden në [faqen tonë](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Kërkesat e sistemit

PCSX2 mbështet Windows, Linux dhe Mac. [Faqja jonë e dokumentacionit të konfigurimit](https://pcsx2.net/docs/setup/requirements) ka më shumë detaje për kërkesat e softuerit dhe harduerit.

Ki parasysh se për të përdorur emulatorin nevojitet një dump BIOS nga një konsolë PS2 e zotëruar ligjërisht. Për më shumë informacion, vizito [këtë faqe](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Kontributi / Ndërtimi

PCSX2 mund të përkthehet në gjuhë të tjera përmes [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Shih [Udhëzuesin e kontributit](https://pcsx2.net/docs/contributing/) për më shumë se si të kontribuosh.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Shkarko</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temat</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontet</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Faqja</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

