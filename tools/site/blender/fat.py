# The fat PlayStation 2 (SCPH-30001 / 39001 era): 301 x 182 x 78 mm from Sony's manual. Every position below was measured
# from photographs rectified through a solved camera (see compare.py). The insides follow a real teardown: lid, tray, drive,
# shields, main board, power board, fan, expansion bay, the controller board, the USB board and the button flex.
from mathutils import Matrix, Vector
from ps2kit import Part, mat, plane, export_glb

W, D, H = 301, 182, 78
LOW_X = 275            # the lower block stops short of the right end
LOW_Y = 14             # and sits back from the front
BOT = 1.5              # it stands on feet: 78 mm is to the bottom of the feet
FIN_SIDE = 2.7         # how deep the slits cut on the right end
PORT_Z = (41.9, 47.0)  # the controller ports take the place of the fourth plate
LOW_Z = 31.6
FIN = 6.0              # how deep the slits cut
SLITS = (70.2, 62.65, 55.15, 47.7, 40.15)
GAP = 3.4
# the plates between the slits, top to bottom
PLATES = [(SLITS[0] + GAP / 2, H), (SLITS[1] + GAP / 2, SLITS[0] - GAP / 2), (SLITS[2] + GAP / 2, SLITS[1] - GAP / 2),
          (SLITS[3] + GAP / 2, SLITS[2] - GAP / 2), (SLITS[4] + GAP / 2, SLITS[3] - GAP / 2), (LOW_Z + 0.4, SLITS[4] - GAP / 2)]
TRAY = (145.0, 273.0)
PORT1, PORT2 = (21.5, 61.5), (73.5, 114.5)
CARD1, CARD2 = (20.6, 63.0), (72.5, 115.6)
BTN = (279.0, 290.0)
NOSE = 291.0


def materials(tex):
    return dict(
        case=mat('fat_case', '#222224', rough=0.62, normal=tex + 'hatch_n.png', normal_strength=0.3),
        fin=mat('fat_fin', '#141518', rough=0.24),
        inner=mat('fat_inner', '#08080a', rough=0.8),
        shell=mat('fat_shell', '#121316', rough=0.75),
        dark=mat('fat_recess', '#030304', rough=0.9, spec=0.0),
        blue=mat('usb_blue', '#0b52e6', rough=0.45, spec=0.25),
        bluetext=mat('usb_print', '#a9c6f7', rough=0.5),
        silver=mat('metal_silver', '#c4c7cb', rough=0.34, metal=1.0),
        steel=mat('metal_steel', '#9aa0a6', rough=0.5, metal=1.0),
        zinc=mat('metal_zinc', '#c4c8ca', rough=0.55, metal=0.35),
        gold=mat('metal_gold', '#d9b35a', rough=0.3, metal=1.0),
        label=mat('fat_print', '#a8aab0', rough=0.6),
        ink=mat('fat_ink', '#000000', rough=0.7, spec=0.0),
        portface=mat('port_face', '#26272b', rough=0.45),
        portrim=mat('port_rim', '#5d5e64', rough=0.42),
        portin=mat('port_inner', '#17181b', rough=0.6),
        portpin=mat('port_pin', '#9a9ba0', rough=0.45),
        doorprint=mat('fat_door_print', '#7f8187', rough=0.6),
        rocker=mat('rocker', '#101012', rough=0.5, spec=0.3),
        block=mat('rear_block', '#17181b', rough=0.5),
        rimdark=mat('rim_dark', '#303136', rough=0.5),
        edge_hi=mat('edge_hi', '#8a8b91', rough=0.3),
        edge_hi2=mat('edge_hi2', '#4a4b50', rough=0.3),
        blackgloss=mat('black_gloss', '#0a0a0c', rough=0.16),
        tab=mat('bay_tab', '#dfe1e2', rough=0.5, metal=0.2),
        bay1=mat('bay_lit', '#6f7274', rough=0.6, metal=0.2),
        bay2=mat('bay_mid', '#4a4c4e', rough=0.65, metal=0.1),
        bay3=mat('bay_dim', '#2a2b2d', rough=0.7),
        bay4=mat('bay_deep', '#141516', rough=0.8),
        white=mat('print_white', '#dcdde2', rough=0.5),
        grey=mat('sticker_grey', '#d8d8d8', rough=0.7),
        black=mat('plastic_black', '#0c0c0e', rough=0.45),
        rubber=mat('rubber', '#0a0a0b', rough=0.9),
        teal=mat('reset_teal', '#051c1b', rough=0.22),
        tealglow=mat('reset_glow', '#37e6d2', rough=0.4, emit='#37e6d2', emit_power=0.35),
        bluebtn=mat('eject_dark', '#090e1c', rough=0.22),
        blueglow=mat('eject_glow', '#3f7dff', rough=0.4, emit='#3f7dff', emit_power=0.35),
        logo_lo=mat('logo_cyan', '#7fe0f4', rough=0.35),
        logo_mid=mat('logo_blue', '#7a9bf0', rough=0.35),
        logo_hi=mat('logo_violet', '#7f7fe0', rough=0.35),
        ps_red=mat('ps_red', '#d8231c', rough=0.3),
        ps_yel=mat('ps_yellow', '#f2b400', rough=0.3),
        ps_blu=mat('ps_blue', '#1f6fc4', rough=0.3),
        ps_grn=mat('ps_green', '#1fa24a', rough=0.3),
        board=mat('board_fat', tex=tex + 'board_fat.jpg', rough=0.45),
        pcb=mat('pcb_teal', '#16705f', rough=0.45),
        psu=mat('board_psu', tex=tex + 'psu.jpg', rough=0.6),
        chip=mat('chip_black', '#141416', rough=0.42),
        chiplid=mat('chip_lid', '#c9cbcc', rough=0.3, metal=1.0),
        chipprint=mat('chip_print', '#d2d4d8', rough=0.5),
        chipdark=mat('chip_print_dark', '#2a2c30', rough=0.5),
        cap=mat('cap_alu', '#b8bcc0', rough=0.35, metal=1.0),
        capblue=mat('cap_blue', '#27306e', rough=0.4),
        capgold=mat('cap_gold', '#c79a3a', rough=0.45),
        ferrite=mat('ferrite', '#2c2c30', rough=0.8),
        copper=mat('copper', '#b87333', rough=0.4, metal=1.0),
        peach=mat('copper_pale', '#c9a184', rough=0.42, metal=0.5),
        laser=mat('sticker_laser', tex=tex + 'laser.jpg', rough=0.6),
        rating=mat('rear_rating', tex=tex + 'rating.jpg', rough=0.24),
        rating_side=mat('rear_rating_side', tex=tex + 'rating_side.jpg', rough=0.24),
        disc=mat('disc_silver', tex=tex + 'disc.jpg', rough=0.14, metal=1.0),
        drive=mat('drive_black', '#101012', rough=0.55),
        fan=mat('fan_black', '#09090a', rough=0.7, spec=0.2),
        foil=mat('isolation_sheet', '#d9d6c6', rough=0.55, alpha=0.6),
        flex=mat('flex_amber', '#b5721e', rough=0.45),
        cell=mat('cr2032', '#b4b6b8', rough=0.28, metal=1.0),
    )


