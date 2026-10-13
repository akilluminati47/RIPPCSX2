# RIPPCSX2

The [RIPPS2](https://github.com/akilluminati47/RIPPS2) lab's PCSX2: **PCSX2 v2.9.96** (the build the lab ran) with one
change, **HDTV output**, so a test shows RIPPS2's 720p and 1080i the way an HDTV shows them. It lives on the
`rippcsx2` branch. An unofficial fork, not affiliated with the PCSX2 team; GPL-3.0 like PCSX2 (see `COPYING.GPLv3`).

## Why

RIPPS2 (and Open PS2 Loader) draw 720p into a 640 x 720 buffer and 1080i into 640 x 1080, and let the GS stretch
every line across 1280 or 1920 pixels (`DISPLAY.MAGH`). Stock PCSX2 knows the modes apart (`SMODE1.LC` 22, with or
without `SMODE2.INT`) but presents them as standard definition:

- in the default **Auto 4:3/3:2** aspect, only 480p counts as progressive (3:2); 720p and 1080i are drawn **4:3**;
- a **video capture** is the raw buffer stretched to the capture size and tagged 4:3: 640 x 480 with the lab's fixed
  size, or 1920 x 2160 (640 x 720 at 3x) with automatic resolution, which a reel then had to stretch by hand;
- a **screenshot** comes out at the window's size or the buffer's shape, never 1280 x 720 or 1920 x 1080.

So the lab tested HD themes in 480i with a 16:9 picture instead of the real thing.

## What changes: `[EmuCore/GS] HDTVOutput` (on by default)

In an HDTV mode (720p or 1080i), with `HDTVOutput = true`:

| | Stock PCSX2 | RIPPCSX2 |
|---|---|---|
| The window | 4:3 in Auto | **16:9** in every aspect setting except Stretch |
| Video capture | 640 x 480 (fixed) or the buffer x upscale, tagged 4:3 | **1280 x 720** or **1920 x 1080**, each frame stretched as the GS stretches it, tagged 16:9. With automatic resolution, that raster x the upscale multiplier (at most 3840 x 2160). A fixed size that is already 16:9 is kept. |
| A mode switch while recording | the file keeps its first size | once the new mode has held for half a second, the recording **goes on in a new file** at the new size (as PCSX2 already does after a reset) |
| Screenshots | window size or the buffer's shape | **1280 x 720** or **1920 x 1080** ("Internal Resolution (Aspect Uncorrected)" still saves the raw buffer) |
| Window Size presets | 4:3 widths | 16:9: 1x of 720p is 1280 x 720 |
| Where 1080i sits | moved up 42 lines: the top cut off, a black band at the bottom | from line 40, where the console's own 1080i timing starts the picture area |

Standard definition (NTSC, PAL, 480p, VESA) is untouched, and so is everything with `HDTVOutput = false`. There is
no switch in the settings dialogs yet: set it in `inis/PCSX2.ini`. The code is in
`pcsx2/GS/Renderers/Common/GSRenderer.cpp` (look for `RIPPCSX2`), `pcsx2/VMManager.cpp` and the option in
`pcsx2/Config.h` / `pcsx2/Pcsx2Config.cpp`. It needs proper testing beyond RIPPS2 and OPL.

## Testing themes with it (OPL, RiptOPL, RIPPS2)

1. Unzip a release, start `pcsx2-qt.exe` and point it at your own BIOS dump.
2. Boot the front end: System > Start File (`OPNPS2LD.ELF`, `RIPPS2.elf` ...), or `pcsx2-qt.exe -fastboot -elf <file>`.
3. Put the theme where the front end looks for themes: a `THM` folder holding `thm_<name>` folders on a device it
   reads. Under PCSX2 that is the internal HDD image (Settings > Network & HDD) or a network share through DEV9.
4. Pick the theme and set the front end's Video Mode to 720p or 1080i: the window turns 16:9 at once.
5. F8 saves a screenshot at 1280 x 720 or 1920 x 1080 (`snaps`), F11 records at that size (`videos`).

For a side-by-side with stock behaviour, set `HDTVOutput = false` under `[EmuCore/GS]` in `inis/PCSX2.ini`.
Releases are tagged `v2.9.96-rippcsx2.N`; a tag in that form keeps PCSX2's auto updater off, so a RIPPCSX2 build is
never offered stock PCSX2 as an update. Please report problems to RIPPS2 (its psx-place thread or GitHub issues),
not to the PCSX2 project.

## Checked in the lab (2026-10-13)

RIPPS2 v0.1.0 beta, RIPGRID, the same take (the grid, then a game's info page) in each mode, with the lab's
settings (fixed 640 x 480 capture, window-size screenshots):

| Mode | Stock v2.9.96: capture / screenshot | RIPPCSX2: capture / screenshot |
|---|---|---|
| 720p | 640 x 480 (4:3) / 1284 x 963 | **1280 x 720 (16:9) / 1280 x 720** |
| 1080i | 640 x 480 (4:3) / 1284 x 963 | **1920 x 1080 (16:9) / 1920 x 1080** |
| 480i | 640 x 480 (4:3) / 1284 x 963 | 640 x 480 (4:3) / 1284 x 963, byte for byte the same screenshots |

In 720p and 1080i the text and art now have their real proportions (stock showed them squeezed into 4:3), and
1080i's two fields come out combined with no combing. The first lab build still showed what stock does in 1080i:
the picture moved up 42 lines, its top cut off and a black band at the bottom. That is a PCSX2 bug. Its table of
where each mode's picture starts holds a per-field line for NTSC and PAL (25 and 36, doubled for interlace to 50 and
72) but already a frame line for 1080i (40), which the same doubling makes 80. The console's own 1080i timing, as
the BIOS sets it (SYNCV VS 10, VBPE 2, VBP 28, VDP 1080: 1125 lines), starts the picture area 40 lines after sync,
and gsKit places RIPPS2's 1080i picture at DY 38, so stock PCSX2 moved it 38 - 80 = -42 lines. With HDTVOutput on,
RIPPCSX2 counts 1080i from line 40 (`ModeStartLine` in `pcsx2/GS/GSState.cpp`); RIPPS2's picture then sits 2 lines
high, where gsKit really puts it. RIPPCSX2 logs the sync and display registers on every video mode change
("RIPPCSX2: video mode ..." in `logs/emulog.txt`). Commercial 1080i games are still to be checked against it.

The CI build's version reads 0.0.0.0: the checkout is shallow, so `git describe` cannot reach the v2.9.96 tag.

## Building

Pushing to `rippcsx2` runs **RIPPCSX2 lab build** (`.github/workflows/rippcsx2_build.yml`): PCSX2's own Windows
dependency and MSBuild jobs, one x64 AVX2 Release build, uploaded as the artifact `RIPPCSX2-windows-x64-avx2-...`.
The first run builds the dependencies (up to an hour and a half); later runs reuse them from the cache. Upstream's
Windows, Linux and macOS matrices skip this branch. To build by hand, follow PCSX2's
[build guide](https://pcsx2.net/docs/advanced/building/).

## Into the lab

`ripps2-lab/` describes the lab and installs a build into it: `ripps2-lab/install-lab.ps1 -Build <the artifact's
.zip or folder>` puts the new binaries in the lab's portable PCSX2 and keeps its settings, cards, captures and
save states. See `ripps2-lab/README.md`.

## About upstream

PCSX2's `AGENTS.md` asks that AI-generated changes never reach the PCSX2 project as pull requests, issues or
comments, and that a contributor be able to explain every change without AI help. RIPPCSX2 is made with Claude for
the RIPPS2 lab: it stays a fork and is never offered upstream as it is.
