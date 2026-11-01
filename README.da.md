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
  <b>Dansk</b> |
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

<p align="center"><sub>Oversættelse af den engelske README; hvis de afviger, gælder den engelske. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Hent</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temaer</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Skrifttyper</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Websted</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**En PlayStation 2-emulator til at teste og udvikle homebrew, lavet til at blive styret af dig eller af en AI-agent.**

RIPPCSX2 er PCSX2 v2.9.96 med de ændringer, en PS2-homebrewudvikler har brug for for at se det ægte billede: HD-videotilstande vist, optaget og fotograferet sådan som et HD-tv viser dem, og EE’ens hardware-databreakpoint, så menuer i spillet og videotilstandsværktøjer, der kobler sig på GS-registrene (Open PS2 Loaders GSM, RIPPS2s menu i spillet), virker som på en konsol. Alt andet er almindelig PCSX2. Det begyndte som testlaboratorium for frontenden [RIPPS2](https://github.com/akilluminati47/RIPPS2) og er beregnet til alle, der laver PS2-homebrew, temaer eller værktøjer.

### [Hent RIPPCSX2 (Windows-zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 eller 11, x64, en CPU med AVX2. Pak den ud hvor som helst, start `pcsx2-qtx64-avx2.exe`, og peg den mod dit eget BIOS-dump. Zip-filen har en tom `portable.txt` ved siden af exe-filen, så RIPPCSX2 holder alle sine indstillinger og filer i sin egen mappe: en PCSX2, du allerede har installeret, beholder sine egne indstillinger, urørte. Udgivelsen indeholder altid det nyeste build ([dens side](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klippene nedenfor ligger i [docs/videos](docs/videos).

**Den kører `.elf`-programmer til test:** System > Start File eller `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, og programmet starter, som det ville fra et memorycard eller en USB-nøgle på en PS2. Den **opfører sig som rigtig hardware**: et ELF, der starter et andet ELF, overlader maskinen og er væk, en menu i spillet, der kobler sig på GS, tegner oven på spillets ægte billede, og sluk lukker VM’en som en konsol, der slukkes.

## Se den virke

Hvert klip er en ægte laboratoriekørsel på dette build, klippet ned til under 12 sekunder.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**En AI-agent tester et ELF.** Optaget fra nederste højre hjørne af brugerens skærm (proceslinjen, en del af Claude-sessionen): Claude starter `RIPPS2.elf` i RIPPCSX2 på et skjult skrivebord, starter Aqua Teen Hunger Force fra HDD-billedet og åbner RIPPS2s menu i spillet oven på det. Det lille panel er det eneste på skærmen; brugeren beholder tastatur og mus.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menuen i spillet, hver funktion.** L1+L2+R1+R2+SELECT+START oven på et kørende spil: ACHIEVEMENTS, RESUME (spillet kører videre), menuen igen oven på et senere billede og så POWER OFF, som lukker VM’en. Menuen ved, hvilket billede den skal tegne oven på, fordi RIPPCSX2 emulerer EE’ens breakpoint for dataskrivning.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Et ELF, der starter et ELF, som en rigtig PS2.** RIPPS2s Memory Files åbner `mc0:/RIPPS2/RIPPS2.ELF` (det nyeste build, kopieret til kortet) og kører det. Den kørende RIPPS2 overlader og er væk; den nye indlæses fra kortet og starter op i sin spilliste.

## Hvad du får i forhold til almindelig PCSX2 v2.9.96

- **HD-tilstande ser rigtige ud.** 720p og 1080i vises i 16:9 (originalen tegner dem i 4:3), med alle billedformatindstillinger undtagen Stretch.
- **HD-optagelser og skærmbilleder.** F11 optager 720p i 1280 x 720 og 1080i i 1920 x 1080 (eller det gange opskaleringen), mærket 16:9; F8 gemmer skærmbilleder i samme størrelser. Originalen giver 640 x 480 eller den rå buffer på 640 i bredden.
- **Et tilstandsskift midt i en optagelse** fortsætter i en ny fil i den nye størrelse i stedet for at blive klemt ind i den første.
- **1080i på rette sted.** Originalen flytter et 1080i-billede 42 linjer op (toppen skåret af, sort bånd forneden); RIPPCSX2 begynder det på linje 40, hvor konsollens egen timing gør det.
- **EE’ens breakpoint for dataskrivning** (nyt i rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) virker: en skrivning til en overvåget adresse udløser fejlsøgningsundtagelsen på niveau 2 ved `0x80000100`, før den udføres, i fortolkeren og i rekompileren. OPLs GSM og RIPPS2s menu i spillet har brug for det for at vide, hvilket billede et spil viser.
- **Loglinjer for videotilstand.** Hvert tilstandsskift logger synkroniseringstiming og skærmregistre (`RIPPCSX2: video mode ...` i `logs/emulog.txt`).
- **Ingen tilbud fra den automatiske opdatering.** Udgivelsesmærker holder PCSX2s opdatering slukket, så den aldrig "opdaterer" dig tilbage til originalen.
- Standardopløsning er urørt: 480i-skærmbilleder er byte for byte de samme som originalens. `HDTVOutput = false` under `[EmuCore/GS]` i `inis/PCSX2.ini` bringer den originale HD-opførsel tilbage til en side om side-sammenligning.

## Hvad den er til

- **Temamagere** (Open PS2 Loader, RiptOPL, RIPPS2): bedøm et tema i 720p og 1080i, som et tv viser det, og lav forhåndsvisninger i fuld størrelse og rundvisningsvideoer.
- **Homebrewudviklere:** test ELF’er, der skifter videotilstand, kobler sig på GS eller bruger EE’ens fejlsøgningsregistre, og læs i loggen de præcise skærmregistre, en tilstand sætter.
- **Menuer i spillet og GS-værktøjer:** OPLs GSM, RIPPS2s menu i spillet og alt andet, der bygger på breakpointet for dataskrivning, kører i emulatoren i stedet for kun på hardware.
- **Automatiseret og AI-assisteret test:** scriptede kørsler på et skjult skrivebord med skærmbilleder, optagelser, gemte tilstande og PINE-hukommelseslæsninger, uden at overtage din pc.

## Til AI-agenter, LLM’er og deres brugere

Dette repo er skrevet, så en agent kan sætte en bruger op ud fra linket alene. Giv din assistent `https://github.com/akilluminati47/RIPPCSX2`, og bed den installere RIPPCSX2; alt, hvad den har brug for, står her:

1. **Hent buildet:** `RIPPCSX2-windows-x64-avx2.zip` fra den løbende udgivelse ([direkte link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) eller `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Pak den ud i sin egen mappe; dens `portable.txt` ligger allerede ved exe-filen, så den rører aldrig en installeret PCSX2s indstillinger.
2. **BIOS:** brugeren leverer BIOS-dumpet fra sin egen konsol (hent aldrig et): læg det i mappen `bios` ved siden af exe-filen (eller lad `[Folders] Bios` i `inis/PCSX2.ini` pege på det), og vælg det i guiden ved første start (`[Filenames] BIOS`).
3. **Kør noget:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` eller `-- <game.iso>`. Indstillingerne er almindelig INI i `inis/PCSX2.ini`; logfiler går til `logs/emulog.txt` (`[Logging] EnableEEConsole = true` tilføjer EE’ens printf).
4. **Styr og iagttag den:** F8 skærmbillede (`snaps/`), F11 optagelse (`videos/`), F1 gemt tilstand (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) til at læse og skrive PS2-hukommelse fra et script.
5. **Test uden at stjæle skærmen:** [`ripps2-lab/`](ripps2-lab/README.md) beskriver en laboratorieinstallation (`install-lab.ps1` lægger et build i en flytbar mappe og beholder dens kort, indstillinger og optagelser), og RIPPS2-repoets `tools/dev/ps2bg.ps1` kører trinlister (knapper, ventetider, skærmbilleder, optagelser) på et skjult skrivebord med et proceslinjepanel, som brugeren kan se, stoppe eller overtage.

Hvad der er ændret og hvorfor, fil for fil: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenter, der arbejder på denne forks kode: åbn aldrig pull requests, issues eller kommentarer hos PCSX2-projektet (dets `AGENTS.md` forbyder bidrag lavet af AI); RIPPCSX2 forbliver en fork.

**Ikke tilknyttet PCSX2-holdet.** GPL-3.0 som PCSX2. Rapportér RIPPCSX2-problemer til RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), aldrig til PCSX2. PCSX2s egen README følger.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 er en fri PlayStation 2-emulator (PS2) med åben kildekode. Formålet er at emulere PS2’ens hardware ved hjælp af en kombination af [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) til MIPS-CPU’en, [rekompilere](https://en.wikipedia.org/wiki/Dynamic_recompilation) og en [virtuel maskine](https://en.wikipedia.org/wiki/Virtual_machine), der styrer hardwaretilstande og PS2’ens systemhukommelse. Det lader dig spille PS2-spil på din pc med mange ekstra funktioner og fordele.

## Projektdetaljer

PCSX2 har været under udvikling i mere end 20 år. Tidligere versioner kunne kun køre nogle få spildemoer fra det offentlige domæne, men nyere versioner kan køre de fleste spil i fuld hastighed, også populære titler som Final Fantasy X og Devil May Cry 3. Besøg [PCSX2s kompatibilitetsliste](https://pcsx2.net/compat/) for den seneste kompatibilitetsstatus for spil (med mere end 2500 testede titler).

Installationsprogrammer og binære filer til både stabile og nightly builds findes på [vores hjemmeside](https://pcsx2.net/downloads/).

## Systemkrav

PCSX2 understøtter Windows, Linux og Mac. Vores [dokumentationsside om opsætning](https://pcsx2.net/docs/setup/requirements) har flere detaljer om software- og hardwarekrav.

Bemærk, at et BIOS-dump fra en lovligt ejet PS2-konsol er påkrævet for at bruge emulatoren. Besøg [denne side](https://pcsx2.net/docs/setup/bios/) for mere information.

## Bidrag / Byg

PCSX2 kan oversættes til andre sprog via [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Se [Bidragsguiden](https://pcsx2.net/docs/contributing/) for mere om, hvordan du bidrager.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Hent</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temaer</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Skrifttyper</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Websted</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

