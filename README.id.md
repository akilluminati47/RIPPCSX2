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
  <a href="README.vi.md">Tiếng Việt</a> |
  <a href="README.lo.md">ລາວ</a> |
  <b>Bahasa Indonesia</b> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Terjemahan README bahasa Inggris; jika berbeda, yang berlaku bahasa Inggris. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Unduh</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fon</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Situs</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Emulator PlayStation 2 untuk menguji dan mengembangkan homebrew, dibuat agar bisa dikendalikan oleh Anda atau agen AI.**

RIPPCSX2 adalah PCSX2 v2.9.96 dengan perubahan yang dibutuhkan pengembang homebrew PS2 untuk melihat yang sebenarnya: mode video HD ditampilkan, direkam, dan di-screenshot seperti yang ditampilkan TV HD, plus breakpoint data perangkat keras milik EE, sehingga menu dalam game dan alat mode video yang mengait ke register GS (GSM milik Open PS2 Loader, menu dalam game RIPPS2) bekerja seperti di konsol. Selebihnya PCSX2 biasa. Awalnya ini lab uji untuk front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) dan ditujukan bagi siapa pun yang membuat homebrew, tema, atau alat untuk PS2.

### [Unduh RIPPCSX2 (zip Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 atau 11, x64, CPU dengan AVX2. Ekstrak di mana saja, jalankan `pcsx2-qtx64-avx2.exe`, dan arahkan ke dump BIOS milik Anda sendiri. Zip ini membawa `portable.txt` kosong di samping exe, jadi RIPPCSX2 menyimpan semua pengaturan dan file di foldernya sendiri: PCSX2 yang sudah Anda pasang tetap memakai pengaturannya, tidak tersentuh. Rilisnya selalu build terbaru ([halamannya](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); klip di bawah ada di [docs/videos](docs/videos).

**Menjalankan program `.elf` untuk pengujian:** System > Start File, atau `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, dan program akan boot seperti dari kartu memori atau flashdisk USB di PS2. Ia **berperilaku seperti perangkat keras asli**: ELF yang menjalankan ELF lain menyerahkan mesin kepadanya lalu pergi, menu dalam game yang mengait ke GS menggambar di atas frame asli game, dan mematikan daya menutup VM seperti konsol yang dimatikan.

## Lihat cara kerjanya

Setiap klip adalah jalannya lab sungguhan pada build ini, dipangkas hingga kurang dari 12 detik.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Agen AI menguji ELF.** Direkam dari pojok kanan bawah layar pengguna (taskbar, bagian dari sesi Claude): Claude menjalankan `RIPPS2.elf` di RIPPCSX2 pada desktop tersembunyi, menjalankan Aqua Teen Hunger Force dari image HDD, dan membuka menu dalam game RIPPS2 di atasnya. Panel kecil itu satu-satunya yang ada di layar; keyboard dan mouse tetap milik pengguna.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Menu dalam game, semua fungsinya.** L1+L2+R1+R2+SELECT+START di atas game yang berjalan: ACHIEVEMENTS, RESUME (game berlanjut), menu lagi di atas frame berikutnya, lalu POWER OFF yang menutup VM. Menu tahu frame mana yang harus digambari karena RIPPCSX2 mengemulasikan breakpoint penulisan data milik EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF menjalankan ELF, seperti PS2 asli.** Memory Files milik RIPPS2 membuka dan menjalankan `mc0:/RIPPS2/RIPPS2.ELF` (build terbaru, disalin ke kartu). RIPPS2 yang sedang berjalan menyerahkan kendali dan menghilang; yang baru dimuat dari kartu dan boot sampai ke daftar gamenya.

## Apa yang Anda dapat dibanding PCSX2 v2.9.96 biasa

- **Mode HD tampil benar.** 720p dan 1080i tampil 16:9 (aslinya menggambarnya 4:3), pada setiap pengaturan rasio aspek kecuali Stretch.
- **Rekaman dan screenshot HD.** F11 merekam 720p pada 1280 x 720 dan 1080i pada 1920 x 1080 (atau kelipatan upscale-nya), bertanda 16:9; F8 menyimpan screenshot dengan ukuran yang sama. Aslinya memberi 640 x 480 atau buffer mentah selebar 640.
- **Ganti mode di tengah rekaman** berlanjut di file baru dengan ukuran baru, bukannya dijejalkan ke file pertama.
- **1080i di tempat yang benar.** Aslinya menggeser gambar 1080i 42 baris ke atas (atas terpotong, pita hitam di bawah); RIPPCSX2 memulainya di baris 40 seperti timing konsol itu sendiri.
- **Breakpoint penulisan data EE** (baru di rippcsx2.2). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) berfungsi: penulisan ke alamat yang diawasi memicu exception debug level 2 di `0x80000100` sebelum dieksekusi, di interpreter maupun recompiler. GSM milik OPL dan menu dalam game RIPPS2 memerlukannya untuk tahu frame mana yang sedang ditampilkan game.
- **Baris log mode video.** Setiap pergantian mode mencatat timing sinkronisasi dan register tampilan (`RIPPCSX2: video mode ...` di `logs/emulog.txt`).
- **Tidak ada tawaran pembaru otomatis.** Tag rilis membuat pembaru PCSX2 tetap mati, jadi ia tidak pernah "memperbarui" Anda kembali ke versi asli.
- Resolusi standar tidak diubah: screenshot 480i identik byte demi byte dengan aslinya. `HDTVOutput = false` di bawah `[EmuCore/GS]` dalam `inis/PCSX2.ini` mengembalikan perilaku HD asli untuk perbandingan berdampingan.

## Untuk apa

- **Pembuat tema** (Open PS2 Loader, RiptOPL, RIPPS2): nilai tema di 720p dan 1080i seperti tampilan TV, dan buat pratinjau ukuran asli serta video tur.
- **Pengembang homebrew:** uji ELF yang mengganti mode video, mengait ke GS, atau memakai register debug EE, dan baca di log register tampilan persis yang diatur sebuah mode.
- **Menu dalam game dan alat GS:** GSM milik OPL, menu dalam game RIPPS2, dan apa pun yang dibangun di atas breakpoint penulisan data berjalan di emulator, bukan hanya di perangkat keras.
- **Pengujian otomatis dan berbantuan AI:** jalankan skrip di desktop tersembunyi dengan screenshot, rekaman, save state, dan pembacaan memori lewat PINE, tanpa mengambil alih komputer Anda.

## Untuk agen AI, LLM, dan penggunanya

Repo ini ditulis agar sebuah agen bisa menyiapkan semuanya untuk pengguna hanya dari tautannya. Berikan `https://github.com/akilluminati47/RIPPCSX2` kepada asisten Anda dan minta ia memasang RIPPCSX2; semua yang ia perlukan ada di sini:

