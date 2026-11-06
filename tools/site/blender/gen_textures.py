# The surface textures the consoles use, all generated here (no photographs): python tools/site/blender/gen_textures.py
# The boards are drawn from where the chips sit on a real SCPH-3xxxx and SCPH-7xxxx, not traced from any picture.
import math
import random
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent / 'textures'
OUT.mkdir(exist_ok=True)
FONT = 'C:/Windows/Fonts/arial.ttf'


def tile_noise(n, blur, seed):
    r = np.random.default_rng(seed).normal(size=(n, n))
    f = np.fft.fft2(r)
    fx = np.fft.fftfreq(n)[:, None]
    fy = np.fft.fftfreq(n)[None, :]
    f *= np.exp(-2 * (math.pi * blur) ** 2 * (fx ** 2 + fy ** 2))
    a = np.real(np.fft.ifft2(f))
    return (a - a.mean()) / a.std()


def normal_from_height(h, strength):
    dx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) * strength
    dy = (np.roll(h, -1, 0) - np.roll(h, 1, 0)) * strength
    nz = np.ones_like(h)
    ln = np.sqrt(dx * dx + dy * dy + nz * nz)
    return np.uint8(np.stack([(-dx / ln + 1) * 127.5, (dy / ln + 1) * 127.5, (nz / ln + 1) * 127.5], axis=-1))


def normals():
    # the fat's lid: a fine woven hatch you only see close up
    n = 256
    y, x = np.mgrid[0:n, 0:n] / n
    k = 2 * math.pi * 24
    h = 0.5 * np.sin(k * (x + y)) * np.sin(k * (x - y)) + 0.35 * tile_noise(n, 1.2, 1)
    Image.fromarray(normal_from_height(h, 0.28)).save(OUT / 'hatch_n.png')
    # the slim's lid: an even stipple
    h = tile_noise(n, 1.1, 2) + 0.6 * tile_noise(n, 2.4, 3)
    Image.fromarray(normal_from_height(h, 0.34)).save(OUT / 'stipple_n.png')
    # and its grain in the colour too: a photograph of it reads as fine speckle even from across a room
    c = tile_noise(n, 1.1, 5)
    c = (c - c.mean()) / c.std()
    v = np.clip(31 + 8 * c, 0, 255)
    Image.fromarray(np.uint8(np.stack([v, v, v * 1.04], -1))).save(OUT / 'stipple_c.jpg', quality=88)


TEAL, TEAL2, TEAL3 = (24, 118, 104), (32, 142, 122), (16, 96, 86)
GOLD, COPPER = (205, 160, 70), (196, 132, 48)


def traces(d, rnd, box, count, color, width=2, jog=True):
    x0, y0, x1, y1 = box
    for _ in range(count):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        pts = [(x, y)]
        for _ in range(rnd.randint(2, 5)):
            step = rnd.uniform(14, 90)
            a = rnd.choice([0, 45, 90, 135, 180, 225, 270, 315]) if jog else rnd.choice([0, 90, 180, 270])
            x = min(x1, max(x0, x + step * math.cos(math.radians(a))))
            y = min(y1, max(y0, y + step * math.sin(math.radians(a))))
            pts.append((x, y))
        d.line(pts, fill=color, width=width)


def smd(d, rnd, box, count):
    x0, y0, x1, y1 = box
    for _ in range(count):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        w, h = rnd.choice([(7, 4), (4, 7), (9, 5), (5, 9), (6, 3), (3, 6)])
        c = rnd.choice([(40, 40, 42), (60, 50, 40), (150, 120, 80), (90, 80, 70), (200, 190, 170), (30, 30, 30)])
        d.rectangle([x - w / 2 - 1.5, y - h / 2 - 1, x + w / 2 + 1.5, y + h / 2 + 1], fill=(190, 186, 176))
        d.rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], fill=c)


