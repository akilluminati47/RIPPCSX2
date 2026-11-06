# Makes marks.py: the printed logos on the fat as outlines, so they are the logos' own shapes and not the nearest font.
#   python gen_marks.py <folder of svg files> marks.py [preview.png]
# Every shape is taken in paint order: a dark one adds, a white one cuts. It needs shapely (and Pillow for the preview), on the
# PC and not in Blender. The result is plain data. The svg files come from Wikimedia Commons and are not kept in the repository.
import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET

from shapely.geometry import LineString, MultiPolygon, Polygon, box
from shapely.ops import unary_union
from shapely import affinity

TRIM = {'ps2_lines': [(-0.6, -0.3, 0.6, -0.022), (0.455, -0.03, 0.6, 0.04)], 'wm_ps2': (0.335, -0.06, 0.39, -0.005), 'dvd_rom': (0.4, -0.17, 0.49, -0.115), 'dvd_video': (0.4, -0.17, 0.49, -0.115),
        'dolby': (0.455, 0.12, 0.51, 0.175), 'dts': (0.445, 0.17, 0.51, 0.235)}
NUM = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?')


def mul(a, b):
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1], a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5])


def apply(m, p):
    return (m[0] * p[0] + m[2] * p[1] + m[4], m[1] * p[0] + m[3] * p[1] + m[5])