def ps2_logo(p, plane_at, s0, u0, unit, width, ms):
    """The PS2 mark from its three strokes as measured on the lid: reading length 126 mm, height 21 mm at unit=1."""
    def art(points):
        return [(s0 + s * unit, u0 + u * unit) for s, u in points]
    lo, mid, hi = ms
    # P: the stem and middle bar in the lighter tone, the right side and top bar in the violet
    p.stroke(art([(0, 0), (0, 10.0)]), width, plane_at, lo)
    p.stroke(art([(0, 10.0), (39, 10.0), (39, 21)]), width, plane_at, mid)
    p.stroke(art([(39, 21), (0, 21)]), width, plane_at, hi)
    # S: the bottom bar, the riser, the top bar
    p.stroke(art([(40.5, 0), (60, 0), (60, 10.5)]), width, plane_at, lo)
    p.stroke(art([(60, 10.5), (60, 21)]), width, plane_at, mid)
    p.stroke(art([(60, 21), (81, 21)]), width, plane_at, hi)
    # 2: the bottom bar, the left side, the middle bar, the right side, the top bar
    p.stroke(art([(126, 0), (87.5, 0), (87.5, 10.0)]), width, plane_at, lo)
    p.stroke(art([(87.5, 10.0), (125, 10.0), (125, 21)]), width, plane_at, mid)
    p.stroke(art([(125, 21), (87.5, 21)]), width, plane_at, hi)


def ps_badge(p, cx, y, cz, s, m):
    """The small coloured PlayStation mark: 6.9 x 5.2 at s=1, centred on (cx, cz). The P stands, the S lies flat in front of it."""
    art = plane((cx, y, cz), (1, 0, 0), (0, 0, 1))
    def at(points):
        return [(a * s, b * s) for a, b in points]
    p.poly(at([(-0.85, -1.3), (0.25, -1.75), (0.25, 1.75), (0.75, 1.85), (1.05, 1.55), (1.05, 0.7), (0.7, 0.35), (0.7, -0.25), (1.35, -0.1), (1.85, 0.55), (1.85, 1.75), (1.2, 2.45), (-0.85, 2.6)]), art, m['ps_red'], depth=0.1)
    art2 = plane((cx, y - 0.1, cz), (1, 0, 0), (0, 0, 1))
    p.poly(at([(-3.45, -1.25), (-1.9, -0.85), (0.2, -0.45), (0.2, -0.95), (-1.2, -1.1), (-2.2, -1.25), (-1.8, -1.45), (-0.5, -1.75), (-1.6, -2.0), (-3.2, -1.7)]), art2, m['ps_yel'], depth=0.1)
    p.poly(at([(0.35, -0.95), (1.2, -1.1), (2.1, -1.15), (1.5, -1.45), (0.35, -1.75), (0.35, -2.3), (1.2, -2.1), (2.9, -1.55), (3.45, -1.05), (3.0, -0.7), (1.8, -0.75)]), art2, m['ps_blu'], depth=0.1)
    p.poly(at([(-0.5, -1.75), (0.35, -1.75), (0.35, -2.3), (-0.25, -2.6), (-1.0, -2.3)]), art2, m['ps_grn'], depth=0.1)


def ladder(p, x0, x1, z0, z1, y0, y1, slots, cols, bar, m, dark):
    """A vent: louvres with thin dividers set back behind them, real holes. A web render has no shadows, so each louvre's top and underside are painted dark."""
    pitch = (z1 - z0) / slots
    for i in range(slots + 1):
        z = z0 + i * pitch
        p.box(x0, x1, y0, y1, z - bar / 2, z + bar / 2, m, bevel=0.16)
        p.box(x0, x1, y0 + 0.2, y1, z + bar / 2 - 0.01, z + bar / 2 + 0.02, dark)
        p.box(x0, x1, y0 + 0.2, y1, z - bar / 2 - 0.02, z - bar / 2 + 0.01, dark)
    cw = (x1 - x0) / cols
    for c in range(cols + 1):
        x = x0 + c * cw
        p.box(x - 0.35, x + 0.35, y0 + 0.9, y1 + 0.6, z0, z1, m)


def stadium(cx, cz, w, h, n=8):
    """A rounded bar's outline, for a port's lobe."""
    import math
    r = h / 2
    pts = []
    for i in range(n + 1):
        a = -math.pi / 2 + math.pi * i / n
        pts.append((cx + (w / 2 - r) + r * math.cos(a), cz + r * math.sin(a)))
    for i in range(n + 1):
        a = math.pi / 2 + math.pi * i / n
        pts.append((cx - (w / 2 - r) + r * math.cos(a), cz + r * math.sin(a)))
    return pts


def rrect(cx, cz, w, h, r, n=5):
    """A rounded rectangle's outline, counter-clockwise."""
    import math
    pts = []
    for ax, az, a0 in ((cx + w / 2 - r, cz - h / 2 + r, -90), (cx + w / 2 - r, cz + h / 2 - r, 0), (cx - w / 2 + r, cz + h / 2 - r, 90), (cx - w / 2 + r, cz - h / 2 + r, 180)):
        for i in range(n + 1):
            a = math.radians(a0 + 90 * i / n)
            pts.append((ax + r * math.cos(a), az + r * math.sin(a)))
    return pts


