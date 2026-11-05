# Solves the third photo's camera with many starts, and writes it into cams.json. It sees the left end, which no other photo does.
import json, numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation
pairs = [((0, 0, 78), (144, 308)), ((301, 0, 78), (690, 172)), ((301, 182, 78), (517, 14)), ((0, 14, 1.5), (126, 419)), ((275, 14, 1.5), (615, 296)),
         ((43.5, 14, 5.8), (204, 396)), ((7, 14, 5.8), (137, 414))]
size = (700, 420)
def comp(p):
    f, cx, cy = p[:3]
    R = Rotation.from_rotvec(p[3:6]).as_matrix()
    K = np.array([[f, 0, cx], [0, f, cy], [0, 0, 1.0]])
    return K @ np.hstack([R, p[6:9][:, None]])
def proj(P, X):
    h = P @ np.array([*X, 1.0])
    return h[:2] / h[2]
def res(p):
    P = comp(p)
    r = []
    for X, u in pairs:
        r.extend(proj(P, X) - np.array(u))
    r.extend(0.01 * (p[1:3] - np.array(size) / 2))
    return np.array(r)
best = None
rng = np.random.default_rng(3)
for i in range(400):
    f = rng.uniform(500, 4000)
    # the camera looks from the front left, above: world +X runs right and away, -Y towards it
    az = rng.uniform(0.1, 1.2)
    el = rng.uniform(0.2, 1.0)
    d = rng.uniform(300, 2000)
    C = np.array([150, 90, 40]) + d * np.array([-np.sin(az) * np.cos(el), -np.cos(az) * np.cos(el), np.sin(el)])
    fwd = (np.array([150, 90, 40]) - C); fwd /= np.linalg.norm(fwd)
    right = np.cross(fwd, [0, 0, 1]); right /= np.linalg.norm(right)
    down = np.cross(fwd, right)
    R = np.vstack([right, down, fwd])
    t = -R @ C
    p0 = np.array([f, 350, 210, *Rotation.from_matrix(R).as_rotvec(), *t])
    try:
        s = least_squares(res, p0, method='lm', max_nfev=4000)
    except Exception:
        continue
    if best is None or s.cost < best.cost:
        best = s
p = best.x
P = comp(p)
print('f %.0f c %.0f %.0f' % tuple(p[:3]), 'errors', ' '.join('%.1f' % np.linalg.norm(proj(P, X) - np.array(u)) for X, u in pairs))
c = json.load(open('refs/cams.json'))
c['fat_FR'] = {'P': P.tolist(), 'size': list(size), 'src': 'refs/fat_FR.png'}
json.dump(c, open('refs/cams.json', 'w'), indent=1)