def board(name, size, seed, silk, keepouts):
    w, h = size
    rnd = random.Random(seed)
    im = Image.new('RGB', size, TEAL)
    d = ImageDraw.Draw(im)
    # planes of slightly different copper under the mask
    for _ in range(28):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        d.rectangle([x, y, x + rnd.uniform(40, 200), y + rnd.uniform(30, 150)], fill=rnd.choice([TEAL2, TEAL3, TEAL, TEAL3]))
    traces(d, rnd, (0, 0, w, h), 520, TEAL3, 2)
    traces(d, rnd, (0, 0, w, h), 300, (44, 158, 136), 1)
    # via fields
    for _ in range(1300):
        x, y = rnd.uniform(6, w - 6), rnd.uniform(6, h - 6)
        d.ellipse([x - 1.6, y - 1.6, x + 1.6, y + 1.6], fill=(150, 170, 150))
    smd(d, rnd, (10, 10, w - 10, h - 10), 900)
    # exposed copper round the edge, as on the real boards
    edge = int(min(w, h) * 0.018)
    d.rectangle([0, 0, w, edge], fill=COPPER)
    d.rectangle([0, h - edge, w, h], fill=COPPER)
    d.rectangle([0, 0, edge, h], fill=COPPER)
    d.rectangle([w - edge, 0, w, h], fill=COPPER)
    # solder lands where the modelled chips sit: a dark pad and bright pins
    for (x0, y0, x1, y1) in keepouts:
        d.rectangle([x0, y0, x1, y1], fill=(20, 40, 38), outline=(220, 200, 150), width=2)
    f = ImageFont.truetype(FONT, 20)
    for text, x, y in silk:
        d.text((x, y), text, font=f, fill=(226, 236, 226))
    im = im.filter(ImageFilter.GaussianBlur(0.4))
    im.save(OUT / name, quality=88)


def psu():
    w, h = 512, 512
    rnd = random.Random(9)
    im = Image.new('RGB', (w, h), (150, 92, 38))
    d = ImageDraw.Draw(im)
    traces(d, rnd, (0, 0, w, h), 140, (128, 76, 30), 5, jog=False)
    f = ImageFont.truetype(FONT, 18)
    for i in range(60):
        x, y = rnd.uniform(10, w - 40), rnd.uniform(10, h - 20)
        d.rectangle([x, y, x + rnd.uniform(12, 40), y + rnd.uniform(6, 22)], outline=(235, 232, 220))
    for t, x, y in (('CAUTION: HIGH VOLTAGE', 30, 30), ('F1 250V', 340, 460), ('T1', 230, 240), ('C1', 110, 180)):
        d.text((x, y), t, font=f, fill=(238, 236, 226))
    im.filter(ImageFilter.GaussianBlur(0.5)).save(OUT / 'psu.jpg', quality=85)


def drive():
    # the top of the drive's cover: black with a yellow laser warning sticker
    w, h = 256, 128
    im = Image.new('RGB', (w, h), (232, 196, 40))
    d = ImageDraw.Draw(im)
    d.rectangle([3, 3, w - 4, h - 4], outline=(20, 20, 20), width=3)
    f = ImageFont.truetype(FONT, 22)
    d.text((14, 12), 'CAUTION', font=f, fill=(20, 20, 20))
    f2 = ImageFont.truetype(FONT, 13)
    for i, t in enumerate(('LASER RADIATION WHEN OPEN.', 'DO NOT STARE INTO BEAM.', 'CLASS 3R LASER PRODUCT', 'AVOID DIRECT EYE EXPOSURE')):
        d.text((14, 42 + i * 18), t, font=f2, fill=(20, 20, 20))
    im.save(OUT / 'laser.jpg', quality=88)


def disc():
    # a DVD's data side: a rainbow sheen from the angle-dependent stripe is left to the material; this is its silver and ring
    n = 512
    y, x = np.mgrid[0:n, 0:n] - n / 2 + 0.5
    r = np.hypot(x, y) / (n / 2)
    a = np.arctan2(y, x)
    base = np.stack([190 + 36 * np.cos(a * 2), 190 + 36 * np.cos(a * 2 + 2.1), 196 + 36 * np.cos(a * 2 + 4.2)], -1)
    base[r < 0.40] = (215, 215, 220)
    base[r < 0.31] = (240, 240, 242)
    base[r < 0.125] = (0, 0, 0)
    Image.fromarray(np.uint8(np.clip(base, 0, 255))).save(OUT / 'disc.jpg', quality=85)


if __name__ == '__main__':
    normals()
    # the fat's main board, 264 x 161 mm at 3.88 px/mm
    board('board_fat.jpg', (1024, 624), 7, [('RIPPCSX2', 860, 60), ('GH-RIP', 620, 190), ('1-000-000-11', 620, 214)],
          [(180, 250, 420, 500), (195, 95, 340, 220), (82, 240, 165, 305), (82, 345, 165, 410), (300, 395, 420, 505), (700, 90, 800, 180)])
    # the slim's main board, 196 x 138 mm
    board('board_slim.jpg', (1024, 720), 11, [('RIPPCSX2', 40, 40), ('GH-RIP', 780, 640)], [(330, 230, 620, 500), (660, 250, 760, 350), (680, 400, 800, 490)])
    psu()
    drive()
    disc()
    import gen_labels  # the back's label, seal and connector shell
    gen_labels.main()
    print('textures in', OUT)
