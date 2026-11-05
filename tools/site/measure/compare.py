# Side by side and an overlay of a render through a photo's solved camera, with an optional close crop.
import sys
from PIL import Image, ImageChops, ImageDraw
name = sys.argv[1]
ref = {'fat_FL': 'refs/fat_FL.png', 'fat_FR': 'refs/fat_FR.png', 'fat_back': 'refs/fat_back.jpg', 'slim_FL': 'refs/slim_FL.jpg', 'slim_BR': 'refs/slim_BR.jpg'}[name]
a = Image.open(ref).convert('RGB')
b0 = Image.open('r/%s.png' % name).convert('RGBA').resize(a.size)
b = Image.new('RGBA', a.size, (255, 255, 255, 255))
b.alpha_composite(b0)
b = b.convert('RGB')
crop = None
if len(sys.argv) > 2:
    crop = tuple(int(v) for v in sys.argv[2].split(','))
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
if crop:
    a = a.crop(crop); b = b.crop(crop)
if scale != 1:
    s = (int(a.width * scale), int(a.height * scale))
    a = a.resize(s, Image.LANCZOS); b = b.resize(s, Image.LANCZOS)
blend = Image.blend(a, b, 0.5)
stack = '--stack' in sys.argv
if stack:
    o = Image.new('RGB', (a.width, a.height * 2 + 4), (255, 0, 255))
    o.paste(a, (0, 0)); o.paste(b, (0, a.height + 4))
else:
    o = Image.new('RGB', (a.width * 3 + 8, a.height), (255, 0, 255))
    o.paste(a, (0, 0)); o.paste(b, (a.width + 4, 0)); o.paste(blend, (a.width * 2 + 8, 0))
o.save('cmp_%s.png' % name)
print('cmp_%s.png' % name, o.size)
