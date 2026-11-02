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
  <b>Български</b> |
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

<p align="center"><sub>Превод на английския README; при разлики важи английският. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Изтегляне</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Теми</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Шрифтове</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Сайт</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Емулатор на PlayStation 2 за тестване и разработка на homebrew, направен да се управлява от вас или от ИИ агент.**

RIPPCSX2 е PCSX2 v2.9.96 с промените, от които разработчикът на homebrew за PS2 има нужда, за да види истинската картина: HD видео режимите показани, записани и заснети така, както ги показва HD телевизор, и хардуерната точка на прекъсване за данни на EE, така че менютата в игра и инструментите за видео режими, които се закачат за регистрите на GS (GSM на Open PS2 Loader, менюто в игра на RIPPS2), да работят като на конзола. Всичко останало е чист PCSX2. Започна като тестова лаборатория на фронтенда [RIPPS2](https://github.com/akilluminati47/RIPPS2) и е предназначен за всеки, който прави homebrew, теми или инструменти за PS2.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Изтеглете RIPPCSX2 (zip за Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 или 11, x64, процесор с AVX2. Разархивирайте го където и да е, стартирайте `pcsx2-qtx64-avx2.exe` и го насочете към собствения си дъмп на BIOS. Zip файлът съдържа празен `portable.txt` до exe файла, така че RIPPCSX2 държи всичките си настройки и файлове в собствената си папка: вече инсталиран PCSX2 запазва своите настройки, недокоснати. Изданието винаги съдържа най-новия билд ([страницата му](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); клиповете по-долу са в [docs/videos](docs/videos).

**Пуска `.elf` програми за тестване:** System > Start File или `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, и програмата стартира, както би стартирала от карта с памет или USB флашка на PS2. Той **се държи като истински хардуер**: ELF, който пуска друг ELF, му предава машината и изчезва, меню в игра, закачено за GS, рисува върху истинския кадър на играта, а изключването затваря VM като изключваща се конзола.

<a id="see-it-work"></a>

## Вижте го в действие

Всеки клип е истинско пускане в лабораторията на този билд, съкратено под 12 секунди.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**ИИ агент тества ELF.** Записано от долния десен ъгъл на екрана на потребителя (лентата на задачите, част от сесията с Claude): Claude стартира `RIPPS2.elf` в RIPPCSX2 на скрит работен плот, пуска Aqua Teen Hunger Force от образа на HDD и отваря върху нея менюто в игра на RIPPS2. Малкият панел е единственото на екрана; потребителят запазва клавиатурата и мишката.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Менюто в игра, всяка функция.** L1+L2+R1+R2+SELECT+START върху вървяща игра: ACHIEVEMENTS, RESUME (играта продължава), менюто отново върху по-късен кадър, после POWER OFF, което затваря VM. Менюто знае върху кой кадър да рисува, защото RIPPCSX2 емулира точката на прекъсване при запис на данни на EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF, който пуска ELF, като истинско PS2.** Memory Files на RIPPS2 отваря `mc0:/RIPPS2/RIPPS2.ELF` (най-новия билд, копиран на картата) и го пуска. Работещият RIPPS2 предава управлението и изчезва; новият се зарежда от картата и стартира до списъка си с игри.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Какво получавате спрямо обикновения PCSX2 v2.9.96

- **HD режимите изглеждат правилно.** 720p и 1080i се показват в 16:9 (оригиналът ги рисува в 4:3), при всяка настройка на съотношението освен Stretch.
- **HD записи и снимки на екрана.** F11 записва 720p в 1280 x 720 и 1080i в 1920 x 1080 (или това по мащабирането), отбелязано като 16:9; F8 запазва снимки в същите размери. Оригиналът дава 640 x 480 или суровия буфер с ширина 640.
- **Смяна на режима по време на запис** продължава в нов файл с новия размер, вместо да се натъпче в първия.
- **1080i на правилното място.** Оригиналът мести 1080i картина с 42 реда нагоре (изрязан горен край, черна лента отдолу); RIPPCSX2 я започва от ред 40, където я започва и синхронизацията на самата конзола.
- **Точка на прекъсване при запис на данни на EE** (ново в rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) работи: запис на наблюдаван адрес предизвиква изключението за отстраняване на грешки от ниво 2 на `0x80000100`, преди да се изпълни, в интерпретатора и в рекомпилатора. GSM на OPL и менюто в игра на RIPPS2 се нуждаят от нея, за да знаят кой кадър показва играта.
- **Редове в дневника за видео режима.** Всяка смяна на режима записва синхронизацията и регистрите на дисплея (`RIPPCSX2: video mode ...` в `logs/emulog.txt`).
- **Без предложения от автоматичния актуализатор.** Етикетите на изданията държат актуализатора на PCSX2 изключен, така че никога не ви „актуализира“ обратно до оригинала.
- Стандартната разделителна способност е непокътната: снимките в 480i са байт по байт същите като на оригинала. `HDTVOutput = false` под `[EmuCore/GS]` в `inis/PCSX2.ini` връща оригиналното HD поведение за сравнение.

<a id="what-it-is-for"></a>

## За какво е

- **Създатели на теми** (Open PS2 Loader, RiptOPL, RIPPS2): преценете тема в 720p и 1080i така, както я показва телевизор, и правете визуализации в реален размер и видео обиколки.
- **Разработчици на homebrew:** тествайте ELF, които сменят видео режима, закачат се за GS или ползват регистрите за отстраняване на грешки на EE, и четете в дневника точните регистри на дисплея, които задава даден режим.
- **Менюта в игра и GS инструменти:** GSM на OPL, менюто в игра на RIPPS2 и всичко друго, изградено върху точката на прекъсване при запис на данни, работят в емулатора, а не само на хардуера.
- **Автоматизирано и подпомогнато от ИИ тестване:** скриптирани пускания на скрит работен плот със снимки, записи, запазени състояния и четене на памет през PINE, без да превземат компютъра ви.

<a id="for-ai-agents-llms-and-their-users"></a>

## За ИИ агенти, LLM и техните потребители

Това хранилище е написано така, че агент да може да настрои всичко за потребителя само по връзката. Дайте на асистента си `https://github.com/akilluminati47/RIPPCSX2` и го помолете да инсталира RIPPCSX2; всичко, от което се нуждае, е тук:

1. **Вземете билда:** `RIPPCSX2-windows-x64-avx2.zip` от непрекъснатото издание ([директна връзка](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) или `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Разархивирайте го в отделна папка; неговият `portable.txt` вече е до exe файла, така че никога не пипа настройките на инсталиран PCSX2.
2. **BIOS:** потребителят предоставя дъмпа на BIOS от собствената си конзола (никога не изтегляйте такъв): сложете го в папката `bios` до exe файла (или насочете `[Folders] Bios` в `inis/PCSX2.ini` към нея) и го изберете в съветника при първо стартиране (`[Filenames] BIOS`).
3. **Пуснете нещо:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` или `-- <game.iso>`. Настройките са обикновен INI в `inis/PCSX2.ini`; дневниците отиват в `logs/emulog.txt` (`[Logging] EnableEEConsole = true` добавя printf на EE).
4. **Управлявайте и наблюдавайте:** F8 снимка на екрана (`snaps/`), F11 запис (`videos/`), F1 запазено състояние (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) за четене и запис на паметта на PS2 от скрипт.
5. **Тествайте, без да отнемате екрана:** [`ripps2-lab/`](ripps2-lab/README.md) описва лабораторна инсталация (`install-lab.ps1` слага билд в преносима папка и пази картите, настройките и записите му), а `tools/dev/ps2bg.ps1` от хранилището на RIPPS2 изпълнява списъци от стъпки (бутони, изчаквания, снимки, записи) на скрит работен плот с панел в лентата на задачите, който потребителят може да гледа, спре или поеме.

Какво се промени и защо, файл по файл: **[RIPPCSX2.md](RIPPCSX2.md)**. Агенти, които работят по кода на този fork: никога не отваряйте pull request-и, issues или коментари в проекта PCSX2 (неговият `AGENTS.md` забранява приноси, направени от ИИ); RIPPCSX2 остава fork.

**Не е свързан с екипа на PCSX2.** GPL-3.0 като PCSX2. Съобщавайте проблеми с RIPPCSX2 на RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), никога на PCSX2. Следва собственото README на PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 е безплатен емулатор на PlayStation 2 (PS2) с отворен код. Целта му е да емулира хардуера на PS2 чрез комбинация от [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) за процесора MIPS, [рекомпилатори](https://en.wikipedia.org/wiki/Dynamic_recompilation) и [виртуална машина](https://en.wikipedia.org/wiki/Virtual_machine), която управлява състоянията на хардуера и системната памет на PS2. Това ви позволява да играете игри за PS2 на компютъра си, с много допълнителни функции и предимства.

<a id="project-details"></a>

## Подробности за проекта

PCSX2 се разработва повече от 20 години. По-старите версии можеха да пускат само няколко демонстрации от обществено достояние, но по-новите пускат повечето игри с пълна скорост, включително популярни заглавия като Final Fantasy X и Devil May Cry 3. Посетете [списъка за съвместимост на PCSX2](https://pcsx2.net/compat/) за най-новото състояние на съвместимост на игрите (с над 2500 тествани заглавия).

Инсталатори и двоични файлове за стабилните и нощните билдове има на [нашия сайт](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Системни изисквания

PCSX2 поддържа Windows, Linux и Mac. Нашата [страница с документация за настройка](https://pcsx2.net/docs/setup/requirements) съдържа повече подробности за софтуерните и хардуерните изисквания.

Моля, имайте предвид, че за използване на емулатора е нужен дъмп на BIOS от законно притежавана конзола PS2. За повече информация посетете [тази страница](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Принос / Изграждане

PCSX2 може да се превежда на други езици чрез [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Вижте [Ръководството за принос](https://pcsx2.net/docs/contributing/) за повече за това как да допринесете.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Изтегляне</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Теми</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Шрифтове</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Сайт</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

