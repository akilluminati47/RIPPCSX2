# The fat PlayStation 2 (SCPH-30001 / 39001 era): 301 x 182 x 78 mm from Sony's manual. Every position below was measured
# from photographs rectified through a solved camera (see compare.py). The insides follow a real teardown: lid, tray, drive,
# shields, main board, power board, fan, expansion bay, the controller board, the USB board and the button flex.
from mathutils import Matrix, Vector
from ps2kit import Part, mat, plane, export_glb
import ps_mark
from marks import MARKS

W, D, H = 301, 182, 78
LOW_X = 274.5          # the lower block stops short of the right end
LOW_Y = 14             # and sits back from the front
BOT = 1.5              # it stands on feet: 78 mm is to the bottom of the feet
FIN_SIDE = 2.7         # how deep the slits cut on the right and left ends
LEFT_FIN = 14.5        # the slits wrap the left end too, this far back from the front, then the flat side wall starts
PORT_Z = (42.6, 47.7)  # the controller ports take the place of the fourth plate
LOW_Z = 35.8           # the seam between the shell and the lower block
FIN = 6.0              # how deep the slits cut on the front
SLITS = (71.35, 63.8, 56.25, 48.7, 41.15)
GAP = 3.3
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
        slot=mat('edge_slot', '#4d4742', rough=0.55),
        portpin=mat('port_pin', '#9a9ba0', rough=0.45),
        doorprint=mat('fat_door_print', '#7f8187', rough=0.6),
        rocker=mat('rocker', '#17181b', rough=0.4, spec=0.4),
        block=mat('rear_block', '#0e0f11', rough=0.5),
        plug_plate=mat('plug_plate', '#1d1d20', rough=0.55),
        plug_well=mat('plug_well', '#121214', rough=0.75),
        plug_pin=mat('plug_pin', '#e4e4df', rough=0.3, metal=0.25),
        plug_shaft=mat('plug_shaft', '#17171a', rough=0.5),
        scoop=mat('side_scoop', '#101114', rough=0.6),
        rimdark=mat('rim_dark', '#303136', rough=0.5),
        edge_hi=mat('edge_hi', '#a5a6ac', rough=0.3),
        edge_hi2=mat('edge_hi2', '#4a4b50', rough=0.3),
        blackgloss=mat('black_gloss', '#0a0a0c', rough=0.16),
        tab=mat('bay_tab', '#8f8d8c', rough=0.5, metal=0.15),
        bay_floor=mat('bay_floor', tex=tex + 'bay_floor.jpg', rough=0.8),
        bay_wall=mat('bay_wall', tex=tex + 'bay_wall.jpg', rough=0.8),
        bay_rim1=mat('bay_rim_lit', '#3b3c3f', rough=0.6),
        bay_rim2=mat('bay_rim_mid', '#1c1c1e', rough=0.7),
        bay_rim3=mat('bay_rim_deep', '#0c0c0d', rough=0.8),
        bay_press=mat('bay_press', '#050506', rough=0.8),
        bay_edge=mat('bay_edge', '#6a6b6f', rough=0.5),
        bay4=mat('bay_deep', '#111213', rough=0.9),
        white=mat('print_white', '#dcdde2', rough=0.5),
        grey=mat('sticker_grey', '#d8d8d8', rough=0.7),
        black=mat('plastic_black', '#0c0c0e', rough=0.45),
        rubber=mat('rubber', '#0a0a0b', rough=0.9),
        lid_floor=mat('fat_scoop_floor', '#1e1e20', rough=0.68),
        lid_lip=mat('fat_scoop_lip', '#6a6c74', rough=0.4),
        sony_hi=mat('fat_sony', '#b6b8bc', rough=0.38),
        rear_tone=mat('fat_rear_tone', '#2e2f34', rough=0.55),
        usb_print=mat('fat_usb_print', '#99a3bf', rough=0.55),
        lid_shade=mat('fat_scoop_shade', '#000000', rough=0.9, spec=0.0),
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
        rating=mat('rear_rating', tex=tex + 'rating.jpg', rough=0.3),
        serial=mat('rear_serial', tex=tex + 'serial.jpg', rough=0.5),
        foot=mat('fat_foot', '#232326', rough=0.52),
        raise_top=mat('fat_raise_top', '#1c1d20', rough=0.62),
        raise_lit=mat('fat_raise_lit', '#3d3f46', rough=0.45),
        raise_shade=mat('fat_raise_shade', '#030304', rough=0.9, spec=0.0),
        net_screw=mat('net_screw', '#44464c', rough=0.24, metal=0.75),
        net_well=mat('net_well', '#26272b', rough=0.6),
        conn=mat('hdd_conn_shell', tex=tex + 'conn_shell.jpg', rough=0.55),
        conn_rim=mat('hdd_conn_rim', '#dcd2c0', rough=0.3, metal=0.5),
        conn_mouth=mat('hdd_conn_mouth', '#050506', rough=0.7),
        conn_tongue=mat('hdd_conn_tongue', '#2a2a31', rough=0.42),
        conn_pin=mat('hdd_conn_pin', '#b58c4e', rough=0.35, metal=0.7),
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


def ps_badge(p, cx, y, cz, width, m, body=True):
    """The PlayStation mark, `width` mm wide, centred on (cx, cz), its back at y. On the fat it is an object, not print: a black emblem
    die-cut to the mark's silhouette, standing proud across the fins, the four colours laid on it and the P a step above them. The outlines
    are the mark's own curves (ps_mark.py). With body=False the colours sit straight on whatever is behind them."""
    gloss = dict(rough=0.2)
    inks = {'#f3c202': mat('ps_yellow_gloss', '#f7c312', **gloss), '#00aa9e': mat('ps_teal', '#10b8a6', **gloss),
            '#326db3': mat('ps_blue_gloss', '#3a7fe0', **gloss), '#de0029': mat('ps_red_gloss', '#e4002b', **gloss)}
    face = y - (1.7 if body else 0.0)
    if body:
        p.curve([ps_mark.BODY], width, plane((cx, y - 0.85, cz), (1, 0, 0), (0, 0, 1)), m['blackgloss'], 1.7, bevel=0.26)
    for fill, outlines in ps_mark.COLOURS.items():
        red = fill == '#de0029'
        # the S lies on the emblem, the P a step proud of it
        p.curve(outlines, width, plane((cx, face - (0.17 if red else 0.05), cz), (1, 0, 0), (0, 0, 1)), inks[fill], 0.32 if red else 0.1)


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


