# Rectifies the photo and the render through the same camera and plane, stacked with a mm grid: rows and ports read off directly.
import json
import sys
import numpy as np
from PIL import Image
from camfit import rect, project
cams = json.load(open('refs/cams.json'))
PLANES = {
    'fat_front': ('fat_FL', lambda u, v: (u, 0, v), 0, 301, 28, 78, 4.4, False),
    'fat_lower': ('fat_FL', lambda u, v: (u, 14, v), 0, 285, 0, 34, 4.4, False),
    'fat_lid': ('fat_FL', lambda u, v: (u, v, 78), 0, 301, 0, 182, 3.4, False),
    'fat_rear': ('fat_back', lambda u, v: (u, 182, v), 0, 301, 0, 78, 4.2, True),
    'slim_front': ('slim_FL', lambda u, v: (u, 0, v), 0, 230, 0, 28, 5.6, False),
    'slim_lower': ('slim_FL', lambda u, v: (u, 7, v), 0, 225, 0, 16, 5.6, False),
    'slim_lid': ('slim_FL', lambda u, v: (u, v, 28), 0, 230, 0, 152, 4.0, False),
    'slim_rear': ('slim_BR', lambda u, v: (u, 152, v), 0, 230, 0, 28, 5.2, True),
}
for name in sys.argv[1:]:
    cam, fn, u0, u1, v0, v1, ppm, flip = PLANES[name]
    c = cams[cam]
    P = np.array(c['P'])
    rect(P, c['src'], 'e_a.png', fn, u0, u1, v0, v1, ppm=ppm, flipu=flip)
    im = Image.open('r/%s.png' % cam).convert('RGBA').resize(tuple(c['size']))
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    bg.alpha_composite(im)
    bg.convert('RGB').save('e_tmp.png')
    rect(P, 'e_tmp.png', 'e_b.png', fn, u0, u1, v0, v1, ppm=ppm, flipu=flip)
    a, b = Image.open('e_a.png'), Image.open('e_b.png')
    o = Image.new('RGB', (a.width, a.height * 2 + 4), (255, 0, 255))
    o.paste(a, (0, 0))
    o.paste(b, (0, a.height + 4))
    o.save('e_%s.png' % name)
    print('e_%s.png' % name, o.size)
