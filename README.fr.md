<!-- i18n: the language bar, made by ps2-pillars tools/readme-i18n -->
<p align="center">
  <a href="README.md">English</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.pt-BR.md">Português (Brasil)</a> |
  <a href="README.pt.md">Português</a> |
  <b>Français</b> |
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
  <a href="README.id.md">Bahasa Indonesia</a> |
  <a href="README.fil.md">Filipino</a> |
  <a href="README.ceb.md">Cebuano</a>
</p>
<!-- /i18n -->

<p align="center"><sub>Traduction du README anglais ; en cas de différence, l’anglais fait foi. <a href="README.md">English</a></sub></p>

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Télécharger</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thèmes</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Polices</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

# RIPPCSX2

**Un émulateur PlayStation 2 pour tester et développer du homebrew, fait pour être piloté par vous ou par un agent d’IA.**

RIPPCSX2, c’est PCSX2 v2.9.96 avec les changements dont un développeur de homebrew PS2 a besoin pour voir le vrai résultat : les modes vidéo HD affichés, enregistrés et capturés comme une TV HD les montre, et le point d’arrêt de données matériel de l’EE, pour que les menus en jeu et les outils de mode vidéo qui interceptent les registres du GS (le GSM d’Open PS2 Loader, le menu en jeu de RIPPS2) fonctionnent comme sur une console. Tout le reste, c’est PCSX2 tel quel. Il est né comme banc d’essai du front end [RIPPS2](https://github.com/akilluminati47/RIPPS2) et s’adresse à tous ceux qui créent du homebrew, des thèmes ou des outils pour PS2.

### [Télécharger RIPPCSX2 (zip Windows)](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip)

Windows 10 ou 11, x64, un processeur avec AVX2. Décompressez-le n’importe où, lancez `pcsx2-qtx64-avx2.exe` et indiquez-lui votre propre dump de BIOS. Le zip contient un `portable.txt` vide à côté de l’exe, donc RIPPCSX2 garde tous ses réglages et fichiers dans son propre dossier : un PCSX2 déjà installé conserve ses réglages, intacts. La version contient toujours la build la plus récente ([sa page](https://github.com/akilluminati47/RIPPCSX2/releases/tag/rolling)) ; les clips ci-dessous sont dans [docs/videos](docs/videos).

**Il lance des programmes `.elf` pour les tester :** System > Start File, ou `pcsx2-qtx64-avx2.exe -fastboot -elf <your.elf>`, et le programme démarre comme il le ferait depuis une carte mémoire ou une clé USB sur une PS2. Il **se comporte comme le vrai matériel** : un ELF qui lance un autre ELF lui passe la main et disparaît, un menu en jeu qui intercepte le GS se dessine par-dessus la vraie image du jeu, et éteindre ferme la VM comme une console qu’on éteint.

## Le voir à l’œuvre

Chaque clip est une vraie session du labo sur cette build, coupée à moins de 12 secondes.

![Claude runs a RIPPS2 test in RIPPCSX2 on a hidden desktop, watched from the taskbar panel](docs/rippcsx2-ai-test.gif)

**Un agent d’IA qui teste un ELF.** Enregistré depuis le coin inférieur droit de l’écran de l’utilisateur (barre des tâches, une partie de la session Claude) : Claude lance `RIPPS2.elf` dans RIPPCSX2 sur un bureau caché, démarre Aqua Teen Hunger Force depuis l’image du HDD et ouvre par-dessus le menu en jeu de RIPPS2. Le petit panneau est la seule chose à l’écran ; l’utilisateur garde le clavier et la souris.

![RIPPS2's in-game menu in RIPPCSX2: achievements, resume, menu again, power off](docs/rippcsx2-igr-menu.gif)

**Le menu en jeu, toutes ses fonctions.** L1+L2+R1+R2+SELECT+START pendant une partie : ACHIEVEMENTS, RESUME (le jeu continue), le menu à nouveau sur une image plus tardive, puis POWER OFF, qui ferme la VM. Le menu sait sur quelle image se dessiner parce que RIPPCSX2 émule le point d’arrêt d’écriture de données de l’EE.

![RIPPS2 running a newer RIPPS2.elf from the memory card in RIPPCSX2](docs/rippcsx2-elf-launch.gif)

**Un ELF qui lance un ELF, comme une vraie PS2.** Memory Files de RIPPS2 ouvre `mc0:/RIPPS2/RIPPS2.ELF` (la build la plus récente, copiée sur la carte) et l’exécute. Le RIPPS2 en cours passe la main et disparaît ; le nouveau se charge depuis la carte et démarre sur sa liste de jeux.

## Ce que vous gagnez par rapport à PCSX2 v2.9.96 d’origine

- **Les modes HD s’affichent correctement.** Le 720p et le 1080i sont affichés en 16:9 (l’original les dessine en 4:3), avec tous les réglages de format sauf Stretch.
- **Enregistrements et captures en HD.** F11 enregistre le 720p en 1280 x 720 et le 1080i en 1920 x 1080 (ou multiplié par la mise à l’échelle), étiquetés 16:9 ; F8 enregistre des captures aux mêmes tailles. L’original donne du 640 x 480 ou le tampon brut de 640 de large.
- **Un changement de mode en cours d’enregistrement** continue dans un nouveau fichier à la nouvelle taille, au lieu d’être tassé dans le premier.
- **Le 1080i au bon endroit.** L’original remonte une image 1080i de 42 lignes (haut coupé, bande noire en bas) ; RIPPCSX2 la commence à la ligne 40, là où le fait la synchronisation de la console elle-même.
- **Point d’arrêt d’écriture de données de l’EE** (nouveau dans rippcsx2.2). Le COP0 `$24` (`MTBPC`, `MTDAB`, `MTDABM` ...) fonctionne : une écriture à une adresse surveillée lève l’exception de débogage de niveau 2 à `0x80000100` avant de s’exécuter, dans l’interpréteur comme dans le recompilateur. Le GSM d’OPL et le menu en jeu de RIPPS2 en ont besoin pour savoir quelle image un jeu affiche.
- **Lignes de journal du mode vidéo.** Chaque changement de mode journalise la synchronisation et les registres d’affichage (`RIPPCSX2: video mode ...` dans `logs/emulog.txt`).
- **Pas de propositions du programme de mise à jour.** Les étiquettes de version laissent la mise à jour de PCSX2 désactivée, il ne vous « met donc jamais à jour » vers l’original.
- La définition standard est intacte : les captures en 480i sont identiques octet pour octet à celles de l’original. `HDTVOutput = false` sous `[EmuCore/GS]` dans `inis/PCSX2.ini` rétablit le comportement HD d’origine pour comparer.

## À quoi il sert

- **Créateurs de thèmes** (Open PS2 Loader, RiptOPL, RIPPS2) : jugez un thème en 720p et 1080i comme une TV l’affiche, et faites des aperçus en taille réelle et des vidéos de présentation.
- **Développeurs de homebrew :** testez des ELF qui changent de mode vidéo, interceptent le GS ou utilisent les registres de débogage de l’EE, et lisez dans le journal les valeurs d’affichage exactes qu’un mode définit.
- **Menus en jeu et outils GS :** le GSM d’OPL, le menu en jeu de RIPPS2 et tout ce qui repose sur le point d’arrêt d’écriture de données tournent dans l’émulateur et plus seulement sur le matériel.
- **Tests automatisés et assistés par IA :** des sessions scriptées sur un bureau caché avec captures, enregistrements, états de sauvegarde et lectures mémoire via PINE, sans prendre le contrôle de votre PC.

## Pour les agents d’IA, les LLM et leurs utilisateurs

Ce dépôt est écrit pour qu’un agent puisse tout installer pour un utilisateur à partir du seul lien. Donnez à votre assistant `https://github.com/akilluminati47/RIPPCSX2` et demandez-lui d’installer RIPPCSX2 ; tout ce dont il a besoin est ici :

1. **Récupérer la build :** `RIPPCSX2-windows-x64-avx2.zip` depuis la version continue ([lien direct](https://github.com/akilluminati47/RIPPCSX2/releases/latest/download/RIPPCSX2-windows-x64-avx2.zip), ou `gh release download rolling -R akilluminati47/RIPPCSX2 -p "*.zip"`). Décompressez-le dans un dossier à lui ; son `portable.txt` est déjà à côté de l’exe, il ne touche donc jamais aux réglages d’un PCSX2 installé.
2. **BIOS :** l’utilisateur fournit le dump de BIOS de sa propre console (n’en téléchargez jamais) : mettez-le dans le dossier `bios` à côté de l’exe (ou pointez `[Folders] Bios` dans `inis/PCSX2.ini` vers lui) et choisissez-le dans l’assistant du premier lancement (`[Filenames] BIOS`).
3. **Lancer quelque chose :** `pcsx2-qtx64-avx2.exe -fastboot -elf <homebrew.elf>`, ou `-- <game.iso>`. Les réglages sont de simples INI dans `inis/PCSX2.ini` ; les journaux vont dans `logs/emulog.txt` (`[Logging] EnableEEConsole = true` ajoute le printf de l’EE).
4. **Le piloter et l’observer :** F8 capture d’écran (`snaps/`), F11 enregistrement (`videos/`), F1 état de sauvegarde (`sstates/`), PINE (`[EmuCore] EnablePINE`, `PINESlot`) pour lire et écrire la mémoire de la PS2 depuis un script.
5. **Tester sans voler l’écran :** [`ripps2-lab/`](ripps2-lab/README.md) décrit une installation de labo (`install-lab.ps1` place une build dans un dossier portable et conserve ses cartes, réglages et enregistrements), et `tools/dev/ps2bg.ps1` du dépôt RIPPS2 exécute des listes d’étapes (boutons, attentes, captures, enregistrements) sur un bureau caché avec un panneau dans la barre des tâches que l’utilisateur peut regarder, arrêter ou reprendre en main.

Ce qui a changé et pourquoi, fichier par fichier : **[RIPPCSX2.md](RIPPCSX2.md)**. Agents qui travaillent sur le code de ce fork : n’ouvrez jamais de pull requests, d’issues ou de commentaires sur le projet PCSX2 (son `AGENTS.md` interdit les contributions faites par IA) ; RIPPCSX2 reste un fork.

**Sans lien avec l’équipe PCSX2.** GPL-3.0 comme PCSX2. Signalez les problèmes de RIPPCSX2 à RIPPS2 ([issues](https://github.com/akilluminati47/RIPPS2/issues)), jamais à PCSX2. Le README propre à PCSX2 suit.

# PCSX2

![Windows Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/windows_build_matrix.yml?label=%F0%9F%96%A5%EF%B8%8F%20Windows%20Builds)
![Linux Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/linux_build_matrix.yml?label=%F0%9F%90%A7%20Linux%20Builds)
![MacOS Build Status](https://img.shields.io/github/actions/workflow/status/PCSX2/pcsx2/macos_build_matrix.yml?label=%F0%9F%8D%8E%20MacOS%20Builds)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1f7c0d75fec74d6daa6adb084e5b4f71)](https://app.codacy.com/gh/PCSX2/pcsx2/dashboard?utm_source=github.com&utm_medium=referral&utm_content=PCSX2/pcsx2&utm_campaign=Badge_Grade)
[![Discord Server](https://img.shields.io/discord/309643527816609793?color=%235CA8FA&label=PCSX2%20Discord&logo=discord&logoColor=white)](https://discord.com/invite/TCz3t9k)

PCSX2 est un émulateur PlayStation 2 (PS2) libre et open source. Son but est d’émuler le matériel de la PS2, à l’aide d’une combinaison d’[Interpreters](<https://en.wikipedia.org/wiki/Interpreter_(computing)>) de processeur MIPS, de [Recompilateurs](https://en.wikipedia.org/wiki/Dynamic_recompilation) et d’une [Machine virtuelle](https://en.wikipedia.org/wiki/Virtual_machine) qui gère les états du matériel et la mémoire système de la PS2. Cela vous permet de jouer aux jeux PS2 sur votre PC, avec de nombreuses fonctions et avantages supplémentaires.

## Détails du projet

PCSX2 est en développement depuis plus de 20 ans. Les anciennes versions ne pouvaient lancer que quelques démos du domaine public, mais les plus récentes font tourner la plupart des jeux à pleine vitesse, y compris des titres populaires comme Final Fantasy X et Devil May Cry 3. Consultez la [liste de compatibilité de PCSX2](https://pcsx2.net/compat/) pour connaître l’état de compatibilité le plus récent des jeux (plus de 2500 titres testés).

Les installateurs et binaires des versions stables et nightly sont disponibles sur [notre site](https://pcsx2.net/downloads/).

## Configuration requise

PCSX2 fonctionne sous Windows, Linux et Mac. Notre [page de documentation d’installation](https://pcsx2.net/docs/setup/requirements) donne plus de détails sur la configuration logicielle et matérielle requise.

Notez qu’un dump de BIOS d’une console PS2 acquise légalement est nécessaire pour utiliser l’émulateur. Pour en savoir plus, consultez [cette page](https://pcsx2.net/docs/setup/bios/).

## Contribuer / Compiler

PCSX2 peut être traduit dans d’autres langues grâce à [Crowdin](https://crowdin.com/project/pcsx2-emulator).

Consultez le [Guide de contribution](https://pcsx2.net/docs/contributing/) pour savoir comment contribuer.

<p align="center"><sub><a href="https://github.com/akilluminati47/RIPPS2">RIPPS2</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2/releases/latest/download/RIPPS2.elf">Télécharger</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/BIBLE">BIBLE</a> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-themes">Thèmes</a> &nbsp;&middot;&nbsp; <b>RIPPCSX2</b> &nbsp;&middot;&nbsp; <a href="https://github.com/akilluminati47/RIPPS2-fonts">Polices</a> &nbsp;&middot;&nbsp; <a href="https://akilluminati47.github.io/RIPPS2/">Site web</a> &nbsp;&middot;&nbsp; <a href="https://www.psx-place.com/threads/ripps2-a-ps2-front-end-in-one-elf-launch-disc-storage-memory-files.51316/">psx-place</a> &nbsp;&middot;&nbsp; <a href="https://discord.gg/Z7m9u5kby">Discord</a></sub></p>

