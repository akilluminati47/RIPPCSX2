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
  <a href="README.ar.md">العربية</a> |
  <a href="README.fa.md">فارسی</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <b>简体中文</b> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>英文 README 的译本；如有出入，以英文为准。 <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下载</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主题</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">字体</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">网站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**一款用于测试和开发 homebrew 的 PlayStation 2 模拟器，可由你或 AI 智能体来操作。**

RIPPCSX2 就是 PCSX2 v2.9.96，加上 PS2 homebrew 开发者看到真实效果所需的改动：HD 视频模式按 HD 电视的显示方式显示、录制和截图，并提供 EE 的硬件数据断点，让挂钩 GS 寄存器的游戏内菜单和视频模式工具（Open PS2 Loader 的 GSM、RIPPS2 的游戏内菜单）像在主机上一样工作。其余一切都是原版 PCSX2。它最初是前端 [RIPPS2](https://github.com/akilluminati47/RIPPS2) 的测试实验室，面向所有为 PS2 制作 homebrew、主题或工具的人。

### [下载 RIPPCSX2（Windows zip）](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 或 11，x64，支持 AVX2 的 CPU。解压到任意位置，运行 `pcsx2-qtx64-avx2.exe`，并指向你自己转储的 BIOS。zip 在 exe 旁带有一个空的 `portable.txt`，因此 RIPPCSX2 把所有设置和文件都放在自己的文件夹里：你已安装的 PCSX2 会保留自己的设置，不受影响。发布页总是最新构建（[页面](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)）；下面的片段在 [docs/videos](docs/videos)。

**可运行 `.elf` 程序进行测试：** System > Start File，或 `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`，程序会像在 PS2 上从记忆卡或 U 盘启动那样启动。它**表现得像真实硬件**：启动另一个 ELF 的 ELF 会把机器交出去然后退出，挂钩 GS 的游戏内菜单绘制在游戏真实的画面帧上，关机会像主机断电一样关闭 VM。

## 实际运行效果

每个片段都是在此构建上真实的实验室运行，剪到 12 秒以内。

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**AI 智能体测试 ELF。** 录自用户屏幕右下角（任务栏，Claude 会话的一部分）：Claude 在隐藏桌面上的 RIPPCSX2 中启动 `RIPPS2.elf`，从 HDD 镜像启动 Aqua Teen Hunger Force，并在其上打开 RIPPS2 的游戏内菜单。屏幕上只有那个小面板；键盘和鼠标始终归用户使用。

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**游戏内菜单，全部功能。** 在运行中的游戏上按 L1+L2+R1+R2+SELECT+START：ACHIEVEMENTS、RESUME（游戏继续）、在稍后的画面帧上再次打开菜单，然后用 POWER OFF 关闭 VM。菜单知道该画在哪一帧上，因为 RIPPCSX2 模拟了 EE 的数据写入断点。

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF 启动 ELF，就像真正的 PS2。** RIPPS2 的 Memory Files 打开并运行 `mc0:/RIPPS2/RIPPS2.ELF`（最新构建，已复制到记忆卡）。正在运行的 RIPPS2 交出控制并退出；新的版本从记忆卡加载，启动到游戏列表。

## 相比原版 PCSX2 v2.9.96 的改进

- **HD 模式显示正确。** 720p 和 1080i 在除 Stretch 以外的所有宽高比设置下都以 16:9 显示（原版画成 4:3）。
- **HD 录制和截图。** F11 以 1280 x 720 录制 720p，以 1920 x 1080（或其放大倍数）录制 1080i，并标记为 16:9；F8 以相同尺寸保存截图。原版给出 640 x 480 或 640 宽的原始缓冲。
- **录制中途切换模式**会以新尺寸在新文件中继续，而不是挤进第一个文件。
- **1080i 位置正确。** 原版把 1080i 画面上移 42 行（顶部被裁，底部黑边）；RIPPCSX2 像主机自身的时序那样从第 40 行开始。
- **EE 数据写入断点**（rippcsx2.2 新增）。COP0 `$24`（`MTBPC`、`MTDAB`、`MTDABM` ...）可用：写入被监视的地址会在执行前于 `0x80000100` 触发 2 级调试异常，解释器和重编译器中都是如此。OPL 的 GSM 和 RIPPS2 的游戏内菜单需要它来得知游戏正在显示哪一帧。
- **视频模式日志行。** 每次模式切换都会记录同步时序和显示寄存器（`logs/emulog.txt` 中的 `RIPPCSX2: video mode ...`）。
- **没有自动更新提示。** 发布标签让 PCSX2 的更新器保持关闭，因此它永远不会把你"更新"回原版。
- 标准分辨率不变：480i 截图与原版逐字节相同。在 `inis/PCSX2.ini` 的 `[EmuCore/GS]` 下设 `HDTVOutput = false` 可恢复原版 HD 行为，便于并排比较。

## 适合做什么

- **主题作者**（Open PS2 Loader、RiptOPL、RIPPS2）：按电视显示的样子在 720p 和 1080i 下评估主题，并制作真实尺寸的预览和介绍视频。
- **homebrew 开发者：** 测试切换视频模式、挂钩 GS 或使用 EE 调试寄存器的 ELF，并在日志中读到某个模式设置的确切显示寄存器。
- **游戏内菜单和 GS 工具：** OPL 的 GSM、RIPPS2 的游戏内菜单，以及任何基于数据写入断点的东西，都能在模拟器中运行，而不只是在硬件上。
- **自动化和 AI 辅助测试：** 在隐藏桌面上运行脚本，带截图、录制、即时存档和 PINE 内存读取，不占用你的电脑。

## 给 AI 智能体、LLM 及其用户

本仓库的写法让智能体只凭链接就能为用户完成配置。把 `https://github.com/akilluminati47/RIPPCSX2` 交给你的助手并让它安装 RIPPCSX2；它需要的一切都在这里：

1. **获取构建：** 滚动发布中的 `RIPPCSX2-windows-x64-avx2.zip`（[直接链接](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)，或 `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`）。解压到它专用的文件夹；`portable.txt` 已在 exe 旁边，因此绝不会触碰已安装的 PCSX2 的设置。
2. **BIOS：** 由用户提供自己主机的 BIOS 转储（切勿下载）：放到 exe 旁的 `bios` 文件夹中（或在 `inis/PCSX2.ini` 中把 `[Folders] Bios` 指向它），并在首次运行向导中选择（`[Filenames] BIOS`）。
3. **运行点什么：** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`，或 `-- <game.iso>`。设置是 `inis/PCSX2.ini` 中的普通 INI；日志写到 `logs/emulog.txt`（`[Logging] EnableEEConsole = true` 会加入 EE 的 printf）。
4. **操作并观察：** F8 截图（`snaps/`），F11 录制（`videos/`），F1 即时存档（`sstates/`），以及用 PINE（`[EmuCore] EnablePINE`、`PINESlot`）从脚本读写 PS2 内存。
5. **测试时不抢屏幕：** [`ripps2-lab/`](ripps2-lab/README.md) 介绍实验室安装（`install-lab.ps1` 把构建放进便携文件夹，并保存它的记忆卡、设置和录制），RIPPS2 仓库里的 `tools/dev/ps2bg.ps1` 在隐藏桌面上运行步骤列表（按键、等待、截图、录制），并提供一个任务栏面板，用户可以观看、停止或接管。

逐个文件说明改了什么、为什么改：**[RIPPCSX2.md](RIPPCSX2.md)**。在这个分支代码上工作的智能体：永远不要在 PCSX2 项目中发起 pull request、issue 或评论（它的 `AGENTS.md` 禁止 AI 生成的贡献）；RIPPCSX2 始终是一个分支。

**与 PCSX2 团队无关。** 与 PCSX2 一样采用 GPL-3.0。RIPPCSX2 的问题请报告给 RIPPS2（[issues](https://github.com/akilluminati47/RIPPS2/issues)），切勿报告给 PCSX2。以下是 PCSX2 自己的 README。

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 是一款免费开源的 PlayStation 2（PS2）模拟器。它的目的是结合 MIPS CPU 的 [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>)、[重编译器](https://en.wikipedia.org/wiki/Dynamic_recompilation) 以及管理硬件状态和 PS2 系统内存的 [虚拟机](https://en.wikipedia.org/wiki/Virtual_machine)，来模拟 PS2 的硬件。这让你可以在电脑上玩 PS2 游戏，并享有许多额外功能和好处。

## 项目详情

PCSX2 已开发超过 20 年。早期版本只能运行少数公有领域的游戏演示，而新版本可以全速运行大多数游戏，包括 Final Fantasy X 和 Devil May Cry 3 等热门作品。访问 [PCSX2 兼容性列表](https://pcsx2.net/compat/) 了解游戏的最新兼容状态（已测试超过 2500 款）。

稳定版和每夜构建的安装程序和二进制文件可在 [我们的网站](https://pcsx2.net/downloads/) 获取。

## 系统要求

PCSX2 支持 Windows、Linux 和 Mac。[安装文档页面](https://pcsx2.net/docs/setup/requirements) 有软件和硬件要求的更多细节。

请注意，使用模拟器需要从合法拥有的 PS2 主机转储的 BIOS。更多信息请访问 [此页面](https://pcsx2.net/docs/setup/bios/)。

## 贡献 / 构建

PCSX2 可通过 [Crowdin](https://crowdin.com/project/pcsx2-emulator) 翻译成其他语言。

如何参与贡献，请参阅 [贡献指南](https://pcsx2.net/docs/contributing/)。

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">下载</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">主题</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">字体</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">网站</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

