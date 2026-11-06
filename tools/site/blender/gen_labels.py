# The fat's back: the label block and the warranty seal as they read on an SCPH-30001, and the bay connector's plated shell.
#   python gen_labels.py     (run by gen_textures.py too; it needs Pillow and numpy, and marks.py and ps_mark.py beside it)
# Positions are in the units of a crop of a rear photo at 11.34 to the mm, measured line by line, and each line of text is fitted to its
# measured width, so the block has the rhythm of the real one. No serial number: the bar is as blank as the photo's.
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

from marks import MARKS
import ps_mark

OUT = Path(__file__).resolve().parent / 'textures'
FONTS = 'C:/Windows/Fonts/'
K = 11.34              # a crop unit to the mm
MM = 30                # texture pixels to the mm
T = MM / K
LEFT, TOP, RIGHT, BOTTOM = 30, 12, 1390, 372   # the block's edges, in crop units
BG = (20, 21, 24)
INK = (120, 124, 140)
BRIGHT = (134, 138, 156)
BAND = (96, 102, 124)
DARK = (17, 18, 20)
RULE = (46, 47, 53)


def font(name, size):
    return ImageFont.truetype(FONTS + name, max(6, int(round(size))))


def fit(line, f, width=None, height=None):
    """A line as a white on black picture, its height the font's, squeezed or spread to exactly `width` pixels. Tokens [PS] [PS2] [MG] are the logos."""
    runs = []
    for i, part in enumerate(line.replace('[', '\0[').replace(']', ']\0').split('\0')):
        if part:
            runs.append(part)
    asc, desc = f.getmetrics()
    h = asc + desc
    x = 0.0
    placed = []
    for r in runs:
        if r in ('[PS]', '[PS2]', '[MG]'):
            w = {'[PS]': 1.5, '[PS2]': 3.3, '[MG]': 7.2}[r] * h * 0.62
            placed.append((r, x, w))
            x += w
        else:
            w = f.getlength(r)
            placed.append((r, x, w))
            x += w
    im = Image.new('L', (int(x) + 4, h + 4), 0)
    d = ImageDraw.Draw(im)
    for r, px, w in placed:
        if r == '[MG]':
            im.paste(255, (int(px), 0), outline('magicgate', w, h + 4, asc))
        elif r == '[PS2]':
            im.paste(255, (int(px), 0), outline('ps2_lines', w, h + 4, asc))
        elif r == '[PS]':
            im.paste(255, (int(px), 0), ps_logo(w, h + 4, asc))
        else:
            d.text((px, 0), r, font=f, fill=255)
    if width is not None:
        im = im.resize((int(width), im.height), Image.LANCZOS)
    return im, asc


def outline(name, width, height, baseline):
    """A logo from marks.py on a mask `height` tall, its foot on the text's baseline."""
    mk = MARKS[name]
    s = 4
    w = max(4, int(width))
    im = Image.new('1', (w * s, height * s), 0)
    k = width * s
    foot = baseline * s
    for lp in mk['loops']:
        one = Image.new('1', im.size, 0)
        ImageDraw.Draw(one).polygon([((x + 0.5) * k, foot - (y + mk['h'] / 2) * k) for x, y in lp], fill=1)
        im = ImageChops.logical_xor(im, one)
    return im.convert('L').resize((w, height), Image.LANCZOS)


def ps_logo(width, height, baseline):
    """The PlayStation mark, one colour, from the same curves as the badge."""
    s = 4
    w = max(4, int(width))
    im = Image.new('1', (w * s, height * s), 0)
    k = width * s
    foot = baseline * s
    for fill, outlines in ps_mark.COLOURS.items():
        for nodes in outlines:
            pts = []
            for i, (c, _, r) in enumerate(nodes):
                n = nodes[(i + 1) % len(nodes)]
                for j in range(12):
                    t = j / 12
                    u = 1 - t
                    pts.append(tuple(u ** 3 * c[a] + 3 * u * u * t * r[a] + 3 * u * t * t * n[1][a] + t ** 3 * n[0][a] for a in (0, 1)))
            one = Image.new('1', im.size, 0)
            ImageDraw.Draw(one).polygon([((x + 0.5) * k, foot - (y + 0.377) * k) for x, y in pts], fill=1)
            im = ImageChops.logical_or(im, one)
    return im.convert('L').resize((w, height), Image.LANCZOS)


