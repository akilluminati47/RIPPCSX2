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

The RIPPS2 repo's `tools/dev/ps2bg.ps1` is a script, not a PCSX2 feature, and works with any `pcsx2-qt.exe` in
the lab folder, stock or RIPPCSX2. It makes a second Windows desktop, `RIPPS2LAB`, that is never shown, starts the
lab PCSX2 there (`-fastboot -elf <RIPPS2.elf>`, minimized and never activated), and runs a step list (`wait:5`,
`cross`, `square`, `rec`, `shot` ...) by posting the `[Pad1]` keyboard bindings as window messages straight to
PCSX2's window, so the real keyboard, mouse and focus stay with whoever is using the PC. `grab` copies the window
with PrintWindow, `rec` and `shot` post F11 (video capture) and F8 (screenshot). At the end it closes PCSX2.
(PINE is on, port **28012**, for tools that read the PS2's memory; the driver does not use it.)

A hidden run is not out of sight: for the whole run a small **"RIPPS2 lab: AI run"** window sits on the user's
taskbar (bottom right), shown without taking the focus. It says which step the run is on, previews the hidden screen
once a second, and has two buttons:

- **Take over** finishes any recording, saves a state (F1), closes the hidden PCSX2 and opens PCSX2 on your own
  desktop at that state, so you play on by hand from where the run was.
- **Stop run** ends the run and closes the hidden PCSX2. Closing the window does the same.

The hidden PCSX2 is tied to the run's process, so ending the run in Task Manager closes it too. (`-NoPanel` leaves
the window out; `-Keep`, which leaves PCSX2 running for a later `-Attach`, is not tied.)

## Playing it yourself

The lab PCSX2 is an ordinary PCSX2 when you start it: open `pcsx2-qt.exe` in the lab folder (or boot RIPPS2 with
`pcsx2-qt.exe -fastboot -elf <RIPPS2.elf>`) and it opens a normal window on your desktop. The pad is bound to an
XInput controller, an SDL controller and the keyboard at once, so a controller just works. Close it when done; a
hidden run needs the lab PCSX2 closed.

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