def capsule(a, b, r0, r1=None, n=5):
    """A rounded bar's outline from a to b, tapering from r0 to r1."""
    import math
    r1 = r0 if r1 is None else r1
    t = math.atan2(b[1] - a[1], b[0] - a[0])
    pts = []
    for c, r, t0 in ((a, r0, t + math.pi / 2), (b, r1, t - math.pi / 2)):
        for i in range(n + 1):
            f = t0 + math.pi * i / n
            pts.append((c[0] + r * math.cos(f), c[1] + r * math.sin(f)))
    return pts


def tab_outline(fold, out, z0, z1, r, n=4):
    """A screw tab's outline as (-x, z): square along the fold, rounded at its two free corners."""
    import math
    s = 1 if out > fold else -1
    pts = [(fold, z0)]
    for i in range(n + 1):
        a = math.pi / 2 * i / n
        pts.append((out - s * r + s * r * math.sin(a), z0 + r - r * math.cos(a)))
    for i in range(n + 1):
        a = math.pi / 2 * i / n
        pts.append((out - s * r + s * r * math.cos(a), z1 - r + r * math.sin(a)))
    pts.append((fold, z1))
    return [(-x, z) for x, z in pts]


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


def raised(p, draw, m):
    """Moulded print standing proud, as on the back: lit along its top, a shadow along its bottom. draw(dx, dz, dy, material) makes one copy."""
    draw(-0.13, -0.13, 0.004, m['raise_shade'])
    draw(0.06, 0.06, 0.008, m['raise_lit'])
    draw(0, 0, 0.014, m['raise_top'])


def sunk(p, draw, m):
    """Print pressed in, as on the lid and the network adapter: shade under its top edge, light along its bottom one."""
    draw(-0.06, -0.08, 0.004, m['lid_lip'])
    draw(0.08, 0.1, 0.008, m['lid_shade'])
    draw(0, 0, 0.014, m['lid_floor'])


def rear_mark(p, name, width, x, z, y, m, style, squash=1.0):
    def draw(dx, dz, dy, material):
        mark(p, name, width, plane((x + dx, y + dy, z + dz), (-1, 0, 0), (0, 0, 1)) @ Matrix.Diagonal((1, squash, 1, 1)), material, 0.012)
    style(p, draw, m)


def rear_text(p, body, size, x, z, y, m, style=raised, font='arial.ttf', **kw):
    def draw(dx, dz, dy, material):
        p.text(body, font, size, plane((x + dx, y + dy, z + dz), (-1, 0, 0), (0, 0, 1)), material, align='CENTER', depth=0.012, **kw)
    style(p, draw, m)


def network_adapter(m):
    """The network adapter, measured from a photo of one on an SCPH-30001: a block as wide as the bay and its posts, nearly the height of the console,
    standing proud of the back with three bars along the top, thumbscrews into the bay's tabs and its print pressed in. ix and iy are pixels in that photo."""
    net = Part('network_adapter', (95, 255, -6), "The network adapter, Sony's Ethernet and hard drive add-on. "
               'Mod it to SATA and the Ethernet port stays. Nobody runs the stock IDE drive now: SSDs and big aftermarket drives read faster and hold '
               'libraries it never could, and RIPPS2 reads them as exFAT.', spin=1.2)
    F = D + 16
    X0, X1 = 138.2, 271.2
    X = lambda ix, iy=197: 145.2 + (ix + (iy - 197) * 0.12 - 180) * 0.08044
    Z = lambda iy: 22.5 + (iy - 197) * (0.0818 if iy > 197 else 0.095)
    J = lambda ix: X(ix, 530)
    # the part that goes into the bay, and the plug on the bay's connector
    net.box(151.2, 255.4, D - 100, D + 0.1, 5.6, 32.4, m['shell'])
    net.box(159.5, 197.0, D - 2, D + 0.1, 35.8, 40.2, m['block'])
    # the block and its bars
    net.box(X0, X1, D + 0.1, F, Z(20), Z(690), m['case'], bevel=0.5)
    net.box(X0 + 0.8, X1 - 0.8, D + 0.1, F - 3.2, Z(690), Z(845), m['dark'])
    for a, b in ((690, 722), (755, 785), (815, 845)):
        net.box(X0, X1, D + 0.1, F - 0.4, Z(a), Z(b), m['fin'], bevel=0.24)
    # the thumbscrews: a dark seat, a domed metal head, a slot across it
    for ix in (180, 1622):
        cx, cz = X(ix), Z(197)
        net.cyl((cx, F, cz), 'y', 5.4, 0.03, m['dark'], n=36)
        net.cyl((cx, F, cz), 'y', 4.5, 0.55, m['net_screw'], n=36, bevel=0.3)
        net.box(cx - 3.9, cx + 3.9, F + 0.5, F + 0.58, cz - 0.42, cz + 0.42, m['dark'])
    net.cyl((X(560), F, Z(193)), 'y', 1.0, 0.03, m['dark'], n=16)

    # its print, pressed in
    rear_mark(net, 'wm_ps2', 26.5, X(830, 272), Z(272), F + 0.02, m, sunk)
    rear_mark(net, 'ps2_lines', 53.4, X(890, 389), Z(389), F + 0.02, m, sunk, squash=0.78)
    rear_mark(net, 'sony', 23.3, X(1470, 630), Z(630), F + 0.02, m, sunk)

    def ps(dx, dz, dy, material):
        at = plane((X(1115, 272) + dx, F + 0.02 + dy, Z(272) + dz), (-1, 0, 0), (0, 0, 1))
        for outlines in ps_mark.COLOURS.values():
            net.curve(outlines, 8.2, at, material, 0.012)
    sunk(net, ps, m)
    rear_text(net, 'NETWORK', 1.7, J(305), Z(642), F + 0.02, m, style=sunk, stretch=1.35)
    rear_text(net, 'LINE', 1.7, J(480), Z(642), F + 0.02, m, style=sunk, stretch=1.35)

    # the jacks in their window, and over each a little mark
    net.box(J(222), J(590), F - 0.02, F + 0.02, Z(462), Z(582), m['dark'])
    net.box(J(232), J(580), F + 0.02, F + 0.03, Z(470), Z(576), m['net_well'])
    for x0, x1, pins in ((245, 398, 8), (432, 562, 4)):
        net.box(J(x0), J(x1), F + 0.03, F + 0.04, Z(478), Z(540), m['conn_mouth'])
        net.box(J(x0 + 34), J(x1 - 34), F + 0.03, F + 0.04, Z(540), Z(575), m['conn_mouth'])
        mid = (x0 + x1) / 2
        for i in range(pins):
            px = mid + (i - (pins - 1) / 2) * 11
            net.box(J(px - 3), J(px + 3), F + 0.04, F + 0.05, Z(492), Z(568), m['conn_pin'])
    for ix in (296, 310, 324):
        net.box(J(ix - 5), J(ix + 5), F + 0.02, F + 0.03, Z(596), Z(604), m['lid_shade'])
    net.box(J(468), J(500), F + 0.02, F + 0.03, Z(596), Z(612), m['lid_shade'])
    net.box(J(473), J(495), F + 0.03, F + 0.04, Z(598), Z(610), m['case'])
    return net


