<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <b>Deutsch</b> |
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

<p align="center"><sub>Übersetzung der englischen README; bei Abweichungen gilt das Englische. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Themes</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Schriften</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Ein PlayStation-2-Emulator zum Testen und Entwickeln von Homebrew, gemacht, um von dir oder von einem KI-Agenten gesteuert zu werden.**

RIPPCSX2 ist PCSX2 v2.9.96 mit den Änderungen, die ein PS2-Homebrew-Entwickler braucht, um das Echte zu sehen: HD-Videomodi so gezeigt, aufgenommen und als Screenshot gespeichert, wie ein HD-Fernseher sie zeigt, und der Hardware-Daten-Breakpoint der EE, damit In-Game-Menüs und Videomodus-Werkzeuge, die sich in die GS-Register einklinken (das GSM von Open PS2 Loader, das In-Game-Menü von RIPPS2), so funktionieren wie auf einer Konsole. Alles andere ist reines PCSX2. Es begann als Testlabor des Frontends [RIPPS2](https://github.com/akilluminati47/RIPPS2) und ist für alle gedacht, die PS2-Homebrew, Themes oder Werkzeuge bauen.

**[Zur Website](https://akilluminati47.github.io/RIPPCSX2/)**: Nimm eine PS2 auseinander oder jage sie in die Luft, mit allem über RIPPCSX2 im Info-Panel.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [RIPPCSX2 herunterladen (Windows-Zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 oder 11, x64, eine CPU mit AVX2. Irgendwo entpacken, `pcsx2-qtx64-avx2.exe` starten und auf deinen eigenen BIOS-Dump verweisen. Das Zip enthält eine leere `portable.txt` neben der Exe, also hält RIPPCSX2 alle Einstellungen und Dateien in seinem eigenen Ordner: ein bereits installiertes PCSX2 behält seine Einstellungen, unberührt. Das Release enthält immer den neuesten Build ([seine Seite](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); die Clips unten liegen in [docs/videos](docs/videos).

**Es führt `.elf`-Programme zum Testen aus:** System > Start File oder `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, und das Programm startet so, wie es auf einer PS2 von einer Memory Card oder einem USB-Stick starten würde. Es **verhält sich wie echte Hardware**: ein ELF, das ein anderes ELF startet, übergibt die Maschine und ist weg, ein In-Game-Menü, das sich in den GS einklinkt, zeichnet über das echte Bild des Spiels, und Ausschalten schließt die VM wie eine Konsole, die abgeschaltet wird.

<a id="see-it-work"></a>

## So sieht es aus

Jeder Clip ist ein echter Laborlauf mit diesem Build, auf unter 12 Sekunden gekürzt.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Ein KI-Agent testet ein ELF.** Aufgenommen in der rechten unteren Ecke des Bildschirms des Nutzers (Taskleiste, Teil der Claude-Sitzung): Claude startet `RIPPS2.elf` in RIPPCSX2 auf einem versteckten Desktop, startet Aqua Teen Hunger Force vom HDD-Image und öffnet darüber das In-Game-Menü von RIPPS2. Das kleine Panel ist das Einzige auf dem Bildschirm; der Nutzer behält Tastatur und Maus.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Das In-Game-Menü, jede Funktion.** L1+L2+R1+R2+SELECT+START über einem laufenden Spiel: ACHIEVEMENTS, RESUME (das Spiel läuft weiter), das Menü erneut über einem späteren Bild, dann POWER OFF, das die VM schließt. Das Menü weiß, über welches Bild es zeichnen muss, weil RIPPCSX2 den Daten-Schreib-Breakpoint der EE emuliert.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Ein ELF startet ein ELF, wie eine echte PS2.** Memory Files von RIPPS2 öffnet `mc0:/RIPPS2/RIPPS2.ELF` (der neueste Build, auf die Karte kopiert) und führt ihn aus. Das laufende RIPPS2 übergibt und ist weg; das neue lädt von der Karte und startet in seine Spieleliste.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Was du gegenüber dem normalen PCSX2 v2.9.96 bekommst

- **Ein RIPPCSX2-Menü** zwischen Debug und Help: Run ELF und Run Last ELF, ein Live-Lab-Monitor, Test Steps, ein Compatibility Report, die Schalter des Forks und die Ordner, in denen alles landet.
- **Eine Taskleisten-Schaltfläche für versteckte Läufe.** Ein auf einem versteckten Desktop gestartetes PCSX2 legt eine Schaltfläche auf deine Taskleiste, sodass ein Lautstärkemixer oder ein Mod für die Lautstärke pro App es wie jedes andere Programm erreicht.
- **HD-Modi sehen richtig aus.** 720p und 1080i werden in 16:9 gezeigt (das Original zeichnet sie in 4:3), bei jeder Seitenverhältnis-Einstellung außer Stretch.
- **HD-Aufnahmen und Screenshots.** F11 nimmt 720p mit 1280 x 720 und 1080i mit 1920 x 1080 auf (oder das mal die Hochskalierung), als 16:9 markiert; F8 speichert Screenshots in denselben Größen. Das Original liefert 640 x 480 oder den rohen, 640 Pixel breiten Puffer.
- **Ein Moduswechsel mitten in der Aufnahme** geht in einer neuen Datei mit der neuen Größe weiter, statt in die erste gequetscht zu werden.
- **1080i an der richtigen Stelle.** Das Original schiebt ein 1080i-Bild 42 Zeilen nach oben (oben abgeschnitten, schwarzer Streifen unten); RIPPCSX2 beginnt es in Zeile 40, wo es auch das Timing der Konsole selbst tut.
- **Daten-Schreib-Breakpoint der EE** (neu in rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funktioniert: ein Schreibzugriff auf eine überwachte Adresse löst die Debug-Ausnahme der Stufe 2 bei `0x80000100` aus, bevor er ausgeführt wird, im Interpreter und im Recompiler. Das GSM von OPL und das In-Game-Menü von RIPPS2 brauchen ihn, um zu wissen, welches Bild ein Spiel zeigt.
- **Logzeilen zum Videomodus.** Jeder Moduswechsel protokolliert das Sync-Timing und die Anzeigeregister (`RIPPCSX2: video mode ...` in `logs/emulog.txt`).
- **Keine Angebote des Auto-Updaters.** Release-Tags lassen den Updater von PCSX2 aus, damit er dich nie zurück auf das Original „aktualisiert“.
- Standardauflösung bleibt unberührt: 480i-Screenshots sind Byte für Byte dieselben wie beim Original. `HDTVOutput = false` unter `[EmuCore/GS]` in `inis/PCSX2.ini` holt das originale HD-Verhalten für einen direkten Vergleich zurück.

<a id="what-it-is-for"></a>

## Wofür es gedacht ist

- **Theme-Macher** (Open PS2 Loader, RiptOPL, RIPPS2): beurteile ein Theme in 720p und 1080i so, wie ein Fernseher es zeigt, und mache Vorschauen in Originalgröße und Rundgang-Videos.
- **Homebrew-Entwickler:** teste ELFs, die Videomodi wechseln, sich in den GS einklinken oder die Debug-Register der EE nutzen, und lies im Log die genauen Anzeigeregister, die ein Modus setzt.
- **In-Game-Menüs und GS-Werkzeuge:** das GSM von OPL, das In-Game-Menü von RIPPS2 und alles andere, was auf dem Daten-Schreib-Breakpoint aufbaut, laufen im Emulator statt nur auf Hardware.
- **Automatisierte und KI-gestützte Tests:** geskriptete Läufe auf einem versteckten Desktop mit Screenshots, Aufnahmen, Speicherständen und PINE-Speicherlesungen, ohne deinen PC zu übernehmen.

<a id="the-end-goal-the-whole-library"></a>

## Das Endziel: die ganze Bibliothek

Die größte Aufgabe ist es, PS2-Spiele über den eigenen Codepfad von Open PS2 Loader zu testen, so wie eine Konsole sie ausführt, und festzuhalten, was jedes braucht: ELFs, KELFs, Homebrew-Apps und Spiele in einer OPL-Sandbox, deren Kompatibilitätsmodi automatisch durchprobiert werden. Damit könnte eines Tages jemand die gesamte Bibliothek zum Laufen bringen. Das ist das Endziel von RIPPCSX2.

Der Compatibility Report ist der erste Schritt: das Ergebnis eines Spiels, die verwendeten OPL-Modi und der Zustand der Maschine, gespeichert in `reports/` als Datei und als Zeile in `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Für KI-Agenten, LLMs und ihre Nutzer

Dieses Repo ist so geschrieben, dass ein Agent einen Nutzer allein mit dem Link einrichten kann. Gib deinem Assistenten `https://github.com/akilluminati47/RIPPCSX2` und bitte ihn, RIPPCSX2 zu installieren; alles, was er braucht, steht hier:

1. **Den Build holen:** `RIPPCSX2-windows-x64-avx2.zip` aus dem fortlaufenden Release ([Direktlink](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) oder `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). In einen eigenen Ordner entpacken; seine `portable.txt` liegt schon neben der Exe, also rührt er die Einstellungen eines installierten PCSX2 nie an.
2. **BIOS:** der Nutzer liefert den BIOS-Dump seiner eigenen Konsole (lade nie einen herunter): lege ihn in den Ordner `bios` neben der Exe (oder richte `[Folders] Bios` in `inis/PCSX2.ini` darauf) und wähle ihn im Ersteinrichtungs-Assistenten (`[Filenames] BIOS`).
3. **Etwas starten:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` oder `-- <game.iso>`. Die Einstellungen sind schlichtes INI in `inis/PCSX2.ini`; Logs landen in `logs/emulog.txt` (`[Logging] EnableEEConsole = true` fügt das printf der EE hinzu).
4. **Steuern und beobachten:** F8 Screenshot (`snaps/`), F11 Aufnahme (`videos/`), F1 Speicherstand (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`), um PS2-Speicher aus einem Skript zu lesen und zu schreiben.
5. **Testen, ohne den Bildschirm zu klauen:** [`ripps2-lab/`](ripps2-lab/README.md) beschreibt eine Laborinstallation (`install-lab.ps1` legt einen Build in einen portablen Ordner und behält dessen Karten, Einstellungen und Aufnahmen), und `tools/dev/ps2bg.ps1` aus dem RIPPS2-Repo führt Schrittlisten (Tasten, Wartezeiten, Screenshots, Aufnahmen) auf einem versteckten Desktop aus, mit einem Taskleisten-Panel, das der Nutzer beobachten, stoppen oder übernehmen kann.

Was sich geändert hat und warum, Datei für Datei: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenten, die am Code dieses Forks arbeiten: öffnet nie Pull Requests, Issues oder Kommentare beim PCSX2-Projekt (dessen `AGENTS.md` verbietet KI-erstellte Beiträge); RIPPCSX2 bleibt ein Fork.

**Nicht mit dem PCSX2-Team verbunden.** GPL-3.0 wie PCSX2. Melde Probleme mit RIPPCSX2 bei RIPPS2 ([Issues](https://github.com/akilluminati47/RIPPS2/issues)), nie bei PCSX2. Es folgt das README von PCSX2 selbst.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 ist ein freier Open-Source-Emulator für die PlayStation 2 (PS2). Sein Zweck ist es, die Hardware der PS2 zu emulieren, mit einer Kombination aus [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) für die MIPS-CPU, [Recompilern](https://en.wikipedia.org/wiki/Dynamic_recompilation) und einer [virtuellen Maschine](https://en.wikipedia.org/wiki/Virtual_machine), die Hardwarezustände und den Systemspeicher der PS2 verwaltet. So kannst du PS2-Spiele auf deinem PC spielen, mit vielen zusätzlichen Funktionen und Vorteilen.

<a id="project-details"></a>

## Projektdetails

PCSX2 ist seit über 20 Jahren in Entwicklung. Frühere Versionen konnten nur ein paar gemeinfreie Spieldemos ausführen, neuere Versionen dagegen die meisten Spiele mit voller Geschwindigkeit, darunter beliebte Titel wie Final Fantasy X und Devil May Cry 3. Auf der [Kompatibilitätsliste von PCSX2](https://pcsx2.net/compat/) findest du den aktuellen Kompatibilitätsstand der Spiele (mit über 2500 getesteten Titeln).

Installer und Binärdateien für stabile und Nightly-Builds gibt es auf [unserer Website](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Systemanforderungen

PCSX2 unterstützt Windows, Linux und Mac. Auf unserer [Seite zur Einrichtung](https://pcsx2.net/docs/setup/requirements) stehen weitere Details zu Software- und Hardwareanforderungen.

Bitte beachte, dass für den Emulator ein BIOS-Dump einer rechtmäßig erworbenen PS2-Konsole nötig ist. Mehr dazu auf [dieser Seite](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Mitwirken / Bauen

PCSX2 lässt sich über [Crowdin](https://crowdin.com/project/pcsx2-emulator) in andere Sprachen übersetzen.

Im [Leitfaden für Beiträge](https://pcsx2.net/docs/contributing/) steht, wie du mitwirken kannst.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Download</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Themes</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Schriften</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Website</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

