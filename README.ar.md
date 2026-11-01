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
  <a href="README.hu.md">Magyar</a> |
  <a href="README.ro.md">Română</a> |
  <a href="README.gl.md">Galego</a> |
  <a href="README.sq.md">Shqip</a> |
  <a href="README.tr.md">Türkçe</a> |
  <b>العربية</b> |
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

<p align="center"><sub>ترجمة لملف README الإنجليزي؛ إن اختلفا فالإنجليزي هو المعتمد. <a href="README.md">English</a></sub></p>

<div dir="rtl">

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">تنزيل</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">السمات</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">الخطوط</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">الموقع</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**محاكي PlayStation 2 لاختبار البرامج المنزلية (homebrew) وتطويرها، مصمَّم ليقوده أنت أو وكيل ذكاء اصطناعي.**

RIPPCSX2 هو PCSX2 v2.9.96 مع التغييرات التي يحتاجها مطوّر homebrew لـ PS2 ليرى الحقيقة: أوضاع فيديو HD تُعرض وتُسجَّل وتُلتقط كما يعرضها تلفاز HD، ونقطة توقف البيانات العتادية في EE، كي تعمل قوائم داخل اللعبة وأدوات أوضاع الفيديو التي تتصل بسجلات GS (‏GSM في Open PS2 Loader، وقائمة RIPPS2 داخل اللعبة) كما تعمل على الجهاز. وكل ما عدا ذلك PCSX2 عادي. بدأ كمختبر اختبار للواجهة [RIPPS2](https://github.com/akilluminati47/RIPPS2) وهو موجّه لكل من يصنع homebrew أو سمات أو أدوات لـ PS2.

### [نزّل RIPPCSX2 (ملف zip لنظام Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 أو 11، ‏x64، ومعالج يدعم AVX2. فك الضغط في أي مكان، وشغّل `pcsx2-qtx64-avx2.exe`، ووجّهه إلى نسخة BIOS الخاصة بجهازك. يحمل ملف zip ملف `portable.txt` فارغًا بجوار exe، لذا يحتفظ RIPPCSX2 بكل إعداداته وملفاته في مجلده: أي PCSX2 مثبَّت لديك يحتفظ بإعداداته دون أن تُمس. يحوي الإصدار دائمًا أحدث بناء ([صفحته](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling))؛ والمقاطع أدناه في [docs/videos](docs/videos).

**يشغّل برامج `.elf` للاختبار:** System > Start File، أو `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`، فيقلع البرنامج كما يقلع من بطاقة ذاكرة أو ذاكرة USB على PS2. وهو **يتصرف كالعتاد الحقيقي**: ELF يشغّل ELF آخر يسلّمه الجهاز ويختفي، وقائمة داخل اللعبة متصلة بـ GS ترسم فوق إطار اللعبة الحقيقي، والإطفاء يغلق الـ VM كجهاز يُطفأ.

## شاهده يعمل

كل مقطع تشغيل حقيقي في المختبر على هذا البناء، مقصوص إلى أقل من 12 ثانية.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**وكيل ذكاء اصطناعي يختبر ELF.** مسجَّل من الزاوية اليمنى السفلى لشاشة المستخدم (شريط المهام، جزء من جلسة Claude): يشغّل Claude ملف `RIPPS2.elf` في RIPPCSX2 على سطح مكتب مخفي، ويشغّل Aqua Teen Hunger Force من صورة القرص الصلب، ويفتح فوقها قائمة RIPPS2 داخل اللعبة. اللوحة الصغيرة هي الشيء الوحيد على الشاشة؛ ويبقى لوحة المفاتيح والفأرة مع المستخدم.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**القائمة داخل اللعبة، بكل وظائفها.** L1+L2+R1+R2+SELECT+START فوق لعبة قيد التشغيل: ACHIEVEMENTS، وRESUME (تستمر اللعبة)، ثم القائمة مجددًا فوق إطار لاحق، ثم POWER OFF الذي يغلق الـ VM. تعرف القائمة فوق أي إطار ترسم لأن RIPPCSX2 يحاكي نقطة توقف كتابة البيانات في EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF يشغّل ELF، كجهاز PS2 حقيقي.** يفتح Memory Files في RIPPS2 الملف `mc0:/RIPPS2/RIPPS2.ELF` (أحدث بناء، منسوخ إلى البطاقة) ويشغّله. يسلّم RIPPS2 العامل المهمة ويختفي؛ ويُحمَّل الجديد من البطاقة ويقلع إلى قائمة ألعابه.

## ما تحصل عليه مقارنة بـ PCSX2 v2.9.96 العادي

- **أوضاع HD تظهر صحيحة.** يُعرض 720p و1080i بنسبة 16:9 (الأصل يرسمهما 4:3)، في كل إعدادات النسبة عدا Stretch.
- **تسجيلات ولقطات HD.** يسجّل F11 دقة 720p بحجم 1280 x 720 و1080i بحجم 1920 x 1080 (أو مضاعف ذلك بالتكبير)، موسومة 16:9؛ ويحفظ F8 لقطات بالأحجام نفسها. يعطي الأصل 640 x 480 أو المخزن الخام بعرض 640.
- **تغيير الوضع أثناء التسجيل** يستمر في ملف جديد بالحجم الجديد بدل أن ينضغط في الأول.
- **1080i في مكانه الصحيح.** يرفع الأصل صورة 1080i بمقدار 42 سطرًا (أعلى مقصوص، وشريط أسود أسفل)؛ ويبدؤها RIPPCSX2 من السطر 40 حيث يبدؤها توقيت الجهاز نفسه.
- **نقطة توقف كتابة البيانات في EE** (جديد في rippcsx2.2). يعمل COP0 `$24` (`MTBPC`، `MTDAB`، `MTDABM` ...): كتابة إلى عنوان مراقَب تُطلق استثناء التصحيح من المستوى 2 عند `0x80000100` قبل تنفيذها، في المفسّر وفي معيد الترجمة. يحتاجها GSM في OPL وقائمة RIPPS2 داخل اللعبة لمعرفة أي إطار تعرضه اللعبة.
- **أسطر سجل لوضع الفيديو.** كل تغيير وضع يسجّل توقيت المزامنة وسجلات العرض (`RIPPCSX2: video mode ...` في `logs/emulog.txt`).
- **لا عروض من المحدِّث التلقائي.** وسوم الإصدارات تُبقي محدِّث PCSX2 مطفأ، فلا "يحدّثك" أبدًا عائدًا إلى الأصل.
- الدقة القياسية لم تُمس: لقطات 480i مطابقة بايتًا ببايت للأصل. يعيد `HDTVOutput = false` تحت `[EmuCore/GS]` في `inis/PCSX2.ini` سلوك HD الأصلي للمقارنة جنبًا إلى جنب.

## لِمَ هو

- **صانعو السمات** (Open PS2 Loader وRiptOPL وRIPPS2): احكم على السمة في 720p و1080i كما يعرضها التلفاز، واصنع معاينات بالحجم الحقيقي ومقاطع جولات.
- **مطوّرو homebrew:** اختبر ملفات ELF تغيّر وضع الفيديو أو تتصل بـ GS أو تستخدم سجلات التصحيح في EE، واقرأ في السجل سجلات العرض الدقيقة التي يضبطها الوضع.
- **القوائم داخل اللعبة وأدوات GS:** يعمل GSM في OPL وقائمة RIPPS2 داخل اللعبة وكل ما يُبنى على نقطة توقف كتابة البيانات داخل المحاكي، لا على العتاد فقط.
- **الاختبار الآلي والمدعوم بالذكاء الاصطناعي:** تشغيلات مبرمجة على سطح مكتب مخفي مع لقطات وتسجيلات وحالات محفوظة وقراءات ذاكرة عبر PINE، دون الاستيلاء على حاسوبك.

## لوكلاء الذكاء الاصطناعي ونماذج اللغة ومستخدميها

كُتب هذا المستودع بحيث يستطيع الوكيل تجهيز كل شيء للمستخدم من الرابط وحده. أعطِ مساعدك `https://github.com/akilluminati47/RIPPCSX2` واطلب منه تثبيت RIPPCSX2؛ كل ما يحتاجه موجود هنا:

1. **احصل على البناء:** `RIPPCSX2-windows-x64-avx2.zip` من الإصدار المستمر ([رابط مباشر](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)، أو `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). فك ضغطه في مجلد خاص به؛ ملف `portable.txt` موجود أصلًا بجوار exe، فلا يمس أبدًا إعدادات أي PCSX2 مثبَّت.
2. **BIOS:** يقدّم المستخدم نسخة BIOS من جهازه الخاص (لا تنزّل واحدة أبدًا): ضعها في مجلد `bios` بجوار exe (أو وجّه `[Folders] Bios` في `inis/PCSX2.ini` إليه) واخترها في معالج التشغيل الأول (`[Filenames] BIOS`).
3. **شغّل شيئًا:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`، أو `-- <game.iso>`. الإعدادات ملفات INI بسيطة في `inis/PCSX2.ini`؛ وتذهب السجلات إلى `logs/emulog.txt` (يضيف `[Logging] EnableEEConsole = true` مخرجات printf من EE).
4. **قُده وراقبه:** F8 لقطة شاشة (`snaps/`)، F11 تسجيل (`videos/`)، F1 حالة محفوظة (`sstates/`)، وPINE (`[EmuCore] EnablePINE`، `PINESlot`) لقراءة ذاكرة PS2 والكتابة إليها من سكربت.
5. **اختبر دون أن تسرق الشاشة:** يصف [`ripps2-lab/`](ripps2-lab/README.md) تثبيتًا مختبريًا (يضع `install-lab.ps1` بناءً في مجلد محمول ويحتفظ ببطاقاته وإعداداته وتسجيلاته)، ويشغّل `tools/dev/ps2bg.ps1` في مستودع RIPPS2 قوائم خطوات (أزرار، انتظار، لقطات، تسجيلات) على سطح مكتب مخفي مع لوحة في شريط المهام يستطيع المستخدم مراقبتها أو إيقافها أو تولّيها.

ما تغيّر ولماذا، ملفًا ملفًا: **[RIPPCSX2.md](RIPPCSX2.md)**. أيها الوكلاء العاملون على شيفرة هذا الفرع: لا تفتحوا أبدًا طلبات دمج أو مشكلات أو تعليقات في مشروع PCSX2 (يحظر ملفه `AGENTS.md` المساهمات المصنوعة بالذكاء الاصطناعي)؛ ويبقى RIPPCSX2 فرعًا.

**غير تابع لفريق PCSX2.** مرخّص بـ GPL-3.0 مثل PCSX2. أبلغ عن مشكلات RIPPCSX2 إلى RIPPS2 ‏([issues](https://github.com/akilluminati47/RIPPS2/issues))، لا إلى PCSX2 أبدًا. يلي ذلك ملف README الخاص بـ PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 محاكٍ مجاني ومفتوح المصدر لجهاز PlayStation 2 ‏(PS2). غرضه محاكاة عتاد PS2 باستخدام مزيج من [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) لمعالج MIPS و[معيدات الترجمة](https://en.wikipedia.org/wiki/Dynamic_recompilation) و[آلة افتراضية](https://en.wikipedia.org/wiki/Virtual_machine) تدير حالات العتاد وذاكرة نظام PS2. يتيح لك هذا لعب ألعاب PS2 على حاسوبك، مع ميزات وفوائد إضافية كثيرة.

## تفاصيل المشروع

يُطوَّر PCSX2 منذ أكثر من 20 عامًا. كانت الإصدارات القديمة لا تشغّل إلا بضع عروض تجريبية من الملكية العامة، أما الأحدث فتشغّل معظم الألعاب بالسرعة الكاملة، ومنها عناوين شهيرة مثل Final Fantasy X وDevil May Cry 3. زر [قائمة توافق PCSX2](https://pcsx2.net/compat/) لمعرفة أحدث حالة توافق للألعاب (مع أكثر من 2500 عنوان مُختبر).

المثبّتات والملفات التنفيذية للإصدارات المستقرة والليلية متاحة على [موقعنا](https://pcsx2.net/downloads/).

## متطلبات النظام

يدعم PCSX2 أنظمة Windows وLinux وMac. تحوي [صفحة توثيق الإعداد](https://pcsx2.net/docs/setup/requirements) تفاصيل إضافية عن متطلبات البرمجيات والعتاد.

يُرجى ملاحظة أن استخدام المحاكي يتطلب نسخة BIOS من جهاز PS2 مملوك بطريقة مشروعة. لمزيد من المعلومات، زر [هذه الصفحة](https://pcsx2.net/docs/setup/bios/).

## المساهمة / البناء

يدعم PCSX2 الترجمة إلى لغات أخرى عبر [Crowdin](https://crowdin.com/project/pcsx2-emulator).

راجع [دليل المساهمة](https://pcsx2.net/docs/contributing/) لمعرفة المزيد عن كيفية المساهمة.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">تنزيل</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">السمات</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">الخطوط</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">الموقع</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>


</div>