def parse_transform(text):
    m = (1, 0, 0, 1, 0, 0)
    for name, args in re.findall(r'(\w+)\s*\(([^)]*)\)', text or ''):
        v = [float(x) for x in NUM.findall(args)]
        if name == 'matrix':
            t = tuple(v)
        elif name == 'translate':
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif name == 'scale':
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == 'rotate':
            c, s = math.cos(math.radians(v[0])), math.sin(math.radians(v[0]))
            t = (c, s, -s, c, 0, 0)
            if len(v) == 3:
                t = mul(mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        else:
            continue
        m = mul(m, t)
    return m


def arc(p0, rx, ry, phi, large, sweep, p1, step=math.radians(6)):
    """Points along an SVG arc, after the end point to centre conversion in the SVG spec."""
    if rx == 0 or ry == 0 or p0 == p1:
        return [p1]
    rx, ry = abs(rx), abs(ry)
    c, s = math.cos(phi), math.sin(phi)
    dx, dy = (p0[0] - p1[0]) / 2, (p0[1] - p1[1]) / 2
    x1, y1 = c * dx + s * dy, -s * dx + c * dy
    lam = x1 * x1 / (rx * rx) + y1 * y1 / (ry * ry)
    if lam > 1:
        rx *= math.sqrt(lam)
        ry *= math.sqrt(lam)
    num = max(0.0, rx * rx * ry * ry - rx * rx * y1 * y1 - ry * ry * x1 * x1)
    den = rx * rx * y1 * y1 + ry * ry * x1 * x1
    k = math.sqrt(num / den) * (-1 if large == sweep else 1) if den else 0.0
    cx1, cy1 = k * rx * y1 / ry, -k * ry * x1 / rx
    cx, cy = c * cx1 - s * cy1 + (p0[0] + p1[0]) / 2, s * cx1 + c * cy1 + (p0[1] + p1[1]) / 2
    t0 = math.atan2((y1 - cy1) / ry, (x1 - cx1) / rx)
    t1 = math.atan2((-y1 - cy1) / ry, (-x1 - cx1) / rx)
    d = t1 - t0
    if sweep and d < 0:
        d += 2 * math.pi
    if not sweep and d > 0:
        d -= 2 * math.pi
    n = max(2, int(abs(d) / step))
    return [(cx + rx * math.cos(t0 + d * i / n) * c - ry * math.sin(t0 + d * i / n) * s,
             cy + rx * math.cos(t0 + d * i / n) * s + ry * math.sin(t0 + d * i / n) * c) for i in range(1, n + 1)]


def path_loops(d, opened=None):
    """Closed point loops from a path, every command, curves at a fine step. Lines left open also go in `opened`."""
    i, n = 0, len(d)
    cmd = None
    loops, cur = [], []
    x = y = sx = sy = 0.0
    cx2 = cy2 = None
    qx = qy = None

    def skip():
        nonlocal i
        while i < n and d[i] in ' ,\t\r\n':
            i += 1

    def num():
        nonlocal i
        skip()
        m = NUM.match(d, i)
        i = m.end()
        return float(m.group())

    def flag():
        nonlocal i
        skip()
        v = d[i]
        i += 1
        return v == '1'

    while True:
        skip()
        if i >= n:
            break
        if d[i].isalpha():
            cmd = d[i]
            i += 1
            if cmd in 'Zz':
                if len(cur) > 2:
                    loops.append(cur)
                cur = []
                x, y = sx, sy
                continue
        rel = cmd.islower()
        c = cmd.upper()
        ox, oy = (x, y) if rel else (0.0, 0.0)
        if c == 'M':
            if len(cur) > 2:
                loops.append(cur)
            if opened is not None and len(cur) > 1:
                opened.append(cur)
            x, y = num() + ox, num() + oy
            sx, sy = x, y
            cur = [(x, y)]
            cmd = 'l' if rel else 'L'
            cx2 = qx = None
        elif c == 'L':
            x, y = num() + ox, num() + oy
            cur.append((x, y))
            cx2 = qx = None
        elif c == 'H':
            x = num() + ox
            cur.append((x, y))
            cx2 = qx = None
        elif c == 'V':
            y = num() + oy
            cur.append((x, y))
            cx2 = qx = None
        elif c in 'CS':
            if c == 'C':
                x1, y1 = num() + ox, num() + oy
            else:
                x1, y1 = (2 * x - cx2, 2 * y - cy2) if cx2 is not None else (x, y)
            x2, y2 = num() + ox, num() + oy
            x3, y3 = num() + ox, num() + oy
            for j in range(1, 21):
                t = j / 20
                u = 1 - t
                cur.append((u ** 3 * x + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t ** 3 * x3, u ** 3 * y + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t ** 3 * y3))
            x, y, cx2, cy2 = x3, y3, x2, y2
            qx = None
        elif c in 'QT':
            if c == 'Q':
                x1, y1 = num() + ox, num() + oy
            else:
                x1, y1 = (2 * x - qx, 2 * y - qy) if qx is not None else (x, y)
            x3, y3 = num() + ox, num() + oy
            for j in range(1, 17):
                t = j / 16
                u = 1 - t
                cur.append((u * u * x + 2 * u * t * x1 + t * t * x3, u * u * y + 2 * u * t * y1 + t * t * y3))
            x, y, qx, qy = x3, y3, x1, y1
            cx2 = None
        elif c == 'A':
            rx, ry, rot = num(), num(), num()
            large, sweep = flag(), flag()
            x3, y3 = num() + ox, num() + oy
            cur += arc((x, y), rx, ry, math.radians(rot), large, sweep, (x3, y3))
            x, y = x3, y3
            cx2 = qx = None
        else:
            raise ValueError(cmd)
    if len(cur) > 2:
        loops.append(cur)
    if opened is not None and len(cur) > 1:
        opened.append(cur)
    return loops


def shape_loops(tag, a):
    if tag == 'path':
        return path_loops(a.get('d', ''))
    if tag in ('polygon', 'polyline'):
        v = [float(x) for x in NUM.findall(a.get('points', ''))]
        return [list(zip(v[0::2], v[1::2]))]
    if tag == 'rect':
        x, y, w, h = (float(a.get(k, 0)) for k in ('x', 'y', 'width', 'height'))
        return [[(x, y), (x + w, y), (x + w, y + h), (x, y + h)]]
    if tag in ('circle', 'ellipse'):
        cx, cy = float(a.get('cx', 0)), float(a.get('cy', 0))
        rx = float(a.get('r', a.get('rx', 0)))
        ry = float(a.get('r', a.get('ry', 0)))
        return [[(cx + rx * math.cos(i * math.pi / 64), cy + ry * math.sin(i * math.pi / 64)) for i in range(128)]]
    return []


def colour_of(text):
    """Black to white, 0 to 1, or None for no paint."""
    text = (text or '').strip().lower()
    if text in ('none', 'transparent'):
        return None
    if text.startswith('url'):
        return 0.0
    named = {'black': 0.0, 'white': 1.0}
    if text in named:
        return named[text]
    m = re.fullmatch(r'#([0-9a-f]{3}|[0-9a-f]{6})', text)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = ''.join(c * 2 for c in h)
        return (int(h[0:2], 16) * 0.3 + int(h[2:4], 16) * 0.59 + int(h[4:6], 16) * 0.11) / 255
    return 0.0


def even_odd(loops):
    out = None
    for lp in loops:
        if len(lp) < 3:
            continue
        p = Polygon(lp).buffer(0)
        out = p if out is None else out.symmetric_difference(p)
    return out


def read_svg(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    text = re.sub(r'\sxmlns(:\w+)?="[^"]*"', '', text)
    text = re.sub(r'\s[\w-]+:[\w-]+="[^"]*"', '', text)
    text = re.sub(r'<(/?)[\w-]+:', r'<\1', text)
    root = ET.fromstring(text)
    by_id = {el.get('id'): el for el in root.iter() if el.get('id')}
    styles = {}
    for st in root.iter('style'):
        for sel, body in re.findall(r'([^{}]+)\{([^}]*)\}', st.text or ''):
            m = re.search(r'fill\s*:\s*([^;]+)', body)
            if m:
                for s in sel.split(','):
                    s = s.strip()
                    if s.startswith('.'):
                        styles[s[1:]] = m.group(1)

    art = [None]

    def fill_of(el, inherited):
        v = inherited
        for c in (el.get('class') or '').split():
            v = styles.get(c, v)
        if el.get('fill') is not None:
            v = el.get('fill')
        m = re.search(r'(?:^|;)\s*fill\s*:\s*([^;]+)', el.get('style') or '')
        if m:
            v = m.group(1)
        return v

    def walk(el, m, fill):
        tag = el.tag
        if tag in ('defs', 'clipPath', 'mask', 'title', 'desc', 'metadata', 'style', 'linearGradient', 'radialGradient', 'symbol', 'pattern'):
            return
        m = mul(m, parse_transform(el.get('transform')))
        fill = fill_of(el, fill)
        loops = shape_loops(tag, el.attrib)
        if tag == 'path' and colour_of(fill) is None and el.get('stroke') not in (None, 'none'):
            # a drawn line, such as the MagicGate logo: its width is in the path's own space, and so is its clip
            lines = []
            path_loops(el.get('d', ''), lines)
            shape = unary_union([LineString(lp).buffer(float(el.get('stroke-width', 1)) / 2, cap_style='flat', join_style='mitre') for lp in lines])
            clip = re.fullmatch(r'url\(#([^)]+)\)', el.get('clip-path') or '')
            if clip:
                shape = shape.intersection(even_odd([lp for ch in by_id[clip.group(1)] for lp in shape_loops(ch.tag, ch.attrib)]))
            shape = affinity.affine_transform(shape, [m[0], m[2], m[1], m[3], m[4], m[5]])
            art[0] = shape if art[0] is None else art[0].union(shape)
        elif loops:
            tone = colour_of(fill)
            shape = even_odd([[apply(m, p) for p in lp] for lp in loops])
            if shape is not None and tone is not None and not shape.is_empty:
                if tone > 0.86:
                    art[0] = art[0].difference(shape) if art[0] is not None else None
                else:
                    art[0] = shape if art[0] is None else art[0].union(shape)
        for ch in el:
            walk(ch, m, fill)

    walk(root, (1, 0, 0, 1, 0, 0), '#000')
    return art[0]


def loops_of(shape, keep_area=0.0):
    polys = shape.geoms if isinstance(shape, MultiPolygon) else [shape]
    out = []
    for p in polys:
        if p.geom_type != 'Polygon' or p.area <= keep_area:
            continue
        out.append(list(p.exterior.coords)[:-1])
        out += [list(r.coords)[:-1] for r in p.interiors if Polygon(r).area > keep_area]
    return out


def main():
    src, dst = sys.argv[1], sys.argv[2]
    marks = {}
    for f in sorted(os.listdir(src)):
        if not f.endswith('.svg'):
            continue
        name = f[:-4]
        try:
            shape = read_svg(os.path.join(src, f))
        except Exception as e:  # a file this reader does not follow is left out, and said so
            print('skipped', f, repr(e))
            continue
        if shape is None or shape.is_empty:
            print('empty', f)
            continue
        x0, y0, x1, y1 = shape.bounds
        k = 1.0 / (x1 - x0)
        shape = affinity.affine_transform(shape, [k, 0, 0, -k, -(x0 + x1) / 2 * k, (y0 + y1) / 2 * k])
        if name in TRIM:  # the small trademark marks, which the console's mouldings do not carry
            for cut in TRIM[name] if isinstance(TRIM[name], list) else [TRIM[name]]:
                shape = shape.difference(box(*cut))
            x0, y0, x1, y1 = shape.bounds
            k = 1.0 / (x1 - x0)
            shape = affinity.affine_transform(shape, [k, 0, 0, k, -(x0 + x1) / 2 * k, -(y0 + y1) / 2 * k])
        shape = shape.simplify(0.00035, preserve_topology=True).buffer(0)
        x0, y0, x1, y1 = shape.bounds
        add(marks, name, shape, y1 - y0)
        if name == 'sony':  # each letter on its own: on the fat they sit one to a fin
            polys = sorted(shape.geoms, key=lambda g: g.bounds[0])
            for letter, g in zip('SONY', polys):
                gx0, gy0, gx1, gy1 = g.bounds
                k = 1.0 / (gx1 - gx0)
                add(marks, 'sony_' + letter, affinity.affine_transform(g, [k, 0, 0, k, -(gx0 + gx1) / 2 * k, -(gy0 + gy1) / 2 * k]), (gy1 - gy0) * k)
    with open(dst, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('# Generated by gen_marks.py: each logo at width 1, centred, up is +. An outline inside another is a hole.\n')
        fh.write('MARKS = ' + json.dumps(marks, separators=(',', ':')) + '\n')
    preview(marks)


def add(marks, name, shape, h):
    marks[name] = {'h': round(h, 4), 'loops': [[[round(x, 5), round(y, 5)] for x, y in lp] for lp in loops_of(shape, 1e-6)]}
    print(name, 'h', marks[name]['h'], 'loops', len(marks[name]['loops']), 'points', sum(len(l) for l in marks[name]['loops']))


def preview(marks):
    if len(sys.argv) > 3:
        from PIL import Image, ImageChops, ImageDraw
        cols, cw, ch = 3, 560, 300
        rows = (len(marks) + cols - 1) // cols
        sheet = Image.new('L', (cols * cw, rows * ch), 255)
        for i, (name, mk) in enumerate(marks.items()):
            im = Image.new('1', (cw, ch), 0)
            w = cw - 40
            s = min(w, (ch - 50) / max(mk['h'], 0.01))
            for lp in mk['loops']:
                one = Image.new('1', (cw, ch), 0)
                ImageDraw.Draw(one).polygon([(cw / 2 + x * s, ch / 2 + 12 - y * s) for x, y in lp], fill=1)
                im = ImageChops.logical_xor(im, one)
            cell = Image.eval(im.convert('L'), lambda v: 255 - v)
            ImageDraw.Draw(cell).text((6, 4), name, fill=120)
            sheet.paste(cell, ((i % cols) * cw, (i // cols) * ch))
        sheet.save(sys.argv[3])


main()
