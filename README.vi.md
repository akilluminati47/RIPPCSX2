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
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <b>Tiếng Việt</b> |
  <a href="README.lo.md">ລາວ</a> |
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Bản dịch README tiếng Anh; nếu khác nhau, bản tiếng Anh là chuẩn. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Tải về</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Giao diện</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Phông chữ</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Trang web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Trình giả lập PlayStation 2 để thử nghiệm và phát triển homebrew, làm ra để bạn hoặc một tác tử AI điều khiển.**

RIPPCSX2 là PCSX2 v2.9.96 cộng thêm những thay đổi mà nhà phát triển homebrew PS2 cần để thấy đúng thực tế: các chế độ video HD được hiển thị, quay và chụp màn hình như một TV HD hiển thị chúng, cùng điểm dừng dữ liệu phần cứng của EE, để các menu trong game và công cụ chế độ video móc vào thanh ghi GS (GSM của Open PS2 Loader, menu trong game của RIPPS2) chạy như trên máy thật. Mọi thứ còn lại là PCSX2 nguyên bản. Nó bắt đầu là phòng thử nghiệm cho front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) và dành cho bất kỳ ai làm homebrew, theme hay công cụ cho PS2.

**[Xem trang web](https://akilluminati47.github.io/RIPPCSX2/)**: tháo rời một chiếc PS2 hoặc cho nổ tung nó, mọi thứ về RIPPCSX2 đều ở bảng Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Tải RIPPCSX2 (file zip cho Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 hoặc 11, x64, CPU hỗ trợ AVX2. Giải nén ở đâu cũng được, chạy `pcsx2-qtx64-avx2.exe` và chỉ nó tới bản dump BIOS của chính bạn. File zip có một `portable.txt` trống cạnh exe, nên RIPPCSX2 giữ mọi cài đặt và tập tin trong thư mục riêng của nó: PCSX2 bạn đã cài vẫn giữ nguyên cài đặt, không bị đụng tới. Bản phát hành luôn là bản build mới nhất ([trang của nó](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); các clip bên dưới nằm trong [docs/videos](docs/videos).

**Chạy chương trình `.elf` để thử nghiệm:** System > Start File, hoặc `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, và chương trình khởi động như khi khởi động từ thẻ nhớ hoặc USB trên PS2. Nó **hoạt động như phần cứng thật**: một ELF khởi chạy ELF khác sẽ trao máy cho nó rồi biến mất, menu trong game móc vào GS được vẽ lên khung hình thật của game, và tắt nguồn sẽ đóng VM như một máy console tắt điện.

<a id="see-it-work"></a>

## Xem nó hoạt động

Mỗi clip là một lần chạy thật trong phòng thử nghiệm trên bản build này, cắt còn dưới 12 giây.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Một tác tử AI thử nghiệm ELF.** Quay từ góc dưới bên phải màn hình người dùng (thanh tác vụ, một phần của phiên Claude): Claude khởi chạy `RIPPS2.elf` trong RIPPCSX2 trên một màn hình ẩn, chạy Aqua Teen Hunger Force từ ảnh HDD và mở menu trong game của RIPPS2 lên trên. Bảng nhỏ là thứ duy nhất trên màn hình; bàn phím và chuột vẫn thuộc về người dùng.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menu trong game, đủ mọi chức năng.** L1+L2+R1+R2+SELECT+START trên một game đang chạy: ACHIEVEMENTS, RESUME (game tiếp tục), lại mở menu trên một khung hình sau đó, rồi POWER OFF để đóng VM. Menu biết vẽ lên khung hình nào vì RIPPCSX2 giả lập điểm dừng ghi dữ liệu của EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF khởi chạy ELF, như một PS2 thật.** Memory Files của RIPPS2 mở và chạy `mc0:/RIPPS2/RIPPS2.ELF` (bản build mới nhất, đã chép vào thẻ). RIPPS2 đang chạy trao quyền và biến mất; bản mới được nạp từ thẻ và khởi động tới danh sách game.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Bạn được gì so với PCSX2 v2.9.96 nguyên bản

- **Một menu RIPPCSX2** giữa Debug và Help: Run ELF và Run Last ELF, Lab Monitor trực tiếp, Test Steps, Compatibility Report, các công tắc của bản fork và các thư mục chứa mọi thứ.
- **Một nút trên thanh tác vụ cho các lần chạy ẩn.** PCSX2 khởi động trên màn hình ẩn sẽ đặt một nút lên thanh tác vụ, nhờ đó bộ trộn âm lượng hoặc mod âm lượng theo ứng dụng có thể tác động như với mọi chương trình khác.
- **Chế độ HD hiển thị đúng.** 720p và 1080i hiển thị 16:9 (bản gốc vẽ chúng 4:3), ở mọi cài đặt tỉ lệ khung hình trừ Stretch.
- **Quay video và chụp màn hình HD.** F11 quay 720p ở 1280 x 720 và 1080i ở 1920 x 1080 (hoặc bội số khi nâng độ phân giải), gắn nhãn 16:9; F8 lưu ảnh chụp ở cùng kích thước. Bản gốc cho ra 640 x 480 hoặc bộ đệm thô rộng 640.
- **Đổi chế độ giữa lúc quay** sẽ tiếp tục trong một file mới ở kích thước mới thay vì bị ép vào file đầu tiên.
- **1080i đúng chỗ.** Bản gốc đẩy hình 1080i lên 42 dòng (bị cắt phía trên, dải đen phía dưới); RIPPCSX2 bắt đầu nó ở dòng 40 như thời gian của chính máy console.
- **Điểm dừng ghi dữ liệu của EE** (mới trong rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) hoạt động: ghi vào một địa chỉ đang được theo dõi sẽ gây ngoại lệ gỡ lỗi cấp 2 tại `0x80000100` trước khi thực thi, cả ở trình thông dịch lẫn trình biên dịch lại. GSM của OPL và menu trong game của RIPPS2 cần nó để biết game đang hiển thị khung hình nào.
- **Dòng log chế độ video.** Mỗi lần đổi chế độ đều ghi lại thời gian đồng bộ và các thanh ghi hiển thị (`RIPPCSX2: video mode ...` trong `logs/emulog.txt`).
- **Không có lời mời tự cập nhật.** Thẻ phát hành giữ trình cập nhật của PCSX2 ở trạng thái tắt, nên nó không bao giờ "cập nhật" bạn trở lại bản gốc.
- Độ phân giải chuẩn không bị đụng tới: ảnh chụp 480i giống hệt bản gốc từng byte. `HDTVOutput = false` dưới `[EmuCore/GS]` trong `inis/PCSX2.ini` trả lại hành vi HD gốc để so sánh song song.

<a id="what-it-is-for"></a>

## Dùng để làm gì

- **Người làm theme** (Open PS2 Loader, RiptOPL, RIPPS2): đánh giá theme ở 720p và 1080i như TV hiển thị, và làm ảnh xem trước đúng kích thước thật cùng video giới thiệu.
- **Nhà phát triển homebrew:** thử các ELF đổi chế độ video, móc vào GS hoặc dùng thanh ghi gỡ lỗi của EE, và đọc trong log chính xác các thanh ghi hiển thị mà một chế độ đặt.
- **Menu trong game và công cụ GS:** GSM của OPL, menu trong game của RIPPS2 và mọi thứ khác dựa trên điểm dừng ghi dữ liệu đều chạy được trong trình giả lập, không chỉ trên phần cứng.
- **Thử nghiệm tự động và có AI hỗ trợ:** chạy bằng script trên một màn hình ẩn với ảnh chụp, video, trạng thái lưu và đọc bộ nhớ qua PINE, mà không chiếm máy tính của bạn.

<a id="the-end-goal-the-whole-library"></a>

## Mục tiêu cuối cùng: toàn bộ thư viện

Công việc lớn nhất phía trước là kiểm thử game PS2 qua chính đường mã của Open PS2 Loader, như cách máy chạy chúng, và ghi lại những gì mỗi game cần: ELF, KELF, ứng dụng homebrew và game trong một sandbox OPL, tự động thử các chế độ tương thích. Một ngày nào đó có người có thể dùng nó để khiến toàn bộ thư viện chạy được. Đó là mục tiêu cuối cùng của RIPPCSX2.

Compatibility Report là bước đầu tiên: kết quả của một game, các chế độ OPL đã dùng và trạng thái máy, lưu trong `reports/` thành một tệp và một dòng trong `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Dành cho tác tử AI, LLM và người dùng của chúng

Kho này được viết để một tác tử có thể cài đặt cho người dùng chỉ từ đường liên kết. Đưa trợ lý của bạn `https://github.com/akilluminati47/RIPPCSX2` và nhờ nó cài RIPPCSX2; mọi thứ nó cần đều ở đây:

1. **Lấy bản build:** `RIPPCSX2-windows-x64-avx2.zip` từ bản phát hành liên tục ([liên kết trực tiếp](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), hoặc `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Giải nén vào một thư mục riêng; `portable.txt` đã nằm cạnh exe, nên nó không bao giờ đụng tới cài đặt của PCSX2 đã cài.
2. **BIOS:** người dùng cung cấp bản dump BIOS từ máy console của chính họ (đừng bao giờ tải về): đặt vào thư mục `bios` cạnh exe (hoặc trỏ `[Folders] Bios` trong `inis/PCSX2.ini` tới đó) và chọn nó trong trình hướng dẫn lần chạy đầu (`[Filenames] BIOS`).
3. **Chạy thứ gì đó:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, hoặc `-- <game.iso>`. Cài đặt là INI thuần trong `inis/PCSX2.ini`; log ghi vào `logs/emulog.txt` (`[Logging] EnableEEConsole = true` thêm printf của EE).
4. **Điều khiển và quan sát:** F8 chụp màn hình (`snaps/`), F11 quay (`videos/`), F1 lưu trạng thái (`sstates/`), và PINE (`[EmuCore] EnablePINE`, `PINESlot`) để đọc và ghi bộ nhớ PS2 từ một script.
5. **Thử nghiệm mà không chiếm màn hình:** [`ripps2-lab/`](ripps2-lab/README.md) mô tả bản cài phòng thử nghiệm (`install-lab.ps1` đặt một bản build vào thư mục di động và giữ thẻ nhớ, cài đặt và video của nó), còn `tools/dev/ps2bg.ps1` trong kho RIPPS2 chạy danh sách bước (nút, chờ, ảnh chụp, video) trên một màn hình ẩn, kèm một bảng trên thanh tác vụ mà người dùng có thể xem, dừng hoặc tiếp quản.

Thay đổi gì và vì sao, từng file một: **[RIPPCSX2.md](RIPPCSX2.md)**. Các tác tử làm việc trên mã của bản fork này: đừng bao giờ mở pull request, issue hay bình luận trong dự án PCSX2 (`AGENTS.md` của nó cấm đóng góp do AI tạo ra); RIPPCSX2 vẫn là một bản fork.

**Không liên kết với nhóm PCSX2.** GPL-3.0 như PCSX2. Báo lỗi RIPPCSX2 cho RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), đừng bao giờ báo cho PCSX2. Tiếp theo là README của chính PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 là trình giả lập PlayStation 2 (PS2) miễn phí và mã nguồn mở. Mục đích của nó là giả lập phần cứng PS2 bằng sự kết hợp giữa [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) cho CPU MIPS, [Trình biên dịch lại](https://en.wikipedia.org/wiki/Dynamic_recompilation) và một [Máy ảo](https://en.wikipedia.org/wiki/Virtual_machine) quản lý trạng thái phần cứng và bộ nhớ hệ thống PS2. Nhờ vậy bạn có thể chơi game PS2 trên PC, với nhiều tính năng và lợi ích bổ sung.

<a id="project-details"></a>

## Chi tiết dự án

PCSX2 đã được phát triển hơn 20 năm. Các phiên bản cũ chỉ chạy được vài bản demo game thuộc phạm vi công cộng, còn phiên bản mới chạy được hầu hết game ở tốc độ tối đa, kể cả những tựa nổi tiếng như Final Fantasy X và Devil May Cry 3. Xem [danh sách tương thích PCSX2](https://pcsx2.net/compat/) để biết tình trạng tương thích mới nhất của game (hơn 2500 tựa đã thử).

Trình cài đặt và file thực thi của bản ổn định lẫn bản nightly có trên [trang web của chúng tôi](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Yêu cầu hệ thống

PCSX2 hỗ trợ Windows, Linux và Mac. [Trang tài liệu cài đặt](https://pcsx2.net/docs/setup/requirements) có thêm chi tiết về yêu cầu phần mềm và phần cứng.

Xin lưu ý rằng để dùng trình giả lập cần có bản dump BIOS từ một máy PS2 sở hữu hợp pháp. Để biết thêm, hãy xem [trang này](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Đóng góp / Build

PCSX2 có thể được dịch sang các ngôn ngữ khác qua [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Xem [Hướng dẫn đóng góp](https://pcsx2.net/docs/contributing/) để biết thêm về cách đóng góp.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Tải về</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Giao diện</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Phông chữ</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Trang web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