1. **Ambil build-nya:** `RIPPCSX2-windows-x64-avx2.zip` dari rilis bergulir ([tautan langsung](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), atau `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Ekstrak ke folder khusus untuknya; `portable.txt` sudah ada di samping exe, jadi ia tidak pernah menyentuh pengaturan PCSX2 yang terpasang.
2. **BIOS:** pengguna menyediakan dump BIOS dari konsolnya sendiri (jangan pernah mengunduhnya): taruh di folder `bios` di samping exe (atau arahkan `[Folders] Bios` di `inis/PCSX2.ini` ke sana) dan pilih di wizard jalankan-pertama (`[Filenames] BIOS`).
3. **Jalankan sesuatu:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, atau `-- <game.iso>`. Pengaturan berupa INI biasa di `inis/PCSX2.ini`; log masuk ke `logs/emulog.txt` (`[Logging] EnableEEConsole = true` menambahkan printf milik EE).
4. **Kendalikan dan amati:** F8 screenshot (`snaps/`), F11 rekam (`videos/`), F1 save state (`sstates/`), dan PINE (`[EmuCore] EnablePINE`, `PINESlot`) untuk membaca dan menulis memori PS2 dari skrip.
5. **Uji tanpa merebut layar:** [`ripps2-lab/`](ripps2-lab/README.md) menjelaskan instalasi lab (`install-lab.ps1` menaruh build di folder portabel dan menyimpan kartu, pengaturan, serta rekamannya), dan `tools/dev/ps2bg.ps1` di repo RIPPS2 menjalankan daftar langkah (tombol, jeda, screenshot, rekaman) di desktop tersembunyi dengan panel taskbar yang bisa ditonton, dihentikan, atau diambil alih oleh pengguna.

Apa yang berubah dan mengapa, file demi file: **[RIPPCSX2.md](RIPPCSX2.md)**. Agen yang mengerjakan kode fork ini: jangan pernah membuka pull request, issue, atau komentar di proyek PCSX2 (`AGENTS.md`-nya melarang kontribusi buatan AI); RIPPCSX2 tetap menjadi fork.

**Tidak berafiliasi dengan tim PCSX2.** GPL-3.0 seperti PCSX2. Laporkan masalah RIPPCSX2 ke RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), jangan pernah ke PCSX2. Berikutnya adalah README milik PCSX2 sendiri.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 adalah emulator PlayStation 2 (PS2) gratis dan open source. Tujuannya mengemulasikan perangkat keras PS2 dengan kombinasi [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) CPU MIPS, [Recompiler](https://en.wikipedia.org/wiki/Dynamic_recompilation), dan [Mesin virtual](https://en.wikipedia.org/wiki/Virtual_machine) yang mengelola status perangkat keras dan memori sistem PS2. Ini memungkinkan Anda memainkan game PS2 di PC, dengan banyak fitur dan keuntungan tambahan.

## Detail proyek

PCSX2 telah dikembangkan lebih dari 20 tahun. Versi lama hanya bisa menjalankan beberapa demo game domain publik, tetapi versi baru bisa menjalankan sebagian besar game dengan kecepatan penuh, termasuk judul populer seperti Final Fantasy X dan Devil May Cry 3. Kunjungi [daftar kompatibilitas PCSX2](https://pcsx2.net/compat/) untuk status kompatibilitas game terbaru (lebih dari 2500 judul telah diuji).

Installer dan binary untuk build stabil maupun nightly tersedia di [situs web kami](https://pcsx2.net/downloads/).

## Kebutuhan sistem

PCSX2 mendukung Windows, Linux, dan Mac. [Halaman dokumentasi penyiapan](https://pcsx2.net/docs/setup/requirements) memuat detail tambahan tentang kebutuhan perangkat lunak dan perangkat keras.

Perlu diingat bahwa dump BIOS dari konsol PS2 yang dimiliki secara sah diperlukan untuk memakai emulator. Untuk info lebih lanjut, kunjungi [halaman ini](https://pcsx2.net/docs/setup/bios/).

## Berkontribusi / Build

PCSX2 bisa diterjemahkan ke bahasa lain melalui [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Lihat [Panduan Kontribusi](https://pcsx2.net/docs/contributing/) untuk mempelajari cara berkontribusi.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Unduh</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Tema</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Fon</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Situs</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