def side_foot(p, y, z0, m):
    """A rubber foot on the left end, which the console stands on upright, centred at y with its bottom at z0. Measured from two photos
    taken from opposite ends of the side, whose parallax tells what stands proud from what lies on the wall: 12.6 mm long, 8.3 mm tall and
    only 1.6 mm proud, on a thin base strip 14.4 mm long. One section runs its whole length, so the same arc shows at both ends. From the
    bottom it is a long shallow curve, then a slope back in to the wall with two fine grooves along it."""
    import math
    length, tall, proud, mid, n = 12.6, 8.3, 1.6, 4.4, 2.2
    strip = 14.4
    # where the slope takes over from the curve, and where it reaches the wall
    k0, k1 = (7.15, 1.3), (8.15, 0.2)
    arc = []
    for i in range(1, 33):
        h = 7.15 * i / 32
        arc.append((h, proud * (1 - abs((h - mid) / mid) ** n) ** (1 / n)))
    body = [(0.0, -0.3), (0.0, 0.0)] + arc + [k1, (tall, 0.0), (tall, -0.3)]
    across = plane((0, y, z0), (0, 0, 1), (-1, 0, 0))
    # where it meets the side: a web render has no shadows
    p.poly(rrect(0, tall / 2 + 0.1, length + 0.3, tall + 0.2, 1.2), plane((-0.03, y, z0), (0, -1, 0), (0, 0, 1)), m['dark'], depth=0)
    # the base strip: its top edge runs past the body at both ends, and a hair of it shows below each lower corner
    p.curve([[(7.85, -0.2), (7.85, 0.32), (8.4, 0.2), (8.45, 0.0), (8.45, -0.2)]], 1.0, across, m['foot'], strip, bevel=0.06)
    for e in (-1, 1):
        p.box(-0.14, -0.02, y + e * 7.0 - 0.1, y + e * 7.0 + 0.1, z0 - 0.7, z0 + 0.3, m['rubber'])
    p.curve([body], 1.0, across, m['foot'], length, bevel=0.2)
    # both ends are the same cut, and read darker than the face
    cut = [(0.3, 0.0)] + [(h, s0 * 0.86) for h, s0 in arc[2:]] + [(8.0, 0.2), (8.0, 0.0)]
    for e in (-1, 1):
        p.poly(cut, plane((0, y + e * (length / 2 + 0.003), z0), (0, 0, 1), (-1, 0, 0)), m['rubber'], depth=0)
    # the two grooves along the slope
    tz, tp = k1[0] - k0[0], k1[1] - k0[1]
    n0 = math.hypot(tz, tp)
    tz, tp = tz / n0, tp / n0
    nz, np_ = -tp, tz
    for f in (0.32, 0.68):
        cz, cp = k0[0] + (k1[0] - k0[0]) * f, k0[1] + (k1[1] - k0[1]) * f
        q = [(cz + nz * a + tz * b, cp + np_ * a + tp * b) for a, b in ((-0.08, -0.09), (0.04, -0.09), (0.04, 0.09), (-0.08, 0.09))]
        p.curve([q], 1.0, across, m['rubber'], length - 0.6)


def mark(p, name, width, at, m, depth=0.02):
    """A printed logo, its own outline, `width` mm wide, centred on the plane's origin."""
    p.curve(MARKS[name]['loops'], width, at, m, depth)