class Label:
    def __init__(self, size):
        self.im = Image.new('RGB', size, BG)
        self.d = ImageDraw.Draw(self.im)

    def at(self, px, py):
        return (px - LEFT) * T, (py - TOP) * T

    def text(self, body, px, base, size, name='arial.ttf', fill=INK, width=None):
        mask, asc = fit(body, font(name, size * T), None if width is None else width * T)
        x, y = self.at(px, base)
        self.im.paste(fill, (int(x), int(y - asc)), mask)

    def box(self, x0, y0, x1, y1, fill):
        self.d.rectangle([*self.at(x0, y0), *self.at(x1, y1)], fill=fill)

    def mark(self, name, x0, top, width, fill):
        w = int(width * T)
        h = int(MARKS[name]['h'] * width * T) + 2
        x, y = self.at(x0, top)
        self.im.paste(fill, (int(x), int(y)), outline(name, w, h, h - 1))


BAY_FLOOR_GAIN = 1.0   # what the site's lights do to those faces, taken back out
BAY_WALL_GAIN = 1.0


def rating():
    w, h = int((RIGHT - LEFT) * T), int((BOTTOM - TOP) * T)
    k = Label((w, h))
    k.d.rounded_rectangle([3, 3, w - 4, h - 4], radius=int(1.6 * MM), outline=RULE, width=3)

    # the names
    k.mark('sony', 40, 24, 172, BRIGHT)
    k.text('MODEL NO.', 250, 53, 13, width=82)
    k.text('SCPH-30001', 340, 58, 27, width=170)
    k.text('R', 530, 58, 27)
    k.mark('wm_ps2', 42, 64, 204, BRIGHT)
    k.box(258, 71, 370, 103, BAND)
    k.box(373, 71, 448, 103, BAND)
    k.text('NTSC', 286, 96, 21, 'arialbd.ttf', DARK, width=60)
    k.text('U/C', 391, 96, 21, 'arialbd.ttf', DARK, width=40)
    k.text('Sony Computer Entertainment Inc.', 44, 129, 22, 'segoeui.ttf', width=404)
    k.text('AC120V  60Hz  79W', 44, 160, 24, width=200)
    k.text('MADE IN JAPAN', 352, 163, 12, width=98)
    k.box(44, 168, 450, 198, BAND)
    k.text('SERIAL', 52, 191, 20, fill=DARK, width=70)
    k.text('U', 178, 191, 20, fill=DARK)

    # certification
    k.text('CERTIFICATION', 45, 216, 16, width=120)
    for line, base, width in (('PRODUCT COMPLIES WITH DHHS RULES 21 CFR', 231, 307), ('SUBCHAPTER J APPLICABLE AT DATE OF MANUFACTURE.', 245, 355),
                              ('SONY COMPUTER ENTERTAINMENT Inc. 7-1-1, AKASAKA,', 259, 355), ('MINATO-KU, TOKYO, 107-0052 JAPAN', 273, 237),
                              ('MANUFACTURED : SKZ KISARAZU JAPAN', 291, 250)):
        k.text(line, 45, base, 12.5, width=width)
    k.text('DATE CODE', 305, 291, 11, width=70)
    k.box(384, 276, 416, 298, BRIGHT)
    k.text('1C', 391, 293, 15, 'arialbd.ttf', DARK)

    # the listing marks
    k.text('VIDEO/AUDIO', 486, 96, 12, 'arialbd.ttf', width=77)
    k.text('PRODUCT', 506, 112, 12, 'arialbd.ttf', width=57)
    cx, cy = k.at(520, 141)
    r = 26 * T
    k.d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=max(2, int(3.2 * T)))
    k.text('UL', 503, 152, 30, 'arialbd.ttf', width=35)
    k.text('c', 482, 150, 13, 'arialbd.ttf')
    k.text('US', 549, 150, 12, 'arialbd.ttf', width=16)
    k.text('LISTED 9C06', 486, 183, 12, 'arialbd.ttf', width=77)

    # FCC, and Canada's two lines
    k.text('FC', 604, 88, 38, 'arialbd.ttf', BRIGHT, width=38)
    k.text('Tested To Comply', 650, 72, 12, width=112)
    k.text('With FCC Standards', 650, 87, 12, width=126)
    k.text('FOR HOME OR OFFICE USE', 604, 103, 12, width=180)
    for i, (line, width) in enumerate((('THIS CLASS B DIGITAL APPARATUS', 182), ('COMPLIES WITH CANADIAN ICES-003.', 190), ('CET APPAREIL NUMERIQUE DE LA', 165),
                                       ('CLASSE B EST CONFORME A LA', 160), ('NORME NMB-003 DU CANADA.', 160))):
        k.text(line, 604, 119 + i * 15, 11.5, width=width)

    # the patents and trademarks: under the sticker first, then the full width
    k.text('Covered by one or more of U.S. pat. 6,069,635 ; 6,052,131 ; 6,030,292 ;', 848, 180, 13, width=492)
    k.text('6,011,564 ; Additional Pats. marked on package. Other patents pending.', 848, 195.5, 13, width=492)
    para = ('Apparatus Claims of U.S. Patent Nos. 4,631,603, 4,577,216, 4,819,098, and 4,907,093 licensed for limited viewing uses',
            'only. Manufactured under license from Dolby Laboratories. Dolby and the double-D symbol are trademarks of Dolby',
            'Laboratories. Confidential Unpublished Works. \u00a91992-1997 Dolby Laboratories, Inc. All rights reserved. \u201cDTS\u201d and \u201cDTS',
            'Digital Out\u201d are trademarks of Digital Theater Systems, Inc. \u00a92001 Sony Computer Entertainment Inc. All rights',
            'reserved. \u201c[PS]\u201d, and \u201cPlayStation\u201d are registered trademarks and \u201c[PS2]\u201d is a trademark of Sony Computer',
            'Entertainment Inc. \u201cSONY\u201d is a registered trademark of Sony Corporation. [MG] is a copyrighted anti-copying',
            'technology created by Sony Corp. This [MG] mark does not necessarily imply compatibility with other products')
    for i, line in enumerate(para):
        k.text(line, 482, 211 + i * 15.5, 13, width=858)
    k.text('bearing the \u201cMAGICGATE\u201d trademark.', 482, 319.5, 13, width=262)
    k.text('3-071-824-01  DR', 1208, 352, 13, width=132)
    k.im.save(OUT / 'rating.jpg', quality=92, subsampling=0)


