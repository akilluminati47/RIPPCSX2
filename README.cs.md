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
  <b>Čeština</b> |
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

<p align="center"><sub>Překlad anglického README; pokud se liší, platí angličtina. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Stáhnout</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motivy</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Písma</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Emulátor PlayStation 2 pro testování a vývoj homebrew, udělaný tak, aby ho mohl ovládat člověk nebo AI agent.**

RIPPCSX2 je PCSX2 v2.9.96 se změnami, které vývojář homebrew pro PS2 potřebuje, aby viděl skutečný výsledek: HD video režimy zobrazené, nahrávané a snímané tak, jak je ukazuje HD televize, a hardwarový datový breakpoint EE, aby menu ve hře a nástroje video režimů, které se napojují na registry GS (GSM z Open PS2 Loader, menu ve hře RIPPS2), fungovaly jako na konzoli. Všechno ostatní je čisté PCSX2. Vznikl jako testovací laboratoř front endu [RIPPS2](https://github.com/akilluminati47/RIPPS2) a je určen každému, kdo tvoří homebrew, motivy nebo nástroje pro PS2.

**[Podívejte se na web](https://akilluminati47.github.io/RIPPCSX2/)**: rozeberte PS2 nebo ji vyhoďte do povětří, a vše o RIPPCSX2 najdete v panelu Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Stáhnout RIPPCSX2 (zip pro Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 nebo 11, x64, procesor s AVX2. Rozbalte ho kamkoli, spusťte `pcsx2-qtx64-avx2.exe` a nasměrujte ho na vlastní výpis BIOS. Zip obsahuje prázdný `portable.txt` vedle exe, takže RIPPCSX2 drží všechna nastavení a soubory ve vlastní složce: již nainstalované PCSX2 si ponechá svá nastavení, nedotčená. Vydání vždy obsahuje nejnovější build ([jeho stránka](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klipy níže jsou v [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Stáhnout RIPPCSX2 (Linux AppImage)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, procesor s AVX2. Nastavte soubor jako spustitelný a spusťte ho. Je nový v tomto vydání a sestavuje ho stejný workflow jako zip pro Windows, ale na počítači s Linuxem zatím neběžel: dejte nám prosím vědět, jak to dopadlo. Tlačítko na hlavním panelu pro skryté běhy je jen pro Windows.

**Spouští programy `.elf` k testování:** System > Start File, nebo `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, a program nastartuje, jako by startoval z paměťové karty nebo USB disku na PS2. **Chová se jako skutečný hardware**: ELF, který spustí jiný ELF, mu předá stroj a zmizí, menu ve hře napojené na GS kreslí přes skutečný snímek hry a vypnutí zavře VM jako vypínaná konzole.

<a id="see-it-work"></a>

## Podívejte se, jak funguje

Každý klip je skutečný běh v laboratoři na tomto buildu, zkrácený pod 12 sekund.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**AI agent testuje ELF.** Nahráno z pravého dolního rohu obrazovky uživatele (hlavní panel, část relace Claude): Claude spustí `RIPPS2.elf` v RIPPCSX2 na skryté ploše, spustí Aqua Teen Hunger Force z obrazu HDD a otevře přes ni menu ve hře RIPPS2. Malý panel je jediné, co je na obrazovce; uživatel si ponechá klávesnici i myš.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menu ve hře, každá funkce.** L1+L2+R1+R2+SELECT+START přes běžící hru: ACHIEVEMENTS, RESUME (hra pokračuje), znovu menu přes pozdější snímek, pak POWER OFF, které zavře VM. Menu ví, přes který snímek kreslit, protože RIPPCSX2 emuluje breakpoint zápisu dat EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF spouštějící ELF, jako skutečná PS2.** Memory Files v RIPPS2 otevře `mc0:/RIPPS2/RIPPS2.ELF` (nejnovější build, zkopírovaný na kartu) a spustí ho. Běžící RIPPS2 předá řízení a zmizí; nový se načte z karty a nastartuje do seznamu her.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Co získáte oproti běžnému PCSX2 v2.9.96

- **Nabídka RIPPCSX2** mezi Debug a Help: Run ELF a Run Last ELF, živý Lab Monitor, Test Steps, Compatibility Report, přepínače forku a složky, kam vše ukládá.
- **RIPART,** v této nabídce: databáze grafiky OPL Manageru, 16 313 her čtených po rozsazích bajtů z její zálohy na archive.org. Návnadové herní položky, aby šlo posoudit motiv na skutečném seznamu bez her na disku, seznam se zaškrtávacími poli s každým kusem grafiky hry k ponechání nebo vynechání, hledání her na disku bez obalu a složka ART nebo `art.tar`, kam to všechno uložit. Návnady se zobrazují v OPL a RIPPS2 a nespouštějí se; existující soubor se nikdy nenahrazuje. akilluminati47 pomohl této databázi přinést 8bitovou grafiku PNG a ikony disků 128 x 128.
- **Běžné OPL spouští hry.** Zařízení `host`, které si program zaregistruje sám, teď dostává vlastní otevření, takže restart IOP v OPL funguje. Původní verze se zastaví na `file 'host0:' can't open`.
- **EXIT GAME se dostane do prohlížeče.** Přerušení SIO2 se při restartu IOP ztrácelo, a OSDSYS tak čekal na paměťovou kartu s černou obrazovkou.
- **Tlačítko na hlavním panelu pro skryté běhy.** PCSX2 spuštěný na skryté ploše přidá tlačítko na hlavní panel, takže směšovač hlasitosti nebo mod hlasitosti pro aplikace na něj dosáhne jako na jakýkoli jiný program.
- **HD režimy vypadají správně.** 720p a 1080i se zobrazují v 16:9 (originál je kreslí v 4:3), při každém nastavení poměru stran kromě Stretch.
- **HD nahrávky a snímky obrazovky.** F11 nahrává 720p v 1280 x 720 a 1080i v 1920 x 1080 (nebo to krát zvětšení), označené jako 16:9; F8 ukládá snímky ve stejných velikostech. Originál dává 640 x 480 nebo surový buffer šířky 640.
- **Změna režimu uprostřed nahrávání** pokračuje v novém souboru v nové velikosti, místo aby se namáčkla do prvního.
- **1080i na správném místě.** Originál posune obraz 1080i o 42 řádků nahoru (oříznutý vršek, černý pruh dole); RIPPCSX2 ho začíná na řádku 40, kde to dělá časování samotné konzole.
- **Breakpoint zápisu dat EE** (novinka v rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funguje: zápis na sledovanou adresu vyvolá ladicí výjimku úrovně 2 na `0x80000100` dřív, než se provede, v interpretu i v rekompilátoru. GSM z OPL a menu ve hře RIPPS2 ho potřebují, aby věděly, jaký snímek hra ukazuje.
- **Řádky logu o video režimu.** Každá změna režimu zapíše časování synchronizace a registry zobrazení (`RIPPCSX2: video mode ...` v `logs/emulog.txt`).
- **Žádné nabídky automatických aktualizací.** Značky vydání nechávají aktualizátor PCSX2 vypnutý, takže vás nikdy „neaktualizuje“ zpět na originál.
- Standardní rozlišení zůstává nedotčené: snímky v 480i jsou bajt po bajtu stejné jako u originálu. `HDTVOutput = false` pod `[EmuCore/GS]` v `inis/PCSX2.ini` vrátí původní HD chování pro srovnání.

<a id="what-it-is-for"></a>

## K čemu slouží

- **Tvůrci motivů** (Open PS2 Loader, RiptOPL, RIPPS2): posuďte motiv v 720p a 1080i tak, jak ho ukazuje televize, a dělejte náhledy ve skutečné velikosti a prezentační videa.
- **Vývojáři homebrew:** testujte ELF, které mění video režim, napojují se na GS nebo používají ladicí registry EE, a čtěte v logu přesné registry zobrazení, které režim nastaví.
- **Menu ve hře a nástroje GS:** GSM z OPL, menu ve hře RIPPS2 a vše ostatní postavené na breakpointu zápisu dat běží v emulátoru, ne jen na hardwaru.
- **Hry PS1:** spusťte Ember a jeho hry PS1 z virtuálního disku a otestujte spouštění a seznamy PS1, s vlastním BIOSem PS1 na disku.
- **Neutrino a POPStarter:** Neutrino spouští hry přes RIPPS2 v plné rychlosti. POPStarter spouští hry PS1 jen s vypnutým rekompilátorem EE, zatím asi v poloviční rychlosti a s poškozenou grafikou; s rekompilátorem zůstane na černé obrazovce.
- **Automatizované a AI asistované testování:** skriptované běhy na skryté ploše se snímky, nahrávkami, uloženými stavy a čtením paměti přes PINE, aniž by se zmocnily vašeho PC.

<a id="the-end-goal-the-whole-library"></a>

## Konečný cíl: celá knihovna

Největší práce před námi je testovat hry pro PS2 vlastní kódovou cestou Open PS2 Loaderu, tak jak je spouští konzole, a zapisovat, co která potřebuje: ELFy, KELFy, homebrew aplikace a hry v sandboxu OPL s automaticky zkoušenými režimy kompatibility. Jednou by díky tomu někdo mohl rozběhnout celou knihovnu. To je konečný cíl RIPPCSX2.

Compatibility Report je první krok: výsledek hry, použité režimy OPL a stav stroje, uložené v `reports/` jako soubor a řádek v `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Pro AI agenty, LLM a jejich uživatele

Tento repozitář je napsaný tak, aby agent mohl uživatele nastavit jen z odkazu. Dejte svému asistentovi `https://github.com/akilluminati47/RIPPCSX2` a požádejte ho o instalaci RIPPCSX2; vše, co potřebuje, je tady:

1. **Stáhněte build:** `RIPPCSX2-windows-x64-avx2.zip` z průběžného vydání ([přímý odkaz](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), nebo `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Rozbalte ho do vlastní složky; jeho `portable.txt` už leží vedle exe, takže nikdy nesáhne na nastavení nainstalovaného PCSX2.
2. **BIOS:** uživatel dodá výpis BIOS ze své vlastní konzole (nikdy žádný nestahujte): dejte ho do složky `bios` vedle exe (nebo na něj nasměrujte `[Folders] Bios` v `inis/PCSX2.ini`) a vyberte ho v průvodci prvním spuštěním (`[Filenames] BIOS`).
3. **Spusťte něco:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, nebo `-- <game.iso>`. Nastavení jsou obyčejné INI v `inis/PCSX2.ini`; logy jdou do `logs/emulog.txt` (`[Logging] EnableEEConsole = true` přidá printf z EE).
4. **Ovládejte a sledujte ho:** F8 snímek obrazovky (`snaps/`), F11 nahrávka (`videos/`), F1 uložený stav (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) pro čtení a zápis paměti PS2 ze skriptu.
5. **Testujte, aniž byste brali obrazovku:** [`ripps2-lab/`](ripps2-lab/README.md) popisuje laboratorní instalaci (`install-lab.ps1` dá build do přenosné složky a ponechá její karty, nastavení a nahrávky), a `tools/dev/ps2bg.ps1` z repozitáře RIPPS2 spouští seznamy kroků (tlačítka, čekání, snímky, nahrávky) na skryté ploše s panelem na hlavním panelu, který může uživatel sledovat, zastavit nebo převzít.

Co se změnilo a proč, soubor po souboru: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenti pracující na kódu tohoto forku: nikdy neotevírejte pull requesty, issues ani komentáře v projektu PCSX2 (jeho `AGENTS.md` zakazuje příspěvky vytvořené AI); RIPPCSX2 zůstává forkem.

**Nesouvisí s týmem PCSX2.** GPL-3.0 jako PCSX2. Problémy s RIPPCSX2 hlaste u RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nikdy u PCSX2. Následuje vlastní README PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 je svobodný emulátor PlayStation 2 (PS2) s otevřeným kódem. Jeho účelem je emulovat hardware PS2 pomocí kombinace [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) procesoru MIPS, [rekompilátorů](https://en.wikipedia.org/wiki/Dynamic_recompilation) a [virtuálního stroje](https://en.wikipedia.org/wiki/Virtual_machine), který spravuje stavy hardwaru a systémovou paměť PS2. Díky tomu můžete hrát hry pro PS2 na PC s mnoha dalšími funkcemi a výhodami.

<a id="project-details"></a>

## Podrobnosti o projektu

PCSX2 se vyvíjí přes 20 let. Starší verze zvládly spustit jen pár herních dem z volného díla, ale novější verze spustí většinu her v plné rychlosti, včetně populárních titulů jako Final Fantasy X a Devil May Cry 3. Na [seznamu kompatibility PCSX2](https://pcsx2.net/compat/) najdete nejnovější stav kompatibility her (s více než 2500 otestovanými tituly).

Instalátory a binárky stabilních i nightly buildů jsou k dispozici na [našem webu](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Systémové požadavky

PCSX2 podporuje Windows, Linux a Mac. Naše [stránka dokumentace k nastavení](https://pcsx2.net/docs/setup/requirements) obsahuje další podrobnosti o softwarových a hardwarových požadavcích.

Upozorňujeme, že k použití emulátoru je nutný výpis BIOS z legálně vlastněné konzole PS2. Další informace najdete na [této stránce](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Přispívání / Sestavení

PCSX2 lze překládat do dalších jazyků přes [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Více o tom, jak přispět, najdete v [Průvodci přispíváním](https://pcsx2.net/docs/contributing/).

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Stáhnout</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motivy</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Písma</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