def controller_port(p, x0, x1, z0, z1, y, m, lobe_w=11.4, lobe_h=4.6, pitch=12.0, corner=0.6, cz=None):
    """A port: a black well with three small lobes in it, three contacts in each. The well is most of what you see."""
    cx0 = (x0 + x1) / 2
    cz = (z0 + z1) / 2 if cz is None else cz
    p.poly(rrect(cx0, (z0 + z1) / 2, x1 - x0, z1 - z0, corner), plane((0, y, 0), (1, 0, 0), (0, 0, 1)), m['dark'], depth=4)
    art = plane((0, y - 0.01, 0), (1, 0, 0), (0, 0, 1))
    art2 = plane((0, y - 0.03, 0), (1, 0, 0), (0, 0, 1))
    for i in (-1, 0, 1):
        cx = cx0 + i * pitch
        p.poly(stadium(cx, cz, lobe_w, lobe_h), art, m['portrim'], depth=0)
        p.poly(stadium(cx, cz, lobe_w - 1.0, lobe_h - 0.9), art2, m['portin'], depth=0)
        for k in (-1, 0, 1):
            xx = cx + k * (lobe_w - 4.4) / 2
            p.cyl((xx, y - 0.05, cz), 'y', 0.95, 0.02, m['portpin'], n=12, smooth=False)
            p.cyl((xx, y - 0.075, cz), 'y', 0.6, 0.02, m['dark'], n=12, smooth=False)


def usb_a(p, x0, x1, z0, z1, y, m, depth=8.0, shell=None, tongue=True):
    """A socket with a real inside: four thin walls, a black back, the tongue in its upper half and the two small bright contacts on its nose."""
    t = 0.3
    w = shell or m['silver']
    p.box(x0, x1, y, y + depth, z0, z0 + t, w)
    p.box(x0, x1, y, y + depth, z1 - t, z1, w)
    p.box(x0, x0 + t, y, y + depth, z0, z1, w)
    p.box(x1 - t, x1, y, y + depth, z0, z1, w)
    p.box(x0 + t, x1 - t, y + depth - 0.2, y + depth, z0 + t, z1 - t, m['dark'])
    if tongue:
        cz = (z0 + z1) / 2
        p.box(x0 + 1.2, x1 - 1.2, y + 1.4, y + depth - 0.2, cz + 0.15, cz + 1.25, m['black'])
        for f in (0.41, 0.82):
            xx = x0 + (x1 - x0) * f
            p.box(xx - 0.45, xx + 0.45, y + 1.37, y + 1.42, cz + 0.35, cz + 1.05, m['white'])


def screw_cap(p, y, z, m, x=0.0):
    """The rubber cap over a case screw on the left side."""
    p.poly(rrect(0, 0, 9.0, 10.0, 3.0), plane((x - 0.5, y, z), (0, -1, 0), (0, 0, 1)), m['rubber'], depth=0.6)
    p.cyl((x - 0.52, y, z), 'x', 1.6, 0.02, m['dark'], n=14, smooth=False)