def seal():
    """The clear warranty seal across the seam at the left of the back: 60 x 12.6 mm, reading upwards. English, French and Spanish, as it is printed."""
    w, h = 60 * MM, int(12.6 * MM)
    im = Image.new('RGB', (w, h), (24, 25, 28))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([3, 3, w - 4, h - 4], radius=int(0.9 * MM), outline=(40, 41, 46), width=3)
    low = (92, 95, 106)
    y = 0.75 * MM
    for line, width, face, size in (('WARRANTY SEAL', 0.3, 'ariali.ttf', 1.35), ('WARRANTY VOID IF THIS SEAL ON THE PlayStation 2 CONSOLE IS REMOVED.', 0.8, 'ariali.ttf', 1.35),
                                    ('CACHET DE GARANTIE', 0.34, 'ariali.ttf', 1.35), ('LA GARANTIE N\u2019EST PAS VALABLE SI CE CACHET SUR LA CONSOLE PlayStation 2 A \u00c9T\u00c9 ENLEV\u00c9.', 0.96, 'ariali.ttf', 1.35),
                                    ('ETIQUETA DE GARANTIA', 0.36, 'ariali.ttf', 1.35), ('LA GARANTIA NO ES VALIDA SI ESTA ETIQUETA EN LA CONSOLA PlayStation 2 ES REMOVIDA.', 0.96, 'ariali.ttf', 1.35)):
        mask, asc = fit(line, font(face, size * MM), width * (w - 1.6 * MM))
        im.paste(low, (int(0.8 * MM), int(y)), mask)
        y += 1.9 * MM
    im.save(OUT / 'rating_side.jpg', quality=90, subsampling=0)


