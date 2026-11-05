# A private RIPPCSX2 for testing, away from a shared lab: its own folder, exe name, ini, cards and PINE slot, its hard disk off.
# private-copy.py <lab folder> <new folder> [build folder, default the lab]. The exe comes out as pcsx2-menutest.exe.
import os, re, shutil, sys
LAB = sys.argv[1]
OUT = sys.argv[2]
SRC = sys.argv[3] if len(sys.argv) > 3 else LAB
KEEP_OUT = {'inis', 'memcards', 'videos', 'snaps', 'sstates', 'cache', 'covers', 'logs', 'gamesettings', 'cheats', 'patches', 'inputprofiles', 'textures', 'debuggerlayouts', 'debuggersettings', 'reports', 'docs'}
os.makedirs(OUT, exist_ok=True)
for n in os.listdir(SRC):
    if n in KEEP_OUT or n.startswith('crash-') or n.endswith('.pdb'):
        continue
    a, b = os.path.join(SRC, n), os.path.join(OUT, n)
    if os.path.isdir(a):
        shutil.copytree(a, b, dirs_exist_ok=True)
    else:
        shutil.copy2(a, b)
exe = next((n for n in os.listdir(SRC) if re.fullmatch(r'pcsx2-qt(x64-avx2)?\.exe', n)), None)
newest = [n for n in os.listdir(SRC) if n == 'pcsx2-qtx64-avx2.exe'] or [exe]
shutil.copy2(os.path.join(SRC, newest[0]), os.path.join(OUT, 'pcsx2-menutest.exe'))
open(os.path.join(OUT, 'portable.txt'), 'a').close()
for d in ('inis', 'memcards', 'snaps', 'videos', 'logs', 'sstates'):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
for c in ('RIPPS2-CM1.ps2', 'RIPPS2-CM2.ps2'):
    if not os.path.exists(os.path.join(OUT, 'memcards', c)):
        shutil.copy2(os.path.join(LAB, 'memcards', c), os.path.join(OUT, 'memcards', c))
ini = open(os.path.join(LAB, 'inis', 'PCSX2.ini'), encoding='utf-8').read()
ini = re.sub(r'(?m)^PINESlot = .*$', 'PINESlot = 28013', ini)
ini = re.sub(r'(?m)^HddEnable = .*$', 'HddEnable = false', ini)
ini = re.sub(r'(?m)^HddFile = .*$', 'HddFile = ', ini)
ini = re.sub(r'(?m)^Slot1_Filename = .*$', 'Slot1_Filename = RIPPS2-CM1.ps2', ini)
ini = re.sub(r'(?m)^Slot2_Filename = .*$', 'Slot2_Filename = RIPPS2-CM2.ps2', ini)
open(os.path.join(OUT, 'inis', 'PCSX2.ini'), 'w', encoding='utf-8', newline='').write(ini)
print('ready', OUT, 'from', SRC, newest)