def build(col, tex):
    m = materials(tex)
    parts = []

    # ---------------------------------------------------- the lid: the top plate, the fins and the upper shell
    lid = Part('lid', (0, 0, 300), 'The upper shell. The six plates and five slits are the look everyone remembers, and they run round the right end to the back.')
    lid.tile = {'fat_case': 3.0}
    lid.box(0, W, 0, D, PLATES[0][0], H, m['case'], bevel=1.4, seg=3)
    # under the lid's rounded front edge: a seam, then a black face down to the first slit
    lid.box(0.6, W - 0.6, -0.02, 0.8, 74.0, 74.7, m['dark'])
    lid.box(0.6, W - 0.6, -0.015, 0.8, PLATES[0][0], 74.0, m['fin'])
    # the logo and its name on the lid, measured: reading rear to front, 'up' towards the right end
    art = plane((0, D, H + 0.01), (0, -1, 0), (1, 0, 0))
    ps2_logo(lid, art, 28, 162, 1.0, 1.1, (m['logo_lo'], m['logo_mid'], m['logo_hi']))
    lid.text('PlayStation 2', 'segoeui.ttf', 14.0, plane((145.8, D - 90.8, H + 0.01), (0, -1, 0), (1, 0, 0)), m['ink'], align='CENTER', depth=0.03)
    # the disc logos, tone on tone, at the front right
    tone = mat('fat_tone', '#3f4045', rough=0.22)
    lid.text('PlayStation', 'segoeuib.ttf', 2.8, plane((211, 4.6, H + 0.01), (1, 0, 0), (0, 1, 0)), tone)
    lid.text('DVD', 'arialbd.ttf', 6.2, plane((230, 4.8, H + 0.01), (1, 0, 0), (0, 1, 0)), tone, stretch=1.25)
    lid.text('VIDEO', 'arialbd.ttf', 1.9, plane((231, 2.6, H + 0.01), (1, 0, 0), (0, 1, 0)), tone, stretch=1.2)
    lid.box(250, 261, 4, 10, H, H + 0.03, tone)
    lid.text('COMPACT', 'arialbd.ttf', 1.5, plane((250, 2.2, H + 0.01), (1, 0, 0), (0, 1, 0)), tone)
    lid.text('DVD', 'arialbd.ttf', 6.2, plane((265, 4.8, H + 0.01), (1, 0, 0), (0, 1, 0)), tone, stretch=1.25)
    lid.text('ROM', 'arialbd.ttf', 1.9, plane((267, 2.6, H + 0.01), (1, 0, 0), (0, 1, 0)), tone, stretch=1.2)

    # the fins round the right end, front to back (the front rows are laid out below)
    for z0, z1 in PLATES[1:]:
        lid.box(W - FIN_SIDE, W, 0, D, z0, z1, m['fin'], bevel=0.42, seg=2)
        # no shadows in a web render: the slit's floor and roof are dark themselves
        lid.box(W - FIN_SIDE, W - 0.5, 0, D, z1 - 0.01, z1 + 0.02, m['dark'])
        lid.box(W - FIN_SIDE, W - 0.5, 0, D, z0 - 0.02, z0 + 0.01, m['dark'])
    lid.box(W - FIN_SIDE, W - 0.5, 0, D, PLATES[0][0] - 0.02, PLATES[0][0] + 0.01, m['dark'])
    # behind the slits, the wall they are cut into
    wall = m['dark']
    lid.box(W - FIN_SIDE - 1.2, W - FIN_SIDE, 0, D, LOW_Z, PLATES[0][0], wall)
    # the left side is flat, the back above the lower block is flat
    lid.box(0, 1.6, 0, D, LOW_Z, PLATES[0][0], m['fin'], bevel=0.2)
    lid.box(1.6, 70.2, D - 1.6, D, LOW_Z, PLATES[0][0], m['fin'])
    lid.box(134, W - FIN_SIDE, D - 1.6, D, 40.1, PLATES[0][0], m['fin'])
    lid.box(134, 150.7, D - 1.6, D, LOW_Z, 40.1, m['fin'])
    lid.box(204.8, W - FIN_SIDE, D - 1.6, D, LOW_Z, 40.1, m['fin'])
    lid.box(150.7, 204.8, D - 1.6, D, LOW_Z, 32.0, m['fin'])
    # the seam round the rear plate
    lid.box(149.6, 150.2, D - 0.02, D + 0.02, 40, PLATES[0][0], m['dark'])
    # the front wall behind the front fins, leaving the tray's mouth open
    fy = FIN
    lid.box(1.6, TRAY[0], fy, fy + 1.2, LOW_Z, PLATES[0][0], wall)
    lid.box(TRAY[1], W - FIN_SIDE - 1.2, fy, fy + 1.2, LOW_Z, PLATES[0][0], wall)
    lid.box(TRAY[0], TRAY[1], fy, fy + 1.2, PLATES[2][1], PLATES[0][0], wall)
    lid.box(TRAY[0], TRAY[1], fy, fy + 1.2, LOW_Z, PLATES[3][0] + 0.5, wall)
    # front rows, each with the light its rounded top edge catches
    lid.box(0, W, 0.5, fy, PLATES[0][0] - 0.02, PLATES[0][0] + 0.01, m['dark'])
    plate = lambda i: PLATES[i]
    def row(x0, x1, i, p=lid, z=None):
        z0, z1 = z or plate(i)
        p.box(x0, x1, 0, fy, z0, z1, m['fin'], bevel=0.42, seg=2)
        p.box(x0 + 0.4, x1 - 0.4, -0.015, 0.3, z1 - 0.65, z1 - 0.25, m['edge_hi'])
        p.box(x0, x1, 0.5, fy, z1 - 0.01, z1 + 0.02, m['dark'])
        p.box(x0, x1, 0.5, fy, z0 - 0.02, z0 + 0.01, m['dark'])
    # row 1: full width to the buttons, carrying 1, MagicGate, 2
    row(0, BTN[0] - 1, 1)
    # row 2: the card doors sit in it, then the plate either side of the tray
    row(0, CARD1[0], 2)
    row(CARD1[1], CARD2[0], 2)
    row(CARD2[1], TRAY[0] - 0.4, 2)
    row(TRAY[1] + 0.4, NOSE, 2)
    # row 3: the plate left of the tray, and right of it
    row(0, TRAY[0] - 0.4, 3)
    row(TRAY[1] + 0.4, NOSE, 3)
    # row 4: the controller ports take its place, the rest runs on under the tray
    row(0, PORT1[0], 4)
    row(PORT1[1], PORT2[0], 4)
    row(PORT2[1], BTN[0] - 1, 4)
    # row 5, the thick one: the whole width
    row(0, W, 5)
    # a small ledge between the third row and the eject button
    row(BTN[0] - 1, NOSE, None, z=(47.6, 48.8))
    # the nose carries SONY, reading top to bottom; the slits narrow as they cross it
    for z0, z1 in ((66.9, 68.5), (61.8, 66.3), (56.0, 60.6), (48.8, 54.3), (41.2, 47.0)):
        lid.box(NOSE, W, -0.01, fy, z0, z1, m['fin'], bevel=0.42, seg=2)
    lid.text('SONY', 'georgiab.ttf', 7.1, plane((292.6, -0.03, 66.4), (0, 0, -1), (1, 0, 0)), m['white'], depth=0.02, stretch=1.36)
    # front labels on row 1, tone on tone
    lid.text('1', 'arial.ttf', 3.9, plane((41, -0.02, 64.95), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    lid.text('2', 'arial.ttf', 3.9, plane((93, -0.02, 64.95), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    lid.text('MAGICGATE', 'georgiab.ttf', 2.9, plane((66.5, -0.02, 65.2), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER', stretch=0.98)
    # the rubber screw caps on the left side
    for y, z in ((30, 66), (D - 7, 66)):
        screw_cap(lid, y, z, m)
    parts.append(lid)

    # ---------------------------------------------------- the back of the upper shell, printed
    rear = lid
    # the rating print and its small print: one picture, the case's own colour behind it
    rear.quad_on(plane((281, D + 0.03, 41), (-1, 0, 0), (0, 0, 1)), 131, 30, m['rating'])
    rear.box(154.8, 202.4, D, D + 0.05, 56.9, 68.8, m['grey'])
    # the column of print down the left end of the back, reading upwards
    rear.quad_on(plane((1.4, D + 0.03, 3), (0, 0, 1), (1, 0, 0)), 60, 11, m['rating_side'])
    rear.cyl((285, D, 57), 'y', 1.7, 0.06, m['dark'], n=14, smooth=False)
    for x0, x1, z0, z1 in ((54.6, 55, 37.4, 71.9), (23.4, 23.8, 37.4, 71.9), (23.4, 55, 37.4, 37.8), (134, 134.6, 40, 71.9)):
        rear.box(x0, x1, D, D + 0.02, z0, z1, m['dark'])

    # ---------------------------------------------------- the tray: door, deck, disc
    tray = Part('tray', (40, -190, 118), 'The disc tray. It opens on command in RIPPCSX2 too, and a game image in the virtual drive reads like the disc it came from.')
    # its door is the middle of rows 2 and 3, slit between them
    row(TRAY[0], TRAY[1], 2, p=tray)
    row(TRAY[0], TRAY[1], 3, p=tray)
    tray.box(TRAY[0] + 0.5, TRAY[1] - 0.5, fy, fy + 1.0, PLATES[3][0], PLATES[2][1], m['shell'])
    # the deck with its disc well
    deck_z = 50.2
    tray.box(TRAY[0] + 1, TRAY[1] - 1, fy + 1, 150, deck_z - 1, deck_z, m['drive'])
    tray.ring((209, 85, deck_z), 'z', 60.5, 66, 0.9, m['drive'], n=72)
    tray.cyl((209, 85, deck_z), 'z', 60, 0.3, m['black'], n=72)
    tray.box(195, 223, 110, 150, deck_z, deck_z + 0.2, m['dark'])
    # the PS mark on its tile, on the tray's face
    tray.poly(rrect(213, 53.6, 12.6, 8.4, 3.6), plane((0, -0.02, 0), (1, 0, 0), (0, 0, 1)), m['blackgloss'], depth=0.6)
    ps_badge(tray, 213, -0.05, 53.55, 1.55, m)
    parts.append(tray)

    # a game: the disc itself comes out with the tray
    disc = Part('disc', (40, -120, 205), 'A DVD. Most of the PS2 library is one disc image away, and the end goal of RIPPCSX2 is the whole library running through OPL\'s own code path.', spin=2.0)
    disc.disc((209, 85, 50.8), 60, 1.2, m['disc'])
    disc.cyl((209, 85, 52.01), 'z', 7.5, 0.05, m['dark'], n=32)
    parts.append(disc)

    # ---------------------------------------------------- the card slots and controller ports (the controller board)
    ctrl = Part('controller_board', (-70, -170, -8), 'Controllers and memory cards. RIPPCSX2 keeps every card image as a file, so a save can be read, written and compared from a script.')
    for c in (CARD1, CARD2):
        # the slot's door, its lit top edge, the print on it and the small lip under it
        ctrl.box(c[0] + 0.2, c[1] - 0.2, 0.2, fy, PLATES[2][0], 61.3, m['blackgloss'], bevel=0.25)
        ctrl.box(c[0] + 0.6, c[1] - 0.6, 0.17, 0.3, 60.6, 61.1, m['edge_hi'])
        ctrl.box(c[0] + 0.2, c[1] - 0.2, 0.2, fy, 55.8, 56.75, m['blackgloss'])
        ctrl.text('MEMORY CARD', 'arial.ttf', 4.0, plane((c[0] + 20.1, 0.16, 57.45), (1, 0, 0), (0, 0, 1)), m['doorprint'], align='CENTER')
    for c in (PORT1, PORT2):
        controller_port(ctrl, c[0], c[1], PORT_Z[0], PORT_Z[1], 0.8, m, cz=44.6)
    ctrl.box(10, 125, fy + 2, 34, 36.4, 37.0, m['pcb'])
    for c in (PORT1, PORT2):
        ctrl.box(c[0] - 1, c[1] + 1, 4, 30, PORT_Z[0], PORT_Z[1], m['black'])
    for c in (CARD1, CARD2):
        ctrl.box(c[0] - 1, c[1] + 1, 4, 44, PLATES[2][0], PLATES[2][1], m['black'])
    parts.append(ctrl)

    # ---------------------------------------------------- the buttons
    btn = Part('buttons', (95, -150, 62), 'Reset and eject on a flex cable. Exit an ELF, power off from a menu, or reset the VM with the same result as this button.')
    btn.box(BTN[0], BTN[1], 0.5, fy, 61.2, 71.0, m['teal'], bevel=0.3)
    # the power mark and RESET
    pw = plane((284.5, 0.46, 67.4), (1, 0, 0), (0, 0, 1))
    btn.ring((284.5, 0.46, 67.6), 'y', 1.6, 1.9, 0.05, m['tealglow'], n=24)
    btn.box(284.36, 284.64, 0.42, 0.5, 67.6, 69.9, m['tealglow'])
    btn.text('RESET', 'arial.ttf', 1.9, plane((284.5, 0.44, 61.9), (1, 0, 0), (0, 0, 1)), m['tealglow'], align='CENTER')
    btn.box(BTN[0], BTN[1], 0.5, fy, 40.6, 46.9, m['bluebtn'], bevel=0.3)
    ej = plane((284.5, 0.46, 42.4), (1, 0, 0), (0, 0, 1))
    # the eject mark in outline: a triangle's two rising sides and its base, the bar under it
    btn.poly([(-2.2, -0.1), (2.2, -0.1), (2.2, 0.2), (-2.2, 0.2)], ej, m['blueglow'], depth=0.04)
    btn.poly([(-2.2, -0.1), (-1.85, -0.1), (0.15, 2.45), (-0.15, 2.65)], ej, m['blueglow'], depth=0.04)
    btn.poly([(2.2, -0.1), (1.85, -0.1), (-0.15, 2.45), (0.15, 2.65)], ej, m['blueglow'], depth=0.04)
    btn.box(282.4, 286.6, 0.42, 0.5, 41.5, 41.85, m['blueglow'])
    btn.box(279, 290, fy + 1.3, fy + 1.6, 36, 71, m['flex'])
    parts.append(btn)

    # ---------------------------------------------------- the lower block
    base = Part('base', (0, 0, -125), 'The lower shell, with the long vent under the tray and the fan\'s grille at the back.')
    bm = m['fin']
    base.box(0, LOW_X, LOW_Y, D, BOT, BOT + 1.6, m['shell'])
    # the front wall: blue panel opening, the vent, plain the rest of the way
    fw0, fw1 = LOW_Y, LOW_Y + 1.6
    base.box(0, 7, fw0, fw1, BOT, LOW_Z, bm, bevel=0.2)
    base.box(43.5, 57, fw0, fw1, BOT, LOW_Z, bm)
    base.box(245.5, LOW_X, fw0, fw1, BOT, LOW_Z, bm)
    base.box(7, 43.5, fw0, fw1, BOT, 5.8, bm)
    base.box(7, 43.5, fw0, fw1, 25.0, LOW_Z, bm)
    base.box(57, 245.5, fw0, fw1, BOT, 7.8, bm)
    base.box(57, 245.5, fw0, fw1, 22.0, LOW_Z, bm)
    ladder(base, 57, 245.5, 7.8, 22.0, fw0, fw1, 5, 15, 0.72, bm, m['dark'])
    # the duct behind the vent, so nothing inside can be seen lit through it
    base.box(55, 247.5, LOW_Y + 6, LOW_Y + 6.2, BOT, LOW_Z, m['dark'])
    base.box(55, 247.5, fw1, LOW_Y + 6, BOT + 1.6, 7.2, m['dark'])
    base.box(55, 247.5, fw1, LOW_Y + 6, 22.6, LOW_Z, m['dark'])
    base.box(55, 56.4, fw1, LOW_Y + 6, BOT + 1.6, LOW_Z, m['dark'])
    base.box(246.1, 247.5, fw1, LOW_Y + 6, BOT + 1.6, LOW_Z, m['dark'])
    # the top of that wall: a ridge that catches the light, and above it the shade under the plates
    base.box(0.5, LOW_X - 0.5, LOW_Y - 0.015, LOW_Y + 0.2, 27.9, 28.5, m['edge_hi'])
    base.box(0.5, LOW_X - 0.5, LOW_Y - 0.015, LOW_Y + 0.2, 28.8, LOW_Z, m['dark'])
    # the sides
    base.box(0, 1.6, LOW_Y, D, BOT, LOW_Z, bm, bevel=0.2)
    base.box(LOW_X - 1.6, LOW_X, LOW_Y, D, BOT, LOW_Z, bm, bevel=0.2)
    # the back: the fan's opening and the bay's stay open, the rest is solid
    b0, b1 = D - 1.6, D
    base.box(0, 70.2, b0, b1, BOT, LOW_Z, bm)
    base.box(134, 150, b0, b1, BOT, LOW_Z, bm)
    base.box(257.6, LOW_X, b0, b1, BOT, LOW_Z, bm)
    base.box(70.2, 134, b0, b1, BOT, 11.2, bm)
    base.box(150, 257.6, b0, b1, BOT, 3.5, bm)
    # rear connectors' frames, tone on tone, and the seams that join them
    frame = m['black']
    rim = m['rimdark']
    def framed(x0, x1, z0, z1, t=0.45):
        for a0, a1, b0_, b1_ in ((x0, x1, z0, z0 + t), (x0, x1, z1 - t, z1), (x0, x0 + t, z0, z1), (x1 - t, x1, z0, z1)):
            base.box(a0, a1, D + 0.2, D + 0.3, b0_, b1_, rim)
    for x0, x1, z0, z1 in ((39.3, 50, 14.6, 15.0), (61, 70.7, 14.6, 15.0), (70.7, 139, 8.6, 9.0), (134, 134.6, 11.2, LOW_Z)):
        base.box(x0, x1, D, D + 0.02, z0, z1, m['dark'])
    # AV multi out
    framed(14, 39, 8.3, 18.3)
    base.box(14, 39, D + 0.0, D + 0.25, 8.3, 18.3, frame)
    base.box(15.4, 37.6, D + 0.22, D + 0.27, 9.7, 16.9, m['dark'])
    base.box(17.6, 35.4, D + 0.24, D + 0.3, 11.6, 14.6, m['portface'])
    for i in range(12):
        base.box(18.4 + i * 1.3, 19.0 + i * 1.3, D + 0.28, D + 0.32, 12.4, 13.8, m['steel'])
    # the optical port
    framed(50, 61, 8.3, 20.7)
    base.box(50, 61, D + 0.0, D + 0.25, 8.3, 20.7, frame)
    base.box(51.3, 59.7, D + 0.22, D + 0.27, 9.6, 19.4, m['dark'])
    base.box(53, 58, D + 0.24, D + 0.3, 11.2, 17.8, m['portface'])
    base.box(54.6, 56.4, D + 0.28, D + 0.33, 12.6, 16.4, m['dark'])
    base.cyl((43, D, 24.5), 'y', 1.3, 0.2, m['dark'], n=12)
    for y in (30, D - 7):
        screw_cap(base, y, 12, m)
    # feet
    for x, y in ((12, 34), (262, 34), (12, 170), (262, 170)):
        base.cyl((x, y, 0), 'z', 4.5, BOT, m['rubber'], n=14)
    parts.append(base)

    # ---------------------------------------------------- blue USB and i.LINK panel
    usb = Part('usb_board', (-75, -120, -70), 'USB and i.LINK. The ports OPL loads games over, and the ones a lab drives from a file instead of a stick.')
    # the panel, around the real holes its sockets sit in
    u0, u1 = LOW_Y - 0.5, LOW_Y + 2
    for x0, x1, z0, z1 in ((7, 10.6, 5.8, 25), (24, 30.5, 5.8, 25), (37.5, 43.5, 5.8, 25), (10.6, 24, 5.8, 12.4), (10.6, 24, 18.2, 19.9), (10.6, 24, 24.7, 25), (30.5, 37.5, 5.8, 19.4), (30.5, 37.5, 24.6, 25)):
        usb.box(x0, x1, u0, u1, z0, z1, m['blue'])
    usb_a(usb, 10.6, 24, 12.4, 18.2, LOW_Y - 0.45, m)
    usb_a(usb, 10.6, 24, 19.9, 24.7, LOW_Y - 0.45, m)
    usb_a(usb, 30.5, 37.5, 19.4, 24.6, LOW_Y - 0.45, m, depth=4.0, tongue=False)
    # the print on it reads upwards
    usb.text('USB', 'arial.ttf', 1.9, plane((27.2, LOW_Y - 0.53, 12.8), (0, 0, 1), (-1, 0, 0)), m['bluetext'])
    usb.text('S400', 'arial.ttf', 1.9, plane((36.8, LOW_Y - 0.53, 12.8), (0, 0, 1), (-1, 0, 0)), m['bluetext'])
    usb.box(9, 42, LOW_Y + 2, LOW_Y + 26, 5, 6.4, m['pcb'])
    parts.append(usb)

    # ---------------------------------------------------- the drive
    drv = Part('dvd_drive', (40, 25, 215), 'The DVD drive. RIPPCSX2 stands in for it with an image file, and it is where disc timing and OPL\'s compatibility modes meet.')
    dz0, dz1 = 44.0, 69.0
    drv.box(136, 283, 8, 170, dz0, dz0 + 1.2, m['drive'])
    drv.box(136, 283, 8, 170, dz1 - 1.2, dz1, m['drive'], bevel=0.3)
    drv.box(136, 138, 8, 170, dz0, dz1, m['drive'])
    drv.box(281, 283, 8, 170, dz0, dz1, m['drive'])
    drv.box(136, 283, 168, 170, dz0, dz1, m['drive'])
    # vent slots across the top, and its warning sticker
    for i in range(12):
        drv.box(150, 270, 118 + i * 3.6, 119.8 + i * 3.6, dz1 - 0.02, dz1 + 0.02, m['dark'])
    drv.textured_quad(232, 276, 70, 92, dz1 + 0.05, m['laser'])
    drv.ring((209, 85, dz1), 'z', 8, 14, 0.3, m['steel'], n=36)
    drv.cyl((209, 85, dz0 + 3), 'z', 6, 6, m['steel'], n=24)
    # the pickup rails and lens under the deck
    drv.box(170, 172, 90, 160, dz0 + 3, dz0 + 5, m['steel'])
    drv.box(246, 248, 90, 160, dz0 + 3, dz0 + 5, m['steel'])
    drv.box(195, 223, 120, 146, dz0 + 3, dz0 + 8, m['black'])
    drv.cyl((209, 133, dz0 + 8), 'z', 2.2, 0.5, m['chipprint'], n=16)
    parts.append(drv)

    # ---------------------------------------------------- the shields
    top = Part('top_shield', (-20, 10, 135), 'The top shield over the board.')
    top.box(5, 270, 14, 176, 41.2, 41.7, m['zinc'])
    for x, y in ((9, 19), (266, 19), (9, 171), (266, 171)):
        top.box(x - 4, x + 4, y - 4, y + 4, 36, 41.2, m['zinc'])
    for i in range(14):
        top.box(20 + i * 8, 24 + i * 8, 80, 150, 41.68, 41.74, m['steel'])
    parts.append(top)

    bot = Part('bottom_shield', (0, 0, -72), 'The bottom shield, which also grounds the board.')
    bot.box(5, 148, LOW_Y + 7, 176, 3.2, 3.7, m['zinc'])
    bot.box(148, 268, LOW_Y + 7, 58, 3.2, 3.7, m['zinc'])
    for x in (5, 147.5):
        bot.box(x, x + 0.5, LOW_Y + 7, 176, 3.7, 25, m['zinc'])
    parts.append(bot)

    # ---------------------------------------------------- the main board
    brd = Part('main_board', (-10, 0, 55), 'The main board. The Emotion Engine, the Graphics Synthesizer, the RDRAM and the IOP: everything RIPPCSX2 is emulating and everything a compatibility test exercises.')
    bz = 31.0
    brd.box(6, 270, 15, 176, bz - 1.5, bz - 0.02, m['pcb'])
    brd.textured_quad(6, 270, 15, 176, bz, m['board'])
    # the board's own edge print and chips, placed where the real ones sit
    # EE: the big silver lid
    brd.box(52, 108, 79, 134, bz, bz + 1.6, m['chip'])
    brd.box(55, 105, 82, 131, bz + 1.6, bz + 2.5, m['chiplid'], bevel=0.3)
    brd.text('EE', 'arialbd.ttf', 12, plane((80, 96, bz + 2.53), (1, 0, 0), (0, 1, 0)), m['chipdark'], align='CENTER', depth=0.02)
    brd.text('Emotion Engine', 'arial.ttf', 3.4, plane((80, 90, bz + 2.53), (1, 0, 0), (0, 1, 0)), m['chipdark'], align='CENTER', depth=0.02)
    # GS: the black square above it
    brd.box(56, 92, 134, 168, bz, bz + 1.8, m['chip'], bevel=0.2)
    brd.text('GS', 'arialbd.ttf', 8, plane((74, 151, bz + 1.83), (1, 0, 0), (0, 1, 0)), m['chipprint'], align='CENTER', depth=0.02)
    brd.text('Graphics Synthesizer', 'arial.ttf', 2.2, plane((74, 146, bz + 1.83), (1, 0, 0), (0, 1, 0)), m['chipprint'], align='CENTER', depth=0.02)
    # two RDRAM packages at the left of the EE
    for y in (84, 111):
        brd.box(27, 47, y, y + 18, bz, bz + 1.5, m['chiplid'], bevel=0.2)
    # the IOP, lower down
    brd.box(82, 112, 48, 74, bz, bz + 1.6, m['chip'], bevel=0.2)
    brd.text('IOP', 'arialbd.ttf', 5, plane((97, 62, bz + 1.63), (1, 0, 0), (0, 1, 0)), m['chipprint'], align='CENTER', depth=0.02)
    # the DVD and sound chips
    brd.box(186, 208, 136, 158, bz, bz + 1.4, m['chip'], bevel=0.2)
    brd.box(40, 80, 44, 56, bz, bz + 1.2, m['chip'])
    brd.box(170, 186, 74, 90, bz, bz + 1.2, m['chip'], bevel=0.15)
    # the clock battery and the caps
    brd.cyl((144, 118, bz), 'z', 10, 3.2, m['cell'], n=36)
    brd.text('CR2032', 'arial.ttf', 3, plane((144, 118, bz + 3.22), (1, 0, 0), (0, 1, 0)), m['chipdark'], align='CENTER', depth=0.02)
    for x, y, r, h in ((122, 130, 3.2, 6), (122, 112, 3.2, 6), (140, 92, 3, 5.5), (132, 90, 3, 5.5), (118, 86, 2.6, 5), (22, 150, 3.2, 7), (30, 152, 3.2, 7), (22, 160, 3.2, 7), (120, 148, 2.6, 5), (156, 136, 2.6, 5)):
        brd.cyl((x, y, bz), 'z', r, h, m['cap'], n=16)
        brd.cyl((x, y, bz + h), 'z', r * 0.72, 0.04, m['ferrite'], n=12, smooth=False)
    for x, y in ((138, 72, ), (146, 72)):
        brd.box(x, x + 7, y, y + 7, bz, bz + 3.5, m['ferrite'], bevel=0.3)
    # the bay's edge connector, the connector the network adapter plugs into
    brd.box(156, 202, D - 12, D - 2, 33, 39, m['black'])
    brd.box(150.9, 204.6, D - 1.62, D - 1.4, 33.4, 39.8, m['peach'])
    brd.poly(stadium(177.3, 36.6, 40.6, 4.6), plane((0, D - 1.39, 0), (-1, 0, 0), (0, 0, 1)) @ Matrix.Translation((-354.6, 0, 0)), m['chip'], depth=0)
    brd.poly(stadium(177.3, 36.6, 38.2, 2.4), plane((0, D - 1.37, 0), (-1, 0, 0), (0, 0, 1)) @ Matrix.Translation((-354.6, 0, 0)), m['portin'], depth=0)
    brd.box(150.9, 204.6, D - 1.62, D - 1.2, 32.0, 33.2, m['silver'])
    # the flat cable up to the drive
    brd.box(120, 136, 60, 60.3, bz, 43.8, m['flex'])
    parts.append(brd)

    # ---------------------------------------------------- the power board, its sheet and its inlet
    psu = Part('power_board', (-120, 40, -30), 'The power board and the fat\'s own mains inlet: the slim moved all of this into a brick.')
    pz = 9.0
    psu.box(8, 68, 92, 176, pz - 1.4, pz - 0.02, m['pcb'])
    psu.textured_quad(8, 68, 92, 176, pz, m['psu'])
    psu.cyl((38, 120, pz), 'z', 8.5, 16, m['ferrite'], n=24)
    psu.cyl((38, 120, pz + 16), 'z', 8.5, 0.05, m['cap'], n=24, smooth=False)
    psu.cyl((22, 150, pz), 'z', 5, 14, m['capblue'], n=20)
    psu.cyl((52, 150, pz), 'z', 5, 14, m['capblue'], n=20)
    psu.box(44, 62, 104, 122, pz, pz + 14, m['ferrite'], bevel=0.4)
    psu.box(15, 28, 100, 112, pz, pz + 11, m['capgold'], bevel=0.3)
    parts.append(psu)

    inlet = Part('power_inlet', (-100, 120, 45), 'The rocker and the mains inlet.')
    # the inlet's block and the rocker's, one above the other, as dark frames
    inlet.box(25, 53.6, D - 0.8, D + 0.1, 38.6, 52.9, m['block'], bevel=0.25)
    inlet.box(25, 53.6, D - 0.8, D + 0.1, 54.0, 71.9, m['block'], bevel=0.25)
    for a0, a1, b0_, b1_ in ((25, 53.6, 38.6, 39), (25, 53.6, 52.5, 52.9), (25, 25.4, 38.6, 52.9), (53.2, 53.6, 38.6, 52.9), (25, 53.6, 54, 54.4), (25, 53.6, 71.5, 71.9), (25, 25.4, 54, 71.9), (53.2, 53.6, 54, 71.9)):
        inlet.box(a0, a1, D + 0.1, D + 0.16, b0_, b1_, m['rimdark'])
    # the mouth: two lobes and the bar between them, a prong in each
    inlet.box(35, 43.6, D - 0.1, D + 0.12, 42.1, 49.9, m['ink'])
    for x in (35, 43.6):
        inlet.cyl((x, D + 0.12, 46), 'y', 3.9, -0.2, m['ink'], n=24)
        inlet.cyl((x, D + 0.12, 46), 'y', 0.95, 0.06, m['silver'], n=12)
        inlet.cyl((x, D + 0.18, 46), 'y', 0.4, 0.02, m['dark'], n=8)
    # the rocker, I and O
    inlet.box(29.8, 48.8, D - 0.82, D + 0.8, 56.4, 68.8, m['rocker'], bevel=0.5)
    inlet.box(43.3, 43.9, D + 0.78, D + 0.84, 60.2, 63.8, m['white'])
    inlet.ring((35.0, D + 0.78, 62), 'y', 0.85, 1.3, 0.06, m['white'], n=16)
    inlet.box(25, 53.6, D - 26, D - 0.8, 40, 71, m['black'])
    parts.append(inlet)

    # ---------------------------------------------------- the fan
    fan = Part('fan', (-30, 150, 40), 'The fan, and the grille it breathes through. The emulator keeps a game cool by other means.', spin=1.6)
    fc = (101, D - 13, 42)
    parts_fan_body(fan, m)
    parts.append(fan)

    # ---------------------------------------------------- the expansion bay
    bay = Part('expansion_bay', (120, 130, -40), 'The expansion bay, the home of the network adapter and a hard drive. OPL in RIPPCSX2 reads its games from a virtual one.')
    # no shadows in a web render, so the shade the deep end of the bay stands in is in its materials
    zones = ((D - 20, D - 1, m['bay1']), (D - 45, D - 20, m['bay2']), (D - 75, D - 45, m['bay3']), (60, D - 75, m['bay4']))
    for y0_, y1_, zm in zones:
        bay.box(150, 257.6, y0_, y1_, 3, 3.6, zm)
        for x in (150, 257):
            bay.box(x, x + 0.6, y0_, y1_, 3.6, 31, zm)
    bay.box(150, 257.6, 60, 60.6, 3.6, 31, m['bay4'])
    bay.box(150, 257.6, 60, D - 1.2, 30.4, 31.0, m['dark'])
    # its holes
    for j in range(11):
        for i in range(11):
            x = 155.5 + i * 10 + (j % 2) * 5
            if x < 254:
                bay.cyl((x, 72 + j * 9, 3.62), 'z', 2.2, 0.04, m['dark'], n=12, smooth=False)
    # the lip at its mouth: two slots and a warning triangle
    for x0, x1 in ((226, 233), (167, 175)):
        bay.box(x0, x1, 175.5, 176.3, 3.6, 3.68, m['dark'])
    tri = plane((199.6, 177.5, 3.68), (1, 0, 0), (0, 1, 0))
    bay.poly([(-6, 0), (6, 0), (6, 0.5), (-6, 0.5)], tri, m['dark'], depth=0.02)
    bay.poly([(-6, 0), (-5.3, 0), (0.3, 5.2), (-0.3, 5.2)], tri, m['dark'], depth=0.02)
    bay.poly([(5.3, 0), (6, 0), (0.3, 5.2), (-0.3, 5.2)], tri, m['dark'], depth=0.02)
    # the two bright screw tabs either side of the mouth
    for x0, x1, z0, z1 in ((257.6, 266.7, 12.4, 29.0), (141.2, 149.5, 11.7, 28.3)):
        bay.box(x0, x1, D - 0.5, D + 0.05, z0, z1, m['tab'])
        bay.cyl(((x0 + x1) / 2, D + 0.06, (z0 + z1) / 2), 'y', 1.5, 0.05, m['dark'], n=12, smooth=False)
    parts.append(bay)

    # the sheet between the power board and the shield
    sheet = Part('isolation_sheet', (-115, 40, 42), 'The clear insulating sheet.', spin=0.4)
    sheet.box(7, 69, 90, 177, 29.2, 29.45, m['foil'])
    parts.append(sheet)

    return [p.finish(col) for p in parts]


def parts_fan_body(fan, m):
    y0, y1 = D - 25, D - 4
    cx, cz = 101, 42
    # the frame
    fan.box(70, 134.5, y0, y1, 11, 73, m['fan'])
    fan.cyl((cx, y1 + 0.02, cz), 'y', 26, 0.02, m['dark'], n=48, smooth=False)
    fan.cyl((cx, y1 - 18, cz), 'y', 9.5, 19, m['fan'], n=24)
    # the blades
    import math
    for i in range(7):
        a = i * 2 * math.pi / 7
        c, s = math.cos(a), math.sin(a)
        art = plane((cx, y1 + 0.05, cz), (c, 0, s), (-s, 0, c))
        fan.poly([(8.5, -3), (25, -7), (25, 6), (8.5, 3)], art, m['fan'], depth=0.3)
    # the grille: seven rows of slots between thick ribs, three thin uprights, the corners filled to an octagon
    bx0, bx1, bz0, bz1 = 70.2, 134.0, 11.2, 72.6
    rib = 3.2
    for i in range(8):
        z = bz0 + rib / 2 + i * (bz1 - bz0 - rib) / 7
        fan.box(bx0, bx1, D - 2.4, D + 0.02, z - rib / 2, z + rib / 2, m['fin'])
    for x, hw in ((bx0 + 0.5, 0.5), (85.7, 1.2), (100.0, 1.2), (116.7, 1.2), (bx1 - 0.5, 0.5)):
        fan.box(x - hw, x + hw, D - 2.4, D + 0.0, bz0, bz1, m['fin'])
    corner = plane((0, D - 0.4, 0), (-1, 0, 0), (0, 0, 1))
    for cx0, cz0, dx, dz in ((bx0, bz0, 1, 1), (bx1, bz0, -1, 1), (bx0, bz1, 1, -1), (bx1, bz1, -1, -1)):
        tri = [(-cx0, cz0), (-(cx0 + dx * 11), cz0), (-cx0, cz0 + dz * 11)]
        if dx * dz > 0:
            tri = tri[::-1]
        fan.poly(tri, corner, m['fin'], depth=0.2)