def build(col, tex):
    m = materials(tex)
    parts = []

    # ---------------------------------------------------- the lid: the top plate, the fins and the upper shell
    lid = Part('lid', (0, 0, 300), 'The upper shell. The six plates and five slits are the look everyone remembers, and they run round the right end to the back.')
    lid.tile = {'fat_case': 3.0}
    lid.box(0, W, 0, D, PLATES[0][0], H, m['case'], bevel=0.9, seg=3)
    lid.box(1.2, W - FIN_SIDE, D - 0.5, D + 0.012, PLATES[0][0], H - 0.9, m['fin'])
    # under the lid's rounded front edge: a seam, then a black face down to the first slit
    lid.box(0.6, W - 0.6, -0.02, 0.8, 74.7, 75.4, m['dark'])
    lid.box(0.6, W - 0.6, -0.015, 0.8, PLATES[0][0], 74.7, m['fin'])
    # the logo and its name on the lid, measured: reading rear to front, 'up' towards the right end
    art = plane((0, D, H + 0.01), (0, -1, 0), (1, 0, 0))
    ps2_logo(lid, art, 28, 162, 1.0, 1.1, (m['logo_lo'], m['logo_mid'], m['logo_hi']))
    # engraved, measured off a photo: a floor the lid's own colour, the wall facing away from the light in shade and a thin lit wall
    # across from it. A web render has no shadows, and the real step is under a pixel, so it is drawn the way light finds it
    word = lambda dy, dx, z: plane((151.4 + dx, 89.8 + dy, H + z), (0, -1, 0), (1, 0, 0))
    mark(lid, 'wm_ps2', 62.8, word(-0.13, -0.11, 0.006), m['lid_lip'], 0.01)
    mark(lid, 'wm_ps2', 62.8, word(0.2, 0.17, 0.010), m['lid_shade'], 0.01)
    mark(lid, 'wm_ps2', 62.8, word(0, 0, 0.016), m['lid_floor'], 0.01)
    # the disc and sound logos along the front right, pressed into the lid as the word is: their own outlines, each placed by solving the
    # lid's perspective in a photo of an SCPH-30001. The step is shallower than the word's, so the walls are narrower
    def pressed(name, width, x, y):
        at = lambda dx, dy, z: plane((x + dx, y + dy, H + z), (1, 0, 0), (0, 1, 0))
        mark(lid, name, width, at(-0.07, -0.08, 0.006), m['lid_lip'], 0.01)
        mark(lid, name, width, at(0.1, 0.11, 0.010), m['lid_shade'], 0.01)
        mark(lid, name, width, at(0, 0, 0.016), m['lid_floor'], 0.01)
    pressed('cd_word', 15.0, 222.9, 8.9)
    pressed('dolby', 17.8, 241.8, 7.9)
    pressed('dts', 11.2, 258.0, 9.9)
    lid.box(252.33, 263.53, 5.42, 7.02, H + 0.002, H + 0.012, m['lid_lip'])
    lid.box(252.5, 263.7, 5.61, 7.21, H + 0.003, H + 0.015, m['lid_shade'])
    lid.box(252.4, 263.6, 5.5, 7.1, H + 0.004, H + 0.021, m['lid_floor'])
    lid.text('DIGITAL OUT', 'arialbd.ttf', 1.1, plane((258.0, 5.9, H + 0.03), (1, 0, 0), (0, 1, 0)), m['case'], align='CENTER', depth=0.01, stretch=1.2)
    pressed('dvd_video', 10.5, 272.0, 9.2)
    pressed('dvd_rom', 10.2, 286.3, 10.2)
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
    # the slits wrap the left end for its first 14.5 mm, as five teeth like the back of the right end; behind them the side is one flat wall
    lid.box(0, 1.6, LEFT_FIN, D, LOW_Z, PLATES[0][0], m['fin'], bevel=0.2)
    lid.box(-0.012, 0.2, LEFT_FIN, LEFT_FIN + 0.6, LOW_Z, PLATES[0][0], m['dark'])
    for z0, z1 in PLATES[1:]:
        lid.box(0, FIN_SIDE, 0, LEFT_FIN, z0, z1, m['fin'], bevel=0.42, seg=2)
        lid.box(0.5, FIN_SIDE, 0, LEFT_FIN, z1 - 0.01, z1 + 0.02, m['dark'])
        lid.box(0.5, FIN_SIDE, 0, LEFT_FIN, z0 - 0.02, z0 + 0.01, m['dark'])
    lid.box(0.5, FIN_SIDE, 0, LEFT_FIN, PLATES[0][0] - 0.02, PLATES[0][0] + 0.01, m['dark'])
    lid.box(FIN_SIDE, FIN_SIDE + 1, FIN, LEFT_FIN, LOW_Z, PLATES[0][0], m['dark'])
    # the back above the lower block is flat, round the connector's opening
    lid.box(1.6, 25.1, D - 1.6, D, LOW_Z, PLATES[0][0], m['fin'])
    lid.box(53.6, 70.2, D - 1.6, D, LOW_Z, PLATES[0][0], m['fin'])
    lid.box(25.1, 53.6, D - 1.6, D, LOW_Z, 40, m['fin'])
    lid.box(133, W - FIN_SIDE, D - 1.6, D, 41.3, PLATES[0][0], m['fin'])
    lid.box(133, 151, D - 1.6, D, LOW_Z, 41.3, m['fin'])
    lid.box(205.5, W - FIN_SIDE, D - 1.6, D, LOW_Z, 41.3, m['fin'])
    # the seam round the rear plate
    lid.box(149.6, 150.2, D - 0.02, D + 0.02, 40, PLATES[0][0], m['dark'])
    # the front wall behind the front fins, leaving the tray's mouth open
    fy = FIN
    lid.box(FIN_SIDE, TRAY[0], fy, fy + 1.2, LOW_Z, PLATES[0][0], wall)
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
        # under the light, the dark line a rounded edge's next facet makes
        p.box(x0 + 0.4, x1 - 0.4, -0.012, 0.3, z1 - 1.75, z1 - 1.25, m['dark'])
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
    row(BTN[0] - 1, NOSE, None, z=(48.4, 50.1))
    # the nose carries SONY, reading top to bottom; the slits narrow as they cross it
    for z0, z1 in ((63.3, 69.7), (57.5, 62.1), (50.3, 55.8), (42.7, 48.5)):
        lid.box(NOSE, W, -0.01, fy, z0, z1, m['fin'], bevel=0.42, seg=2)
    # SONY reads down the fins, one raised letter to a fin at the fins' own 7.55 mm pitch, 5.4 mm long and 3.4 across, as a photo has them
    for letter, z, length in (('S', 67.6, 5.2), ('O', 60.0, 5.4), ('N', 52.5, 5.6), ('Y', 44.9, 5.6)):
        across = 3.4 / (MARKS['sony_' + letter]['h'] * length)
        at = plane((294.2, -0.12, z), (0, 0, -1), (1, 0, 0)) @ Matrix.Diagonal((1, across, 1, 1))
        mark(lid, 'sony_' + letter, length, at, m['sony_hi'], 0.24)
    # the plug side's words are moulded, standing proud, the case's own black: as big as a photo has them (AV MULTI OUT nearly its port's width)
    rear_text(lid, 'MAIN', 2.6, 12.6, 62.9, D + 0.03, m)
    rear_text(lid, 'POWER', 2.6, 12.6, 59.9, D + 0.03, m)
    rear_text(lid, 'AC IN', 2.6, 12.6, 49.4, D + 0.03, m)
    rear_text(lid, '~', 3.4, 12.6, 46.2, D + 0.03, m)
    lid.text('1', 'arialbd.ttf', 3.9, plane((41, -0.02, 66.2), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    lid.text('2', 'arialbd.ttf', 3.9, plane((93, -0.02, 66.2), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    mark(lid, 'magicgate', 19.0, plane((66.5, -0.02, 67.35), (1, 0, 0), (0, 0, 1)), m['label'])
    # the rubber feet on the left side, the upper two here: centres and bottoms from the two photos
    for y in (30.3, 168.9):
        side_foot(lid, y, 66.1, m)
    parts.append(lid)

    # ---------------------------------------------------- the back of the upper shell, printed
    rear = lid
    # the rating print and its small print: one picture, the case's own colour behind it
    rear.quad_on(plane((274.35, D + 0.03, 40.7), (-1, 0, 0), (0, 0, 1)), 119.93, 31.75, m['rating'])
    rear.quad_on(plane((202.5, D + 0.05, 58.8), (-1, 0, 0), (0, 0, 1)), 47.7, 11.2, m['serial'])
    # the column of print down the left end of the back, reading upwards
    rear.quad_on(plane((1.4, D + 0.03, 3), (0, 0, 1), (1, 0, 0)), 60, 12.6, m['rating_side'])
    rear.cyl((284, D, 58), 'y', 1.7, 0.06, m['dark'], n=14, smooth=False)
    for x0, x1, z0, z1 in ((7.1, 7.5, 61, PLATES[0][0]), (134, 134.6, 41.3, PLATES[0][0])):
        rear.box(x0, x1, D, D + 0.02, z0, z1, m['dark'])

    # ---------------------------------------------------- the tray: door, deck, disc
    tray = Part('tray', (40, -190, 118), 'The disc tray. It opens on command in RIPPCSX2 too, and a game image in the virtual drive reads like the disc it came from.')
    # its door is the middle of rows 2 and 3, slit between them
    row(TRAY[0], TRAY[1], 2, p=tray)
    row(TRAY[0], TRAY[1], 3, p=tray)
    tray.box(TRAY[0] + 0.5, TRAY[1] - 0.5, fy, fy + 1.0, PLATES[3][0], PLATES[2][1], m['shell'])
    # the deck with its disc well
    deck_z = 51.0
    tray.box(TRAY[0] + 1, TRAY[1] - 1, fy + 1, 150, deck_z - 1, deck_z, m['drive'])
    tray.ring((209, 85, deck_z), 'z', 60.5, 66, 0.9, m['drive'], n=72)
    tray.cyl((209, 85, deck_z), 'z', 60, 0.3, m['black'], n=72)
    tray.box(195, 223, 110, 150, deck_z, deck_z + 0.2, m['dark'])
    parts.append(tray)

    # the PS mark on its tile, on the tray's face: a part of its own, because it turns
    badge = Part('badge', (70, -135, 118), 'The PlayStation badge. On a real console it turns a quarter for a vertical stand, and it does here too.', spin=2.0)
    ps_badge(badge, 213, 0.1, 54.45, 10.6, m)
    parts.append(badge)

    # a game: the disc itself comes out with the tray
    disc = Part('disc', (40, -120, 205), 'A DVD. Most of the PS2 library is one disc image away, and the end goal of RIPPCSX2 is the whole library running through OPL\'s own code path.', spin=2.0)
    disc.disc((209, 85, 51.6), 60, 1.2, m['disc'])
    disc.cyl((209, 85, 52.81), 'z', 7.5, 0.05, m['dark'], n=32)
    parts.append(disc)

    # ---------------------------------------------------- the card slots and controller ports (the controller board)
    ctrl = Part('controller_board', (-70, -170, -8), 'Controllers and memory cards. RIPPCSX2 keeps every card image as a file, so a save can be read, written and compared from a script.')
    for c in (CARD1, CARD2):
        # the slot's door, its lit top edge, the print on it and the small lip under it
        ctrl.box(c[0] + 0.2, c[1] - 0.2, 0.2, fy, PLATES[2][0], 62.0, m['blackgloss'], bevel=0.25)
        ctrl.box(c[0] + 0.6, c[1] - 0.6, 0.17, 0.3, 61.3, 61.8, m['edge_hi'])
        ctrl.box(c[0] + 0.2, c[1] - 0.2, 0.2, fy, 56.4, 57.5, m['blackgloss'])
        ctrl.text('MEMORY CARD', 'segoeuil.ttf', 3.9, plane((c[0] + 20.1, 0.16, 58.05), (1, 0, 0), (0, 0, 1)), m['doorprint'], align='CENTER', stretch=1.05, spacing=1.06)
    for c in (PORT1, PORT2):
        controller_port(ctrl, c[0], c[1], PORT_Z[0], PORT_Z[1], 0.8, m, lobe_h=4.4, cz=45.5)
    ctrl.box(10, 125, fy + 2, 34, 36.4, 37.0, m['pcb'])
    for c in (PORT1, PORT2):
        ctrl.box(c[0] - 1, c[1] + 1, 4, 30, PORT_Z[0], PORT_Z[1], m['black'])
    for c in (CARD1, CARD2):
        ctrl.box(c[0] - 1, c[1] + 1, 4, 44, PLATES[2][0], PLATES[2][1], m['black'])
    parts.append(ctrl)

    # ---------------------------------------------------- the buttons
    btn = Part('buttons', (95, -150, 62), 'Reset and eject on a flex cable. Exit an ELF, power off from a menu, or reset the VM with the same result as this button.')
    btn.box(BTN[0], BTN[1], 0.5, fy, 63.0, 72.8, m['teal'], bevel=0.3)
    # the power mark and RESET
    btn.ring((284.5, 0.46, 69.4), 'y', 1.6, 1.9, 0.05, m['tealglow'], n=24)
    btn.box(284.36, 284.64, 0.42, 0.5, 69.4, 71.7, m['tealglow'])
    btn.text('RESET', 'arial.ttf', 1.95, plane((284.5, 0.44, 63.7), (1, 0, 0), (0, 0, 1)), m['tealglow'], align='CENTER', stretch=1.16, spacing=1.05)
    btn.box(BTN[0], BTN[1], 0.5, fy, 42.7, 47.3, m['bluebtn'], bevel=0.3)
    ej = plane((284.5, 0.46, 44.0), (1, 0, 0), (0, 0, 1))
    # the eject mark in outline: a triangle's two rising sides and its base, the bar under it
    btn.poly([(-1.8, -0.1), (1.8, -0.1), (1.8, 0.15), (-1.8, 0.15)], ej, m['blueglow'], depth=0.04)
    btn.poly([(-1.8, -0.1), (-1.5, -0.1), (0.13, 2.0), (-0.13, 2.2)], ej, m['blueglow'], depth=0.04)
    btn.poly([(1.8, -0.1), (1.5, -0.1), (-0.13, 2.0), (0.13, 2.2)], ej, m['blueglow'], depth=0.04)
    btn.box(282.9, 286.1, 0.42, 0.5, 43.2, 43.5, m['blueglow'])
    btn.box(279, 290, fy + 1.3, fy + 1.6, 40, 72, m['flex'])
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
    base.box(7, 43.5, fw0, fw1, BOT, 5.9, bm)
    base.box(7, 43.5, fw0, fw1, 28.0, LOW_Z, bm)
    base.box(57, 245.5, fw0, fw1, BOT, 8.7, bm)
    base.box(57, 245.5, fw0, fw1, 22.9, LOW_Z, bm)
    ladder(base, 57, 245.5, 8.7, 22.9, fw0, fw1, 5, 15, 0.72, bm, m['dark'])
    # the duct behind the vent, so nothing inside can be seen lit through it
    base.box(55, 247.5, LOW_Y + 6, LOW_Y + 6.2, BOT, LOW_Z, m['dark'])
    base.box(55, 247.5, fw1, LOW_Y + 6, BOT + 1.6, 8.1, m['dark'])
    base.box(55, 247.5, fw1, LOW_Y + 6, 23.5, LOW_Z, m['dark'])
    base.box(55, 56.4, fw1, LOW_Y + 6, BOT + 1.6, LOW_Z, m['dark'])
    base.box(246.1, 247.5, fw1, LOW_Y + 6, BOT + 1.6, LOW_Z, m['dark'])
    # the top of that wall is in the shade of the plates
    base.box(0.5, LOW_X - 0.5, LOW_Y - 0.015, LOW_Y + 0.2, 30, LOW_Z, m['dark'])
    # the sides
    base.box(0, 1.6, LOW_Y, D, BOT, LOW_Z, bm, bevel=0.2)
    base.box(LOW_X - 1.6, LOW_X, LOW_Y, D, BOT, LOW_Z, bm, bevel=0.2)
    # the back: the fan's opening and the bay's stay open, the rest is solid
    b0, b1 = D - 1.6, D
    base.box(0, 70.2, b0, b1, BOT, LOW_Z, bm)
    base.box(133, 141, b0, b1, BOT, LOW_Z, bm)
    base.box(141, 150, b0, b1, BOT, 13.7, bm)
    base.box(141, 150, b0, b1, 29.5, LOW_Z, bm)
    base.box(265.8, LOW_X, b0, b1, BOT, LOW_Z, bm)
    base.box(256.6, 265.8, b0, b1, BOT, 14.5, bm)
    base.box(256.6, 265.8, b0, b1, 30.6, LOW_Z, bm)
    base.box(70.2, 133, b0, b1, BOT, 10.7, bm)
    base.box(150, 256.6, b0, b1, BOT, 5.0, bm)
    base.box(205.5, 256.6, b0, b1, 33.0, LOW_Z, bm)
    # rear connectors' frames, tone on tone, and the seams that join them
    frame = m['black']
    rim = m['ink']
    def framed(x0, x1, z0, z1, t=0.45):
        for a0, a1, b0_, b1_ in ((x0, x1, z0, z0 + t), (x0, x1, z1 - t, z1), (x0, x0 + t, z0, z1), (x1 - t, x1, z0, z1)):
            base.box(a0, a1, D + 0.2, D + 0.3, b0_, b1_, rim)
    for x0, x1, z0, z1 in ((38.4, 50.4, 16.2, 16.6), (61.3, 69.7, 16.2, 16.6), (70.7, 139, 10.2, 10.6), (134, 134.6, 10.6, LOW_Z)):
        base.box(x0, x1, D, D + 0.02, z0, z1, m['dark'])
    # AV multi out: a raised frame outlined in black, a slot, the tongue in it
    base.box(14.7, 38.4, D + 0.0, D + 0.2, 10.7, 19.3, m['block'])
    framed(14.7, 38.4, 10.7, 19.3)
    base.box(17.2, 35.6, D + 0.2, D + 0.27, 12.9, 17.1, m['dark'])
    base.box(19.4, 33.4, D + 0.26, D + 0.3, 14.3, 15.7, m['portface'])
    for i in range(12):
        base.box(19.8 + i * 1.1, 20.3 + i * 1.1, D + 0.29, D + 0.32, 14.5, 15.5, m['portrim'])
    # the optical port: a flat shutter in a black outline
    base.box(50.4, 61.3, D + 0.0, D + 0.2, 10.9, 22.3, m['block'])
    framed(50.4, 61.3, 10.9, 22.3)
    base.box(53.2, 58.5, D + 0.2, D + 0.23, 13.6, 19.6, m['fin'])
    rearprint = lambda x, z: plane((x, D + 0.02, z), (-1, 0, 0), (0, 0, 1))
    rear_text(base, 'DIGITAL OUT', 2.9, 55.8, 26.6, D + 0.01, m)
    rear_text(base, '(OPTICAL)', 2.9, 55.8, 23.9, D + 0.01, m)
    rear_text(base, 'AV MULTI OUT', 2.9, 26.5, 21.0, D + 0.01, m, stretch=1.1)
    base.cyl((42.3, D, 26.3), 'y', 1.3, 0.2, m['dark'], n=12)
    # the rubber feet on the left side, the lower two here
    for y in (30.3, 168.9):
        side_foot(base, y, 5.1, m)
    # feet
    for x, y in ((12, 34), (262, 34), (12, 170), (262, 170)):
        base.cyl((x, y, 0), 'z', 4.5, BOT, m['rubber'], n=14)
    parts.append(base)

    # ---------------------------------------------------- blue USB and i.LINK panel
    usb = Part('usb_board', (-75, -120, -70), 'USB and i.LINK. The ports OPL loads games over, and the ones a lab drives from a file instead of a stick.')
    # the panel, around the real holes its sockets sit in
    u0, u1 = LOW_Y - 0.5, LOW_Y + 2
    for x0, x1, z0, z1 in ((7, 10.6, 5.9, 28), (24, 30.5, 5.9, 28), (37.5, 43.5, 5.9, 28), (10.6, 24, 5.9, 12.1), (10.6, 24, 18.3, 20.5), (10.6, 24, 26.4, 28), (30.5, 37.5, 5.9, 19.5), (30.5, 37.5, 25.2, 28)):
        usb.box(x0, x1, u0, u1, z0, z1, m['blue'])
    usb_a(usb, 10.6, 24, 12.1, 18.3, LOW_Y - 0.45, m)
    usb_a(usb, 10.6, 24, 20.5, 26.4, LOW_Y - 0.45, m)
    usb_a(usb, 30.5, 37.5, 19.5, 25.2, LOW_Y - 0.45, m, depth=4.0, tongue=False)
    # its print is two symbols: the USB trident, pointing up, and the i.LINK mark under its socket
    mark(usb, 'usb', 5.8, plane((27.4, LOW_Y - 0.53, 17.6), (0, 0, 1), (-1, 0, 0)), m['usb_print'])
    ilink = plane((36.0, LOW_Y - 0.53, 16.5), (1, 0, 0), (0, 0, 1))
    usb.cyl((36.0, LOW_Y - 0.53, 18.0), 'y', 0.58, 0.02, m['usb_print'], n=20)
    usb.poly(rrect(0, -0.5, 1.5, 2.3, 0.42), ilink, m['usb_print'], depth=0.02)
    usb.cyl((36.95, LOW_Y - 0.53, 15.75), 'y', 0.42, 0.02, m['usb_print'], n=16)
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
    bz = 33.6
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
    brd.box(156, 202, D - 12, D - 2, 34.2, 40.6, m['black'])
    brd.box(151, 205.5, D - 1.62, D - 1.4, 34.9, 41.1, m['peach'])
    # a plated tan shell with a stadium mouth, a bright rim round it, a black tongue, its pins along the top, and a silver lip with four black clips
    brd.quad_on(plane((205.5, D - 1.395, 34.9), (-1, 0, 0), (0, 0, 1)), 54.5, 6.2, m['conn'])
    face = lambda dy: plane((0, D - 1.39 + dy, 0), (-1, 0, 0), (0, 0, 1)) @ Matrix.Translation((-356.6, 0, 0))
    brd.poly(stadium(178.3, 38.0, 43.4, 5.6, n=14), face(0.01), m['conn_rim'], depth=0)
    brd.poly(stadium(178.3, 38.0, 42.7, 4.95, n=14), face(0.02), m['conn_mouth'], depth=0)
    brd.box(159.6, 197.0, D - 1.36, D - 1.34, 36.2, 38.95, m['conn_tongue'])
    for i in range(100):
        brd.box(159.8 + i * 0.37, 160.0 + i * 0.37, D - 1.36, D - 1.34, 39.0, 39.95, m['conn_pin'])
    brd.box(151, 205.5, D - 1.62, D - 1.2, 32.9, 34.8, m['tab'])
    for x0, x1 in ((196.6, 200.7), (180.1, 192.7), (163.9, 176.2), (155.9, 159.8)):
        brd.box(x0, x1, D - 1.24, D - 1.18, 34.62, 34.98, m['block'])
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
    # Measured from a photo of the back, squared up at about 23 px a mm. Art on the back runs u = -x, so its normal points out of the back.
    import math
    back = lambda y: plane((0, y, 0), (-1, 0, 0), (0, 0, 1))

    def outline(xz):
        """(x, z) points as (u, v) on the back, counter-clockwise so the face looks out."""
        uv = [(-x, z) for x, z in xz]
        area = sum(u0 * v1 - u1 * v0 for (u0, v0), (u1, v1) in zip(uv, uv[1:] + uv[:1]))
        return uv if area > 0 else uv[::-1]

    def circle(cu, cv, r, n=28):
        return [(cu + r * math.cos(2 * math.pi * i / n), cv + r * math.sin(2 * math.pi * i / n)) for i in range(n)]

    # Two plates in the case's own tone sit in a black recess, a real gap round them. The inlet's is cut through, and behind the cut is a well
    # 13 mm deep with two thick pins standing in it, their split tips 2 mm down. Traced from the photo, through the unit's four corners.
    # The mouth: a square lobe toward the middle of the back, a round one toward the end, a deep tooth down from the top and a shallow one up from the bottom.
    arc = [(34.85 + 4.17 * math.cos(math.radians(t)), 47.85 + 4.17 * math.sin(math.radians(t))) for t in range(-66, -293, -8)]
    mouth = outline([(47.2, 51.55), (47.2, 44.15), (47.1, 43.9), (46.85, 43.8), (40.6, 43.8), (40.1, 44.25), (39.5, 45.0), (39.15, 45.55), (38.75, 45.85),
                     (38.4, 45.75), (37.8, 44.86), (37.2, 44.07)] + arc +
                    [(37.4, 51.75), (37.85, 50.9), (38.18, 49.9), (38.49, 49.15), (38.65, 49.02), (38.8, 49.06), (39.04, 49.42), (39.57, 50.38), (40.24, 51.33),
                     (40.88, 51.85), (46.85, 51.9), (47.1, 51.8)])
    inlet.curve([rrect(-39.35, 57.0, 28.5, 34.0, 0.4, n=3), mouth], 1.0, back(D - 0.75), m['ink'], 0.7)
    inlet.curve([rrect(-39.15, 47.98, 26.75, 14.15, 0.7, n=4), mouth], 1.0, back(D - 0.35), m['plug_plate'], 0.9, bevel=0.14)
    inlet.box(25.65, 53.05, D - 0.8, D + 0.1, 55.75, 73.55, m['plug_plate'], bevel=0.14)
    # the well, and what closes the unit round it
    inlet.curve([rrect(-39.35, 48.0, 22.0, 12.5, 0.6, n=3), mouth], 1.0, back(D - 7.4), m['plug_well'], 12.6)
    inlet.poly(rrect(-39.35, 48.0, 22.0, 12.5, 0.6, n=3), back(D - 13.6), m['ink'], depth=0)
    inlet.box(25.1, 53.6, D - 13.7, D - 1.1, 54.25, 71, m['black'])
    inlet.box(25.1, 53.6, D - 13.7, D - 1.1, 40, 41.75, m['black'])
    inlet.box(25.1, 28.35, D - 13.7, D - 1.1, 41.75, 54.25, m['black'])
    inlet.box(50.35, 53.6, D - 13.7, D - 1.1, 41.75, 54.25, m['black'])
    # the case's lit lip under the unit
    inlet.box(24.8, 53.9, D, D + 0.05, 39.5, 39.8, m['raise_lit'])
    # the pins, each tip split three ways
    for x in (42.63, 34.34):
        inlet.cyl((x, D - 13.6, 48.13), 'y', 1.05, 11.7, m['plug_shaft'], n=24, bevel=0.1)
        inlet.poly(circle(-x, 48.13, 0.98), back(D - 1.895), m['plug_pin'], depth=0)
        for a in (90, 210, 330):
            c, s_ = math.cos(math.radians(a)), math.sin(math.radians(a))
            bar = [(-x + 0.5 * c * k - 0.075 * s_ * j, 48.13 + 0.5 * s_ * k + 0.075 * c * j) for k, j in ((0.1, -1), (1.65, -1), (1.65, 1), (0.1, 1))]
            inlet.poly(bar, back(D - 1.88), m['ink'], depth=0)

    # the rocker's bezel: a raised frame round the opening, its well dark
    inlet.curve([rrect(-39.6, 64.7, 23.6, 16.4, 0.9, n=4), rrect(-39.6, 64.85, 18.2, 12.7, 0.4, n=3)], 1.0, back(D + 0.35), m['plug_plate'], 0.6, bevel=0.2)
    inlet.poly(outline([(30.5, 58.5), (48.7, 58.5), (48.7, 71.2), (30.5, 71.2)]), back(D + 0.13), m['ink'], depth=0)
    # the rocker: rounded edges, rocked over a few degrees with the I side in, as a photo has it
    tilt = math.radians(4.0)
    U, V = (-math.cos(tilt), math.sin(tilt), 0), (0, 0, 1)
    N = (math.sin(tilt), math.cos(tilt), 0)
    o = (39.35, D + 0.05, 64.65)
    inlet.curve([rrect(0, 0, 16.9, 11.7, 0.6, n=4)], 1.0, plane(o, U, V), m['rocker'], 2.0, bevel=0.35)
    face = plane(tuple(o[i] + N[i] * 1.012 for i in range(3)), U, V)
    inlet.poly([(-4.65, -1.95), (-4.15, -1.95), (-4.15, 0.95), (-4.65, 0.95)], face, m['white'], depth=0)
    inlet.curve([circle(4.25, -0.65, 1.6), circle(4.25, -0.65, 1.12)], 1.0, face, m['white'], 0.02)
    inlet.box(25.1, 53.6, D - 26, D - 13.7, 40, 71, m['black'])
    parts.append(inlet)

    # ---------------------------------------------------- the fan
    fan = Part('fan', (-30, 150, 40), 'The fan, and the grille it breathes through. The emulator keeps a game cool by other means.', spin=1.6)
    fc = (101, D - 13, 42)
    parts_fan_body(fan, m)
    parts.append(fan)

    # ---------------------------------------------------- the expansion bay
    bay = Part('expansion_bay', (120, 130, -40), 'The expansion bay, the home of the network adapter and a hard drive. OPL in RIPPCSX2 reads its games from a virtual one.')
    # One sheet of metal, measured from a photo squared up to the floor's plane: the tabs at the mouth fold in to be the side walls, and the walls the floor.
    # There are no shadows in a web render, so the light falling off into it is painted on.
    MOUTH = D - 1.2
    FLOOR = 5.0
    bay.textured_quad(150, 256.6, 60, MOUTH, FLOOR, m['bay_floor'])
    bay.box(150, 256.6, 60, MOUTH, 4.4, FLOOR - 0.02, m['bay4'])
    bay.box(150, 256.6, 60, 60.6, FLOOR, 33, m['bay4'])
    bay.box(150, 256.6, 60, MOUTH, 33.0, 33.6, m['dark'])
    bay.box(150, 256.6, MOUTH - 0.5, MOUTH + 0.05, FLOOR, FLOOR + 0.1, m['bay_edge'])
    for x in (150, 256):
        bay.box(x, x + 0.6, 60, MOUTH - 0.4, FLOOR, 33, m['bay4'])
        bay.box(x, x + 0.6, MOUTH - 0.4, MOUTH + 0.05, FLOOR, 33, m['tab'])
    bay.quad_on(plane((255.98, MOUTH, FLOOR), (0, -1, 0), (0, 0, 1)), MOUTH - 60, 28, m['bay_wall'])
    bay.quad_on(plane((150.62, 60, FLOOR), (0, 1, 0), (0, 0, 1)), MOUTH - 60, 28, m['bay_wall'], flip_u=True)
    # the long slots in the walls, and the two little reliefs on the fold
    for wall in (255.96, 150.64):
        at = plane((wall, MOUTH, FLOOR), (0, -1, 0), (0, 0, 1))
        for z in (18, 26):
            for d in (32, 59.5, 87):
                bay.poly(stadium(d, z - FLOOR, 21, 4.1, n=6), at, m['dark'], depth=0)
        bay.poly([(0, 16), (1.1, 16), (1.1, 21), (0, 21)], at, m['dark'], depth=0)
        bay.poly([(0, 7), (0.8, 7), (0.8, 8.5), (0, 8.5)], at, m['dark'], depth=0)

    # the floor's holes and marks, each with the far wall of its cut catching the light
    import math

    def on_floor(lift):
        return plane((0, 0, FLOOR + lift), (1, 0, 0), (0, 1, 0))

    def rim(y):
        return m['bay_rim1'] if y > 150 else m['bay_rim2'] if y > 112 else m['bay_rim3']

    def punched(outline, y, inside=None):
        bay.poly([(u, v - 0.3) for u, v in outline], on_floor(0.012), rim(y), depth=0)
        bay.poly(outline, on_floor(0.02), inside or m['dark'], depth=0)

    for r in range(9):
        y = 159.5 - r * 10.7
        x0 = 209.7 if r % 2 else 203.85
        for k in range(-5, 5):
            x = x0 + k * 11.85
            if not 160 < x < 248 or (r == 0 and abs(x - 203.85) < 3) or math.hypot(x - 200.75, y - 125) < 12.5:
                continue
            punched(rrect(x, y, 5.7, 5.7, 2.85, n=4), y)
    punched(rrect(200.75, 125, 14.2, 14.2, 7.1, n=10), 125)
    # two pressed bars, and the warning triangle: three bars that stop short of the corners, and the ! inside, its point toward the mouth
    press = m['bay_press']
    for x in (174.7, 233.1):
        punched(rrect(x, 166.8, 9.8, 3.4, 0.7, n=3), 166, press)
    punched(capsule((193.75, 174.5), (202.5, 158.1), 0.55), 166, press)
    punched(capsule((213.75, 173.75), (205.0, 158.5), 0.55), 166, press)
    punched(capsule((195.0, 177.2), (212.0, 177.2), 0.5), 166, press)
    punched(capsule((203.7, 171.4), (203.7, 162.2), 0.55, 1.15), 166, press)
    punched(rrect(203.7, 174.2, 2.1, 2.1, 1.05, n=3), 166, press)

    # the screw tabs: the same sheet coming round the fold, in windows set back from the back's face
    for fold, out, z0, z1, hx, hz in ((256.0, 265.8, 14.5, 30.6, 261.2, 23.0), (150.6, 141.0, 13.7, 29.5, 145.2, 22.0)):
        bay.poly(tab_outline(fold, out, z0, z1, 1.0), plane((0, MOUTH, 0), (-1, 0, 0), (0, 0, 1)), m['tab'], depth=0.5)
        bay.cyl((hx, MOUTH + 0.01, hz), 'y', 1.6, 0.01, m['dark'], n=20, smooth=False)
        bay.cyl((hx, MOUTH + 0.02, hz), 'y', 1.25, 0.01, m['silver'], n=20, smooth=False)
        bay.cyl((hx, MOUTH + 0.03, hz), 'y', 0.75, 0.01, m['dark'], n=16, smooth=False)
    parts.append(bay)
    parts.append(network_adapter(m))

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
    # the grille: seven rows of slots 9 mm apart between thick ribs, three thin uprights, the corners filled to an octagon
    bx0, bx1 = 70.2, 133.0
    for z0, z1 in ((10.7, 14.3), (20, 23.1), (28.9, 32), (37.7, 40.9), (46.9, 49.7), (56, 58.7), (64.9, 68), (73.3, 74.5)):
        fan.box(bx0, bx1, D - 2.4, D + 0.02, z0, z1, m['fin'])
    for x, hw in ((bx0 + 0.5, 0.5), (86.1, 0.85), (100.9, 1.15), (116.8, 0.85), (bx1 - 0.5, 0.5)):
        fan.box(x - hw, x + hw, D - 2.4, D + 0.0, 10.7, 74.5, m['fin'])
    corner = plane((0, D - 0.4, 0), (-1, 0, 0), (0, 0, 1))
    for cx0, cz0, dx, dz in ((bx0, 14.3, 1, 1), (bx1, 14.3, -1, 1), (bx0, 73.3, 1, -1), (bx1, 73.3, -1, -1)):
        tri = [(-cx0, cz0), (-(cx0 + dx * 8), cz0), (-cx0, cz0 + dz * 8.7)]
        if dx * dz > 0:
            tri = tri[::-1]
        fan.poly(tri, corner, m['fin'], depth=0.2)