def serial():
    """The serial sticker, 47.7 x 11.2 mm. The photo this is measured from has it blanked out, and so has this model: a barcode and no number."""
    w, h = int(47.7 * MM), int(11.2 * MM)
    im = Image.new('RGB', (w, h), (226, 224, 216))
    d = ImageDraw.Draw(im)
    rng = np.random.default_rng(30001)
    x = int(2.2 * MM)
    while x < w - 2.2 * MM:
        bar = int(rng.choice([3, 3, 6, 6, 9, 12]))
        d.rectangle([x, int(1.4 * MM), x + bar, int(8.2 * MM)], fill=(24, 24, 26))
        x += bar + int(rng.choice([4, 4, 7, 10]))
    mask, asc = fit('SERIAL NO.', font('arial.ttf', 1.5 * MM))
    im.paste((40, 40, 44), (int(2.2 * MM), int(8.7 * MM)), mask)
    im.save(OUT / 'serial.jpg', quality=90)


def connector():
    """The bay connector's plated shell: a dull tan, mottled, its edges rubbed darker. 54.5 x 6.2 mm."""
    w, h = 1090, 124
    rng = np.random.default_rng(47)
    a = rng.normal(size=(h, w))
    fine = np.asarray(Image.fromarray(np.uint8(np.clip(a * 40 + 128, 0, 255))).filter(ImageFilter.GaussianBlur(1.1)), float) - 128
    big = np.asarray(Image.fromarray(np.uint8(np.clip(rng.normal(size=(h, w)) * 60 + 128, 0, 255))).filter(ImageFilter.GaussianBlur(14)), float) - 128
    tone = 1 + fine / 170 + big / 26
    base = np.stack([214 * tone, 168 * tone, 118 * tone], axis=-1)
    edge = np.minimum.reduce([np.arange(h)[:, None] * np.ones((1, w)), (h - 1 - np.arange(h))[:, None] * np.ones((1, w)),
                              np.arange(w)[None, :] * np.ones((h, 1)), (w - 1 - np.arange(w))[None, :] * np.ones((h, 1))])
    base *= (0.62 + 0.38 * np.clip(edge / 7, 0, 1))[..., None]
    Image.fromarray(np.uint8(np.clip(base, 0, 255))).save(OUT / 'conn_shell.jpg', quality=88)


def bay():
    """The light falling off into the expansion bay, read from a photo of one: a web render has no shadows, so it is painted on."""
    # the floor's brightness in the photo, a row every 10 mm from the mouth in, a column every 15 mm across from the low x wall
    floor = np.array((
        (78, 78, 78, 78, 76, 75, 75),
        (58, 62, 59, 54, 54, 54, 48),
        (39, 40, 37, 33, 30, 30, 27),
        (32, 30, 28, 24, 19, 18, 16),
        (26, 24, 24, 21, 16, 11, 11),
        (24, 23, 21, 15, 12, 8, 8),
        (23, 22, 21, 19, 9, 6, 7),
        (22, 22, 21, 20, 14, 6, 6),
        (23, 23, 23, 23, 15, 5, 6),
        (24, 24, 24, 22, 18, 6, 6),
        (14, 14, 14, 14, 11, 5, 5),
        (7, 7, 7, 7, 6, 4, 4),
    ), dtype=np.float32) * BAY_FLOOR_GAIN
    im = Image.fromarray(np.uint8(np.clip(floor, 0, 255))).resize((256, 256), Image.BICUBIC)
    a = np.asarray(im, dtype=np.float32)[..., None] * np.array((0.96, 1.0, 1.05))
    Image.fromarray(np.uint8(np.clip(a, 0, 255))).save(OUT / 'bay_floor.jpg', quality=90)
    # a wall: bright by the fold, then gone within a few cm, a little brighter low down. Runs from the mouth (left) in, with the floor along the bottom
    d, z = np.meshgrid(np.linspace(0, 120.8, 256), np.linspace(1, 0, 64))
    v = (9 + 47 * np.exp(-d / 9)) * (0.78 + 0.32 * (1 - z)) * (1 - 0.5 * np.clip((d - 40) / 80, 0, 1)) * BAY_WALL_GAIN
    a = v[..., None] * np.array((0.97, 1.0, 1.04))
    Image.fromarray(np.uint8(np.clip(a, 0, 255))).save(OUT / 'bay_wall.jpg', quality=90)


def main():
    OUT.mkdir(exist_ok=True)
    bay()
    rating()
    seal()
    serial()
    connector()


if __name__ == '__main__':
    main()
