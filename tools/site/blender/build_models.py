# Builds the site's consoles: blender -b --python tools/site/blender/build_models.py -- [fat] [slim] [--glb DIR] [--renders DIR]
#   [--cams refs/cams.json --refs DIR]   also renders each model through each solved photo camera, for compare.py
#   [--studio]                           turntable beauty shots and the exploded view
# Blender is the only dependency. The .glb files are what the site loads.
import json
import math
import os
import sys

import bpy
import numpy as np
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ps2kit
import importlib

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TEX = HERE.replace('\\', '/') + '/textures/'
GLB = opt('--glb', os.path.join(HERE, '..', '..', '..', 'site', 'models'))
RENDERS = opt('--renders')
CAMS = opt('--cams')
SAMPLES = int(opt('--samples', '48'))


def setup_render(res=(800, 600)):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    try:
        prefs = bpy.context.preferences.addons['cycles'].preferences
        prefs.compute_device_type = 'OPTIX'
        prefs.get_devices()
        for d in prefs.devices:
            d.use = d.type in ('OPTIX',)
        sc.cycles.device = 'GPU'
    except Exception as e:
        print('GPU not available', e)
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.film_transparent = True
    sc.view_settings.view_transform = 'Standard'
    sc.view_settings.look = 'None'
    w = bpy.data.worlds.new('w')
    sc.world = w
    w.use_nodes = True
    w.node_tree.nodes['Background'].inputs['Color'].default_value = (1, 1, 1, 1)
    w.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.42
    return sc


def photo_lights(sc, center, size):
    """A plain white studio like the reference photographs': a big soft key overhead and white all round."""
    for name, loc, power, sz in (('key', (center[0] - size * 0.2, center[1] - size * 0.9, center[2] + size * 1.8), 6, size * 2.0),):
        li = bpy.data.lights.new(name, 'AREA')
        li.energy = power * (size / 0.3) ** 2
        li.size = sz
        ob = bpy.data.objects.new(name, li)
        ob.location = loc
        sc.collection.objects.link(ob)


def set_camera_from_P(sc, P, size):
    """A solved photo camera, its 3 x 4 matrix in mm, becomes a Blender camera with the same picture."""
    P = np.array(P, float)
    M = P[:3, :3]
    # RQ decomposition
    def rq(A):
        q, r = np.linalg.qr(np.flipud(A).T)
        R = np.flipud(r.T)
        R = np.fliplr(R)
        Q = np.flipud(q.T)
        return R, Q
    K, R = rq(M)
    T = np.diag(np.sign(np.diag(K)))
    K = K @ T
    R = T @ R
    t = np.linalg.solve(K, P[:, 3])
    if np.linalg.det(R) < 0:
        R = -R
        t = -t
    K = K / K[2, 2]
    C = -R.T @ t
    W, H = size
    sc.render.resolution_x, sc.render.resolution_y = int(W), int(H)
    cam = bpy.data.cameras.new('photo')
    cam.sensor_fit = 'HORIZONTAL'
    cam.sensor_width = 36
    fx = K[0, 0]
    cam.lens = fx * 36 / W
    cam.shift_x = -(K[0, 2] - W / 2) / W
    cam.shift_y = (K[1, 2] - H / 2) / W
    ob = bpy.data.objects.new('photo', cam)
    # OpenCV camera axes (x right, y down, z forward) to Blender's (x right, y up, -z forward)
    Rb = np.diag([1, -1, -1]) @ R
    mat = np.eye(4)
    mat[:3, :3] = Rb.T
    mat[:3, 3] = C * 0.001
    ob.matrix_world = Matrix(mat.tolist())
    sc.collection.objects.link(ob)
    sc.camera = ob
    return ob


def render(sc, path):
    sc.render.filepath = path
    sc.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still=True)


def beauty_rig(sc, objs, res=(1280, 800), az=-35, el=24, dist_k=1.5, name='beauty', dark=True):
    lo = np.array([min((o.matrix_world @ Vector(c))[i] for o in objs for c in o.bound_box) for i in range(3)])
    hi = np.array([max((o.matrix_world @ Vector(c))[i] for o in objs for c in o.bound_box) for i in range(3)])
    c = (lo + hi) / 2
    r = np.linalg.norm(hi - lo) / 2
    sc.render.resolution_x, sc.render.resolution_y = res
    cam = bpy.data.cameras.new(name)
    cam.lens = 70
    ob = bpy.data.objects.new(name, cam)
    a, e = math.radians(az), math.radians(el)
    d = r * dist_k * 2.2
    ob.location = (c[0] + d * math.sin(a) * math.cos(e), c[1] - d * math.cos(a) * math.cos(e), c[2] + d * math.sin(e))
    look = Vector(c) - ob.location
    ob.rotation_euler = look.to_track_quat('-Z', 'Y').to_euler()
    sc.collection.objects.link(ob)
    sc.camera = ob
    return ob


def build_one(which):
    ps2kit.reset_scene()
    ps2kit._mats.clear()
    col = bpy.data.collections.new(which)
    bpy.context.scene.collection.children.link(col)
    mod = importlib.import_module(which)
    importlib.reload(ps2kit)
    importlib.reload(mod)
    ps2kit._mats.clear()
    objs = mod.build(col, TEX)
    bpy.context.view_layer.update()
    tris = sum(sum(len(p.vertices) - 2 for p in o.data.polygons) for o in objs)
    os.makedirs(GLB, exist_ok=True)
    size = ps2kit.export_glb(os.path.join(GLB, 'ps2-%s.glb' % which), objs)
    print('BUILT', which, 'parts', len(objs), 'tris', tris, 'glb KB', size // 1024)
    return objs


def main():
    which = [w for w in ('fat', 'slim') if w in argv] or ['fat', 'slim']
    for w in which:
        objs = build_one(w)
        if not RENDERS:
            continue
        os.makedirs(RENDERS, exist_ok=True)
        sc = setup_render()
        lo = [min((o.matrix_world @ Vector(c))[i] for o in objs for c in o.bound_box) for i in range(3)]
        hi = [max((o.matrix_world @ Vector(c))[i] for o in objs for c in o.bound_box) for i in range(3)]
        center = [(a + b) / 2 for a, b in zip(lo, hi)]
        photo_lights(sc, center, 0.3)
        if CAMS:
            cams = json.load(open(CAMS))
            for name, c in cams.items():
                if not name.startswith(w):
                    continue
                set_camera_from_P(sc, c['P'], c['size'])
                render(sc, os.path.join(RENDERS, name + '.png'))
        if '--studio' in argv:
            for name, az, el in (('front', -32, 22), ('back', 148, 24), ('top', -10, 62), ('side', 90, 12)):
                beauty_rig(sc, objs, az=az, el=el, name=name)
                render(sc, os.path.join(RENDERS, '%s_%s.png' % (w, name)))
            # the exploded view
            home = {o.name: o.location.copy() for o in objs}
            for o in objs:
                o.location = home[o.name] + Vector(o['explode'])
            bpy.context.view_layer.update()
            beauty_rig(sc, objs, az=-34, el=26, dist_k=1.25, name='exploded')
            render(sc, os.path.join(RENDERS, w + '_exploded.png'))
            for o in objs:
                o.location = home[o.name]


main()
