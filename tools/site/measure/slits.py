# The same five slits seen from every camera that can see them: are they level, and at what height?
import json, numpy as np
from PIL import Image
from camfit import rect
cams = json.load(open('refs/cams.json'))
def v(cam, fn, u0, u1, z0, z1, ppm=14.0):
    c = cams[cam]
    rect(np.array(c['P']), c['src'], 'e_a.png', fn, u0, u1, z0, z1, ppm=ppm, flipu=False)
    return np.median(np.asarray(Image.open('e_a.png').convert('L'), dtype=float), axis=1)
def slits(cam, fn, u0, u1, z0=30, z1=78, dark=30, white=None):
    a = v(cam, fn, u0, u1, z0, z1)
    dz = (z1 - z0) / len(a)
    out = []; st = None
    test = (lambda x: x > 200) if white else (lambda x: x < dark)
    # the sheets carry grid lines every 10 mm: skip single-row blips
    rows = [test(x) for x in a]
    i = 0
    while i < len(rows):
        if rows[i]:
            j = i
            while j + 1 < len(rows) and (rows[j + 1] or (j + 2 < len(rows) and rows[j + 2])):
                j += 1
            h = (j - i + 1) * dz
            if h >= 1.2:
                out.append('%.1f-%.1f' % (z1 - i * dz, z1 - (j + 1) * dz))
            i = j + 1
        else:
            i += 1
    return '  '.join(out)
F = lambda y: (lambda u, w: (u, y, w))
X = lambda x: (lambda u, w: (x, u, w))
print('front plane, FL camera')
for x0, x1 in ((6, 16), (66, 72), (120, 135), (150, 165), (185, 200), (230, 250), (262, 272)):
    print('  X %3d-%3d' % (x0, x1), slits('fat_FL', F(0), x0, x1))
print('front plane, third camera')
for x0, x1 in ((6, 16), (66, 72), (120, 135), (150, 165), (185, 200), (230, 250), (262, 272)):
    print('  X %3d-%3d' % (x0, x1), slits('fat_FR', F(0), x0, x1))
print('right end, FL camera')
for y0, y1 in ((10, 20), (30, 45), (60, 80), (100, 120), (140, 160), (165, 178)):
    print('  Y %3d-%3d' % (y0, y1), slits('fat_FL', X(301), y0, y1))
print('right end, third camera')
for y0, y1 in ((10, 20), (30, 45), (60, 80), (100, 120), (140, 160)):
    print('  Y %3d-%3d' % (y0, y1), slits('fat_FR', X(301), y0, y1))
print('rear plane notches, rear camera (white)')
for x0, x1 in ((299.4, 300.6), (298.6, 299.6)):
    print('  X %.1f-%.1f' % (x0, x1), slits('fat_back', F(182), x0, x1, white=True))
