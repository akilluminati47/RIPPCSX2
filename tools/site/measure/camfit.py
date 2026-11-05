# Solves each reference photo's camera (DLT, then a small refinement) from known 3D corners, saves it for Blender, and
# rectifies any world plane through it.
import json
import numpy as np
from PIL import Image, ImageDraw

W, D, H = 301, 182, 78
SW, SD, SH = 230, 152, 28
REFS = {
    # file: (image, [(world mm), (image px)]). Only what is known: the lid's corners at the top, the feet line at the bottom.
    # The heights in between are what the cameras are for, so none of them may be assumed here.
    'fat_FL': ('refs/fat_FL.png', [((0, 0, 78), (-2, 167)), ((301, 0, 78), (550, 310)), ((301, 182, 78), (690, 138)), ((0, 182, 78), (157, 15)),
                                   ((275, 14, 1.5), (508, 407)), ((0, 14, 1.5), (17, 284))]),
    'fat_back': ('refs/fat_back.jpg', [((0, 182, 78), (684, 276)), ((0, 182, 1.5), (680, 451)), ((301, 182, 78), (14, 231)), ((275, 182, 1.5), (81, 405)),
                                       ((301, 0, 78), (154, 149)), ((0, 0, 78), (785, 185))]),
    'fat_FR': ('refs/fat_FR.png', [((0, 0, 78), (144, 308)), ((301, 0, 78), (690, 172)), ((301, 182, 78), (517, 14)), ((0, 14, 1.5), (126, 419)),
                                   ((275, 14, 1.5), (615, 296))]),
    'slim_FL': ('refs/slim_FL.jpg', [((0, 0, 28), (62, 283)), ((230, 0, 28), (587, 434)), ((230, 152, 28), (747, 260)), ((0, 152, 28), (239, 119)),
                                     ((0, 7, 1.2), (69.5, 335)), ((212, 7, 1.2), (547, 474))]),
    'slim_BR': ('refs/slim_BR.jpg', [((0, 152, 28), (583, 438)), ((230, 152, 28), (61, 283)), ((230, 0, 28), (237, 118)), ((0, 0, 28), (745, 254)),
                                     ((0, 152, 1.2), (584, 488)), ((212, 152, 1.2), (102, 351))]),
}


def fit(pairs):
    A = []
    for (X, Y, Z), (u, v) in pairs:
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -u * X, -u * Y, -u * Z, -u])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -v * X, -v * Y, -v * Z, -v])
    _, _, vh = np.linalg.svd(np.array(A, float))
    P = vh[-1].reshape(3, 4)
    return P / np.linalg.norm(P[2, :3])


def rodrigues(w):
    th = np.linalg.norm(w)
    if th < 1e-12:
        return np.eye(3)
    k = w / th
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K


def compose(p):
    f, cx, cy = p[:3]
    R = rodrigues(p[3:6])
    t = p[6:9]
    K = np.array([[f, 0, cx], [0, f, cy], [0, 0, 1.0]])
    return K @ np.hstack([R, t[:, None]])


def fit_square(pairs, size):
    """Square pixels and no skew: f, the principal point (held near the middle), rotation, translation, Levenberg-Marquardt from the DLT."""
    P0 = fit(pairs)
    M = P0[:3, :3]
    q, r = np.linalg.qr(np.flipud(M).T)
    K = np.fliplr(np.flipud(r.T))
    R = np.flipud(q.T)
    T = np.diag(np.sign(np.diag(K)))
    K = K @ T
    R = T @ R
    t = np.linalg.solve(K, P0[:, 3])
    if np.linalg.det(R) < 0:
        R = -R
        t = -t
    K = K / K[2, 2]
    # a rotation vector from R
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    w = th / (2 * np.sin(th)) * np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    p = np.array([(K[0, 0] + K[1, 1]) / 2, size[0] / 2, size[1] / 2, *w, *t], float)
    def resid(p):
        Q = compose(p)
        r = []
        for X, u in pairs:
            r.extend(project(Q, X) - np.array(u))
        r.extend(0.02 * (p[1:3] - np.array(size) / 2))
        return np.array(r)
    lam = 1e-3
    best = resid(p)
    for _ in range(400):
        J = np.zeros((len(best), len(p)))
        for i in range(len(p)):
            d = max(abs(p[i]) * 1e-6, 1e-6)
            q2 = p.copy()
            q2[i] += d
            J[:, i] = (resid(q2) - best) / d
        A = J.T @ J
        g = J.T @ best
        step = np.linalg.solve(A + lam * np.diag(np.diag(A) + 1e-9), -g)
        new = resid(p + step)
        if new @ new < best @ best:
            p = p + step
            best = new
            lam = max(lam * 0.5, 1e-9)
        else:
            lam = min(lam * 4, 1e8)
    return compose(p)


def project(P, X):
    x = P @ np.array([*X, 1.0])
    return x[:2] / x[2]


def solve_h(dst, src):
    A = []
    b = []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()


def rect(P, src, out, fn, umin, umax, vmin, vmax, ppm=5, grid=10, flipu=False, labels=True):
    """fn(u, v) -> world point: rectify that plane."""
    im = Image.open(src).convert('RGB')
    w, h = int((umax - umin) * ppm), int((vmax - vmin) * ppm)
    def px(u, v):
        x = (u - umin) * ppm
        return (w - x if flipu else x, (vmax - v) * ppm)
    cs = [(umin, vmin), (umax, vmin), (umax, vmax), (umin, vmax)]
    o = im.transform((w, h), Image.PERSPECTIVE, solve_h([px(*c) for c in cs], [tuple(project(P, fn(*c))) for c in cs]), Image.BICUBIC)
    if labels:
        d = ImageDraw.Draw(o)
        u = (umin // grid) * grid
        while u <= umax:
            x, _ = px(u, vmin)
            d.line([(x, 0), (x, h)], fill=(255, 70, 70) if u % 50 == 0 else (130, 50, 50))
            if u % 50 == 0:
                d.text((x + 2, 1), str(int(u)), fill=(255, 255, 0))
            u += grid
        v = (vmin // grid) * grid
        while v <= vmax:
            _, y = px(umin, v)
            d.line([(0, y), (w, y)], fill=(60, 200, 255) if v % 50 == 0 else (40, 90, 120))
            d.text((1, y - 10), str(int(v)), fill=(255, 255, 0))
            v += grid
    o.save(out)
    print(out, o.size)


if __name__ == '__main__':
    cams = {}
    for name, (src, pairs) in REFS.items():
        im = Image.open(src)
        P = fit_square(pairs, im.size)
        err = [np.linalg.norm(project(P, X) - np.array(u)) for X, u in pairs]
        cams[name] = {'P': P.tolist(), 'size': im.size, 'src': src}
        print(name, 'reprojection px', ' '.join('%.1f' % e for e in err), 'size', im.size)
    json.dump(cams, open('refs/cams.json', 'w'), indent=1)
