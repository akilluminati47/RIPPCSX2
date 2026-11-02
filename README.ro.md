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
  <b>Română</b> |
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

<p align="center"><sub>Traducerea README-ului în engleză; dacă diferă, este valabilă engleza. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descarcă</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fonturi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Un emulator PlayStation 2 pentru testarea și dezvoltarea homebrew, făcut să fie condus de tine sau de un agent AI.**

RIPPCSX2 este PCSX2 v2.9.96 cu schimbările de care un dezvoltator de homebrew pentru PS2 are nevoie ca să vadă realitatea: modurile video HD afișate, înregistrate și capturate așa cum le arată un televizor HD, și punctul de întrerupere hardware pentru date al EE, ca meniurile din joc și uneltele de mod video care se agață de regiștrii GS (GSM din Open PS2 Loader, meniul din joc al RIPPS2) să funcționeze ca pe o consolă. Restul e PCSX2 simplu. A pornit ca laborator de test al front end-ului [RIPPS2](https://github.com/akilluminati47/RIPPS2) și e gândit pentru oricine face homebrew, teme sau unelte pentru PS2.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Descarcă RIPPCSX2 (zip pentru Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 sau 11, x64, un procesor cu AVX2. Dezarhivează-l oriunde, pornește `pcsx2-qtx64-avx2.exe` și indică-i propriul dump de BIOS. Zip-ul are un `portable.txt` gol lângă exe, așa că RIPPCSX2 își ține toate setările și fișierele în propriul folder: un PCSX2 pe care îl ai deja instalat își păstrează setările, neatinse. Versiunea conține mereu cel mai nou build ([pagina ei](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); clipurile de mai jos sunt în [docs/videos](docs/videos).

**Rulează programe `.elf` pentru test:** System > Start File, sau `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, iar programul pornește cum ar porni de pe un card de memorie sau un stick USB pe un PS2. **Se comportă ca hardware-ul real**: un ELF care pornește alt ELF îi predă mașina și dispare, un meniu din joc agățat de GS se desenează peste cadrul real al jocului, iar oprirea închide VM-ul ca o consolă care se stinge.

<a id="see-it-work"></a>

## Vezi-l lucrând

Fiecare clip e o rulare reală în laborator pe acest build, tăiată sub 12 secunde.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Un agent AI testând un ELF.** Înregistrat din colțul din dreapta jos al ecranului utilizatorului (bara de activități, o parte din sesiunea Claude): Claude pornește `RIPPS2.elf` în RIPPCSX2 pe un desktop ascuns, lansează Aqua Teen Hunger Force de pe imaginea HDD și deschide peste el meniul din joc al RIPPS2. Panoul mic e singurul lucru de pe ecran; utilizatorul își păstrează tastatura și mouse-ul.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Meniul din joc, fiecare funcție.** L1+L2+R1+R2+SELECT+START peste un joc care rulează: ACHIEVEMENTS, RESUME (jocul continuă), din nou meniul peste un cadru mai târziu, apoi POWER OFF, care închide VM-ul. Meniul știe peste ce cadru să deseneze pentru că RIPPCSX2 emulează punctul de întrerupere la scrierea datelor al EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Un ELF care lansează un ELF, ca un PS2 real.** Memory Files din RIPPS2 deschide `mc0:/RIPPS2/RIPPS2.ELF` (cel mai nou build, copiat pe card) și îl rulează. RIPPS2 care rula predă controlul și dispare; cel nou se încarcă de pe card și pornește până la lista lui de jocuri.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Ce primești față de PCSX2 v2.9.96 simplu

- **Modurile HD arată corect.** 720p și 1080i sunt afișate în 16:9 (originalul le desenează în 4:3), cu orice setare de aspect în afară de Stretch.
- **Înregistrări și capturi HD.** F11 înregistrează 720p la 1280 x 720 și 1080i la 1920 x 1080 (sau asta înmulțit cu scalarea), marcate 16:9; F8 salvează capturi la aceleași dimensiuni. Originalul dă 640 x 480 sau bufferul brut lat de 640.
- **O schimbare de mod în timpul înregistrării** continuă într-un fișier nou la noua dimensiune, în loc să se înghesuie în primul.
- **1080i la locul lui.** Originalul mută o imagine 1080i cu 42 de linii în sus (tăiată sus, bandă neagră jos); RIPPCSX2 o începe la linia 40, unde o începe și sincronizarea consolei înseși.
- **Punctul de întrerupere la scrierea datelor al EE** (nou în rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funcționează: o scriere la o adresă urmărită ridică excepția de depanare de nivel 2 la `0x80000100` înainte de a se executa, în interpretor și în recompilator. GSM din OPL și meniul din joc al RIPPS2 au nevoie de el ca să știe ce cadru arată un joc.
- **Linii de jurnal pentru modul video.** Fiecare schimbare de mod înregistrează sincronizarea și regiștrii de afișare (`RIPPCSX2: video mode ...` în `logs/emulog.txt`).
- **Fără oferte de actualizare automată.** Etichetele de versiune țin oprit actualizatorul PCSX2, așa că nu te „actualizează” niciodată înapoi la original.
- Definiția standard rămâne neatinsă: capturile în 480i sunt identice octet cu octet cu ale originalului. `HDTVOutput = false` sub `[EmuCore/GS]` în `inis/PCSX2.ini` aduce înapoi comportamentul HD original pentru comparație.

<a id="what-it-is-for"></a>

## La ce folosește

- **Creatori de teme** (Open PS2 Loader, RiptOPL, RIPPS2): judecă o temă în 720p și 1080i așa cum o arată un televizor, și fă previzualizări la mărime reală și videoclipuri de prezentare.
- **Dezvoltatori de homebrew:** testează ELF-uri care schimbă modul video, se agață de GS sau folosesc regiștrii de depanare ai EE, și citește în jurnal regiștrii de afișare exacți pe care îi setează un mod.
- **Meniuri din joc și unelte GS:** GSM din OPL, meniul din joc al RIPPS2 și orice altceva construit pe punctul de întrerupere la scrierea datelor rulează în emulator, nu doar pe hardware.
- **Testare automată și asistată de AI:** rulări scriptate pe un desktop ascuns cu capturi, înregistrări, stări salvate și citiri de memorie prin PINE, fără să-ți acapareze PC-ul.

<a id="for-ai-agents-llms-and-their-users"></a>

## Pentru agenți AI, LLM-uri și utilizatorii lor

Acest depozit e scris ca un agent să poată configura totul pentru un utilizator doar din link. Dă-i asistentului tău `https://github.com/akilluminati47/RIPPCSX2` și cere-i să instaleze RIPPCSX2; tot ce îi trebuie e aici:

1. **Ia build-ul:** `RIPPCSX2-windows-x64-avx2.zip` din versiunea continuă ([link direct](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), sau `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Dezarhivează-l într-un folder propriu; `portable.txt` e deja lângă exe, așa că nu atinge niciodată setările unui PCSX2 instalat.
2. **BIOS:** utilizatorul furnizează dump-ul de BIOS al propriei console (nu descărca niciodată unul): pune-l în folderul `bios` lângă exe (sau îndreaptă `[Folders] Bios` din `inis/PCSX2.ini` spre el) și alege-l în expertul de la prima pornire (`[Filenames] BIOS`).
3. **Rulează ceva:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, sau `-- <game.iso>`. Setările sunt INI simplu în `inis/PCSX2.ini`; jurnalele merg în `logs/emulog.txt` (`[Logging] EnableEEConsole = true` adaugă printf-ul EE).
4. **Condu-l și observă-l:** F8 captură (`snaps/`), F11 înregistrare (`videos/`), F1 stare salvată (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) ca să citești și să scrii memoria PS2 dintr-un script.
5. **Testează fără să furi ecranul:** [`ripps2-lab/`](ripps2-lab/README.md) descrie o instalare de laborator (`install-lab.ps1` pune un build într-un folder portabil și îi păstrează cardurile, setările și înregistrările), iar `tools/dev/ps2bg.ps1` din depozitul RIPPS2 rulează liste de pași (butoane, așteptări, capturi, înregistrări) pe un desktop ascuns, cu un panou în bara de activități pe care utilizatorul îl poate urmări, opri sau prelua.

Ce s-a schimbat și de ce, fișier cu fișier: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenți care lucrați la codul acestui fork: nu deschideți niciodată pull requesturi, issues sau comentarii în proiectul PCSX2 (`AGENTS.md`-ul lui interzice contribuțiile făcute de AI); RIPPCSX2 rămâne un fork.

**Nu este afiliat echipei PCSX2.** GPL-3.0 ca PCSX2. Raportează problemele RIPPCSX2 la RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), niciodată la PCSX2. Urmează README-ul propriu al PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 este un emulator PlayStation 2 (PS2) gratuit și open source. Scopul lui este să emuleze hardware-ul PS2 folosind o combinație de [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) pentru procesorul MIPS, [Recompilatoare](https://en.wikipedia.org/wiki/Dynamic_recompilation) și o [Mașină virtuală](https://en.wikipedia.org/wiki/Virtual_machine) care gestionează stările hardware și memoria de sistem a PS2. Asta îți permite să joci jocuri PS2 pe PC, cu multe funcții și avantaje suplimentare.

<a id="project-details"></a>

## Detalii despre proiect

PCSX2 e în dezvoltare de peste 20 de ani. Versiunile vechi puteau rula doar câteva demo-uri din domeniul public, dar cele noi rulează majoritatea jocurilor la viteză maximă, inclusiv titluri populare ca Final Fantasy X și Devil May Cry 3. Vezi [lista de compatibilitate PCSX2](https://pcsx2.net/compat/) pentru cea mai recentă stare de compatibilitate a jocurilor (peste 2500 de titluri testate).

Programele de instalare și binarele pentru build-urile stabile și nightly sunt disponibile pe [site-ul nostru](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Cerințe de sistem

PCSX2 suportă Windows, Linux și Mac. [Pagina noastră de documentație despre configurare](https://pcsx2.net/docs/setup/requirements) are mai multe detalii despre cerințele software și hardware.

Reține că pentru a folosi emulatorul e nevoie de un dump de BIOS de pe o consolă PS2 deținută legal. Pentru mai multe informații, vezi [această pagină](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuții / Compilare

PCSX2 poate fi tradus în alte limbi prin [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Vezi [Ghidul de contribuție](https://pcsx2.net/docs/contributing/) pentru mai multe despre cum poți contribui.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Descarcă</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fonturi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

