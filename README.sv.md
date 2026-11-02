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
  <b>Svenska</b> |
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

<p align="center"><sub>Översättning av den engelska README; vid skillnader gäller den engelska. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Ladda ner</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teman</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Typsnitt</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Webbplats</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**En PlayStation 2-emulator för att testa och utveckla homebrew, gjord för att styras av dig eller av en AI-agent.**

RIPPCSX2 är PCSX2 v2.9.96 med de ändringar en PS2-homebrewutvecklare behöver för att se det verkliga resultatet: HD-videolägen visade, inspelade och fångade så som en HD-tv visar dem, och EE:s hårdvarubrytpunkt för data, så att menyer i spelet och videolägesverktyg som kopplar in sig på GS-registren (Open PS2 Loaders GSM, RIPPS2:s meny i spelet) fungerar som på en konsol. Allt annat är vanlig PCSX2. Det började som testlabb för frontenden [RIPPS2](https://github.com/akilluminati47/RIPPS2) och är tänkt för alla som bygger PS2-homebrew, teman eller verktyg.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Ladda ner RIPPCSX2 (zip för Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 eller 11, x64, en processor med AVX2. Packa upp den var som helst, starta `pcsx2-qtx64-avx2.exe` och peka den mot din egen BIOS-dump. Zip-filen har en tom `portable.txt` bredvid exe-filen, så RIPPCSX2 håller alla sina inställningar och filer i sin egen mapp: en PCSX2 du redan har installerad behåller sina egna inställningar, orörda. Utgåvan innehåller alltid det nyaste bygget ([dess sida](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klippen nedan ligger i [docs/videos](docs/videos).

**Den kör `.elf`-program för test:** System > Start File, eller `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, och programmet startar som det skulle från ett minneskort eller ett USB-minne på en PS2. Den **beter sig som riktig hårdvara**: ett ELF som startar ett annat ELF lämnar över maskinen och är borta, en meny i spelet som kopplar in sig på GS ritar ovanpå spelets riktiga bild, och avstängning stänger VM:en som en konsol som stängs av.

<a id="see-it-work"></a>

## Se den fungera

Varje klipp är en riktig labbkörning med det här bygget, nerklippt till under 12 sekunder.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**En AI-agent som testar ett ELF.** Inspelat från nedre högra hörnet av användarens skärm (aktivitetsfältet, en del av Claude-sessionen): Claude startar `RIPPS2.elf` i RIPPCSX2 på ett dolt skrivbord, startar Aqua Teen Hunger Force från HDD-avbildningen och öppnar RIPPS2:s meny i spelet ovanpå. Den lilla panelen är det enda på skärmen; användaren behåller tangentbord och mus.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menyn i spelet, varje funktion.** L1+L2+R1+R2+SELECT+START ovanpå ett spel som körs: ACHIEVEMENTS, RESUME (spelet fortsätter), menyn igen ovanpå en senare bild, sedan POWER OFF, som stänger VM:en. Menyn vet vilken bild den ska rita ovanpå eftersom RIPPCSX2 emulerar EE:s brytpunkt för dataskrivning.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Ett ELF som startar ett ELF, som en riktig PS2.** RIPPS2:s Memory Files öppnar `mc0:/RIPPS2/RIPPS2.ELF` (det nyaste bygget, kopierat till kortet) och kör det. Den körande RIPPS2 lämnar över och är borta; den nya laddas från kortet och startar till sin spellista.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Det du får jämfört med vanliga PCSX2 v2.9.96

- **HD-lägen ser rätt ut.** 720p och 1080i visas i 16:9 (originalet ritar dem i 4:3), med alla inställningar för bildförhållande utom Stretch.
- **HD-inspelningar och skärmbilder.** F11 spelar in 720p i 1280 x 720 och 1080i i 1920 x 1080 (eller det gånger uppskalningen), märkt 16:9; F8 sparar skärmbilder i samma storlekar. Originalet ger 640 x 480 eller den råa bufferten på 640 i bredd.
- **Ett lägesbyte mitt i en inspelning** fortsätter i en ny fil i den nya storleken, i stället för att klämmas in i den första.
- **1080i på rätt plats.** Originalet flyttar upp en 1080i-bild 42 linjer (överkanten bortskuren, svart band nedtill); RIPPCSX2 börjar den på linje 40, där konsolens egen timing gör det.
- **EE:s brytpunkt för dataskrivning** (ny i rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) fungerar: en skrivning till en bevakad adress utlöser felsökningsundantaget på nivå 2 vid `0x80000100` innan den utförs, i tolken och i omkompilatorn. OPL:s GSM och RIPPS2:s meny i spelet behöver den för att veta vilken bild ett spel visar.
- **Loggrader för videoläget.** Varje lägesbyte loggar synktiming och skärmregister (`RIPPCSX2: video mode ...` i `logs/emulog.txt`).
- **Inga erbjudanden från den automatiska uppdateraren.** Utgåvetaggar håller PCSX2:s uppdaterare avstängd, så den aldrig "uppdaterar" dig tillbaka till originalet.
- Standardupplösning är orörd: skärmbilder i 480i är byte för byte desamma som originalets. `HDTVOutput = false` under `[EmuCore/GS]` i `inis/PCSX2.ini` tar tillbaka originalets HD-beteende för en jämförelse sida vid sida.

<a id="what-it-is-for"></a>

## Vad den är till för

- **Temamakare** (Open PS2 Loader, RiptOPL, RIPPS2): bedöm ett tema i 720p och 1080i så som en tv visar det, och gör förhandsvisningar i verklig storlek och genomgångsvideor.
- **Homebrewutvecklare:** testa ELF:er som byter videoläge, kopplar in sig på GS eller använder EE:s felsökningsregister, och läs i loggen exakt vilka skärmregister ett läge sätter.
- **Menyer i spelet och GS-verktyg:** OPL:s GSM, RIPPS2:s meny i spelet och allt annat som bygger på brytpunkten för dataskrivning körs i emulatorn i stället för bara på hårdvara.
- **Automatiserad och AI-assisterad testning:** skriptade körningar på ett dolt skrivbord med skärmbilder, inspelningar, sparlägen och PINE-minnesläsningar, utan att ta över din dator.

<a id="for-ai-agents-llms-and-their-users"></a>

## För AI-agenter, LLM:er och deras användare

Det här repot är skrivet så att en agent kan sätta upp allt åt en användare bara utifrån länken. Ge din assistent `https://github.com/akilluminati47/RIPPCSX2` och be den installera RIPPCSX2; allt den behöver finns här:

1. **Hämta bygget:** `RIPPCSX2-windows-x64-avx2.zip` från den löpande utgåvan ([direktlänk](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), eller `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Packa upp den i en egen mapp; dess `portable.txt` ligger redan bredvid exe-filen, så den rör aldrig en installerad PCSX2:s inställningar.
2. **BIOS:** användaren tillhandahåller BIOS-dumpen från sin egen konsol (ladda aldrig ner en): lägg den i mappen `bios` bredvid exe-filen (eller peka `[Folders] Bios` i `inis/PCSX2.ini` mot den) och välj den i guiden vid första start (`[Filenames] BIOS`).
3. **Kör något:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, eller `-- <game.iso>`. Inställningarna är vanlig INI i `inis/PCSX2.ini`; loggar hamnar i `logs/emulog.txt` (`[Logging] EnableEEConsole = true` lägger till EE:s printf).
4. **Styr och observera den:** F8 skärmbild (`snaps/`), F11 inspelning (`videos/`), F1 sparläge (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) för att läsa och skriva PS2-minne från ett skript.
5. **Testa utan att ta över skärmen:** [`ripps2-lab/`](ripps2-lab/README.md) beskriver en labbinstallation (`install-lab.ps1` lägger ett bygge i en portabel mapp och behåller dess kort, inställningar och inspelningar), och RIPPS2-repots `tools/dev/ps2bg.ps1` kör steglistor (knappar, väntetider, skärmbilder, inspelningar) på ett dolt skrivbord med en panel i aktivitetsfältet som användaren kan titta på, stoppa eller ta över.

Vad som ändrats och varför, fil för fil: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenter som arbetar med den här forkens kod: öppna aldrig pull requests, issues eller kommentarer hos PCSX2-projektet (dess `AGENTS.md` förbjuder AI-gjorda bidrag); RIPPCSX2 förblir en fork.

**Inte knuten till PCSX2-teamet.** GPL-3.0 som PCSX2. Rapportera problem med RIPPCSX2 till RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), aldrig till PCSX2. PCSX2:s egen README följer.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 är en fri PlayStation 2-emulator (PS2) med öppen källkod. Syftet är att emulera PS2:ns hårdvara med en kombination av [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) för MIPS-processorn, [omkompilatorer](https://en.wikipedia.org/wiki/Dynamic_recompilation) och en [virtuell maskin](https://en.wikipedia.org/wiki/Virtual_machine) som hanterar hårdvarutillstånd och PS2:ns systemminne. Det låter dig spela PS2-spel på din dator, med många extra funktioner och fördelar.

<a id="project-details"></a>

## Projektdetaljer

PCSX2 har utvecklats i mer än 20 år. Tidigare versioner kunde bara köra några få speldemos i allmän egendom, men nyare versioner kan köra de flesta spel i full hastighet, bland dem populära titlar som Final Fantasy X och Devil May Cry 3. Besök [PCSX2:s kompatibilitetslista](https://pcsx2.net/compat/) för spelens senaste kompatibilitetsstatus (med mer än 2500 testade titlar).

Installationsprogram och binärfiler för både stabila och nightly-byggen finns på [vår webbplats](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Systemkrav

PCSX2 stöder Windows, Linux och Mac. Vår [dokumentationssida om installation](https://pcsx2.net/docs/setup/requirements) har fler detaljer om programvaru- och hårdvarukrav.

Observera att en BIOS-dump från en lagligt ägd PS2-konsol krävs för att använda emulatorn. Mer information finns på [den här sidan](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Bidra / Bygga

PCSX2 kan översättas till andra språk via [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Se [Guiden för bidrag](https://pcsx2.net/docs/contributing/) för mer om hur du bidrar.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Ladda ner</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teman</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Typsnitt</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Webbplats</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

