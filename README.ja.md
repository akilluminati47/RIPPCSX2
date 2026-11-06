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
  <b>日本語</b> |
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

<p align="center"><sub>英語の README の翻訳です。内容が異なる場合は英語版が正です。 <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">ダウンロード</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">テーマ</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">フォント</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">ウェブサイト</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**homebrew のテストと開発のための PlayStation 2 エミュレーター。あなたにも AI エージェントにも操作できるように作られています。**

RIPPCSX2 は、PS2 homebrew 開発者が本物を見るのに必要な変更を加えた PCSX2 v2.9.96 です。HD ビデオモードを HD テレビの映し方どおりに表示・録画・スクリーンショットでき、EE のハードウェアデータブレークポイントにより、GS レジスタにフックするゲーム内メニューやビデオモードツール（Open PS2 Loader の GSM、RIPPS2 のゲーム内メニュー）が実機と同じように動きます。それ以外はすべて素の PCSX2 です。フロントエンド [RIPPS2](https://github.com/akilluminati47/RIPPS2) のテストラボとして始まり、PS2 の homebrew、テーマ、ツールを作るすべての人に向けたものです。

**[ウェブサイトを見る](https://akilluminati47.github.io/RIPPCSX2/)**: PS2 を分解したり爆破したりでき、RIPPCSX2 のすべては Info パネルにあります。

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [RIPPCSX2 をダウンロード（Windows 用 zip）](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 または 11、x64、AVX2 対応 CPU。好きな場所に展開して `pcsx2-qtx64-avx2.exe` を起動し、自分の BIOS ダンプを指定します。zip には exe の隣に空の `portable.txt` が入っているので、RIPPCSX2 は設定とファイルをすべて自分のフォルダーに保存します。すでにインストール済みの PCSX2 の設定はそのまま手つかずです。リリースは常に最新ビルドです（[そのページ](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)）。下のクリップは [docs/videos](docs/videos) にあります。

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [RIPPCSX2 をダウンロード（Linux AppImage）](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64、AVX2 対応の CPU。実行可能にして起動します。このリリースで新しく加わったもので、Windows の zip と同じワークフローでビルドしていますが、Linux マシンではまだ動かしていません。結果をぜひ教えてください。非表示実行用のタスクバーボタンは Windows のみです。

**テスト用に `.elf` プログラムを実行できます：** System > Start File、または `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>` で、PS2 のメモリーカードや USB メモリーから起動するのと同じようにプログラムが起動します。**実機と同じように動作します**：別の ELF を起動した ELF はマシンを引き渡して消え、GS にフックするゲーム内メニューはゲームの本物のフレームの上に描かれ、電源オフでは本体の電源を切るように VM が閉じます。

<a id="see-it-work"></a>

## 動作を見る

どのクリップもこのビルドでの実際のラボ実行で、12 秒未満に切り詰めています。

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**ELF をテストする AI エージェント。** ユーザーの画面の右下（タスクバー、Claude セッションの一部）から録画：Claude が隠しデスクトップ上の RIPPCSX2 で `RIPPS2.elf` を起動し、HDD イメージから Aqua Teen Hunger Force を起動して、その上に RIPPS2 のゲーム内メニューを開きます。画面に出るのは小さなパネルだけで、キーボードとマウスはユーザーのままです。

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**ゲーム内メニューの全機能。** 実行中のゲームの上で L1+L2+R1+R2+SELECT+START：ACHIEVEMENTS、RESUME（ゲームは続行）、少し後のフレームの上で再びメニュー、そして VM を閉じる POWER OFF。RIPPCSX2 が EE のデータ書き込みブレークポイントをエミュレートしているので、メニューはどのフレームの上に描けばよいかを知っています。

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF が ELF を起動する、実機の PS2 のように。** RIPPS2 の Memory Files が `mc0:/RIPPS2/RIPPS2.ELF`（カードにコピーした最新ビルド）を開いて実行します。実行中の RIPPS2 は制御を渡して消え、新しいほうがカードから読み込まれてゲームリストまで起動します。

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## 素の PCSX2 v2.9.96 と比べて得られるもの

- **Debug と Help の間にある RIPPCSX2 メニュー**: Run ELF と Run Last ELF、ライブの Lab Monitor、Test Steps、Compatibility Report、フォークのスイッチ、出力先のフォルダー。
- **RIPART**（同じメニュー内）: OPL Manager のアートデータベースです。16,313 本のゲームを archive.org のバックアップからバイト範囲で読み取ります。ドライブにゲームがなくても実際のリストでテーマを確認できるダミーのゲーム項目、ゲームのアートを 1 点ずつ残すか外すか選べるチェックボックスのリスト、ドライブ上のカバーがないゲームの検索、そしてすべてを入れる ART フォルダーまたは `art.tar` を備えています。ダミーは OPL と RIPPS2 に表示されますが起動はしません。既存のファイルが置き換えられることはありません。このデータベースの 8 ビット PNG アートと 128 x 128 のディスクアイコンの実現には akilluminati47 も協力しました。
- **標準の OPL がゲームを起動できます。** プログラムが自分で登録した `host` デバイスが自身のオープンを受け取るようになり、OPL の IOP リブートが動きます。標準版は `file 'host0:' can't open` で止まります。
- **EXIT GAME がブラウザーに戻ります。** IOP リブートをまたぐと SIO2 割り込みが失われ、OSDSYS が黒い画面のままメモリーカードを待ち続けていました。
- **隠しデスクトップ実行用のタスクバーボタン。** 隠しデスクトップで起動した PCSX2 はタスクバーにボタンを置くので、音量ミキサーやアプリ別音量の mod から他のプログラムと同じように操作できます。
- **HD モードが正しく見える。** 720p と 1080i は、Stretch 以外のどのアスペクト設定でも 16:9 で表示されます（素の版は 4:3 で描画）。
- **HD の録画とスクリーンショット。** F11 は 720p を 1280 x 720、1080i を 1920 x 1080（またはアップスケール倍）で 16:9 として録画し、F8 は同じサイズでスクリーンショットを保存します。素の版は 640 x 480 か、幅 640 の生のバッファです。
- **録画中のモード切り替え**は、最初のファイルに押し込まず、新しいサイズの新しいファイルで続きます。
- **1080i が正しい位置に。** 素の版は 1080i の画像を 42 ライン上にずらします（上が切れ、下に黒帯）。RIPPCSX2 は本体自身のタイミングと同じ 40 ライン目から始めます。
- **EE のデータ書き込みブレークポイント**（rippcsx2.2 の新機能）。COP0 `$24`（`MTBPC`、`MTDAB`、`MTDABM` ...）が動作します：監視中のアドレスへの書き込みは、実行前に `0x80000100` でレベル 2 のデバッグ例外を発生させます。インタープリターでもリコンパイラーでもです。OPL の GSM と RIPPS2 のゲーム内メニューは、ゲームがどのフレームを表示しているかを知るのにこれを必要とします。
- **ビデオモードのログ行。** モードが変わるたびに同期タイミングとディスプレイレジスタを記録します（`logs/emulog.txt` の `RIPPCSX2: video mode ...`）。
- **自動更新の提案なし。** リリースタグにより PCSX2 のアップデーターはオフのままなので、素の版に「アップデート」で戻されることはありません。
- 標準解像度はそのまま：480i のスクリーンショットは素の版とバイト単位で同一です。`inis/PCSX2.ini` の `[EmuCore/GS]` で `HDTVOutput = false` にすると、比較用に素の HD 動作に戻せます。

<a id="what-it-is-for"></a>

## 用途

- **テーマ作者**（Open PS2 Loader、RiptOPL、RIPPS2）：テレビに映るとおりに 720p と 1080i でテーマを判断し、実寸のプレビューや紹介動画を作れます。
- **homebrew 開発者：** ビデオモードを切り替える ELF、GS にフックする ELF、EE のデバッグレジスタを使う ELF をテストし、モードが設定する正確なディスプレイレジスタをログで確認できます。
- **ゲーム内メニューと GS ツール：** OPL の GSM、RIPPS2 のゲーム内メニュー、データ書き込みブレークポイントに頼るほかのすべてが、実機だけでなくエミュレーターでも動きます。
- **PS1 ゲーム:** Ember とその PS1 ゲームを仮想ドライブから動かして、起動と PS1 リストをテストできます。ドライブには自分の PS1 BIOS を置いてください。
- **自動化・AI 支援テスト：** スクリーンショット、録画、ステートセーブ、PINE によるメモリー読み取り付きのスクリプト実行を隠しデスクトップで行い、PC を乗っ取りません。

<a id="the-end-goal-the-whole-library"></a>

## 最終目標: ライブラリ全体

これからの最大の仕事は、PS2 のゲームをコンソールと同じように Open PS2 Loader 自身のコード経路でテストし、それぞれに何が必要かを書き留めることです。OPL のサンドボックスで ELF、KELF、homebrew アプリ、ゲームを動かし、互換モードを自動で試します。いつか誰かがこれでライブラリ全体を動かせるかもしれません。それが RIPPCSX2 の最終目標です。

Compatibility Report はその第一歩です。ゲームの結果、使った OPL モード、マシンの状態を、`reports/` にファイルとして、`compatibility.csv` に行として保存します。

<a id="for-ai-agents-llms-and-their-users"></a>

## AI エージェント、LLM とそのユーザーへ

このリポジトリは、エージェントがリンクだけでユーザーのセットアップを済ませられるように書かれています。アシスタントに `https://github.com/akilluminati47/RIPPCSX2` を渡して RIPPCSX2 のインストールを頼んでください。必要なものはすべてここにあります：

1. **ビルドを入手：** ローリングリリースから `RIPPCSX2-windows-x64-avx2.zip`（[直接リンク](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)、または `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`）。専用のフォルダーに展開します。`portable.txt` はすでに exe の隣にあるので、インストール済みの PCSX2 の設定に触れることはありません。
2. **BIOS：** ユーザー自身の本体の BIOS ダンプを使います（決してダウンロードしない）：exe の隣の `bios` フォルダーに置き（または `inis/PCSX2.ini` の `[Folders] Bios` をそこに向け）、初回起動ウィザードで選びます（`[Filenames] BIOS`）。
3. **何かを実行：** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`、または `-- <game.iso>`。設定は `inis/PCSX2.ini` のプレーンな INI で、ログは `logs/emulog.txt` に出ます（`[Logging] EnableEEConsole = true` で EE の printf も加わります）。
4. **操作して観察：** F8 スクリーンショット（`snaps/`）、F11 録画（`videos/`）、F1 ステートセーブ（`sstates/`）、スクリプトから PS2 のメモリーを読み書きする PINE（`[EmuCore] EnablePINE`、`PINESlot`）。
5. **画面を奪わずにテスト：** [`ripps2-lab/`](ripps2-lab/README.md) はラボ用インストールを説明しています（`install-lab.ps1` がビルドをポータブルフォルダーに置き、カード、設定、録画を保持）。RIPPS2 リポジトリの `tools/dev/ps2bg.ps1` は、ステップのリスト（ボタン、待機、スクリーンショット、録画）を隠しデスクトップで実行し、ユーザーが見たり止めたり引き継いだりできるタスクバーパネルを出します。

何がなぜ変わったかをファイルごとに：**[RIPPCSX2.md](RIPPCSX2.md)**。このフォークのコードで作業するエージェントへ：PCSX2 プロジェクトに pull request、issue、コメントを決して作らないこと（その `AGENTS.md` は AI が作った貢献を禁じています）。RIPPCSX2 はフォークのままです。

**PCSX2 チームとは無関係です。** PCSX2 と同じく GPL-3.0。RIPPCSX2 の問題は PCSX2 ではなく RIPPS2 に報告してください（[issues](https://github.com/akilluminati47/RIPPS2/issues)）。以下は PCSX2 自身の README です。

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 は無料でオープンソースの PlayStation 2（PS2）エミュレーターです。MIPS CPU の [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>)、[リコンパイラー](https://en.wikipedia.org/wiki/Dynamic_recompilation)、ハードウェアの状態と PS2 のシステムメモリーを管理する[仮想マシン](https://en.wikipedia.org/wiki/Virtual_machine)を組み合わせて PS2 のハードウェアをエミュレートすることを目的としています。これにより、PC で PS2 のゲームを、多くの追加機能と利点とともに遊べます。

<a id="project-details"></a>

## プロジェクトの詳細

PCSX2 は 20 年以上開発が続いています。昔のバージョンはパブリックドメインのゲームデモを少し動かせるだけでしたが、新しいバージョンは Final Fantasy X や Devil May Cry 3 などの人気タイトルを含むほとんどのゲームをフルスピードで動かせます。ゲームの最新の互換性状況は [PCSX2 互換性リスト](https://pcsx2.net/compat/)をご覧ください（2500 本以上のタイトルをテスト済み）。

安定版とナイトリー版のインストーラーとバイナリは [公式サイト](https://pcsx2.net/downloads/) から入手できます。

<a id="system-requirements"></a>

## 動作環境

PCSX2 は Windows、Linux、Mac に対応しています。ソフトウェアとハードウェアの要件の詳細は [セットアップのドキュメントページ](https://pcsx2.net/docs/setup/requirements) にあります。

エミュレーターを使うには、正規に所有する PS2 本体の BIOS ダンプが必要です。詳しくは [このページ](https://pcsx2.net/docs/setup/bios/) をご覧ください。

<a id="contributing--building"></a>

## 貢献 / ビルド

PCSX2 は [Crowdin](https://crowdin.com/project/pcsx2-emulator) でほかの言語に翻訳できます。

貢献の方法については [貢献ガイド](https://pcsx2.net/docs/contributing/) をご覧ください。

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">ダウンロード</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">テーマ</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">フォント</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">ウェブサイト</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

