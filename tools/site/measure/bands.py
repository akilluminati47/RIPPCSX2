# Reads a line of brightness down a face of the photo and of the render through the same camera, as bands of dark, mid and bright
# with their heights in mm: where the slits and the lines of light really are, in numbers. Edit S below for the faces you want.
import sys, numpy as np
from PIL import Image
from camfit import rect
import json
cams = json.load(open('refs/cams.json'))
def prof(cam, fn, u0, u1, z0, z1, ppm=12.0, flip=False):
    c = cams[cam]; P = np.array(c['P'])
    rect(P, c['src'], 'e_a.png', fn, u0, u1, z0, z1, ppm=ppm, flipu=flip)
    im = Image.open('r/%s.png' % cam).convert('RGBA').resize(tuple(c['size']))
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im); bg.convert('RGB').save('e_tmp.png')
    rect(P, 'e_tmp.png', 'e_b.png', fn, u0, u1, z0, z1, ppm=ppm, flipu=flip)
    return [np.median(np.asarray(Image.open(f).convert('L'), dtype=float), axis=1) for f in ('e_a.png','e_b.png')]
def bands(v, z1, dz):
    out=[];cur=None;start=0
    for i,x in enumerate(v):
        k='D' if x<28 else ('B' if x>62 else 'm')
        if k!=cur:
            if cur: out.append((cur, z1-start*dz, z1-i*dz, int(np.mean(v[start:i]))))
            cur=k;start=i
    out.append((cur, z1-start*dz, z1-len(v)*dz, int(np.mean(v[start:]))))
    return ' '.join('%s[%.1f-%.1f]%d'%o for o in out if o[1]-o[2]>=0.25)
S=[('fat right end Y70-100','fat_FL',lambda u,v:(301,u,v),70,100,28,78),
   ('fat right end Y20-40','fat_FL',lambda u,v:(301,u,v),20,40,28,78),
   ('fat rear X296-300','fat_back',lambda u,v:(u,182,v),296,300,28,78),
   ('fat rear X285-292','fat_back',lambda u,v:(u,182,v),285,292,28,78),
   ('fat nose X292-299 front','fat_FL',lambda u,v:(u,0,v),292,300,28,78),
   ('slim right end Y60-100','slim_FL',lambda u,v:(230,u,v),60,100,0,28),
   ('slim right end Y10-30','slim_FL',lambda u,v:(230,u,v),10,30,0,28),
   ('slim rear X110-130','slim_BR',lambda u,v:(u,152,v),110,130,0,28),
   ('slim rear X200-225','slim_BR',lambda u,v:(u,152,v),200,225,0,28),
   ('slim rear X3-11 window','slim_BR',lambda u,v:(u,152,v),4,11,0,28),
   ('slim rear X20-26 window','slim_BR',lambda u,v:(u,152,v),20.5,27,0,28),
   ('slim left end Y100-130','slim_BR',lambda u,v:(0,u,v),100,130,0,28)]
for t,cam,fn,u0,u1,z0,z1 in S:
    a,b=prof(cam,fn,u0,u1,z0,z1)
    dz=(z1-z0)/len(a)
    print('==',t);print(' photo',bands(a,z1,dz));print(' model',bands(b,z1,dz))
