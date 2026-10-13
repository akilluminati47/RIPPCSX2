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

Standard definition (NTSC, PAL, 480p, VESA) is untouched, and so is everything with `HDTVOutput = false`. There is
no switch in the settings dialogs yet: set it in `inis/PCSX2.ini`. The code is in
`pcsx2/GS/Renderers/Common/GSRenderer.cpp` (look for `RIPPCSX2`), `pcsx2/VMManager.cpp` and the option in
`pcsx2/Config.h` / `pcsx2/Pcsx2Config.cpp`. It needs proper testing beyond RIPPS2 and OPL.

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
