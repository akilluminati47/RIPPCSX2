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
  <b>한국어</b> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>영어 README의 번역입니다. 내용이 다르면 영어판이 기준입니다. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">다운로드</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">테마</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">글꼴</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">웹사이트</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**homebrew를 테스트하고 개발하기 위한 PlayStation 2 에뮬레이터. 사용자나 AI 에이전트가 직접 조작하도록 만들었습니다.**

RIPPCSX2는 PS2 homebrew 개발자가 실제 모습을 보는 데 필요한 변경을 더한 PCSX2 v2.9.96입니다. HD 비디오 모드를 HD TV가 보여 주는 그대로 표시하고 녹화하고 스크린샷으로 남기며, EE의 하드웨어 데이터 브레이크포인트 덕분에 GS 레지스터에 후킹하는 게임 내 메뉴와 비디오 모드 도구(Open PS2 Loader의 GSM, RIPPS2의 게임 내 메뉴)가 실기와 똑같이 동작합니다. 나머지는 모두 순정 PCSX2입니다. 프런트엔드 [RIPPS2](https://github.com/akilluminati47/RIPPS2)의 테스트 랩으로 시작했으며, PS2용 homebrew, 테마, 도구를 만드는 모든 사람을 위한 것입니다.

**[웹사이트 보기](https://akilluminati47.github.io/RIPPCSX2/)**: PS2를 분해하거나 폭파해 보세요. RIPPCSX2의 모든 내용은 Info 패널에 있습니다.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [RIPPCSX2 다운로드 (Windows zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 또는 11, x64, AVX2를 지원하는 CPU. 원하는 곳에 압축을 풀고 `pcsx2-qtx64-avx2.exe`를 실행한 뒤 직접 덤프한 BIOS를 지정하세요. zip에는 exe 옆에 빈 `portable.txt`가 들어 있어 RIPPCSX2는 모든 설정과 파일을 자기 폴더에 보관합니다. 이미 설치한 PCSX2의 설정은 손대지 않고 그대로 남습니다. 릴리스는 항상 최신 빌드입니다([해당 페이지](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)). 아래 클립은 [docs/videos](docs/videos)에 있습니다.

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [RIPPCSX2 다운로드 (Linux AppImage)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, AVX2를 지원하는 CPU. 실행 권한을 주고 시작하세요. 이번 릴리스에 새로 추가되었고 Windows zip과 같은 워크플로로 빌드하지만 아직 Linux 컴퓨터에서 실행해 보지 않았습니다. 결과를 알려 주세요. 숨겨진 실행용 작업 표시줄 버튼은 Windows 전용입니다.

**테스트용 `.elf` 프로그램을 실행합니다:** System > Start File 또는 `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`로, PS2의 메모리 카드나 USB 메모리에서 부팅하듯이 프로그램이 부팅됩니다. **실제 하드웨어처럼 동작합니다**: 다른 ELF를 실행한 ELF는 기기를 넘겨주고 사라지고, GS에 후킹하는 게임 내 메뉴는 게임의 실제 프레임 위에 그려지며, 전원 끄기는 콘솔 전원을 끄듯 VM을 닫습니다.

<a id="see-it-work"></a>

## 실제로 동작하는 모습

각 클립은 이 빌드에서 실제로 랩을 돌린 것으로, 12초 미만으로 잘랐습니다.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**ELF를 테스트하는 AI 에이전트.** 사용자 화면의 오른쪽 아래(작업 표시줄, Claude 세션의 일부)에서 녹화: Claude가 숨겨진 데스크톱의 RIPPCSX2에서 `RIPPS2.elf`를 실행하고, HDD 이미지에서 Aqua Teen Hunger Force를 실행한 뒤 그 위에 RIPPS2의 게임 내 메뉴를 엽니다. 화면에 보이는 것은 작은 패널뿐이며, 키보드와 마우스는 계속 사용자가 씁니다.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**게임 내 메뉴의 모든 기능.** 실행 중인 게임 위에서 L1+L2+R1+R2+SELECT+START: ACHIEVEMENTS, RESUME(게임 계속), 나중 프레임 위에서 다시 메뉴, 그리고 VM을 닫는 POWER OFF. RIPPCSX2가 EE의 데이터 쓰기 브레이크포인트를 에뮬레이트하므로 메뉴는 어느 프레임 위에 그려야 할지 압니다.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF가 ELF를 실행합니다, 실제 PS2처럼.** RIPPS2의 Memory Files가 `mc0:/RIPPS2/RIPPS2.ELF`(카드에 복사한 최신 빌드)를 열어 실행합니다. 실행 중이던 RIPPS2는 넘겨주고 사라지며, 새 빌드가 카드에서 로드되어 게임 목록까지 부팅됩니다.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## 순정 PCSX2 v2.9.96보다 나은 점

- **Debug와 Help 사이의 RIPPCSX2 메뉴**: Run ELF와 Run Last ELF, 실시간 Lab Monitor, Test Steps, Compatibility Report, 포크의 스위치, 결과물이 저장되는 폴더.
- **RIPART,** 같은 메뉴에 있습니다: OPL Manager의 아트 데이터베이스로, 16,313개 게임을 archive.org의 백업에서 바이트 범위로 읽습니다. 드라이브에 게임이 없어도 실제 목록에서 테마를 판단할 수 있는 미끼 게임 항목, 게임 아트를 조각별로 남기거나 뺄 수 있는 체크박스 목록, 드라이브에서 커버가 없는 게임 찾기, 그리고 모두 담을 ART 폴더 또는 `art.tar`를 제공합니다. 미끼는 OPL과 RIPPS2에 표시되지만 시작되지 않으며, 이미 있는 파일은 절대 교체하지 않습니다. akilluminati47은 이 데이터베이스에 8비트 PNG 아트와 128 x 128 디스크 아이콘이 들어오도록 도왔습니다.
- **기본 OPL이 게임을 시작합니다.** 프로그램이 직접 등록한 `host` 장치가 이제 자기 열기 요청을 받으므로 OPL의 IOP 재부팅이 동작합니다. 원본은 `file 'host0:' can't open`에서 멈춥니다.
- **EXIT GAME이 브라우저까지 갑니다.** IOP 재부팅 중 SIO2 인터럽트가 사라져 OSDSYS가 검은 화면으로 메모리 카드를 기다렸습니다.
- **숨김 실행용 작업 표시줄 버튼.** 숨겨진 바탕 화면에서 시작한 PCSX2는 작업 표시줄에 버튼을 하나 놓으므로, 볼륨 믹서나 앱별 볼륨 모드가 다른 프로그램처럼 접근할 수 있습니다.
- **HD 모드가 제대로 보입니다.** 720p와 1080i는 Stretch를 제외한 모든 화면비 설정에서 16:9로 표시됩니다(순정판은 4:3으로 그립니다).
- **HD 녹화와 스크린샷.** F11은 720p를 1280 x 720, 1080i를 1920 x 1080(또는 업스케일 배수)으로 16:9 태그를 붙여 녹화하고, F8은 같은 크기로 스크린샷을 저장합니다. 순정판은 640 x 480 또는 폭 640의 원시 버퍼를 줍니다.
- **녹화 중 모드 변경**은 첫 파일에 억지로 넣지 않고 새 크기의 새 파일로 이어집니다.
- **1080i가 제자리에.** 순정판은 1080i 화면을 42라인 위로 올립니다(위가 잘리고 아래에 검은 띠). RIPPCSX2는 콘솔 자체 타이밍처럼 40번째 라인에서 시작합니다.
- **EE 데이터 쓰기 브레이크포인트**(rippcsx2.2 신기능). COP0 `$24`(`MTBPC`, `MTDAB`, `MTDABM` ...)가 동작합니다: 감시 중인 주소에 쓰면 실행 전에 `0x80000100`에서 레벨 2 디버그 예외가 발생하며, 인터프리터와 리컴파일러 모두에서 그렇습니다. OPL의 GSM과 RIPPS2의 게임 내 메뉴는 게임이 어떤 프레임을 표시하는지 알기 위해 이것이 필요합니다.
- **비디오 모드 로그 줄.** 모드가 바뀔 때마다 동기 타이밍과 디스플레이 레지스터를 기록합니다(`logs/emulog.txt`의 `RIPPCSX2: video mode ...`).
- **자동 업데이트 제안 없음.** 릴리스 태그가 PCSX2 업데이터를 꺼 두므로 순정판으로 "업데이트"되어 돌아가는 일이 없습니다.
- 표준 해상도는 그대로입니다: 480i 스크린샷은 순정판과 바이트 단위로 같습니다. `inis/PCSX2.ini`의 `[EmuCore/GS]` 아래 `HDTVOutput = false`로 나란히 비교할 수 있게 순정 HD 동작을 되돌립니다.

<a id="what-it-is-for"></a>

## 용도

- **테마 제작자**(Open PS2 Loader, RiptOPL, RIPPS2): TV에 보이는 그대로 720p와 1080i에서 테마를 판단하고, 실제 크기의 미리보기와 소개 영상을 만드세요.
- **homebrew 개발자:** 비디오 모드를 바꾸거나 GS에 후킹하거나 EE 디버그 레지스터를 쓰는 ELF를 테스트하고, 모드가 설정하는 정확한 디스플레이 레지스터를 로그에서 읽으세요.
- **게임 내 메뉴와 GS 도구:** OPL의 GSM, RIPPS2의 게임 내 메뉴, 그리고 데이터 쓰기 브레이크포인트를 쓰는 모든 것이 실기뿐 아니라 에뮬레이터에서도 돌아갑니다.
- **PS1 게임:** 가상 드라이브에서 Ember와 PS1 게임을 실행해 시작과 PS1 목록을 테스트합니다. 드라이브에는 본인의 PS1 BIOS를 두세요.
- **Neutrino와 POPStarter:** Neutrino는 RIPPS2를 통해 게임을 최고 속도로 실행합니다. POPStarter는 EE 리컴파일러를 꺼야만 PS1 게임을 시작하며, 현재는 약 절반 속도에 그래픽이 손상됩니다. 리컴파일러를 쓰면 검은 화면에 머뭅니다.
- **자동화 및 AI 지원 테스트:** 숨겨진 데스크톱에서 스크린샷, 녹화, 상태 저장, PINE 메모리 읽기를 곁들인 스크립트 실행을, PC를 점령하지 않고 할 수 있습니다.

<a id="the-end-goal-the-whole-library"></a>

## 최종 목표: 라이브러리 전체

앞으로의 가장 큰 일은 PS2 게임을 콘솔이 실행하는 방식 그대로 Open PS2 Loader 자체의 코드 경로로 테스트하고, 각 게임에 무엇이 필요한지 기록하는 것입니다. OPL 샌드박스에서 ELF, KELF, 홈브루 앱과 게임을 돌리며 호환 모드를 자동으로 시험합니다. 언젠가 누군가 이것으로 라이브러리 전체를 실행할 수 있을 것입니다. 그것이 RIPPCSX2의 최종 목표입니다.

Compatibility Report가 그 첫걸음입니다. 게임의 결과, 사용한 OPL 모드, 기기 상태를 `reports/`에 파일로, `compatibility.csv`에 행으로 저장합니다.

<a id="for-ai-agents-llms-and-their-users"></a>

## AI 에이전트, LLM과 그 사용자에게

이 저장소는 에이전트가 링크만으로 사용자의 설정을 끝낼 수 있도록 작성되었습니다. 어시스턴트에게 `https://github.com/akilluminati47/RIPPCSX2`를 주고 RIPPCSX2 설치를 부탁하세요. 필요한 것은 모두 여기에 있습니다:

1. **빌드 받기:** 롤링 릴리스의 `RIPPCSX2-windows-x64-avx2.zip`([직접 링크](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) 또는 `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). 전용 폴더에 압축을 푸세요. `portable.txt`가 이미 exe 옆에 있으므로 설치된 PCSX2의 설정은 절대 건드리지 않습니다.
2. **BIOS:** 사용자가 자기 콘솔의 BIOS 덤프를 제공합니다(절대 다운로드하지 마세요): exe 옆의 `bios` 폴더에 넣고(또는 `inis/PCSX2.ini`의 `[Folders] Bios`를 그곳으로 지정하고) 첫 실행 마법사에서 선택합니다(`[Filenames] BIOS`).
3. **무언가 실행:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` 또는 `-- <game.iso>`. 설정은 `inis/PCSX2.ini`의 일반 INI이며, 로그는 `logs/emulog.txt`로 갑니다(`[Logging] EnableEEConsole = true`면 EE의 printf가 추가됩니다).
4. **조작하고 관찰:** F8 스크린샷(`snaps/`), F11 녹화(`videos/`), F1 상태 저장(`sstates/`), 스크립트에서 PS2 메모리를 읽고 쓰는 PINE(`[EmuCore] EnablePINE`, `PINESlot`).
5. **화면을 빼앗지 않고 테스트:** [`ripps2-lab/`](ripps2-lab/README.md)은 랩 설치를 설명합니다(`install-lab.ps1`이 빌드를 포터블 폴더에 넣고 카드, 설정, 녹화를 보관). RIPPS2 저장소의 `tools/dev/ps2bg.ps1`은 단계 목록(버튼, 대기, 스크린샷, 녹화)을 숨겨진 데스크톱에서 실행하며, 사용자가 지켜보거나 멈추거나 넘겨받을 수 있는 작업 표시줄 패널을 띄웁니다.

무엇이 왜 바뀌었는지 파일별로: **[RIPPCSX2.md](RIPPCSX2.md)**. 이 포크의 코드를 다루는 에이전트에게: PCSX2 프로젝트에 pull request, issue, 댓글을 절대 만들지 마세요(그쪽 `AGENTS.md`는 AI가 만든 기여를 금지합니다). RIPPCSX2는 포크로 남습니다.

**PCSX2 팀과 관계없습니다.** PCSX2와 같은 GPL-3.0. RIPPCSX2 문제는 PCSX2가 아니라 RIPPS2에 보고하세요([issues](https://github.com/akilluminati47/RIPPS2/issues)). 아래는 PCSX2 자체의 README입니다.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2는 무료 오픈 소스 PlayStation 2(PS2) 에뮬레이터입니다. MIPS CPU [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>), [리컴파일러](https://en.wikipedia.org/wiki/Dynamic_recompilation), 그리고 하드웨어 상태와 PS2 시스템 메모리를 관리하는 [가상 머신](https://en.wikipedia.org/wiki/Virtual_machine)을 조합해 PS2 하드웨어를 에뮬레이트하는 것이 목적입니다. 덕분에 PC에서 PS2 게임을 여러 추가 기능과 이점과 함께 즐길 수 있습니다.

<a id="project-details"></a>

## 프로젝트 상세

PCSX2는 20년 넘게 개발되어 왔습니다. 예전 버전은 퍼블릭 도메인 게임 데모 몇 개만 돌릴 수 있었지만, 새 버전은 Final Fantasy X와 Devil May Cry 3 같은 인기작을 포함해 대부분의 게임을 풀 스피드로 돌립니다. 게임의 최신 호환성 상태는 [PCSX2 호환성 목록](https://pcsx2.net/compat/)을 확인하세요(2500개 이상의 타이틀 테스트).

안정판과 나이틀리 빌드의 설치 파일과 바이너리는 [웹사이트](https://pcsx2.net/downloads/)에 있습니다.

<a id="system-requirements"></a>

## 시스템 요구 사항

PCSX2는 Windows, Linux, Mac을 지원합니다. 소프트웨어와 하드웨어 요구 사항의 자세한 내용은 [설정 문서 페이지](https://pcsx2.net/docs/setup/requirements)에 있습니다.

에뮬레이터를 쓰려면 합법적으로 소유한 PS2 콘솔에서 덤프한 BIOS가 필요합니다. 자세한 내용은 [이 페이지](https://pcsx2.net/docs/setup/bios/)를 참고하세요.

<a id="contributing--building"></a>

## 기여 / 빌드

PCSX2는 [Crowdin](https://crowdin.com/project/pcsx2-emulator)에서 다른 언어로 번역할 수 있습니다.

기여 방법은 [기여 가이드](https://pcsx2.net/docs/contributing/)를 참고하세요.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">다운로드</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">테마</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">글꼴</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">웹사이트</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

