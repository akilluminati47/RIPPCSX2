<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.it.md">Italiano</a> |
  <b>Nederlands</b> |
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

<p align="center"><sub>Vertaling van de Engelse README; bij verschillen geldt het Engels. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Downloaden</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thema's</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Lettertypen</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Een PlayStation 2-emulator om homebrew te testen en te ontwikkelen, gemaakt om door jou of door een AI-agent bestuurd te worden.**

RIPPCSX2 is PCSX2 v2.9.96 met de wijzigingen die een PS2-homebrewontwikkelaar nodig heeft om het echte beeld te zien: HD-videomodi getoond, opgenomen en vastgelegd zoals een HD-tv ze toont, en het hardware-databreekpunt van de EE, zodat in-game menu’s en videomodushulpmiddelen die op de GS-registers inhaken (het GSM van Open PS2 Loader, het in-game menu van RIPPS2) werken zoals op een console. Al het andere is gewoon PCSX2. Het begon als testlab van de front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) en is bedoeld voor iedereen die PS2-homebrew, thema’s of hulpmiddelen maakt.

**[Bekijk de website](https://akilluminati47.github.io/RIPPCSX2/)**: haal een PS2 uit elkaar of blaas er een op, met alles over RIPPCSX2 in het Info-paneel.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [RIPPCSX2 downloaden (Windows-zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 of 11, x64, een CPU met AVX2. Pak het ergens uit, start `pcsx2-qtx64-avx2.exe` en wijs het je eigen BIOS-dump aan. De zip bevat een lege `portable.txt` naast de exe, dus RIPPCSX2 bewaart al zijn instellingen en bestanden in zijn eigen map: een PCSX2 dat je al hebt geïnstalleerd houdt zijn eigen instellingen, onaangeroerd. De release bevat altijd de nieuwste build ([de pagina ervan](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); de clips hieronder staan in [docs/videos](docs/videos).

**Het draait `.elf`-programma’s om te testen:** System > Start File, of `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, en het programma start zoals het op een PS2 vanaf een geheugenkaart of USB-stick zou starten. Het **gedraagt zich als echte hardware**: een ELF dat een ander ELF start, geeft de machine door en is weg, een in-game menu dat op de GS inhaakt tekent over het echte beeld van het spel, en uitschakelen sluit de VM zoals een console die uitgaat.

<a id="see-it-work"></a>

## Zie het werken

Elke clip is een echte labrun op deze build, ingekort tot onder de 12 seconden.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Een AI-agent die een ELF test.** Opgenomen in de rechterbenedenhoek van het scherm van de gebruiker (taakbalk, deel van de Claude-sessie): Claude start `RIPPS2.elf` in RIPPCSX2 op een verborgen bureaublad, start Aqua Teen Hunger Force vanaf het HDD-image en opent daarover het in-game menu van RIPPS2. Het kleine paneel is het enige op het scherm; de gebruiker houdt toetsenbord en muis.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Het in-game menu, elke functie.** L1+L2+R1+R2+SELECT+START over een lopend spel: ACHIEVEMENTS, RESUME (het spel speelt verder), het menu opnieuw over een later beeld, dan POWER OFF, dat de VM sluit. Het menu weet over welk beeld het moet tekenen omdat RIPPCSX2 het data-schrijfbreekpunt van de EE emuleert.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Een ELF dat een ELF start, zoals een echte PS2.** Memory Files van RIPPS2 opent `mc0:/RIPPS2/RIPPS2.ELF` (de nieuwste build, naar de kaart gekopieerd) en voert hem uit. De draaiende RIPPS2 geeft over en is weg; de nieuwe laadt van de kaart en start op in zijn spellijst.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Wat je krijgt ten opzichte van gewone PCSX2 v2.9.96

- **Een RIPPCSX2-menu** tussen Debug en Help: Run ELF en Run Last ELF, een live Lab Monitor, Test Steps, een Compatibility Report, de schakelaars van de fork en de mappen waar alles terechtkomt.
- **Een taakbalkknop voor verborgen runs.** Een PCSX2 die op een verborgen bureaublad start, zet een knop op je taakbalk, zodat een volumemixer of een volumemod per app hem bereikt zoals elk ander programma.
- **HD-modi zien er goed uit.** 720p en 1080i worden in 16:9 getoond (het origineel tekent ze in 4:3), bij elke beeldverhouding-instelling behalve Stretch.
- **HD-opnames en schermafbeeldingen.** F11 neemt 720p op in 1280 x 720 en 1080i in 1920 x 1080 (of dat maal de opschaling), gemarkeerd als 16:9; F8 bewaart schermafbeeldingen in dezelfde formaten. Het origineel geeft 640 x 480 of de ruwe buffer van 640 breed.
- **Een moduswissel midden in een opname** gaat verder in een nieuw bestand met het nieuwe formaat, in plaats van in het eerste te worden geperst.
- **1080i op de juiste plek.** Het origineel schuift een 1080i-beeld 42 regels omhoog (bovenkant eraf, zwarte balk onder); RIPPCSX2 begint het op regel 40, waar de timing van de console zelf dat doet.
- **Data-schrijfbreekpunt van de EE** (nieuw in rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) werkt: een schrijfactie naar een bewaakt adres veroorzaakt de debug-uitzondering van niveau 2 op `0x80000100` voordat die wordt uitgevoerd, in de interpreter en in de recompiler. Het GSM van OPL en het in-game menu van RIPPS2 hebben het nodig om te weten welk beeld een spel toont.
- **Logregels voor de videomodus.** Elke moduswissel logt de synctiming en de beeldregisters (`RIPPCSX2: video mode ...` in `logs/emulog.txt`).
- **Geen aanbiedingen van de automatische updater.** Releasetags houden de updater van PCSX2 uit, zodat hij je nooit terug "bijwerkt" naar het origineel.
- Standaardresolutie blijft ongemoeid: schermafbeeldingen in 480i zijn byte voor byte hetzelfde als die van het origineel. `HDTVOutput = false` onder `[EmuCore/GS]` in `inis/PCSX2.ini` brengt het originele HD-gedrag terug voor een vergelijking naast elkaar.

<a id="what-it-is-for"></a>

## Waar het voor is

- **Themamakers** (Open PS2 Loader, RiptOPL, RIPPS2): beoordeel een thema in 720p en 1080i zoals een tv het toont, en maak voorbeelden op ware grootte en rondleidingsvideo’s.
- **Homebrewontwikkelaars:** test ELF’s die van videomodus wisselen, op de GS inhaken of de debugregisters van de EE gebruiken, en lees in het log de exacte beeldregisters die een modus instelt.
- **In-game menu’s en GS-hulpmiddelen:** het GSM van OPL, het in-game menu van RIPPS2 en alles wat op het data-schrijfbreekpunt is gebouwd, draaien in de emulator in plaats van alleen op hardware.
- **Geautomatiseerd en AI-ondersteund testen:** gescripte runs op een verborgen bureaublad met schermafbeeldingen, opnames, save states en PINE-geheugenlezingen, zonder je pc over te nemen.

<a id="the-end-goal-the-whole-library"></a>

## Het einddoel: de hele bibliotheek

De grootste klus die nog komt, is PS2-games testen via het eigen codepad van Open PS2 Loader, zoals een console ze draait, en opschrijven wat elke game nodig heeft: ELF's, KELF's, homebrew-apps en games in een OPL-sandbox, met de compatibiliteitsmodi automatisch uitgeprobeerd. Iemand zou hiermee ooit de hele bibliotheek aan de praat kunnen krijgen. Dat is het einddoel van RIPPCSX2.

De Compatibility Report is de eerste stap: het resultaat van een game, de gebruikte OPL-modi en de toestand van de machine, opgeslagen in `reports/` als bestand en als rij in `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Voor AI-agenten, LLM’s en hun gebruikers

Deze repo is zo geschreven dat een agent een gebruiker alleen met de link kan instellen. Geef je assistent `https://github.com/akilluminati47/RIPPCSX2` en vraag hem RIPPCSX2 te installeren; alles wat hij nodig heeft staat hier:

1. **Haal de build:** `RIPPCSX2-windows-x64-avx2.zip` uit de doorlopende release ([directe link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), of `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Pak hem uit in een eigen map; zijn `portable.txt` staat al naast de exe, dus hij raakt de instellingen van een geïnstalleerd PCSX2 nooit aan.
2. **BIOS:** de gebruiker levert de BIOS-dump van zijn eigen console (download er nooit een): zet hem in de map `bios` naast de exe (of laat `[Folders] Bios` in `inis/PCSX2.ini` ernaar wijzen) en kies hem in de wizard bij de eerste start (`[Filenames] BIOS`).
3. **Start iets:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, of `-- <game.iso>`. De instellingen zijn gewone INI in `inis/PCSX2.ini`; logs gaan naar `logs/emulog.txt` (`[Logging] EnableEEConsole = true` voegt de printf van de EE toe).
4. **Bestuur en bekijk het:** F8 schermafbeelding (`snaps/`), F11 opname (`videos/`), F1 save state (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) om PS2-geheugen vanuit een script te lezen en te schrijven.
5. **Test zonder het scherm in te pikken:** [`ripps2-lab/`](ripps2-lab/README.md) beschrijft een labinstallatie (`install-lab.ps1` zet een build in een draagbare map en houdt de kaarten, instellingen en opnames bij), en `tools/dev/ps2bg.ps1` uit de RIPPS2-repo draait stappenlijsten (knoppen, wachttijden, schermafbeeldingen, opnames) op een verborgen bureaublad met een taakbalkpaneel dat de gebruiker kan bekijken, stoppen of overnemen.

Wat er veranderde en waarom, bestand voor bestand: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenten die aan de code van deze fork werken: open nooit pull requests, issues of reacties bij het PCSX2-project (de `AGENTS.md` daarvan verbiedt bijdragen die door AI zijn gemaakt); RIPPCSX2 blijft een fork.

**Niet verbonden aan het PCSX2-team.** GPL-3.0 zoals PCSX2. Meld problemen met RIPPCSX2 bij RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nooit bij PCSX2. Hierna volgt de eigen README van PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 is een vrije en opensource-emulator voor de PlayStation 2 (PS2). Het doel is de hardware van de PS2 te emuleren met een combinatie van [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) voor de MIPS-CPU, [Recompilers](https://en.wikipedia.org/wiki/Dynamic_recompilation) en een [virtuele machine](https://en.wikipedia.org/wiki/Virtual_machine) die de hardwaretoestanden en het systeemgeheugen van de PS2 beheert. Zo kun je PS2-spellen op je pc spelen, met veel extra functies en voordelen.

<a id="project-details"></a>

## Projectdetails

PCSX2 is al meer dan 20 jaar in ontwikkeling. Eerdere versies konden maar een paar spel-demo’s uit het publieke domein draaien, maar nieuwere versies draaien de meeste spellen op volle snelheid, waaronder populaire titels als Final Fantasy X en Devil May Cry 3. Bekijk de [compatibiliteitslijst van PCSX2](https://pcsx2.net/compat/) voor de nieuwste compatibiliteitsstatus van spellen (met meer dan 2500 geteste titels).

Installatieprogramma’s en binaire bestanden voor zowel stabiele als nightly builds staan op [onze website](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Systeemvereisten

PCSX2 ondersteunt Windows, Linux en Mac. Onze [documentatiepagina over installatie](https://pcsx2.net/docs/setup/requirements) bevat meer details over software- en hardwarevereisten.

Let op: om de emulator te gebruiken is een BIOS-dump van een legaal verkregen PS2-console nodig. Bezoek [deze pagina](https://pcsx2.net/docs/setup/bios/) voor meer informatie.

<a id="contributing--building"></a>

## Bijdragen / Bouwen

PCSX2 kan via [Crowdin](https://crowdin.com/project/pcsx2-emulator) in andere talen worden vertaald.

Zie de [Gids voor bijdragers](https://pcsx2.net/docs/contributing/) voor meer informatie over bijdragen.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Downloaden</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thema's</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Lettertypen</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

