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
  <b>Polski</b> |
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

<p align="center"><sub>Tłumaczenie angielskiego README; w razie różnic obowiązuje wersja angielska. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Pobierz</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motywy</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Czcionki</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Strona</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Emulator PlayStation 2 do testowania i tworzenia homebrew, zrobiony tak, by sterować nim mógł człowiek albo agent AI.**

RIPPCSX2 to PCSX2 v2.9.96 ze zmianami, których twórca homebrew na PS2 potrzebuje, by zobaczyć prawdziwy obraz: tryby wideo HD wyświetlane, nagrywane i zrzucane tak, jak pokazuje je telewizor HD, oraz sprzętowy punkt przerwania danych EE, dzięki czemu menu w grze i narzędzia trybów wideo, które podpinają się pod rejestry GS (GSM z Open PS2 Loader, menu w grze RIPPS2), działają jak na konsoli. Cała reszta to czysty PCSX2. Powstał jako laboratorium testowe front endu [RIPPS2](https://github.com/akilluminati47/RIPPS2) i jest przeznaczony dla każdego, kto tworzy homebrew, motywy lub narzędzia na PS2.

**[Zobacz stronę](https://akilluminati47.github.io/RIPPCSX2/)**: rozbierz PS2 albo wysadź ją w powietrze, a wszystko o RIPPCSX2 znajdziesz w panelu Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Pobierz RIPPCSX2 (zip dla Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 lub 11, x64, procesor z AVX2. Rozpakuj go gdziekolwiek, uruchom `pcsx2-qtx64-avx2.exe` i wskaż własny zrzut BIOS-u. Zip zawiera pusty `portable.txt` obok pliku exe, więc RIPPCSX2 trzyma wszystkie ustawienia i pliki we własnym folderze: zainstalowany już PCSX2 zachowuje swoje ustawienia, nietknięte. Wydanie zawsze zawiera najnowszą kompilację ([jego strona](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klipy poniżej są w [docs/videos](docs/videos).

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [Pobierz RIPPCSX2 (AppImage dla Linuksa)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, procesor z AVX2. Nadaj plikowi prawo wykonywania i uruchom go. To nowość w tym wydaniu, budowana tym samym workflow co zip dla Windows, ale jeszcze nie uruchamiana na maszynie z Linuksem: daj znać, jak poszło. Przycisk na pasku zadań dla ukrytych uruchomień działa tylko w Windows.

**Uruchamia programy `.elf` do testów:** System > Start File albo `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, a program startuje tak, jak z karty pamięci lub pendrive’a na PS2. **Zachowuje się jak prawdziwy sprzęt**: ELF, który uruchamia inny ELF, oddaje mu maszynę i znika, menu w grze podpięte pod GS rysuje się na prawdziwej klatce gry, a wyłączenie zamyka VM jak wyłączana konsola.

<a id="see-it-work"></a>

## Zobacz, jak działa

Każdy klip to prawdziwy przebieg w laboratorium na tej kompilacji, przycięty poniżej 12 sekund.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Agent AI testujący ELF.** Nagrane z prawego dolnego rogu ekranu użytkownika (pasek zadań, część sesji Claude): Claude uruchamia `RIPPS2.elf` w RIPPCSX2 na ukrytym pulpicie, startuje Aqua Teen Hunger Force z obrazu HDD i otwiera nad nią menu w grze RIPPS2. Mały panel to jedyna rzecz na ekranie; użytkownik zachowuje klawiaturę i mysz.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menu w grze, każda funkcja.** L1+L2+R1+R2+SELECT+START podczas gry: ACHIEVEMENTS, RESUME (gra toczy się dalej), znów menu nad późniejszą klatką, potem POWER OFF, które zamyka VM. Menu wie, nad którą klatką rysować, bo RIPPCSX2 emuluje punkt przerwania zapisu danych EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF uruchamiający ELF, jak prawdziwa PS2.** Memory Files z RIPPS2 otwiera `mc0:/RIPPS2/RIPPS2.ELF` (najnowszą kompilację, skopiowaną na kartę) i ją uruchamia. Działający RIPPS2 oddaje kontrolę i znika; nowy wczytuje się z karty i startuje do listy gier.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Co zyskujesz względem zwykłego PCSX2 v2.9.96

- **Menu RIPPCSX2** między Debug a Help: Run ELF i Run Last ELF, Lab Monitor na żywo, Test Steps, Compatibility Report, przełączniki forka i foldery, do których wszystko trafia.
- **RIPART,** w tym menu: baza grafik OPL Managera, 16 313 gier odczytywanych zakresami bajtów z jej kopii na archive.org. Wpisy gier-wabików, by ocenić motyw na prawdziwej liście bez gier na dysku, lista z polami wyboru z każdym elementem grafiki gry do zachowania lub pominięcia, wyszukiwanie gier na dysku bez okładki oraz folder ART lub `art.tar` na całość. Wabiki widać w OPL i RIPPS2 i nie uruchamiają się; istniejący plik nigdy nie jest zastępowany. akilluminati47 pomógł wprowadzić do tej bazy 8-bitową grafikę PNG i ikony płyt 128 x 128.
- **Zwykły OPL uruchamia gry.** Urządzenie `host`, które program rejestruje sam, dostaje teraz własne otwarcia, więc restart IOP w OPL działa. Oryginał zatrzymuje się na `file 'host0:' can't open`.
- **EXIT GAME dociera do przeglądarki.** Przerwanie SIO2 ginęło przy restarcie IOP, przez co OSDSYS czekał na kartę pamięci przy czarnym ekranie.
- **Przycisk na pasku zadań dla ukrytych uruchomień.** PCSX2 uruchomiony na ukrytym pulpicie umieszcza przycisk na pasku zadań, dzięki czemu mikser głośności lub mod głośności dla aplikacji dociera do niego jak do każdego innego programu.
- **Tryby HD wyglądają jak należy.** 720p i 1080i są pokazywane w 16:9 (oryginał rysuje je w 4:3), przy każdym ustawieniu proporcji oprócz Stretch.
- **Nagrania i zrzuty w HD.** F11 nagrywa 720p w 1280 x 720 i 1080i w 1920 x 1080 (albo razy skalowanie), oznaczone jako 16:9; F8 zapisuje zrzuty w tych samych rozmiarach. Oryginał daje 640 x 480 albo surowy bufor o szerokości 640.
- **Zmiana trybu w trakcie nagrywania** jest kontynuowana w nowym pliku w nowym rozmiarze, zamiast wciskać się w pierwszy.
- **1080i we właściwym miejscu.** Oryginał przesuwa obraz 1080i o 42 linie w górę (ucięta góra, czarny pas na dole); RIPPCSX2 zaczyna go w linii 40, tam gdzie robi to taktowanie samej konsoli.
- **Punkt przerwania zapisu danych EE** (nowość w rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) działa: zapis pod obserwowany adres wywołuje wyjątek debugowania poziomu 2 pod `0x80000100` przed wykonaniem, w interpreterze i w rekompilatorze. GSM z OPL i menu w grze RIPPS2 potrzebują go, by wiedzieć, którą klatkę gra pokazuje.
- **Wpisy w logu o trybie wideo.** Każda zmiana trybu zapisuje taktowanie synchronizacji i rejestry wyświetlania (`RIPPCSX2: video mode ...` w `logs/emulog.txt`).
- **Bez propozycji automatycznej aktualizacji.** Tagi wydań trzymają aktualizator PCSX2 wyłączony, więc nigdy nie „zaktualizuje” cię z powrotem do oryginału.
- Standardowa rozdzielczość jest nietknięta: zrzuty w 480i są bajt w bajt takie same jak w oryginale. `HDTVOutput = false` w `[EmuCore/GS]` w `inis/PCSX2.ini` przywraca oryginalne zachowanie HD do porównania.

<a id="what-it-is-for"></a>

## Do czego służy

- **Twórcy motywów** (Open PS2 Loader, RiptOPL, RIPPS2): oceniaj motyw w 720p i 1080i tak, jak pokazuje go telewizor, i rób podglądy w rzeczywistym rozmiarze oraz filmy z prezentacją.
- **Twórcy homebrew:** testuj ELF-y, które zmieniają tryb wideo, podpinają się pod GS lub używają rejestrów debugowania EE, i czytaj w logu dokładne rejestry wyświetlania, które ustawia dany tryb.
- **Menu w grze i narzędzia GS:** GSM z OPL, menu w grze RIPPS2 i wszystko inne oparte na punkcie przerwania zapisu danych działa w emulatorze, a nie tylko na sprzęcie.
- **Gry PS1:** uruchom Ember i jego gry PS1 z wirtualnego dysku, by przetestować start i listy PS1, z własnym BIOS-em PS1 na dysku.
- **Testy automatyczne i wspomagane AI:** skryptowane przebiegi na ukrytym pulpicie ze zrzutami, nagraniami, stanami zapisu i odczytami pamięci przez PINE, bez przejmowania twojego komputera.

<a id="the-end-goal-the-whole-library"></a>

## Cel ostateczny: cała biblioteka

Największe zadanie przed nami to testowanie gier PS2 własną ścieżką kodu Open PS2 Loadera, tak jak uruchamia je konsola, i zapisywanie, czego potrzebuje każda z nich: ELF-y, KELF-y, aplikacje homebrew i gry w piaskownicy OPL, z automatycznym sprawdzaniem trybów zgodności. Kiedyś ktoś może dzięki temu uruchomić całą bibliotekę. To jest ostateczny cel RIPPCSX2.

Compatibility Report to pierwszy krok: wynik gry, użyte tryby OPL i stan maszyny, zapisane w `reports/` jako plik i wiersz w `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Dla agentów AI, LLM i ich użytkowników

To repozytorium jest napisane tak, by agent mógł wszystko przygotować dla użytkownika na podstawie samego linku. Daj swojemu asystentowi `https://github.com/akilluminati47/RIPPCSX2` i poproś o instalację RIPPCSX2; wszystko, czego potrzebuje, jest tutaj:

1. **Pobierz kompilację:** `RIPPCSX2-windows-x64-avx2.zip` z wydania ciągłego ([bezpośredni link](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) albo `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Rozpakuj do osobnego folderu; jego `portable.txt` leży już obok pliku exe, więc nigdy nie rusza ustawień zainstalowanego PCSX2.
2. **BIOS:** użytkownik dostarcza zrzut BIOS-u z własnej konsoli (nigdy go nie pobieraj): umieść go w folderze `bios` obok pliku exe (albo skieruj na niego `[Folders] Bios` w `inis/PCSX2.ini`) i wybierz w kreatorze pierwszego uruchomienia (`[Filenames] BIOS`).
3. **Uruchom coś:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` albo `-- <game.iso>`. Ustawienia to zwykłe INI w `inis/PCSX2.ini`; logi trafiają do `logs/emulog.txt` (`[Logging] EnableEEConsole = true` dodaje printf z EE).
4. **Steruj i obserwuj:** F8 zrzut ekranu (`snaps/`), F11 nagranie (`videos/`), F1 stan zapisu (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) do odczytu i zapisu pamięci PS2 ze skryptu.
5. **Testuj, nie zabierając ekranu:** [`ripps2-lab/`](ripps2-lab/README.md) opisuje instalację laboratoryjną (`install-lab.ps1` wrzuca kompilację do przenośnego folderu i zachowuje jej karty, ustawienia i nagrania), a `tools/dev/ps2bg.ps1` z repozytorium RIPPS2 wykonuje listy kroków (przyciski, oczekiwania, zrzuty, nagrania) na ukrytym pulpicie z panelem na pasku zadań, który użytkownik może oglądać, zatrzymać lub przejąć.

Co się zmieniło i dlaczego, plik po pliku: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenci pracujący nad kodem tego forka: nigdy nie otwierajcie pull requestów, issues ani komentarzy w projekcie PCSX2 (jego `AGENTS.md` zabrania wkładu tworzonego przez AI); RIPPCSX2 pozostaje forkiem.

**Niezwiązany z zespołem PCSX2.** GPL-3.0 jak PCSX2. Problemy z RIPPCSX2 zgłaszaj do RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), nigdy do PCSX2. Dalej następuje README samego PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 to darmowy emulator PlayStation 2 (PS2) o otwartym kodzie. Jego celem jest emulowanie sprzętu PS2 za pomocą połączenia [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) procesora MIPS, [rekompilatorów](https://en.wikipedia.org/wiki/Dynamic_recompilation) i [maszyny wirtualnej](https://en.wikipedia.org/wiki/Virtual_machine), która zarządza stanami sprzętu i pamięcią systemową PS2. Dzięki temu możesz grać w gry z PS2 na komputerze, z wieloma dodatkowymi funkcjami i korzyściami.

<a id="project-details"></a>

## Szczegóły projektu

PCSX2 jest rozwijany od ponad 20 lat. Dawne wersje potrafiły uruchomić tylko kilka dem z domeny publicznej, ale nowsze uruchamiają większość gier z pełną szybkością, w tym popularne tytuły jak Final Fantasy X i Devil May Cry 3. Odwiedź [listę zgodności PCSX2](https://pcsx2.net/compat/), by sprawdzić najnowszy stan zgodności gier (przetestowano ponad 2500 tytułów).

Instalatory i pliki binarne wersji stabilnych i nightly są dostępne na [naszej stronie](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Wymagania systemowe

PCSX2 działa na Windows, Linux i Mac. Nasza [strona dokumentacji konfiguracji](https://pcsx2.net/docs/setup/requirements) zawiera więcej szczegółów o wymaganiach programowych i sprzętowych.

Pamiętaj, że do korzystania z emulatora potrzebny jest zrzut BIOS-u z legalnie posiadanej konsoli PS2. Więcej informacji na [tej stronie](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Współtworzenie / Kompilacja

PCSX2 można tłumaczyć na inne języki przez [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Zobacz [Przewodnik dla współtwórców](https://pcsx2.net/docs/contributing/), by dowiedzieć się, jak pomóc.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Pobierz</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Motywy</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Czcionki</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Strona</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

