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
  <b>Srpski</b> |
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

<p align="center"><sub>Prevod engleskog README-a; ako se razlikuju, važi engleski. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontovi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sajt</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Emulator PlayStationa 2 za testiranje i razvoj homebrewa, napravljen da njime upravljate vi ili AI agent.**

RIPPCSX2 je PCSX2 v2.9.96 sa izmenama koje su razvijaocu homebrewa za PS2 potrebne da vidi pravo stanje: HD video režimi prikazani, snimljeni i uslikani onako kako ih prikazuje HD televizor, i hardverska tačka prekida za podatke EE-a, kako bi meniji u igri i alati za video režime koji se kače na registre GS-a (GSM iz Open PS2 Loader-a, meni u igri RIPPS2) radili kao na konzoli. Sve ostalo je čisti PCSX2. Nastao je kao test laboratorija front enda [RIPPS2](https://github.com/akilluminati47/RIPPS2) i namenjen je svakome ko pravi homebrew, teme ili alate za PS2.

**[Pogledaj veb-sajt](https://akilluminati47.github.io/RIPPCSX2/)**: rastavi PS2 ili ga razneti, a sve o RIPPCSX2 je u panelu Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Preuzmite RIPPCSX2 (zip za Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ili 11, x64, procesor sa AVX2. Raspakujte ga bilo gde, pokrenite `pcsx2-qtx64-avx2.exe` i usmerite ga na sopstveni dump BIOS-a. Zip sadrži prazan `portable.txt` pored exe datoteke, pa RIPPCSX2 drži sva podešavanja i datoteke u sopstvenoj fascikli: već instalirani PCSX2 zadržava svoja podešavanja, netaknuta. Izdanje uvek sadrži najnoviji build ([njegova stranica](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); snimci ispod su u [docs/videos](docs/videos).

**Pokreće `.elf` programe za testiranje:** System > Start File, ili `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, i program se pokreće kao što bi sa memorijske kartice ili USB fleša na PS2. **Ponaša se kao pravi hardver**: ELF koji pokrene drugi ELF predaje mu mašinu i nestaje, meni u igri koji se kači na GS crta preko pravog kadra igre, a gašenje zatvara VM kao konzola koja se gasi.

<a id="see-it-work"></a>

## Pogledajte kako radi

Svaki snimak je pravo pokretanje u laboratoriji na ovom buildu, skraćeno ispod 12 sekundi.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**AI agent testira ELF.** Snimljeno iz donjeg desnog ugla korisnikovog ekrana (traka zadataka, deo Claude sesije): Claude pokreće `RIPPS2.elf` u RIPPCSX2 na skrivenoj radnoj površini, pokreće Aqua Teen Hunger Force sa slike HDD-a i otvara preko nje meni u igri RIPPS2. Mali panel je jedino na ekranu; korisnik zadržava tastaturu i miš.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Meni u igri, svaka funkcija.** L1+L2+R1+R2+SELECT+START preko igre koja teče: ACHIEVEMENTS, RESUME (igra se nastavlja), ponovo meni preko kasnijeg kadra, zatim POWER OFF, koji zatvara VM. Meni zna preko kog kadra da crta jer RIPPCSX2 emulira tačku prekida za upis podataka EE-a.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF koji pokreće ELF, kao pravi PS2.** Memory Files u RIPPS2 otvara `mc0:/RIPPS2/RIPPS2.ELF` (najnoviji build, kopiran na karticu) i pokreće ga. Pokrenuti RIPPS2 predaje i nestaje; novi se učitava sa kartice i pokreće do liste igara.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Šta dobijate u odnosu na obični PCSX2 v2.9.96

- **Meni RIPPCSX2** između Debug i Help: Run ELF i Run Last ELF, Lab Monitor uživo, Test Steps, Compatibility Report, prekidači forka i fascikle u koje sve stiže.
- **Dugme na traci zadataka za skrivena pokretanja.** PCSX2 pokrenut na skrivenoj radnoj površini stavlja dugme na tvoju traku zadataka, pa ga mikser jačine zvuka ili mod jačine zvuka po aplikaciji dosegne kao i svaki drugi program.
- **HD režimi izgledaju ispravno.** 720p i 1080i prikazuju se u 16:9 (original ih crta u 4:3), uz svako podešavanje odnosa osim Stretch.
- **HD snimci i snimci ekrana.** F11 snima 720p u 1280 x 720 i 1080i u 1920 x 1080 (ili to puta uvećanje), označeno kao 16:9; F8 čuva snimke ekrana u istim veličinama. Original daje 640 x 480 ili sirovi bafer širine 640.
- **Promena režima usred snimanja** nastavlja se u novoj datoteci u novoj veličini, umesto da se ugura u prvu.
- **1080i na pravom mestu.** Original pomera sliku 1080i 42 reda nagore (odsečen vrh, crna traka dole); RIPPCSX2 je počinje u redu 40, gde to radi i tajming same konzole.
- **Tačka prekida za upis podataka EE-a** (novo u rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) radi: upis na nadziranu adresu podiže izuzetak za otklanjanje grešaka nivoa 2 na `0x80000100` pre izvršenja, u interpreteru i u rekompajleru. GSM iz OPL-a i meni u igri RIPPS2 trebaju je da bi znali koji kadar igra prikazuje.
- **Redovi dnevnika o video režimu.** Svaka promena režima beleži tajming sinhronizacije i registre prikaza (`RIPPCSX2: video mode ...` u `logs/emulog.txt`).
- **Bez ponuda automatskog ažuriranja.** Oznake izdanja drže PCSX2 ažuriranje isključenim, pa vas nikad ne „ažurira” nazad na original.
- Standardna rezolucija ostaje netaknuta: snimci ekrana u 480i su bajt po bajt isti kao kod originala. `HDTVOutput = false` pod `[EmuCore/GS]` u `inis/PCSX2.ini` vraća originalno HD ponašanje za poređenje.

<a id="what-it-is-for"></a>

## Čemu služi

- **Autori tema** (Open PS2 Loader, RiptOPL, RIPPS2): procenite temu u 720p i 1080i onako kako je prikazuje televizor, i napravite preglede u stvarnoj veličini i video obilaske.
- **Razvijaoci homebrewa:** testirajte ELF-ove koji menjaju video režim, kače se na GS ili koriste registre za otklanjanje grešaka EE-a, i čitajte u dnevniku tačne registre prikaza koje režim postavlja.
- **Meniji u igri i GS alati:** GSM iz OPL-a, meni u igri RIPPS2 i sve ostalo zasnovano na tački prekida za upis podataka radi u emulatoru, a ne samo na hardveru.
- **Automatizovano i AI potpomognuto testiranje:** skriptovana pokretanja na skrivenoj radnoj površini sa snimcima ekrana, snimcima, sačuvanim stanjima i čitanjem memorije preko PINE-a, bez preuzimanja vašeg računara.

<a id="the-end-goal-the-whole-library"></a>

## Krajnji cilj: cela biblioteka

Najveći posao pred nama je testiranje PS2 igara kroz sopstveni kodni put Open PS2 Loadera, onako kako ih pokreće konzola, i zapisivanje šta je kojoj potrebno: ELF-ovi, KELF-ovi, homebrew aplikacije i igre u OPL sandboksu, uz automatsko isprobavanje režima kompatibilnosti. Neko bi jednog dana time mogao da pokrene celu biblioteku. To je krajnji cilj RIPPCSX2.

Compatibility Report je prvi korak: rezultat igre, korišćeni OPL režimi i stanje mašine, sačuvani u `reports/` kao datoteka i red u `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Za AI agente, LLM-ove i njihove korisnike

Ovaj repozitorijum je napisan tako da agent može sve da podesi korisniku samo iz linka. Dajte svom asistentu `https://github.com/akilluminati47/RIPPCSX2` i zamolite ga da instalira RIPPCSX2; sve što mu treba je ovde:

1. **Nabavite build:** `RIPPCSX2-windows-x64-avx2.zip` iz kontinuiranog izdanja ([direktan link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ili `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Raspakujte ga u sopstvenu fasciklu; njegov `portable.txt` je već pored exe datoteke, pa nikad ne dira podešavanja instaliranog PCSX2.
2. **BIOS:** korisnik daje dump BIOS-a sopstvene konzole (nikad ga ne preuzimajte): stavite ga u fasciklu `bios` pored exe datoteke (ili usmerite `[Folders] Bios` u `inis/PCSX2.ini` na nju) i izaberite ga u čarobnjaku prvog pokretanja (`[Filenames] BIOS`).
3. **Pokrenite nešto:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ili `-- <game.iso>`. Podešavanja su obični INI u `inis/PCSX2.ini`; dnevnici idu u `logs/emulog.txt` (`[Logging] EnableEEConsole = true` dodaje printf EE-a).
4. **Upravljajte i posmatrajte:** F8 snimak ekrana (`snaps/`), F11 snimanje (`videos/`), F1 sačuvano stanje (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) za čitanje i pisanje memorije PS2 iz skripte.
5. **Testirajte bez otimanja ekrana:** [`ripps2-lab/`](ripps2-lab/README.md) opisuje laboratorijsku instalaciju (`install-lab.ps1` stavlja build u prenosivu fasciklu i čuva njegove kartice, podešavanja i snimke), a `tools/dev/ps2bg.ps1` iz RIPPS2 repozitorijuma izvodi liste koraka (dugmad, čekanja, snimke ekrana, snimanja) na skrivenoj radnoj površini sa panelom na traci zadataka koji korisnik može da gleda, zaustavi ili preuzme.

Šta se promenilo i zašto, datoteku po datoteku: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenti koji rade na kodu ovog forka: nikad ne otvarajte pull requestove, issue-e ni komentare u projektu PCSX2 (njegov `AGENTS.md` zabranjuje doprinose koje je napravio AI); RIPPCSX2 ostaje fork.

**Nije povezan sa timom PCSX2.** GPL-3.0 kao PCSX2. Probleme sa RIPPCSX2 prijavite RIPPS2-u ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nikad PCSX2-u. Sledi PCSX2-ov sopstveni README.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 je besplatan emulator PlayStationa 2 (PS2) otvorenog koda. Svrha mu je da emulira hardver PS2 kombinacijom [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) za MIPS procesor, [rekompajlera](https://en.wikipedia.org/wiki/Dynamic_recompilation) i [virtuelne mašine](https://en.wikipedia.org/wiki/Virtual_machine) koja upravlja stanjima hardvera i sistemskom memorijom PS2. To vam omogućava da igrate PS2 igre na računaru, sa mnogo dodatnih funkcija i prednosti.

<a id="project-details"></a>

## Detalji o projektu

PCSX2 se razvija više od 20 godina. Ranije verzije mogle su da pokrenu tek nekoliko demo igara iz javnog vlasništva, a novije pokreću većinu igara punom brzinom, uključujući popularne naslove poput Final Fantasy X i Devil May Cry 3. Posetite [listu kompatibilnosti PCSX2](https://pcsx2.net/compat/) za najnovije stanje kompatibilnosti igara (sa više od 2500 testiranih naslova).

Instalacioni programi i binarne datoteke stabilnih i nightly buildova dostupni su na [našem sajtu](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Sistemski zahtevi

PCSX2 podržava Windows, Linux i Mac. Naša [stranica dokumentacije o podešavanju](https://pcsx2.net/docs/setup/requirements) sadrži dodatne detalje o softverskim i hardverskim zahtevima.

Imajte na umu da je za korišćenje emulatora potreban dump BIOS-a sa legalno nabavljene konzole PS2. Za više informacija posetite [ovu stranicu](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Doprinos / Pravljenje

PCSX2 može da se prevede na druge jezike preko [Crowdin-a](https://crowdin.com/project/pcsx2-emulator).

Pogledajte [Vodič za doprinos](https://pcsx2.net/docs/contributing/) za više o tome kako da doprinesete.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontovi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sajt</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

