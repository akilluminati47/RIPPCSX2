# The RIPPS2 lab

RIPPS2's tests run in a portable PCSX2 of their own, never the player's: `B:\Emulation\PlayStation\PCSX2\ripps2-lab`
on the RIPPS2 machine. RIPPCSX2 is the PCSX2 inside it.

## Layout

```
ripps2-lab\
  pcsx2-qt.exe, *.dll, resources\ ...   the RIPPCSX2 build (install-lab.ps1 replaces these)
  portable.txt                          keeps PCSX2's settings and data in this folder
  inis\PCSX2.ini                        the lab's settings (lab-settings.ini lists what matters)
  memcards\RIPPS2-*.ps2                 lab cards only: CM1 and CM2 in the slots, REEL for reel takes
  videos\  snaps\  sstates\  logs\      captures (F11 / "rec"), screenshots (F8 / "shot"), save states, logs
```

The BIOS comes from `B:\Emulation\PlayStation\PCSX2\bios`, the internal HDD from an image under `ripps2-test`, and
RIPPS2 itself is started as an ELF from `ripps2-test\tNNN\RIPPS2.elf`.

## Driving it

The RIPPS2 repo's `tools/dev/ps2bg.ps1` starts the lab PCSX2 on its own hidden desktop (it never takes the focus),
runs a step list (`wait:5`, `cross`, `square`, `rec`, `shot` ...) through PINE on port **28012**, and closes it.
`rec` toggles the video capture; under RIPPCSX2 a capture made while RIPPS2 is in 720p or 1080i comes out at
1280 x 720 or 1920 x 1080, and a mode change mid-take continues in a new file (the newest file is the HD one).

## Testing HD

1. Install the build: `.\install-lab.ps1 -Build <RIPPCSX2-windows-x64-avx2 ... .zip>` (the lab PCSX2 must be closed).
2. Set RIPPS2's video mode on the take's card settings: `vmode=10` is 720p, `vmode=11` is 1080i (RIPPS2's
   `rm_mode_table` order).
3. `rec` after the first frame (about 6 s under ps2bg) and `shot` where a look should be checked.

Keep `HDTVOutput = true` in `[EmuCore/GS]` (it is the default). `deinterlace_mode = 0` (automatic) suits 1080i.

## Installing by hand

Unzip the artifact over the lab folder **except** `inis\`, `memcards\`, `videos\`, `snaps\`, `sstates\`, `cache\`,
`covers\`, `logs\`, `gamesettings\`, `cheats\`, `patches\`, `inputprofiles\`, `textures\` and `portable.txt`, then
name the executable `pcsx2-qt.exe` (the lab's driver starts that name).
