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
  <b>Türkçe</b> |
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

<p align="center"><sub>İngilizce README’nin çevirisi; farklılık olursa İngilizce geçerlidir. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">İndir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temalar</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Yazı tipleri</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web sitesi</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Homebrew test etmek ve geliştirmek için, sizin ya da bir yapay zekâ ajanının sürmesi için yapılmış bir PlayStation 2 emülatörü.**

RIPPCSX2, bir PS2 homebrew geliştiricisinin gerçeği görmek için ihtiyaç duyduğu değişikliklerle PCSX2 v2.9.96’dır: HD video modları bir HD televizyonun gösterdiği gibi gösterilir, kaydedilir ve ekran görüntüsü alınır, ayrıca EE’nin donanımsal veri kesme noktası vardır; böylece oyun içi menüler ve GS yazmaçlarına kanca atan video modu araçları (Open PS2 Loader’ın GSM’i, RIPPS2’nin oyun içi menüsü) bir konsoldaki gibi çalışır. Geri kalan her şey düz PCSX2’dir. [RIPPS2](https://github.com/akilluminati47/RIPPS2) ön ucunun test laboratuvarı olarak başladı ve PS2 için homebrew, tema ya da araç yapan herkes içindir.

**[Web sitesine bak](https://akilluminati47.github.io/RIPPCSX2/)**: bir PS2'yi sök ya da havaya uçur, RIPPCSX2 hakkındaki her şey Info panelinde.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [RIPPCSX2’yi indir (Windows zip)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 veya 11, x64, AVX2 destekli bir işlemci. İstediğiniz yere açın, `pcsx2-qtx64-avx2.exe` dosyasını başlatın ve kendi BIOS dökümünüzü gösterin. Zip, exe’nin yanında boş bir `portable.txt` taşır, bu yüzden RIPPCSX2 tüm ayarlarını ve dosyalarını kendi klasöründe tutar: zaten kurulu bir PCSX2 kendi ayarlarını korur, el değmeden. Sürüm her zaman en yeni derlemeyi içerir ([sayfası](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); aşağıdaki klipler [docs/videos](docs/videos) içinde.

<a id="download-rippcsx2-linux-appimagehttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-linux-x64appimage"></a>

### [RIPPCSX2 indir (Linux AppImage)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-linux-x64.AppImage)

x64, AVX2 destekli bir işlemci. Dosyayı çalıştırılabilir yapıp başlatın. Bu sürümde yeni ve Windows zip dosyasıyla aynı iş akışıyla derleniyor, ancak henüz bir Linux makinede çalıştırılmadı: nasıl gittiğini lütfen bize bildirin. Gizli çalıştırmalar için görev çubuğu düğmesi yalnızca Windows içindir.

**Test için `.elf` programları çalıştırır:** System > Start File ya da `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`; program, bir PS2’de hafıza kartından veya USB bellekten açılacağı gibi açılır. **Gerçek donanım gibi davranır**: başka bir ELF başlatan ELF makineyi ona devreder ve gider, GS’ye kanca atan bir oyun içi menü oyunun gerçek karesinin üstüne çizer, kapatmak da VM’yi kapanan bir konsol gibi kapatır.

<a id="see-it-work"></a>

## Çalışırken görün

Her klip, bu derlemede gerçek bir laboratuvar çalışmasıdır, 12 saniyenin altına kırpılmıştır.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Bir yapay zekâ ajanı bir ELF’i test ediyor.** Kullanıcının ekranının sağ alt köşesinden kaydedildi (görev çubuğu, Claude oturumunun bir parçası): Claude gizli bir masaüstünde RIPPCSX2 içinde `RIPPS2.elf` dosyasını başlatır, HDD görüntüsünden Aqua Teen Hunger Force’u açar ve üzerine RIPPS2’nin oyun içi menüsünü açar. Küçük panel ekrandaki tek şeydir; klavye ve fare kullanıcıda kalır.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Oyun içi menü, her işleviyle.** Çalışan bir oyunun üzerinde L1+L2+R1+R2+SELECT+START: ACHIEVEMENTS, RESUME (oyun sürer), daha sonraki bir karenin üstünde yine menü, ardından VM’yi kapatan POWER OFF. Menü hangi karenin üstüne çizeceğini bilir, çünkü RIPPCSX2 EE’nin veri yazma kesme noktasını öykünür.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**ELF başlatan bir ELF, gerçek bir PS2 gibi.** RIPPS2’nin Memory Files’ı `mc0:/RIPPS2/RIPPS2.ELF` dosyasını (karta kopyalanmış en yeni derleme) açar ve çalıştırır. Çalışan RIPPS2 devreder ve gider; yenisi karttan yüklenir ve oyun listesine kadar açılır.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Düz PCSX2 v2.9.96’ya göre ne kazanırsınız

- **Debug ile Help arasında bir RIPPCSX2 menüsü**: Run ELF ve Run Last ELF, canlı Lab Monitor, Test Steps, Compatibility Report, fork'un anahtarları ve her şeyin gittiği klasörler.
- **RIPART,** bu menüde: OPL Manager'ın görsel veritabanı, archive.org'daki yedeğinden bayt aralıklarıyla okunan 16.313 oyun. Sürücüde oyun olmadan bir temayı gerçek bir listede değerlendirmek için sahte oyun girdileri, bir oyunun her görsel parçasını tutmak ya da dışarıda bırakmak için onay kutulu bir liste, sürücüde kapağı olmayan oyunları bulan bir tarama ve hepsini koymak için bir ART klasörü ya da `art.tar`. Sahte girdiler OPL ve RIPPS2'de görünür ve başlamaz; var olan bir dosya asla değiştirilmez. akilluminati47 bu veritabanına 8 bit PNG görsellerini ve 128 x 128 disk simgelerini kazandırmaya yardım etti.
- **Orijinal OPL oyunları başlatır.** Bir programın kendisinin kaydettiği `host` aygıtı artık kendi açmalarını alıyor, bu yüzden OPL'in IOP yeniden başlatması çalışıyor. Orijinal sürüm `file 'host0:' can't open` hatasında durur.
- **EXIT GAME tarayıcıya ulaşır.** Bir SIO2 kesmesi IOP yeniden başlatmasında kayboluyordu ve OSDSYS siyah ekranda hafıza kartını bekliyordu.
- **Gizli çalıştırmalar için bir görev çubuğu düğmesi.** Gizli bir masaüstünde başlatılan PCSX2 görev çubuğuna bir düğme koyar, böylece ses karıştırıcı ya da uygulama başına ses modu ona diğer programlar gibi ulaşır.
- **HD modlar doğru görünür.** 720p ve 1080i, Stretch dışındaki her en-boy ayarında 16:9 gösterilir (orijinal onları 4:3 çizer).
- **HD kayıtlar ve ekran görüntüleri.** F11, 720p’yi 1280 x 720’de, 1080i’yi 1920 x 1080’de (ya da bunun ölçek katında) 16:9 etiketiyle kaydeder; F8 aynı boyutlarda ekran görüntüsü kaydeder. Orijinal 640 x 480 ya da 640 genişliğindeki ham arabelleği verir.
- **Kayıt ortasında mod değişimi** ilk dosyaya sıkışmak yerine yeni boyutta yeni bir dosyada sürer.
- **1080i doğru yerde.** Orijinal bir 1080i görüntüyü 42 satır yukarı kaydırır (üst kesik, altta siyah şerit); RIPPCSX2 onu konsolun kendi zamanlamasının yaptığı gibi 40. satırdan başlatır.
- **EE veri yazma kesme noktası** (rippcsx2.2’de yeni). COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) çalışır: izlenen bir adrese yapılan yazma, yürütülmeden önce `0x80000100` adresinde 2. düzey hata ayıklama istisnasını tetikler, hem yorumlayıcıda hem yeniden derleyicide. OPL GSM’i ve RIPPS2’nin oyun içi menüsü, bir oyunun hangi kareyi gösterdiğini öğrenmek için buna ihtiyaç duyar.
- **Video modu günlük satırları.** Her mod değişimi senkron zamanlamasını ve ekran yazmaçlarını günlüğe yazar (`logs/emulog.txt` içinde `RIPPCSX2: video mode ...`).
- **Otomatik güncelleyici teklifi yok.** Sürüm etiketleri PCSX2’nin güncelleyicisini kapalı tutar, böylece sizi asla orijinale geri "güncellemez".
- Standart çözünürlüğe dokunulmaz: 480i ekran görüntüleri orijinalinkilerle bayt bayt aynıdır. `inis/PCSX2.ini` içinde `[EmuCore/GS]` altındaki `HDTVOutput = false`, karşılaştırma için orijinal HD davranışını geri getirir.

<a id="what-it-is-for"></a>

## Ne işe yarar

- **Tema yapanlar** (Open PS2 Loader, RiptOPL, RIPPS2): bir temayı 720p ve 1080i’de bir televizyonun gösterdiği gibi değerlendirin, gerçek boyutlu önizlemeler ve tanıtım videoları yapın.
- **Homebrew geliştiricileri:** video modu değiştiren, GS’ye kanca atan ya da EE’nin hata ayıklama yazmaçlarını kullanan ELF’leri test edin ve bir modun ayarladığı ekran yazmaçlarını günlükte tam olarak okuyun.
- **Oyun içi menüler ve GS araçları:** OPL GSM’i, RIPPS2’nin oyun içi menüsü ve veri yazma kesme noktası üzerine kurulu her şey yalnızca donanımda değil emülatörde de çalışır.
- **PS1 oyunları:** başlatmayı ve PS1 listelerini denemek için Ember ve PS1 oyunlarını sanal sürücüden çalıştırın, sürücüde kendi PS1 BIOS dosyanız olsun.
- **Neutrino ve POPStarter:** Neutrino oyunları RIPPS2 üzerinden tam hızda çalıştırır. POPStarter PS1 oyunlarını yalnızca EE yeniden derleyicisi kapalıyken başlatır, şimdilik yaklaşık yarı hızda ve bozuk grafiklerle; yeniden derleyici açıkken siyah ekranda kalır.
- **Otomatik ve yapay zekâ destekli test:** gizli bir masaüstünde ekran görüntüleri, kayıtlar, kayıt durumları ve PINE bellek okumalarıyla betikli çalıştırmalar, bilgisayarınızı ele geçirmeden.

<a id="the-end-goal-the-whole-library"></a>

## Nihai hedef: tüm kütüphane

Önümüzdeki en büyük iş, PS2 oyunlarını Open PS2 Loader'ın kendi kod yolundan, bir konsolun çalıştırdığı gibi test etmek ve her birinin neye ihtiyaç duyduğunu yazmaktır: bir OPL korumalı alanında ELF'ler, KELF'ler, homebrew uygulamaları ve oyunlar, uyumluluk modları otomatik olarak denenerek. Biri bir gün bunu kullanarak tüm kütüphaneyi çalıştırabilir. RIPPCSX2'nin nihai hedefi budur.

Compatibility Report ilk adımdır: bir oyunun sonucu, kullanılan OPL modları ve makinenin durumu, `reports/` içine bir dosya ve `compatibility.csv` içine bir satır olarak kaydedilir.

<a id="for-ai-agents-llms-and-their-users"></a>

## Yapay zekâ ajanları, LLM’ler ve kullanıcıları için

Bu depo, bir ajanın yalnızca bağlantıdan yola çıkarak bir kullanıcının kurulumunu yapabileceği şekilde yazıldı. Asistanınıza `https://github.com/akilluminati47/RIPPCSX2` adresini verin ve RIPPCSX2’yi kurmasını isteyin; ihtiyaç duyduğu her şey burada:

1. **Derlemeyi alın:** sürekli sürümden `RIPPCSX2-windows-x64-avx2.zip` ([doğrudan bağlantı](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip) ya da `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Kendine ait bir klasöre açın; `portable.txt` zaten exe’nin yanında, böylece kurulu bir PCSX2’nin ayarlarına asla dokunmaz.
2. **BIOS:** kullanıcı kendi konsolunun BIOS dökümünü sağlar (asla indirmeyin): exe’nin yanındaki `bios` klasörüne koyun (ya da `inis/PCSX2.ini` içindeki `[Folders] Bios` ayarını oraya yöneltin) ve ilk çalıştırma sihirbazında seçin (`[Filenames] BIOS`).
3. **Bir şey çalıştırın:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>` ya da `-- <game.iso>`. Ayarlar `inis/PCSX2.ini` içinde düz INI’dir; günlükler `logs/emulog.txt` dosyasına gider (`[Logging] EnableEEConsole = true` EE’nin printf’ini ekler).
4. **Sürün ve gözlemleyin:** F8 ekran görüntüsü (`snaps/`), F11 kayıt (`videos/`), F1 kayıt durumu (`sstates/`), bir betikten PS2 belleğini okuyup yazmak için PINE (`[EmuCore] EnablePINE`, `PINESlot`).
5. **Ekranı çalmadan test edin:** [`ripps2-lab/`](ripps2-lab/README.md) bir laboratuvar kurulumunu anlatır (`install-lab.ps1` bir derlemeyi taşınabilir bir klasöre koyar ve kartlarını, ayarlarını ve kayıtlarını tutar), RIPPS2 deposundaki `tools/dev/ps2bg.ps1` de adım listelerini (tuşlar, beklemeler, ekran görüntüleri, kayıtlar) gizli bir masaüstünde, kullanıcının izleyebileceği, durdurabileceği ya da devralabileceği bir görev çubuğu paneliyle çalıştırır.

Neyin değiştiği ve neden, dosya dosya: **[RIPPCSX2.md](RIPPCSX2.md)**. Bu fork’un kodu üzerinde çalışan ajanlar: PCSX2 projesinde asla pull request, issue ya da yorum açmayın (onun `AGENTS.md` dosyası yapay zekâ yapımı katkıları yasaklar); RIPPCSX2 bir fork olarak kalır.

**PCSX2 ekibiyle bağlantısı yoktur.** PCSX2 gibi GPL-3.0. RIPPCSX2 sorunlarını PCSX2’ye değil, RIPPS2’ye bildirin ([issues](https://github.com/akilluminati47/RIPPS2/issues)). Ardından PCSX2’nin kendi README’si gelir.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2, ücretsiz ve açık kaynaklı bir PlayStation 2 (PS2) emülatörüdür. Amacı, MIPS işlemci [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>), [Yeniden derleyiciler](https://en.wikipedia.org/wiki/Dynamic_recompilation) ve donanım durumlarını ve PS2 sistem belleğini yöneten bir [Sanal makine](https://en.wikipedia.org/wiki/Virtual_machine) birleşimiyle PS2’nin donanımını öykünmektir. Bu sayede PS2 oyunlarını bilgisayarınızda, pek çok ek özellik ve avantajla oynayabilirsiniz.

<a id="project-details"></a>

## Proje ayrıntıları

PCSX2 20 yılı aşkın süredir geliştiriliyor. Eski sürümler yalnızca birkaç kamu malı oyun demosunu çalıştırabiliyordu, yeni sürümler ise Final Fantasy X ve Devil May Cry 3 gibi popüler oyunlar dahil çoğu oyunu tam hızda çalıştırabiliyor. Oyunların en güncel uyumluluk durumu için [PCSX2 uyumluluk listesini](https://pcsx2.net/compat/) ziyaret edin (2500’den fazla oyun test edildi).

Kararlı ve nightly derlemelerin kurulum dosyaları ve ikili dosyaları [web sitemizde](https://pcsx2.net/downloads/) bulunur.

<a id="system-requirements"></a>

## Sistem gereksinimleri

PCSX2 Windows, Linux ve Mac’i destekler. [Kurulum belgeleri sayfamız](https://pcsx2.net/docs/setup/requirements) yazılım ve donanım gereksinimleriyle ilgili ek ayrıntılar içerir.

Emülatörü kullanmak için yasal olarak sahip olunan bir PS2 konsolundan alınmış BIOS dökümünün gerektiğini unutmayın. Daha fazla bilgi için [bu sayfayı](https://pcsx2.net/docs/setup/bios/) ziyaret edin.

<a id="contributing--building"></a>

## Katkı / Derleme

PCSX2, [Crowdin](https://crowdin.com/project/pcsx2-emulator) üzerinden diğer dillere çevrilebilir.

Nasıl katkıda bulunacağınızı öğrenmek için [Katkı Kılavuzu](https://pcsx2.net/docs/contributing/)’na bakın.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">İndir</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temalar</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Yazı tipleri</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Web sitesi</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

