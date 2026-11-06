# The modelling kit for the site's consoles. Run inside Blender (see build_models.py). All sizes are real millimetres;
# X runs left to right as you face the console, Y from the front to the back, Z up. A Part is one thing that comes
# away in the exploded view: one object, its origin at its own centre, its explode vector and caption in its extras.
import math
import os
import bmesh
import bpy
from mathutils import Matrix, Vector

MM = 0.001
FONTS = 'C:/Windows/Fonts/'


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


_mats = {}


def srgb(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c] + [1.0]


def mat(name, color='#000000', rough=0.5, metal=0.0, emit=None, emit_power=1.0, tex=None, normal=None, normal_strength=1.0,
        alpha=None, spec=None):
    """A Principled material (the part of it glTF keeps); tex and normal are image files in the textures folder."""
    if name in _mats:
        return _mats[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = srgb(color)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    if spec is not None:
        b.inputs['Specular IOR Level'].default_value = spec
    if emit:
        b.inputs['Emission Color'].default_value = srgb(emit)
        b.inputs['Emission Strength'].default_value = emit_power
    if tex:
        n = nt.nodes.new('ShaderNodeTexImage')
        n.image = bpy.data.images.load(tex, check_existing=True)
        nt.links.new(n.outputs['Color'], b.inputs['Base Color'])
    if normal:
        n = nt.nodes.new('ShaderNodeTexImage')
        n.image = bpy.data.images.load(normal, check_existing=True)
        n.image.colorspace_settings.name = 'Non-Color'
        nm = nt.nodes.new('ShaderNodeNormalMap')
        nm.inputs['Strength'].default_value = normal_strength
        nt.links.new(n.outputs['Color'], nm.inputs['Color'])
        nt.links.new(nm.outputs['Normal'], b.inputs['Normal'])
    if alpha is not None:
        b.inputs['Alpha'].default_value = alpha
        m.surface_render_method = 'BLENDED'
    _mats[name] = m
    return m


class Part:
    def __init__(self, name, explode=(0, 0, 0), caption='', spin=1.0):
        self.name = name
        self.explode = explode
        self.caption = caption
        self.spin = spin
        self.bm = bmesh.new()
        self.uv = self.bm.loops.layers.uv.new('UVMap')
        self.mats = []
        self.fixed_uv = set()
        self.tile = {}  # material name -> mm per texture repeat

    def _mi(self, m):
        if m not in self.mats:
            self.mats.append(m)
        return self.mats.index(m)

    # ---- solids ----
    def box(self, x0, x1, y0, y1, z0, z1, m, bevel=0.0, seg=1):
        if x1 < x0: x0, x1 = x1, x0
        if y1 < y0: y0, y1 = y1, y0
        if z1 < z0: z0, z1 = z1, z0
        bm = self.bm
        r = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)) @ Matrix.Diagonal((x1 - x0, y1 - y0, z1 - z0, 1)))
        vs = r['verts']
        fs = list({f for v in vs for f in v.link_faces})
        mi = self._mi(m)
        for f in fs:
            f.material_index = mi
        if bevel > 0:
            es = list({e for v in vs for e in v.link_edges})
            out = bmesh.ops.bevel(bm, geom=es + vs, offset=bevel, offset_type='OFFSET', segments=seg, profile=0.5, affect='EDGES', clamp_overlap=True)
            for f in out.get('faces', []):
                f.material_index = mi
        return self

    def cyl(self, center, axis, r, h, m, n=24, bevel=0.0, r2=None, smooth=True):
        """A cylinder standing on center, h along axis ('x', 'y', 'z', sign in h)."""
        bm = self.bm
        d = {'x': Vector((1, 0, 0)), 'y': Vector((0, 1, 0)), 'z': Vector((0, 0, 1))}[axis]
        q = Vector((0, 0, 1)).rotation_difference(d)
        mid = Vector(center) + d * (h / 2)
        res = bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=n, radius1=r, radius2=r if r2 is None else r2, depth=abs(h),
                                    matrix=Matrix.Translation(mid) @ q.to_matrix().to_4x4())
        vs = res['verts']
        fs = list({f for v in vs for f in v.link_faces})
        mi = self._mi(m)
        for f in fs:
            f.material_index = mi
            f.smooth = smooth and len(f.verts) == 4
        if bevel > 0:
            rims = [e for e in {e for v in vs for e in v.link_edges} if len(e.link_faces) == 2 and (e.link_faces[0].normal.dot(e.link_faces[1].normal) < 0.5)]
            out = bmesh.ops.bevel(bm, geom=rims, offset=bevel, offset_type='OFFSET', segments=1, profile=0.5, affect='EDGES', clamp_overlap=True)
            for f in out.get('faces', []):
                f.material_index = mi
        return self

    def disc(self, center, r, h, m, n=96):
        """A flat round thing standing on center, its picture mapped straight down from above."""
        bm = self.bm
        res = bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=n, radius1=r, radius2=r, depth=abs(h),
                                    matrix=Matrix.Translation(Vector(center) + Vector((0, 0, h / 2))))
        mi = self._mi(m)
        for f in list({f for v in res['verts'] for f in v.link_faces}):
            f.material_index = mi
            f.smooth = len(f.verts) == 4
            for lo in f.loops:
                lo[self.uv].uv = ((lo.vert.co.x - center[0]) / (2 * r) + 0.5, (lo.vert.co.y - center[1]) / (2 * r) + 0.5)
            self.fixed_uv.add(f)
        return self

    def ring(self, center, axis, r0, r1, h, m, n=32):
        """A flat washer: outer r1, inner r0, height h along axis."""
        bm = self.bm
        d = {'x': Vector((1, 0, 0)), 'y': Vector((0, 1, 0)), 'z': Vector((0, 0, 1))}[axis]
        q = Vector((0, 0, 1)).rotation_difference(d).to_matrix()
        c = Vector(center)
        low0, low1, hi0, hi1 = [], [], [], []
        for i in range(n):
            a = 2 * math.pi * i / n
            ca, sa = math.cos(a), math.sin(a)
            low0.append(bm.verts.new(c + q @ Vector((r0 * ca, r0 * sa, 0))))
            low1.append(bm.verts.new(c + q @ Vector((r1 * ca, r1 * sa, 0))))
            hi0.append(bm.verts.new(c + q @ Vector((r0 * ca, r0 * sa, h))))
            hi1.append(bm.verts.new(c + q @ Vector((r1 * ca, r1 * sa, h))))
        mi = self._mi(m)
        for i in range(n):
            j = (i + 1) % n
            for quad in ((hi0[i], hi1[i], hi1[j], hi0[j]), (low1[i], low0[i], low0[j], low1[j]), (hi1[i], low1[i], low1[j], hi1[j]), (low0[i], hi0[i], hi0[j], low0[j])):
                f = bm.faces.new(quad)
                f.material_index = mi
        return self

    def poly(self, pts, plane, m, depth=0.05):
        """A flat extruded polygon. pts are (u, v) in mm on plane (a Matrix: u, v, normal as columns, then origin)."""
        bm = self.bm
        vs = [bm.verts.new(plane @ Vector((u, v, 0))) for u, v in pts]
        f = bm.faces.new(vs)
        mi = self._mi(m)
        f.material_index = mi
        bmesh.ops.triangulate(bm, faces=[f], quad_method='BEAUTY', ngon_method='EAR_CLIP')
        if depth:
            vs2 = [bm.verts.new(plane @ Vector((u, v, -depth))) for u, v in pts]
            k = len(pts)
            for i in range(k):
                j = (i + 1) % k
                s = bm.faces.new((vs[j], vs[i], vs2[i], vs2[j]))
                s.material_index = mi
        return self

    def stroke(self, path, width, plane, m, depth=0.04):
        """Line art on a plane: each run of the path as a thin bar, corners squared."""
        w = width / 2
        for (a, b) in zip(path, path[1:]):
            ux, uy = a
            vx, vy = b
            if abs(ux - vx) > abs(uy - vy):
                x0, x1 = sorted((ux, vx))
                self.poly([(x0 - w, uy - w), (x1 + w, uy - w), (x1 + w, uy + w), (x0 - w, uy + w)], plane, m, depth)
            else:
                y0, y1 = sorted((uy, vy))
                self.poly([(ux - w, y0 - w), (ux + w, y0 - w), (ux + w, y1 + w), (ux - w, y1 + w)], plane, m, depth)
        return self

    def curve(self, outlines, scale, plane, m, depth, bevel=0.0, res=16):
        """Filled outlines as real geometry with a rounded edge. An outline is a list of (x, y) points, or of Bezier nodes
        (point, left handle, right handle); an outline inside another is a hole. Unlike poly, a concave shape stays concave."""
        cu = bpy.data.curves.new('c', 'CURVE')
        cu.dimensions = '2D'
        cu.fill_mode = 'BOTH'
        cu.resolution_u = res
        cu.extrude = max(0.0, depth / 2 - bevel)
        cu.bevel_depth = bevel
        cu.bevel_resolution = 3 if bevel else 0
        cu.offset = -bevel
        for line in outlines:
            if isinstance(line[0][0], (int, float)):
                sp = cu.splines.new('POLY')
                sp.points.add(len(line) - 1)
                for q, (x, y) in zip(sp.points, line):
                    q.co = (x * scale, y * scale, 0, 1)
            else:
                sp = cu.splines.new('BEZIER')
                sp.bezier_points.add(len(line) - 1)
                for q, (c, l, r) in zip(sp.bezier_points, line):
                    q.handle_left_type = q.handle_right_type = 'FREE'
                    q.co = (c[0] * scale, c[1] * scale, 0)
                    q.handle_left = (l[0] * scale, l[1] * scale, 0)
                    q.handle_right = (r[0] * scale, r[1] * scale, 0)
            sp.use_cyclic_u = True
            sp.use_smooth = True
        ob = bpy.data.objects.new('c', cu)
        bpy.context.scene.collection.objects.link(ob)
        dg = bpy.context.evaluated_depsgraph_get()
        me = ob.evaluated_get(dg).to_mesh()
        tmp = bmesh.new()
        tmp.from_mesh(me)
        bmesh.ops.transform(tmp, matrix=plane, verts=tmp.verts)
        tmp.to_mesh(me)
        before = set(self.bm.faces)
        self.bm.from_mesh(me)
        tmp.free()
        mi = self._mi(m)
        for f in self.bm.faces:
            if f not in before:
                f.material_index = mi
        ob.evaluated_get(dg).to_mesh_clear()
        bpy.data.objects.remove(ob)
        bpy.data.curves.remove(cu)
        return self

    def text(self, body, font, size, plane, m, align='LEFT', depth=0.03, stretch=1.0, spacing=1.0):
        """Text as real geometry on a plane, so it stays sharp and needs no texture."""
        cu = bpy.data.curves.new('t', 'FONT')
        cu.body = body
        cu.font = bpy.data.fonts.load(FONTS + font, check_existing=True)
        cu.size = size
        cu.align_x = align
        cu.space_character = spacing
        cu.extrude = depth / 2
        cu.resolution_u = 3
        ob = bpy.data.objects.new('t', cu)
        bpy.context.scene.collection.objects.link(ob)
        dg = bpy.context.evaluated_depsgraph_get()
        me = ob.evaluated_get(dg).to_mesh()
        offset = len(self.bm.verts)
        tmp = bmesh.new()
        tmp.from_mesh(me)
        bmesh.ops.transform(tmp, matrix=plane @ Matrix.Diagonal((stretch, 1, 1, 1)), verts=tmp.verts)
        tmp.to_mesh(me)
        before = set(self.bm.faces)
        self.bm.from_mesh(me)
        tmp.free()
        mi = self._mi(m)
        for f in self.bm.faces:
            if f not in before:
                f.material_index = mi
        ob.evaluated_get(dg).to_mesh_clear()
        bpy.data.objects.remove(ob)
        bpy.data.curves.remove(cu)
        return self

    def textured_quad(self, x0, x1, y0, y1, z, m, flip_u=False, flip_v=False):
        """A quad on the XY plane with its own 0..1 UVs (a board's picture)."""
        bm = self.bm
        vs = [bm.verts.new(v) for v in ((x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z))]
        f = bm.faces.new(vs)
        f.material_index = self._mi(m)
        uv = [(0, 0), (1, 0), (1, 1), (0, 1)]
        for lo, (u, v) in zip(f.loops, uv):
            lo[self.uv].uv = ((1 - u) if flip_u else u, (1 - v) if flip_v else v)
        self.fixed_uv.add(f)
        return self

    def quad_on(self, plane_at, w, h, m):
        """A w x h rectangle on a plane with its own 0..1 UVs (a printed label)."""
        bm = self.bm
        vs = [bm.verts.new(plane_at @ Vector(v)) for v in ((0, 0, 0), (w, 0, 0), (w, h, 0), (0, h, 0))]
        f = bm.faces.new(vs)
        f.material_index = self._mi(m)
        for lo, uv in zip(f.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
            lo[self.uv].uv = uv
        self.fixed_uv.add(f)
        return self

    # ---- finishing ----
    def finish(self, parent_collection):
        bm = self.bm
        bm.normal_update()
        bm.verts.ensure_lookup_table()
        tile_by_index = {i: self.tile.get(m.name, 10.0) for i, m in enumerate(self.mats)}
        for f in bm.faces:
            if f in self.fixed_uv:
                continue
            n = f.normal
            ax = max(range(3), key=lambda i: abs(n[i]))
            a, b = [(1, 2), (0, 2), (0, 1)][ax]
            t = tile_by_index.get(f.material_index, 10.0)
            for lo in f.loops:
                lo[self.uv].uv = (lo.vert.co[a] / t, lo.vert.co[b] / t)
        # the origin at the part's centre, sizes into metres
        lo = Vector((min(v.co[i] for v in bm.verts) for i in range(3)))
        hi = Vector((max(v.co[i] for v in bm.verts) for i in range(3)))
        c = (lo + hi) / 2
        bmesh.ops.transform(bm, matrix=Matrix.Diagonal((MM, MM, MM, 1)) @ Matrix.Translation(-c), verts=bm.verts)
        me = bpy.data.meshes.new(self.name)
        bm.to_mesh(me)
        bm.free()
        for m in self.mats:
            me.materials.append(m)
        ob = bpy.data.objects.new(self.name, me)
        ob.location = c * MM
        ob['explode'] = [e * MM for e in self.explode]
        ob['caption'] = self.caption
        ob['spin'] = self.spin
        parent_collection.objects.link(ob)
        return ob


def plane(origin, u, v):
    """A placement for flat art: origin, then the world directions of the art's +u and +v. The art's normal is u x v."""
    O, U, V = Vector(origin), Vector(u), Vector(v)
    N = U.cross(V)
    M = Matrix(((U.x, V.x, N.x, O.x), (U.y, V.y, N.y, O.y), (U.z, V.z, N.z, O.z), (0, 0, 0, 1)))
    return M


def export_glb(path, objs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', use_selection=True, export_yup=True, export_apply=False,
                              export_extras=True, export_normals=True, export_materials='EXPORT', export_image_format='AUTO',
                              export_cameras=False, export_lights=False, export_animations=False)
    return os.path.getsize(path)
