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
  <b>Hrvatski</b> |
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

<p align="center"><sub>Prijevod engleskog README-a; ako se razlikuju, vrijedi engleski. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontovi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Emulator PlayStationa 2 za testiranje i razvoj homebrewa, napravljen da njime upravljate vi ili AI agent.**

RIPPCSX2 je PCSX2 v2.9.96 s promjenama koje razvijatelju homebrewa za PS2 trebaju da vidi pravo stanje: HD video načini prikazani, snimljeni i uslikani onako kako ih prikazuje HD televizor, i hardverska podatkovna prekidna točka EE-a, kako bi izbornici u igri i alati za video načine koji se kače na registre GS-a (GSM iz Open PS2 Loadera, izbornik u igri RIPPS2) radili kao na konzoli. Sve ostalo je čisti PCSX2. Nastao je kao testni laboratorij front enda [RIPPS2](https://github.com/akilluminati47/RIPPS2) i namijenjen je svakome tko radi homebrew, teme ili alate za PS2.

### [Preuzmi RIPPCSX2 (zip za Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ili 11, x64, procesor s AVX2. Raspakirajte ga bilo gdje, pokrenite `pcsx2-qtx64-avx2.exe` i usmjerite ga na vlastiti dump BIOS-a. Zip sadrži prazan `portable.txt` pokraj exe datoteke, pa RIPPCSX2 drži sve postavke i datoteke u vlastitoj mapi: već instalirani PCSX2 zadržava svoje postavke, netaknute. Izdanje uvijek sadrži najnoviji build ([njegova stranica](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); isječci ispod su u [docs/videos](docs/videos).

**Pokreće `.elf` programe za testiranje:** System > Start File, ili `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, a program se pokreće kao što bi s memorijske kartice ili USB sticka na PS2. **Ponaša se kao pravi hardver**: ELF koji pokrene drugi ELF predaje mu stroj i nestaje, izbornik u igri koji se kači na GS crta preko pravog kadra igre, a gašenje zatvara VM kao konzola koja se gasi.

## Pogledajte kako radi

Svaki isječak je pravo pokretanje u laboratoriju na ovom buildu, skraćeno ispod 12 sekundi.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**AI agent testira ELF.** Snimljeno iz donjeg desnog kuta korisnikova zaslona (programska traka, dio Claude sesije): Claude pokreće `RIPPS2.elf` u RIPPCSX2 na skrivenoj radnoj površini, pokreće Aqua Teen Hunger Force sa slike HDD-a i otvara preko nje izbornik u igri RIPPS2. Mala ploča jedino je na zaslonu; korisnik zadržava tipkovnicu i miš.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Izbornik u igri, svaka funkcija.** L1+L2+R1+R2+SELECT+START preko igre koja teče: ACHIEVEMENTS, RESUME (igra se nastavlja), ponovno izbornik preko kasnijeg kadra, zatim POWER OFF, koji zatvara VM. Izbornik zna preko kojeg kadra crtati jer RIPPCSX2 emulira prekidnu točku upisa podataka EE-a.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF koji pokreće ELF, kao pravi PS2.** Memory Files u RIPPS2 otvara `mc0:/RIPPS2/RIPPS2.ELF` (najnoviji build, kopiran na karticu) i pokreće ga. Pokrenuti RIPPS2 predaje i nestaje; novi se učitava s kartice i pokreće do popisa igara.

## Što dobivate u odnosu na obični PCSX2 v2.9.96

- **HD načini izgledaju ispravno.** 720p i 1080i prikazuju se u 16:9 (izvornik ih crta u 4:3), uz svaku postavku omjera osim Stretch.
- **HD snimke i snimke zaslona.** F11 snima 720p u 1280 x 720 i 1080i u 1920 x 1080 (ili to puta povećanje), označeno kao 16:9; F8 sprema snimke zaslona u istim veličinama. Izvornik daje 640 x 480 ili sirovi međuspremnik širine 640.
- **Promjena načina usred snimanja** nastavlja se u novoj datoteci u novoj veličini, umjesto da se ugura u prvu.
- **1080i na pravom mjestu.** Izvornik pomiče sliku 1080i 42 retka gore (odrezan vrh, crna traka dolje); RIPPCSX2 je počinje u retku 40, gdje to radi i vremenski raspored same konzole.
- **Prekidna točka upisa podataka EE-a** (novo u rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) radi: upis na nadziranu adresu podiže iznimku za ispravljanje razine 2 na `0x80000100` prije izvršavanja, u interpreteru i u rekompajleru. GSM iz OPL-a i izbornik u igri RIPPS2 trebaju je kako bi znali koji kadar igra prikazuje.
- **Retci zapisnika o video načinu.** Svaka promjena načina bilježi vremenski raspored sinkronizacije i registre prikaza (`RIPPCSX2: video mode ...` u `logs/emulog.txt`).
- **Bez ponuda automatskog ažuriranja.** Oznake izdanja drže PCSX2-ovo ažuriranje isključenim, pa vas nikad ne „ažurira” natrag na izvornik.
- Standardna razlučivost ostaje netaknuta: snimke zaslona u 480i bajt su po bajt iste kao u izvorniku. `HDTVOutput = false` pod `[EmuCore/GS]` u `inis/PCSX2.ini` vraća izvorno HD ponašanje za usporedbu.

## Čemu služi

- **Izrađivači tema** (Open PS2 Loader, RiptOPL, RIPPS2): procijenite temu u 720p i 1080i onako kako je prikazuje televizor, i izradite preglede u stvarnoj veličini i videa obilaska.
- **Razvijatelji homebrewa:** testirajte ELF-ove koji mijenjaju video način, kače se na GS ili koriste registre za ispravljanje EE-a, i čitajte u zapisniku točne registre prikaza koje način postavlja.
- **Izbornici u igri i GS alati:** GSM iz OPL-a, izbornik u igri RIPPS2 i sve ostalo izgrađeno na prekidnoj točki upisa podataka radi u emulatoru, a ne samo na hardveru.
- **Automatizirano i AI potpomognuto testiranje:** skriptirana pokretanja na skrivenoj radnoj površini sa snimkama zaslona, snimkama, spremljenim stanjima i čitanjem memorije preko PINE-a, bez preuzimanja vašeg računala.

## Za AI agente, LLM-ove i njihove korisnike

Ovaj repozitorij napisan je tako da agent može postaviti sve korisniku samo iz poveznice. Dajte svom asistentu `https://github.com/akilluminati47/RIPPCSX2` i zamolite ga da instalira RIPPCSX2; sve što mu treba je ovdje:

1. **Nabavite build:** `RIPPCSX2-windows-x64-avx2.zip` iz kontinuiranog izdanja ([izravna poveznica](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ili `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Raspakirajte ga u vlastitu mapu; njegov `portable.txt` već je pokraj exe datoteke, pa nikad ne dira postavke instaliranog PCSX2.
2. **BIOS:** korisnik daje dump BIOS-a vlastite konzole (nikad ga ne preuzimajte): stavite ga u mapu `bios` pokraj exe datoteke (ili usmjerite `[Folders] Bios` u `inis/PCSX2.ini` na nju) i odaberite ga u čarobnjaku prvog pokretanja (`[Filenames] BIOS`).
3. **Pokrenite nešto:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ili `-- <game.iso>`. Postavke su obični INI u `inis/PCSX2.ini`; zapisnici idu u `logs/emulog.txt` (`[Logging] EnableEEConsole = true` dodaje printf EE-a).
4. **Upravljajte i promatrajte:** F8 snimka zaslona (`snaps/`), F11 snimanje (`videos/`), F1 spremljeno stanje (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) za čitanje i pisanje memorije PS2 iz skripte.
5. **Testirajte bez otimanja zaslona:** [`ripps2-lab/`](ripps2-lab/README.md) opisuje laboratorijsku instalaciju (`install-lab.ps1` stavlja build u prijenosnu mapu i čuva njegove kartice, postavke i snimke), a `tools/dev/ps2bg.ps1` iz RIPPS2 repozitorija izvodi popise koraka (tipke, čekanja, snimke zaslona, snimanja) na skrivenoj radnoj površini s pločom na programskoj traci koju korisnik može gledati, zaustaviti ili preuzeti.

Što se promijenilo i zašto, datoteku po datoteku: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenti koji rade na kodu ovog forka: nikad ne otvarajte pull requestove, issuese ni komentare u projektu PCSX2 (njegov `AGENTS.md` zabranjuje doprinose koje je izradio AI); RIPPCSX2 ostaje fork.

**Nije povezan s timom PCSX2.** GPL-3.0 kao PCSX2. Probleme s RIPPCSX2 prijavite RIPPS2-u ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nikad PCSX2-u. Slijedi PCSX2-ov vlastiti README.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 je besplatan emulator PlayStationa 2 (PS2) otvorenog koda. Svrha mu je emulirati hardver PS2 kombinacijom [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) za MIPS procesor, [rekompajlera](https://en.wikipedia.org/wiki/Dynamic_recompilation) i [virtualnog stroja](https://en.wikipedia.org/wiki/Virtual_machine) koji upravlja stanjima hardvera i sistemskom memorijom PS2. To vam omogućuje igranje PS2 igara na računalu, s mnogo dodatnih značajki i prednosti.

## Pojedinosti o projektu

PCSX2 se razvija više od 20 godina. Ranije su verzije mogle pokrenuti tek nekoliko demo igara iz javnog vlasništva, a novije pokreću većinu igara punom brzinom, uključujući popularne naslove poput Final Fantasy X i Devil May Cry 3. Posjetite [popis kompatibilnosti PCSX2](https://pcsx2.net/compat/) za najnovije stanje kompatibilnosti igara (s više od 2500 testiranih naslova).

Instalacijski programi i binarne datoteke stabilnih i nightly buildova dostupni su na [našoj stranici](https://pcsx2.net/downloads/).

## Zahtjevi sustava

PCSX2 podržava Windows, Linux i Mac. Naša [stranica dokumentacije o postavljanju](https://pcsx2.net/docs/setup/requirements) sadrži dodatne pojedinosti o softverskim i hardverskim zahtjevima.

Imajte na umu da je za korištenje emulatora potreban dump BIOS-a s legalno nabavljene konzole PS2. Za više informacija posjetite [ovu stranicu](https://pcsx2.net/docs/setup/bios/).

## Doprinos / Izrada

PCSX2 se može prevesti na druge jezike putem [Crowdina](https://crowdin.com/project/pcsx2-emulator).

Pogledajte [Vodič za doprinos](https://pcsx2.net/docs/contributing/) za više o tome kako pridonijeti.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Preuzmi</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Teme</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fontovi</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

