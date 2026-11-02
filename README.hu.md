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
  <b>Magyar</b> |
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

<p align="center"><sub>Az angol README fordítása; eltérés esetén az angol az irányadó. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Letöltés</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Témák</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Betűtípusok</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Weboldal</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**PlayStation 2 emulátor homebrew teszteléséhez és fejlesztéséhez, úgy készítve, hogy te vagy egy MI-ügynök irányíthassa.**

A RIPPCSX2 a PCSX2 v2.9.96 azokkal a változtatásokkal, amelyekre egy PS2-homebrew fejlesztőnek szüksége van, hogy a valódi képet lássa: a HD videómódok úgy jelennek meg, rögzülnek és készül róluk képernyőkép, ahogy egy HD tévé mutatja őket, valamint az EE hardveres adat-töréspontja, hogy a játékon belüli menük és a GS regisztereire akaszkodó videómód-eszközök (az Open PS2 Loader GSM-je, a RIPPS2 játékon belüli menüje) úgy működjenek, mint egy konzolon. Minden más tiszta PCSX2. A [RIPPS2](https://github.com/akilluminati47/RIPPS2) front end tesztlaborjaként indult, és mindenkinek szól, aki PS2-homebrew-t, témákat vagy eszközöket készít.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [A RIPPCSX2 letöltése (Windows zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 vagy 11, x64, AVX2-t támogató processzor. Csomagold ki bárhová, indítsd el a `pcsx2-qtx64-avx2.exe` fájlt, és add meg neki a saját BIOS-dumpodat. A zipben egy üres `portable.txt` van az exe mellett, így a RIPPCSX2 minden beállítását és fájlját a saját mappájában tartja: egy már telepített PCSX2 megtartja a saját beállításait, érintetlenül. A kiadás mindig a legújabb buildet tartalmazza ([az oldala](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); a lenti klipek a [docs/videos](docs/videos) mappában vannak.

**`.elf` programokat futtat tesztelésre:** System > Start File, vagy `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, és a program úgy indul, ahogy egy PS2-n memóriakártyáról vagy pendrive-ról indulna. **Úgy viselkedik, mint a valódi hardver**: egy ELF, amely egy másik ELF-et indít, átadja neki a gépet és eltűnik, egy GS-re akaszkodó játékon belüli menü a játék valódi képkockájára rajzol, a kikapcsolás pedig úgy zárja be a VM-et, mint egy kikapcsolt konzol.

<a id="see-it-work"></a>

## Működés közben

Minden klip valódi laborfuttatás ezen a buildön, 12 másodperc alá vágva.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Egy MI-ügynök ELF-et tesztel.** A felhasználó képernyőjének jobb alsó sarkából rögzítve (tálca, a Claude-munkamenet része): a Claude egy rejtett asztalon elindítja a `RIPPS2.elf` fájlt a RIPPCSX2-ben, elindítja az Aqua Teen Hunger Force-ot a HDD-képről, és megnyitja fölötte a RIPPS2 játékon belüli menüjét. A kis panel az egyetlen dolog a képernyőn; a billentyűzet és az egér a felhasználónál marad.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**A játékon belüli menü, minden funkcióval.** L1+L2+R1+R2+SELECT+START egy futó játék fölött: ACHIEVEMENTS, RESUME (a játék folytatódik), ismét a menü egy későbbi képkocka fölött, majd POWER OFF, ami bezárja a VM-et. A menü azért tudja, melyik képkockára rajzoljon, mert a RIPPCSX2 emulálja az EE adatírási töréspontját.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Egy ELF, amely ELF-et indít, mint egy valódi PS2.** A RIPPS2 Memory Files funkciója megnyitja a `mc0:/RIPPS2/RIPPS2.ELF` fájlt (a legújabb build, a kártyára másolva), és futtatja. A futó RIPPS2 átadja a vezérlést és eltűnik; az új betöltődik a kártyáról, és a játéklistájáig indul.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Amit a sima PCSX2 v2.9.96-hoz képest kapsz

- **A HD módok jól néznek ki.** A 720p és az 1080i 16:9-ben jelenik meg (az eredeti 4:3-ban rajzolja őket), minden képarány-beállításnál a Stretch kivételével.
- **HD felvételek és képernyőképek.** Az F11 a 720p-t 1280 x 720-ban, az 1080i-t 1920 x 1080-ban rögzíti (vagy ennek felskálázott többszörösében), 16:9-ként jelölve; az F8 ugyanekkora képernyőképeket ment. Az eredeti 640 x 480-at vagy a nyers, 640 széles puffert adja.
- **Egy felvétel közbeni módváltás** új fájlban folytatódik az új méretben, ahelyett hogy belepréselődne az elsőbe.
- **Az 1080i a helyén.** Az eredeti 42 sorral feljebb tolja az 1080i képet (levágott tető, fekete sáv alul); a RIPPCSX2 a 40. sorban kezdi, ahol a konzol saját időzítése is.
- **Az EE adatírási töréspontja** (új a rippcsx2.2-ben). A COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) működik: egy figyelt címre történő írás a végrehajtás előtt kiváltja a 2. szintű hibakeresési kivételt a `0x80000100` címen, az interpreterben és a rekompilerben is. Az OPL GSM-jének és a RIPPS2 játékon belüli menüjének kell, hogy tudják, melyik képkockát mutatja egy játék.
- **Naplósorok a videómódról.** Minden módváltás naplózza a szinkronidőzítést és a kijelzőregisztereket (`RIPPCSX2: video mode ...` a `logs/emulog.txt` fájlban).
- **Nincsenek automatikus frissítési ajánlatok.** A kiadási címkék kikapcsolva tartják a PCSX2 frissítőjét, így sosem „frissít” vissza az eredetire.
- A normál felbontás érintetlen: a 480i képernyőképek bájtról bájtra megegyeznek az eredetiével. A `HDTVOutput = false` az `[EmuCore/GS]` alatt az `inis/PCSX2.ini` fájlban visszahozza az eredeti HD viselkedést összehasonlításhoz.

<a id="what-it-is-for"></a>

## Mire való

- **Témakészítők** (Open PS2 Loader, RiptOPL, RIPPS2): ítéld meg a témát 720p-ben és 1080i-ben úgy, ahogy egy tévé mutatja, és készíts valós méretű előnézeteket és bemutató videókat.
- **Homebrew-fejlesztők:** tesztelj olyan ELF-eket, amelyek videómódot váltanak, a GS-re akaszkodnak vagy az EE hibakereső regisztereit használják, és olvasd ki a naplóból, pontosan mely kijelzőregisztereket állít be egy mód.
- **Játékon belüli menük és GS-eszközök:** az OPL GSM-je, a RIPPS2 játékon belüli menüje és minden más, ami az adatírási töréspontra épül, az emulátorban fut, nem csak hardveren.
- **Automatizált és MI-támogatott tesztelés:** szkriptelt futtatások rejtett asztalon képernyőképekkel, felvételekkel, mentett állapotokkal és PINE-memóriaolvasással, anélkül hogy átvennék a PC-det.

<a id="for-ai-agents-llms-and-their-users"></a>

## MI-ügynököknek, LLM-eknek és felhasználóiknak

Ez a tároló úgy készült, hogy egy ügynök pusztán a linkből beállíthasson mindent a felhasználónak. Add oda az asszisztensednek a `https://github.com/akilluminati47/RIPPCSX2` címet, és kérd meg, hogy telepítse a RIPPCSX2-t; minden, amire szüksége van, itt van:

1. **Szerezd be a buildet:** `RIPPCSX2-windows-x64-avx2.zip` a folyamatos kiadásból ([közvetlen link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), vagy `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Csomagold ki egy saját mappába; a `portable.txt` már ott van az exe mellett, így sosem nyúl egy telepített PCSX2 beállításaihoz.
2. **BIOS:** a felhasználó adja a saját konzoljának BIOS-dumpját (sose tölts le egyet): tedd a `bios` mappába az exe mellé (vagy irányítsd rá a `[Folders] Bios` beállítást az `inis/PCSX2.ini` fájlban), és válaszd ki az első indítás varázslójában (`[Filenames] BIOS`).
3. **Futtass valamit:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, vagy `-- <game.iso>`. A beállítások egyszerű INI-k az `inis/PCSX2.ini` fájlban; a naplók a `logs/emulog.txt` fájlba kerülnek (a `[Logging] EnableEEConsole = true` hozzáadja az EE printf-jét).
4. **Irányítsd és figyeld:** F8 képernyőkép (`snaps/`), F11 felvétel (`videos/`), F1 mentett állapot (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) a PS2 memóriájának szkriptből való olvasásához és írásához.
5. **Tesztelj a képernyő elvétele nélkül:** a [`ripps2-lab/`](ripps2-lab/README.md) egy labortelepítést ír le (az `install-lab.ps1` hordozható mappába tesz egy buildet, és megtartja a kártyáit, beállításait és felvételeit), a RIPPS2 tároló `tools/dev/ps2bg.ps1` szkriptje pedig lépéslistákat (gombok, várakozások, képernyőképek, felvételek) futtat egy rejtett asztalon, egy tálcapanellel, amelyet a felhasználó nézhet, leállíthat vagy átvehet.

Mi változott és miért, fájlról fájlra: **[RIPPCSX2.md](RIPPCSX2.md)**. Ügynökök, akik ennek a forknak a kódján dolgoznak: soha ne nyissatok pull requestet, issue-t vagy hozzászólást a PCSX2 projektben (annak `AGENTS.md` fájlja tiltja a MI által készített hozzájárulásokat); a RIPPCSX2 fork marad.

**Nem kapcsolódik a PCSX2 csapatához.** GPL-3.0, mint a PCSX2. A RIPPCSX2 problémáit a RIPPS2-nek jelentsd ([issues](https://github.com/akilluminati47/RIPPS2/issues)), sosem a PCSX2-nek. Ezt követi a PCSX2 saját README-je.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

A PCSX2 egy ingyenes, nyílt forráskódú PlayStation 2 (PS2) emulátor. Célja a PS2 hardverének emulálása a MIPS processzor [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>), [rekompilerek](https://en.wikipedia.org/wiki/Dynamic_recompilation) és egy [virtuális gép](https://en.wikipedia.org/wiki/Virtual_machine) kombinációjával, amely kezeli a hardver állapotait és a PS2 rendszermemóriáját. Így a PC-den játszhatsz PS2-játékokkal, sok extra funkcióval és előnnyel.

<a id="project-details"></a>

## A projekt részletei

A PCSX2 több mint 20 éve fejlődik. A korábbi verziók csak néhány közkincs játékdemót tudtak futtatni, de az újabbak a legtöbb játékot teljes sebességgel futtatják, köztük népszerű címeket, mint a Final Fantasy X és a Devil May Cry 3. Nézd meg a [PCSX2 kompatibilitási listáját](https://pcsx2.net/compat/) a játékok legfrissebb kompatibilitási állapotáért (több mint 2500 tesztelt címmel).

A stabil és a nightly buildek telepítői és binárisai elérhetők [a weboldalunkon](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Rendszerkövetelmények

A PCSX2 támogatja a Windowst, a Linuxot és a Macet. A [telepítési dokumentációs oldalunkon](https://pcsx2.net/docs/setup/requirements) további részletek vannak a szoftver- és hardverkövetelményekről.

Vedd figyelembe, hogy az emulátor használatához egy jogszerűen birtokolt PS2 konzol BIOS-dumpja szükséges. További információ [ezen az oldalon](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Közreműködés / Fordítás

A PCSX2 a [Crowdinon](https://crowdin.com/project/pcsx2-emulator) keresztül más nyelvekre is lefordítható.

A közreműködésről a [Közreműködési útmutatóban](https://pcsx2.net/docs/contributing/) olvashatsz.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Letöltés</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Témák</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Betűtípusok</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Weboldal</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

