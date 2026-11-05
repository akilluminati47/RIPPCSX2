<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.de.md">Deutsch</a> |
  <b>Italiano</b> |
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

<p align="center"><sub>Traduzione del README inglese; se differiscono, vale l’inglese. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Scarica</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temi</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sito</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Un emulatore PlayStation 2 per testare e sviluppare homebrew, fatto per essere guidato da te o da un agente IA.**

RIPPCSX2 è PCSX2 v2.9.96 con le modifiche che servono a uno sviluppatore di homebrew PS2 per vedere la realtà: modalità video HD mostrate, registrate e catturate come le mostra una TV HD, e il breakpoint hardware sui dati dell’EE, così i menu in gioco e gli strumenti di modalità video che si agganciano ai registri del GS (il GSM di Open PS2 Loader, il menu in gioco di RIPPS2) funzionano come su una console. Tutto il resto è PCSX2 puro. È nato come laboratorio di prova del front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) ed è pensato per chiunque crei homebrew, temi o strumenti per PS2.

**[Vedi il sito](https://akilluminati47.github.io/RIPPCSX2/)**: smonta una PS2 o falla esplodere, con tutto su RIPPCSX2 nel suo pannello Info.

<a id="download-rippcsx2-windows-ziphttpsgithubcomakilluminati47rippcsx2releaseslatestdownloadrippcsx2-windows-x64-avx2zip"></a>

### [Scarica RIPPCSX2 (zip per Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 o 11, x64, una CPU con AVX2. Estrailo dove vuoi, avvia `pcsx2-qtx64-avx2.exe` e indicagli il tuo dump del BIOS. Lo zip contiene un `portable.txt` vuoto accanto all’exe, quindi RIPPCSX2 tiene tutte le impostazioni e i file nella propria cartella: un PCSX2 già installato conserva le sue impostazioni, intatte. La release contiene sempre la build più recente ([la sua pagina](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)); le clip qui sotto sono in [docs/videos](docs/videos).

**Esegue programmi `.elf` per i test:** System > Start File, oppure `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, e il programma si avvia come farebbe da una memory card o da una chiavetta USB su una PS2. **Si comporta come l’hardware reale**: un ELF che avvia un altro ELF gli passa la macchina e sparisce, un menu in gioco che si aggancia al GS disegna sopra il vero fotogramma del gioco, e lo spegnimento chiude la VM come una console che si spegne.

<a id="see-it-work"></a>

## Guardalo all’opera

Ogni clip è una vera esecuzione del laboratorio su questa build, tagliata sotto i 12 secondi.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Un agente IA che testa un ELF.** Registrato dall’angolo in basso a destra dello schermo dell’utente (barra delle applicazioni, parte della sessione di Claude): Claude avvia `RIPPS2.elf` in RIPPCSX2 su un desktop nascosto, lancia Aqua Teen Hunger Force dall’immagine dell’HDD e ci apre sopra il menu in gioco di RIPPS2. Il pannellino è l’unica cosa sullo schermo; l’utente tiene tastiera e mouse.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Il menu in gioco, ogni funzione.** L1+L2+R1+R2+SELECT+START durante una partita: ACHIEVEMENTS, RESUME (il gioco continua), di nuovo il menu sopra un fotogramma successivo, poi POWER OFF, che chiude la VM. Il menu sa su quale fotogramma disegnare perché RIPPCSX2 emula il breakpoint di scrittura dati dell’EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Un ELF che avvia un ELF, come una vera PS2.** Memory Files di RIPPS2 apre `mc0:/RIPPS2/RIPPS2.ELF` (la build più recente, copiata sulla scheda) e lo esegue. Il RIPPS2 in esecuzione passa il controllo e sparisce; quello nuovo si carica dalla scheda e si avvia sulla sua lista dei giochi.

<a id="what-you-get-over-vanilla-pcsx2-v2996"></a>

## Cosa ottieni rispetto a PCSX2 v2.9.96 originale

- **Un menu RIPPCSX2** tra Debug e Help: Run ELF e Run Last ELF, un Lab Monitor in tempo reale, Test Steps, un Compatibility Report, gli interruttori del fork e le cartelle dove finisce tutto.
- **Un pulsante sulla barra delle applicazioni per le esecuzioni nascoste.** Un PCSX2 avviato su un desktop nascosto mette un pulsante sulla tua barra delle applicazioni, così un mixer del volume o una mod del volume per app lo raggiunge come qualsiasi altro programma.
- **Le modalità HD si vedono bene.** 720p e 1080i vengono mostrati in 16:9 (l’originale li disegna in 4:3), con ogni impostazione di formato tranne Stretch.
- **Registrazioni e screenshot in HD.** F11 registra il 720p a 1280 x 720 e il 1080i a 1920 x 1080 (o moltiplicato per l’upscale), etichettati 16:9; F8 salva screenshot alle stesse dimensioni. L’originale dà 640 x 480 o il buffer grezzo largo 640.
- **Un cambio di modalità durante la registrazione** continua in un nuovo file alla nuova dimensione, invece di schiacciarsi nel primo.
- **Il 1080i al posto giusto.** L’originale sposta in alto un’immagine 1080i di 42 righe (tagliata in alto, banda nera sotto); RIPPCSX2 la fa partire dalla riga 40, come fa la temporizzazione della console stessa.
- **Breakpoint di scrittura dati dell’EE** (nuovo in rippcsx2.2). Il COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) funziona: una scrittura su un indirizzo sorvegliato solleva l’eccezione di debug di livello 2 a `0x80000100` prima di essere eseguita, nell’interprete e nel ricompilatore. Il GSM di OPL e il menu in gioco di RIPPS2 ne hanno bisogno per sapere quale fotogramma mostra un gioco.
- **Righe di log della modalità video.** Ogni cambio di modalità registra la temporizzazione di sincronia e i registri di visualizzazione (`RIPPCSX2: video mode ...` in `logs/emulog.txt`).
- **Niente offerte dell’aggiornamento automatico.** I tag di release tengono spento l’aggiornamento di PCSX2, così non ti "aggiorna" mai di nuovo all’originale.
- La definizione standard resta intatta: gli screenshot a 480i sono identici byte per byte a quelli dell’originale. `HDTVOutput = false` sotto `[EmuCore/GS]` in `inis/PCSX2.ini` riporta il comportamento HD originale per un confronto.

<a id="what-it-is-for"></a>

## A cosa serve

- **Creatori di temi** (Open PS2 Loader, RiptOPL, RIPPS2): valuta un tema in 720p e 1080i come lo mostra una TV, e crea anteprime a grandezza reale e video dimostrativi.
- **Sviluppatori di homebrew:** testa ELF che cambiano modalità video, si agganciano al GS o usano i registri di debug dell’EE, e leggi nel log i registri di visualizzazione esatti che una modalità imposta.
- **Menu in gioco e strumenti per il GS:** il GSM di OPL, il menu in gioco di RIPPS2 e tutto ciò che si basa sul breakpoint di scrittura dati girano nell’emulatore invece che solo sull’hardware.
- **Test automatizzati e assistiti dall’IA:** esecuzioni scriptate su un desktop nascosto con screenshot, registrazioni, salvataggi di stato e letture di memoria via PINE, senza prendere il controllo del tuo PC.

<a id="the-end-goal-the-whole-library"></a>

## L'obiettivo finale: l'intera libreria

Il lavoro più grande che resta è testare i giochi PS2 attraverso il percorso di codice di Open PS2 Loader, come li esegue una console, e annotare ciò che serve a ciascuno: ELF, KELF, app homebrew e giochi in una sandbox OPL, provando automaticamente le sue modalità di compatibilità. Qualcuno potrebbe usarlo per far funzionare l'intera libreria un giorno. Questo è l'obiettivo finale di RIPPCSX2.

Il Compatibility Report è il primo passo: il risultato di un gioco, le modalità OPL usate e lo stato della macchina, salvati in `reports/` come file e come riga in `compatibility.csv`.

<a id="for-ai-agents-llms-and-their-users"></a>

## Per agenti IA, LLM e i loro utenti

Questo repository è scritto perché un agente possa configurare tutto per un utente partendo dal solo link. Dai al tuo assistente `https://github.com/akilluminati47/RIPPCSX2` e chiedigli di installare RIPPCSX2; tutto ciò che gli serve è qui:

1. **Prendi la build:** `RIPPCSX2-windows-x64-avx2.zip` dalla release continua ([link diretto](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), oppure `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Estrailo in una cartella tutta sua; il suo `portable.txt` è già accanto all’exe, quindi non tocca mai le impostazioni di un PCSX2 installato.
2. **BIOS:** l’utente fornisce il dump del BIOS della propria console (non scaricarne mai uno): mettilo nella cartella `bios` accanto all’exe (o punta `[Folders] Bios` in `inis/PCSX2.ini` verso di essa) e sceglilo nella procedura guidata del primo avvio (`[Filenames] BIOS`).
3. **Esegui qualcosa:** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, oppure `-- <game.iso>`. Le impostazioni sono semplici INI in `inis/PCSX2.ini`; i log vanno in `logs/emulog.txt` (`[Logging] EnableEEConsole = true` aggiunge il printf dell’EE).
4. **Guidalo e osservalo:** F8 screenshot (`snaps/`), F11 registrazione (`videos/`), F1 salvataggio di stato (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) per leggere e scrivere la memoria della PS2 da uno script.
5. **Testa senza rubare lo schermo:** [`ripps2-lab/`](ripps2-lab/README.md) descrive un’installazione da laboratorio (`install-lab.ps1` mette una build in una cartella portatile e ne conserva schede, impostazioni e registrazioni), e `tools/dev/ps2bg.ps1` del repository di RIPPS2 esegue elenchi di passi (tasti, attese, screenshot, registrazioni) su un desktop nascosto con un pannello nella barra delle applicazioni che l’utente può guardare, fermare o prendere in mano.

Cosa è cambiato e perché, file per file: **[RIPPCSX2.md](RIPPCSX2.md)**. Agenti che lavorano sul codice di questo fork: non aprite mai pull request, issue o commenti sul progetto PCSX2 (il suo `AGENTS.md` vieta i contributi fatti dall’IA); RIPPCSX2 resta un fork.

**Non affiliato al team di PCSX2.** GPL-3.0 come PCSX2. Segnala i problemi di RIPPCSX2 a RIPPS2 ([issue](https://github.com/akilluminati47/RIPPS2/issues)), mai a PCSX2. Segue il README di PCSX2.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 è un emulatore PlayStation 2 (PS2) libero e open source. Il suo scopo è emulare l’hardware della PS2 usando una combinazione di [Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) per CPU MIPS, [Ricompilatori](https://en.wikipedia.org/wiki/Dynamic_recompilation) e una [Macchina virtuale](https://en.wikipedia.org/wiki/Virtual_machine) che gestisce gli stati dell’hardware e la memoria di sistema della PS2. Così puoi giocare ai giochi PS2 sul tuo PC, con molte funzioni e vantaggi aggiuntivi.

<a id="project-details"></a>

## Dettagli del progetto

PCSX2 è in sviluppo da più di 20 anni. Le versioni passate potevano eseguire solo poche demo di pubblico dominio, mentre le più recenti eseguono la maggior parte dei giochi a piena velocità, compresi titoli popolari come Final Fantasy X e Devil May Cry 3. Visita la [lista di compatibilità di PCSX2](https://pcsx2.net/compat/) per lo stato di compatibilità più recente dei giochi (oltre 2500 titoli testati).

Installer e binari sia delle build stabili sia delle nightly sono disponibili sul [nostro sito](https://pcsx2.net/downloads/).

<a id="system-requirements"></a>

## Requisiti di sistema

PCSX2 supporta Windows, Linux e Mac. La nostra [pagina di documentazione sull’installazione](https://pcsx2.net/docs/setup/requirements) contiene altri dettagli sui requisiti software e hardware.

Tieni presente che per usare l’emulatore serve un dump del BIOS di una console PS2 posseduta legalmente. Per maggiori informazioni, visita [questa pagina](https://pcsx2.net/docs/setup/bios/).

<a id="contributing--building"></a>

## Contribuire / Compilare

PCSX2 supporta la traduzione in altre lingue tramite [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Consulta la [Guida per contribuire](https://pcsx2.net/docs/contributing/) per sapere come contribuire.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Scarica</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Temi</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Font</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Sito</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

