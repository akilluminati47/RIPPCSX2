# The slim PlayStation 2 (SCPH-7000x): 230 x 152 x 28 mm. Positions measured from photographs rectified through a solved camera.
# Its insides follow a real teardown: the lid and flip door, the top-loading drive, the metal plates, the one main board with
# EE and GS on a single chip, the fan under its cover, the battery in its black boot, the rear ports.
import math
from mathutils import Matrix
from ps2kit import Part, mat, plane
from fat import stadium, rrect, ps2_logo, ps_badge, controller_port, usb_a

W, D, H = 230, 152, 28
LID_Z = 26.5               # the lid's edge at the front: a thin lip
PL_T = (25.7, 28.0)        # the seam under the lid, at the back and the ends
PL_M = (19.2, 22.4)        # the middle plate
PL_B = (14.0, 16.8)        # the bottom plate
RAIL_F = 1.2               # the plates sit this far back from the lid's front edge
RAIL_Y = 3.5               # how deep the two slits between them cut
LOW_X = 212.0              # the lower block stops short of the right end
LOW_Y = 7.0                # and sits back from the front
BOT = 1.2
BAND = (82.0, 96.2)        # the glossy band across the lid
PORT1, PORT2 = (3.7, 45.0), (52.4, 94.0)
PORT_Z = (1.7, 9.7)
DOOR1, DOOR2 = (5.5, 47.0), (54.4, 96.8)
USB1, USB2 = (104.4, 118.6), (130.2, 144.6)
USB_Z = (2.8, 8.9)
VENT = ((153.8, 165.6), (168.0, 180.2), (182.8, 194.2))
VENT_ROWS = ((2.1, 3.9), (4.8, 6.7), (7.4, 9.4))
WINDOWS = ((3, 11.7), (12.7, 18), (19.5, 28), (29, 37), (38, 46.6), (47.5, 55), (56, 62), (65, 73))


def materials(tex):
    return dict(
        lid=mat('slim_lid', tex=tex + 'stipple_c.jpg', rough=0.7, normal=tex + 'stipple_n.png', normal_strength=0.55),
        band=mat('slim_band', '#17181a', rough=0.22),
        edge=mat('slim_edge', '#0b0b0d', rough=0.16),
        body=mat('slim_body', '#1a1b1d', rough=0.5),
        inner=mat('slim_inner', '#0a0a0c', rough=0.8),
        dark=mat('slim_recess', '#030304', rough=0.9, spec=0.0),
        ink=mat('slim_ink', '#000000', rough=0.7, spec=0.0),
        tone=mat('slim_tone', '#3f4045', rough=0.22),
        edge_hi=mat('edge_hi', '#a5a6ac', rough=0.3),
        wall=mat('slim_front_wall', '#2c2d30', rough=0.55),
        edge_hi2=mat('edge_hi2', '#4a4b50', rough=0.3),
        blackgloss=mat('black_gloss', '#0a0a0c', rough=0.16),
        rimdark=mat('rim_dark', '#303136', rough=0.5),
        usbshell=mat('usb_shell', '#3a3b3e', rough=0.6),
        irwin=mat('ir_window', '#17181b', rough=0.12),
        print_dim=mat('slim_print_dim', '#5c5e64', rough=0.55),
        glint=mat('window_glint', '#77797f', rough=0.5),
        olive=mat('window_olive', '#4a4a18', rough=0.6),
        door=mat('slim_door_print', '#2c2d31', rough=0.4),
        label=mat('slim_print', '#8f9197', rough=0.55),
        silver=mat('metal_silver', '#c4c7cb', rough=0.34, metal=1.0),
        magic=mat('slim_magic', '#b5b7bd', rough=0.4),
        steel=mat('metal_steel', '#9aa0a6', rough=0.5, metal=1.0),
        zinc=mat('metal_zinc', '#c4c8ca', rough=0.55, metal=0.35),
        gold=mat('metal_gold', '#d9b35a', rough=0.3, metal=1.0),
        yellow=mat('dc_yellow', '#ffe000', rough=0.45, spec=0.15),
        black=mat('plastic_black', '#0c0c0e', rough=0.45),
        white=mat('print_white', '#dcdde2', rough=0.5),
        portrim=mat('port_rim', '#5d5e64', rough=0.42),
        portin=mat('port_inner', '#17181b', rough=0.6),
        portpin=mat('port_pin', '#9a9ba0', rough=0.45),
        irrim=mat('ir_rim', '#77787e', rough=0.4),
        tealglow=mat('reset_glow', '#37e6d2', rough=0.4, emit='#37e6d2', emit_power=0.25),
        blueglow=mat('eject_glow', '#3f7dff', rough=0.4, emit='#3f7dff', emit_power=0.2),
        ps_red=mat('ps_red', '#d8231c', rough=0.3),
        ps_yel=mat('ps_yellow', '#f2b400', rough=0.3),
        ps_blu=mat('ps_blue', '#1f6fc4', rough=0.3),
        ps_grn=mat('ps_green', '#1fa24a', rough=0.3),
        board=mat('board_slim', tex=tex + 'board_slim.jpg', rough=0.45),
        pcb=mat('pcb_teal', '#16705f', rough=0.45),
        chip=mat('chip_black', '#141416', rough=0.42),
        chiplid=mat('chip_lid', '#c9cbcc', rough=0.3, metal=1.0),
        chipprint=mat('chip_print', '#d2d4d8', rough=0.5),
        chipdark=mat('chip_print_dark', '#2a2c30', rough=0.5),
        cap=mat('cap_alu', '#b8bcc0', rough=0.35, metal=1.0),
        ferrite=mat('ferrite', '#2c2c30', rough=0.8),
        laser=mat('sticker_laser', tex=tex + 'laser.jpg', rough=0.6),
        disc=mat('disc_silver', tex=tex + 'disc.jpg', rough=0.14, metal=1.0),
        drive=mat('drive_black', '#101012', rough=0.55),
        fan=mat('fan_black', '#0e0e10', rough=0.6),
        flex=mat('flex_amber', '#b5721e', rough=0.45),
        boot=mat('battery_boot', '#0b0b0c', rough=0.75),
        cell=mat('cr2032', '#b4b6b8', rough=0.28, metal=1.0),
        wire_r=mat('wire_red', '#c01818', rough=0.5),
    )


def build(col, tex):
    m = materials(tex)
    parts = []

    # ---------------------------------------------------- the lid and its two flanking panels
    lid = Part('lid', (0, 0, 165), 'The top case, the fine stipple everyone knows. The left half lifts: the disc goes in from the top.')
    lid.tile = {'slim_lid': 16.0}
    # the two sides of the band
    lid.box(0, BAND[0] - 0.9, 0, D, LID_Z, PL_T[1], m['lid'], bevel=0.6, seg=3)
    lid.box(BAND[1] + 0.9, W, 0, D, LID_Z, PL_T[1], m['lid'], bevel=0.6, seg=3)
    # under it, back from the front: the rest of its edge at the ends and the back, and the plate
    lid.box(0, W, RAIL_Y, D, PL_T[0], LID_Z, m['body'])
    lid.box(0, W, RAIL_Y, D, PL_T[0] - 0.8, PL_T[0], m['inner'])
    lid.box(0.4, W - 0.4, 0.4, RAIL_Y + 0.1, LID_Z - 0.02, LID_Z + 0.01, m['dark'])
    for x0_, x1_ in ((BAND[0] - 0.95, BAND[0] + 0.05), (BAND[1] - 0.05, BAND[1] + 0.95)):
        lid.box(x0_, x1_, 0, D, LID_Z - 0.1, LID_Z + 0.12, m['dark'])
    # the lip along the front: black, with a thin line of light on its rounded edge
    for x0_, x1_ in ((0.5, BAND[0] - 0.9), (BAND[1] + 0.9, W - 0.5)):
        lid.box(x0_, x1_, -0.015, 0.5, LID_Z + 0.05, 27.2, m['edge'])
        lid.box(x0_, x1_, -0.02, 0.3, 27.2, 27.65, m['edge_hi2'])
    # the row of slots under the lid's rim at the back
    for x0_, x1_ in WINDOWS:
        lid.box(x0_, x1_, D - 0.02, D + 0.02, PL_T[0], 27.4, m['dark'])
    # SONY, read from the front, at the back left; the logos at the front right, glossy print that catches the light
    top = lambda x, y: plane((x, y, H + 0.01), (1, 0, 0), (0, 1, 0))
    lid.text('SONY', 'georgiab.ttf', 6.6, plane((7, D - 9.0, H + 0.01), (1, 0, 0), (0, 1, 0)), m['ink'], depth=0.02, stretch=1.35)
    lid.text('PlayStation', 'segoeuib.ttf', 2.4, top(153.5, 7.0), m['tone'])
    lid.text('DVD', 'arialbd.ttf', 5.0, top(170, 7.4), m['tone'], stretch=1.25)
    lid.text('VIDEO', 'arialbd.ttf', 1.7, top(170.6, 5.4), m['tone'], stretch=1.2)
    lid.box(188, 198, 6.6, 11.4, H, H + 0.03, m['tone'])
    lid.text('COMPACT', 'arialbd.ttf', 1.3, top(188, 5.1), m['tone'])
    lid.text('DVD', 'arialbd.ttf', 5.6, top(200.5, 7.2), m['tone'], stretch=1.25)
    lid.text('ROM', 'arialbd.ttf', 1.7, top(202.4, 5.3), m['tone'], stretch=1.2)
    lid.text('DVD', 'arialbd.ttf', 5.6, top(213.5, 7.2), m['tone'], stretch=1.25)
    lid.text('R', 'arialbd.ttf', 1.7, top(217.4, 5.3), m['tone'], stretch=1.2)
    parts.append(lid)

    # ---------------------------------------------------- the band
    band = Part('band', (0, 0, 205), 'The glossy band carrying the PS2 mark, outlined here where the fat printed it in blue.', spin=1.4)
    band.box(BAND[0], BAND[1], 0, D + 0.3, LID_Z, 27.7, m['band'], bevel=0.3, seg=2)
    band.box(BAND[0] + 0.3, BAND[1] - 0.3, -0.015, 0.4, LID_Z + 0.05, 27.2, m['edge'])
    # its back end drops down over the network port as a black block
    band.box(BAND[0], BAND[1], D - 1, D + 0.3, 22.6, LID_Z, m['dark'])
    # the mark in outline at the back end, reading as on the fat: rear to front, 'up' towards the right end
    art = plane((0, D, 27.71), (0, -1, 0), (1, 0, 0))
    k = 0.255
    ps2_logo(band, art, 3.5, 85.6, k, 0.42, (m['ink'], m['ink'], m['ink']))
    band.text('PlayStation 2', 'segoeuib.ttf', 2.4, plane((82.9, D - 19.5, 27.71), (0, -1, 0), (1, 0, 0)), m['ink'], align='CENTER', depth=0.02)
    parts.append(band)

    # ---------------------------------------------------- the middle and bottom plates, and the front's rails
    shell = Part('shell', (0, 0, 90), 'The top half\'s plates. They wrap the front and the right end; at the back they stop at the band, where the ports begin.')
    def rail(x0, x1, z0, z1, lights=True, foot=0.5):
        shell.box(x0, x1, RAIL_F, RAIL_Y, z0, z1, m['edge'], bevel=0.25, seg=2)
        if lights:
            # each plate shows two lines of light, the thick one on its rounded top edge and a second at its foot
            shell.box(x0 + 0.15, x1 - 0.15, RAIL_F - 0.015, RAIL_F + 0.3, z1 - 1.2, z1 - 0.2, m['edge_hi'])
            shell.box(x0 + 0.15, x1 - 0.15, RAIL_F - 0.015, RAIL_F + 0.3, z0 + 0.1, z0 + 0.1 + foot, m['edge_hi2'])
        # no shadows in a web render: the slit's floor and roof are dark themselves
        shell.box(x0, x1, RAIL_F + 0.4, RAIL_Y, z1 - 0.01, z1 + 0.02, m['dark'])
        shell.box(x0, x1, RAIL_F + 0.4, RAIL_Y, z0 - 0.02, z0 + 0.01, m['dark'])
    # the middle plate along the front: the card doors take its left half, the buttons its right end
    rail(0, DOOR1[0], *PL_M)
    rail(DOOR1[1], DOOR2[0], *PL_M)
    rail(DOOR2[1], 101, *PL_M)
    rail(101.4, 157.2, *PL_M)
    rail(167.2, 203.3, *PL_M)
    rail(203.7, 224.6, *PL_M, lights=False)
    rail(225, W, *PL_M)
    # the bottom plate runs the whole width
    rail(0, W, *PL_B, foot=1.0)
    # both plates wrap the right end, back to the rear wall
    for z0, z1 in (PL_M, PL_B):
        shell.box(W - RAIL_Y, W, RAIL_F, D - 1.2, z0, z1, m['edge'], bevel=0.25, seg=2)
        shell.box(W - 0.3, W + 0.015, RAIL_F + 0.3, D - 1.6, z1 - 1.2, z1 - 0.2, m['edge_hi'])
        shell.box(W - RAIL_Y, W - 0.4, RAIL_F, D - 1.2, z1 - 0.01, z1 + 0.02, m['dark'])
        shell.box(W - RAIL_Y, W - 0.4, RAIL_F, D - 1.2, z0 - 0.02, z0 + 0.01, m['dark'])
    # the black walls behind the slits
    shell.box(1.2, W - RAIL_Y, RAIL_Y, RAIL_Y + 1, PL_B[0], PL_T[0], m['dark'])
    shell.box(W - RAIL_Y - 1, W - RAIL_Y, RAIL_Y, D - 1.2, PL_B[0], PL_T[0], m['dark'])
    # the left end is one flat wall behind the corner, with the stand's notches
    shell.box(0, 1.2, 6, D, PL_B[0], PL_T[0], m['body'])
    for y_ in (62.6, 73.6, 85):
        shell.box(-0.02, 0.3, y_ - 1.7, y_ + 1.7, 14.2, 17.7, m['dark'])
    # the back behind the band's right half is flat too, with one seam under the lid
    shell.box(BAND[1], W, D - 1.2, D, PL_B[0], PL_T[0], m['body'])
    shell.box(BAND[1], W, D, D + 0.02, 25.4, 25.9, m['dark'])
    # print on the rail: the eject triangle, RESET and the power mark
    ry = RAIL_F - 0.02
    ej = plane((111, ry, 20.4), (1, 0, 0), (0, 0, 1))
    shell.poly([(-1.1, 0), (1.1, 0), (1.1, 0.14), (-1.1, 0.14)], ej, m['blueglow'], depth=0.02)
    shell.poly([(-1.1, 0), (-0.9, 0), (0.08, 1.3), (-0.08, 1.45)], ej, m['blueglow'], depth=0.02)
    shell.poly([(1.1, 0), (0.9, 0), (-0.08, 1.3), (0.08, 1.45)], ej, m['blueglow'], depth=0.02)
    shell.text('RESET', 'arial.ttf', 1.9, plane((207, ry, 20.6), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    shell.text('I /', 'arial.ttf', 2.0, plane((216.6, ry, 20.6), (1, 0, 0), (0, 0, 1)), m['tealglow'], align='CENTER')
    shell.ring((219.4, ry, 21.3), 'y', 0.6, 0.85, 0.02, m['tealglow'], n=16)
    # on the bottom plate: the MagicGate mark across the ports' gap, and the port numbers
    shell.text('MAGICGATE', 'georgiab.ttf', 2.7, plane((50, RAIL_F - 0.03, 14.6), (1, 0, 0), (0, 0, 1)), m['magic'], align='CENTER', depth=0.02, stretch=1.08)
    shell.text('1', 'arial.ttf', 2.3, plane((25.3, ry, 14.7), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    shell.text('2', 'arial.ttf', 2.3, plane((74.7, ry, 14.7), (1, 0, 0), (0, 0, 1)), m['label'], align='CENTER')
    parts.append(shell)

    # ---------------------------------------------------- the card doors
    doors = Part('card_doors', (-30, -125, 70), 'The memory card slots. RIPPCSX2 keeps each card as a file, so a save can be read, written and compared from a script.')
    for c in (DOOR1, DOOR2):
        doors.box(c[0], c[1], 0.3, 5, 21.1, LID_Z - 0.1, m['blackgloss'], bevel=0.2)
        doors.box(c[0] + 0.2, c[1] - 0.2, 0.28, 0.32, 24.6, 25.2, m['dark'])
        doors.box(c[0], c[1], 0.3, 5, 19.4, 21.1, m['dark'])
        doors.box(c[0], c[1], 0.3, 5, 18.7, 19.4, m['edge'])
        doors.text('MEMORY CARD', 'arialbd.ttf', 4.0, plane(((c[0] + c[1]) / 2, 0.26, 21.4), (1, 0, 0), (0, 0, 1)), m['door'], align='CENTER')
    parts.append(doors)

    # ---------------------------------------------------- the PS badge on the rail
    badge = Part('badge', (60, -115, 80), 'The little PlayStation mark that turns for a vertical stand.', spin=2.0)
    badge.poly(rrect(162.2, 20.9, 10.0, 6.6, 3.0), plane((0, 0.4, 0), (1, 0, 0), (0, 0, 1)), m['blackgloss'], depth=2.5)
    ps_badge(badge, 162.0, 0.37, 20.9, 1.15, m)
    parts.append(badge)

    # ---------------------------------------------------- the lower block
    base = Part('base', (0, 0, -95), 'The lower shell. The rear ports moved here: network, optical, AV and the yellow DC jack. Nothing inside runs off the mains now.')
    bm = m['body']
    base.box(0, LOW_X, LOW_Y, D, BOT, BOT + 1.0, m['inner'])
    # the front wall with its openings
    y0, y1 = LOW_Y, LOW_Y + 1.2
    t = PL_B[0] + 0.4
    bm = m['wall']
    base.box(0, LOW_X, y0, y1, BOT, PORT_Z[0], bm)
    base.box(0, LOW_X, y0, y1, PORT_Z[1], t, bm)
    # around the controller ports and the real holes of the USB sockets
    for a, b in ((0, PORT1[0]), (PORT1[1], PORT2[0]), (PORT2[1], USB1[0]), (USB1[1], USB2[0]), (USB2[1], VENT[0][0]), (VENT[2][1], LOW_X)):
        base.box(a, b, y0, y1, PORT_Z[0], PORT_Z[1], bm)
    for a, b in (USB1, USB2):
        base.box(a, b, y0, y1, PORT_Z[0], USB_Z[0], bm)
        base.box(a, b, y0, y1, USB_Z[1], PORT_Z[1], bm)
    # the vent: three columns, three rows of slots
    vx0, vx1 = VENT[0][0], VENT[2][1]
    base.box(vx0, vx1, y0, y1, PORT_Z[0], VENT_ROWS[0][0], bm)
    base.box(vx0, vx1, y0, y1, VENT_ROWS[0][1], VENT_ROWS[1][0], bm)
    base.box(vx0, vx1, y0, y1, VENT_ROWS[1][1], VENT_ROWS[2][0], bm)
    base.box(vx0, vx1, y0, y1, VENT_ROWS[2][1], PORT_Z[1], bm)
    for a, b in VENT_ROWS:
        base.box(vx0, vx1, y0 + 0.1, y1, a - 0.01, a + 0.02, m['dark'])
        base.box(vx0, vx1, y0 + 0.1, y1, b - 0.02, b + 0.01, m['dark'])
    base.box(VENT[0][1], VENT[1][0], y0, y1, PORT_Z[0], PORT_Z[1], bm)
    base.box(VENT[1][1], VENT[2][0], y0, y1, PORT_Z[0], PORT_Z[1], bm)
    base.box(vx0 - 0.6, vx1 + 0.6, y0 + 4, y0 + 4.2, BOT, t, m['dark'])
    base.box(vx0 - 0.6, vx1 + 0.6, y1, y0 + 4, BOT + 1, PORT_Z[0], m['dark'])
    base.box(vx0 - 0.6, vx1 + 0.6, y1, y0 + 4, PORT_Z[1], t, m['dark'])
    base.box(vx0 - 0.6, vx0, y1, y0 + 4, BOT + 1, t, m['dark'])
    base.box(vx1, vx1 + 0.6, y1, y0 + 4, BOT + 1, t, m['dark'])
    bm = m['body']
    # the sides, with the stand's small notches on the left end
    base.box(0, 1.2, LOW_Y, D, BOT, t, bm, bevel=0.15)
    base.box(LOW_X - 1.2, LOW_X, LOW_Y, D, BOT, t, bm, bevel=0.15)
    # the back: on the left half (X < 97) the wall runs up to the lid and carries the ports; on the right half it stops under the plates
    rb0, rb1 = D - 1.2, D
    base.box(0, BAND[0], rb0, rb1, BOT, PL_T[0], bm)
    base.box(BAND[0], LOW_X, rb0, rb1, BOT, 4.4, bm)
    base.box(BAND[0], LOW_X, rb0, rb1, 8.0, PL_B[0] + 0.9, bm)
    # up behind the network port, to the block under the band's end
    base.box(BAND[0], BAND[1], rb0, rb1, PL_B[0] + 0.9, 22.6, bm)
    # the low vent: four groups of two slots, with real holes
    prev = BAND[0]
    for x0_, x1_ in ((138, 149.6), (152.7, 165), (167.5, 180), (183, 195)):
        base.box(prev, x0_, rb0, rb1, 4.4, 8.0, bm)
        base.box(x0_, x1_, rb0, rb1, 5.9, 6.5, bm)
        prev = x1_
    base.box(prev, LOW_X, rb0, rb1, 4.4, 8.0, bm)
    base.box(136, 197, rb0 - 1.5, rb0 - 1.3, 4.4, 8.0, m['dark'])
    base.box(136, 197, rb0 - 1.3, rb1 - 0.1, 3.9, 4.42, m['dark'])
    base.box(136, 197, rb0 - 1.3, rb1 - 0.1, 7.98, 8.5, m['dark'])
    for x0_, x1_ in ((138, 149.6), (152.7, 165), (167.5, 180), (183, 195)):
        base.box(x0_, x1_, rb0 + 0.1, rb1 - 0.02, 5.88, 5.92, m['dark'])
        base.box(x0_, x1_, rb0 + 0.1, rb1 - 0.02, 6.48, 6.52, m['dark'])
    for x0_, x1_ in WINDOWS:
        base.box(x0_, x1_, D - 0.02, D + 0.02, 22.6, PL_T[0], m['dark'])
    # what shows through the slots: a few small glints, and the green of the board at the left end
    for x0_, x1_ in ((57.5, 60.5), (40, 44.6), (31, 35)):
        base.box(x0_, x1_, D + 0.02, D + 0.04, 24.0, 24.45, m['glint'])
    for x0_, x1_ in ((14, 16.8), (5, 9.5)):
        base.box(x0_, x1_, D + 0.02, D + 0.04, 23.8, 24.8, m['olive'])
    # the screw holes
    base.cyl((206, D, 9.4), 'y', 1.1, 0.05, m['dark'], n=12, smooth=False)
    base.cyl((6, D, 10.2), 'y', 1.1, 0.05, m['dark'], n=12, smooth=False)
    # the print under the ports, read from behind
    back = lambda x, z: plane((x, D + 0.02, z), (-1, 0, 0), (0, 0, 1))
    base.text('NETWORK', 'arial.ttf', 3.2, back(82.4, 7.2), m['print_dim'], align='CENTER', depth=0.01)
    base.text('DIGITAL OUT', 'arial.ttf', 3.0, back(62.5, 7.4), m['print_dim'], align='CENTER', depth=0.01)
    base.text('(OPTICAL)', 'arial.ttf', 3.0, back(62.5, 4.4), m['print_dim'], align='CENTER', depth=0.01)
    base.text('AV MULTI OUT', 'arial.ttf', 3.5, back(39, 7.6), m['print_dim'], align='CENTER', depth=0.01)
    base.text('DC IN 8.5V', 'arial.ttf', 2.8, back(15, 6.6), m['print_dim'], align='CENTER', depth=0.01)
    # the seam along the left end
    base.box(-0.015, 0.2, 6, D, 12.7, 13.4, m['dark'])
    # the stand's two slots on the left end
    for y_ in (71, 79.6):
        base.box(-0.02, 0.3, y_ - 0.6, y_ + 0.6, 5, 12.6, m['dark'])
    # feet
    for x, y in ((14, 20), (198, 20), (14, 140), (198, 140)):
        base.cyl((x, y, 0), 'z', 3.6, BOT, m['ink'], n=12)
    parts.append(base)

    # ---------------------------------------------------- the front's ports
    ctrl = Part('controller_board', (-20, -110, -45), 'Controllers on the front of the board, USB beside them. The ports OPL loads games over.')
    for c in (PORT1, PORT2):
        controller_port(ctrl, c[0], c[1], PORT_Z[0], PORT_Z[1], y0 - 0.02, m, lobe_w=10.6, lobe_h=3.8, pitch=12.0, corner=3.4, cz=5.4)
    for a, b in (USB1, USB2):
        usb_a(ctrl, a, b, USB_Z[0], USB_Z[1], y0 - 0.02, m, shell=m['usbshell'])
    # the USB trident between them, in line art
    us = plane((123.9, y0 - 0.03, 2.6), (1, 0, 0), (0, 0, 1))
    ctrl.poly([(-0.25, 0), (0.25, 0), (0.25, 5), (-0.25, 5)], us, m['portrim'], depth=0)
    ctrl.poly([(-1.6, 2.6), (-1.2, 2.6), (0, 1.0), (0, 1.5)], us, m['portrim'], depth=0)
    ctrl.poly([(1.6, 3.6), (1.2, 3.6), (0, 2.1), (0, 1.6)], us, m['portrim'], depth=0)
    # the IR window: glossy, lit along its left and bottom edges, a small mark in its corner
    ctrl.box(200.6, 207.8, y0 - 0.5, y0 + 0.4, 2.7, 9.3, m['irwin'], bevel=0.3)
    ctrl.box(200.8, 207.6, y0 - 0.52, y0 - 0.4, 2.7, 3.0, m['irrim'])
    ctrl.box(200.7, 201.0, y0 - 0.52, y0 - 0.4, 2.9, 9.1, m['irrim'])
    ctrl.box(201.8, 203.4, y0 - 0.53, y0 - 0.46, 3.4, 5.2, m['irrim'])
    ctrl.box(10, 150, y0 + 8, 34, 4, 5, m['pcb'])
    parts.append(ctrl)

    # ---------------------------------------------------- the rear ports, on the main board's edge
    rp = Part('rear_ports', (-20, 110, -25), 'Network, optical and AV. RIPPCSX2 can bridge the first to a real network, and it is OPL\'s other way to the games.')
    ry = D - 0.02
    def frame(x0, x1, z0, z1, t=0.4):
        for a0, a1, b0, b1 in ((x0, x1, z0, z0 + t), (x0, x1, z1 - t, z1), (x0, x0 + t, z0, z1), (x1 - t, x1, z0, z1)):
            rp.box(a0, a1, ry + 0.02, ry + 0.1, b0, b1, m['dark'])
    # RJ45
    rp.box(74.2, 90.6, ry - 8, ry + 0.02, 10.6, 22.5, m['black'])
    rp.box(76.2, 88.6, ry - 0.02, ry + 0.06, 11.5, 21.3, m['usbshell'])
    rp.box(76.6, 88.2, ry + 0.04, ry + 0.08, 11.9, 20.9, m['dark'])
    rp.box(79.6, 85.2, ry + 0.04, ry + 0.09, 19.5, 21.4, m['black'])
    for i in range(8):
        rp.box(78 + i * 1.15, 78.6 + i * 1.15, ry + 0.06, ry + 0.1, 12.3, 13.9, m['gold'])
    frame(74.2, 90.6, 10.6, 22.5)
    # optical
    rp.box(57.5, 67.5, ry - 8, ry + 0.02, 10.2, 20.2, m['body'])
    frame(59.7, 65.3, 12.4, 18.0, t=0.25)
    frame(57.5, 67.5, 10.2, 20.2)
    # AV multi out
    rp.box(27.7, 50.2, ry - 8, ry + 0.02, 10.2, 19.6, m['body'])
    rp.box(30.2, 47.7, ry + 0.02, ry + 0.05, 12.2, 17.6, m['dark'])
    rp.box(32.2, 45.7, ry + 0.04, ry + 0.07, 14.2, 15.6, m['portrim'])
    for i in range(12):
        rp.box(32.7 + i * 1.08, 33.2 + i * 1.08, ry + 0.06, ry + 0.09, 14.4, 15.4, m['steel'])
    frame(27.7, 50.2, 10.2, 19.6)
    # DC jack, its yellow ring
    rp.cyl((14.6, ry - 6, 14.8), 'y', 5.0, 6.04, m['black'], n=24)
    rp.ring((14.6, ry + 0.03, 14.8), 'y', 2.0, 4.3, 0.1, m['yellow'], n=28)
    rp.cyl((14.6, ry + 0.03, 14.8), 'y', 2.0, 0.04, m['dark'], n=20, smooth=False)
    rp.cyl((14.6, ry + 0.05, 14.8), 'y', 0.8, 0.08, m['gold'], n=10, smooth=False)
    parts.append(rp)

    # ---------------------------------------------------- the drive
    drv = Part('dvd_drive', (-10, 10, 130), 'The top-loading drive, and its spindle. RIPPCSX2 stands in for it with an image file: this is where disc timing and OPL\'s compatibility modes meet.')
    dz0, dz1 = 13.0, 22.0
    drv.box(5, 136, 8, 147, dz0, dz0 + 0.8, m['drive'])
    drv.box(5, 136, 8, 10, dz0, dz1, m['drive'])
    drv.box(5, 136, 145, 147, dz0, dz1, m['drive'])
    drv.box(5, 7, 8, 147, dz0, dz1, m['drive'])
    drv.box(134, 136, 8, 147, dz0, dz1, m['drive'])
    drv.cyl((70, 78, dz0), 'z', 8, 4, m['steel'], n=28)
    drv.cyl((70, 78, dz0 + 4), 'z', 3, 2.4, m['silver'], n=16)
    # the pickup and its rails
    drv.box(40, 42, 20, 136, dz0 + 1, dz0 + 3, m['steel'])
    drv.box(98, 100, 20, 136, dz0 + 1, dz0 + 3, m['steel'])
    drv.box(56, 84, 110, 132, dz0 + 1, dz0 + 6, m['black'])
    drv.cyl((70, 120, dz0 + 6), 'z', 2.2, 0.5, m['chipprint'], n=16)
    drv.quad_on(plane((12, 14, dz0 + 0.85), (1, 0, 0), (0, 1, 0)), 40, 20, m['laser'])
    parts.append(drv)

    disc = Part('disc', (-20, -20, 200), 'A DVD. Most of the PS2 library is one disc image away, and the end goal of RIPPCSX2 is the whole library running through OPL\'s own code path.', spin=2.0)
    disc.disc((70, 78, 19.2), 60, 1.2, m['disc'])
    disc.cyl((70, 78, 20.41), 'z', 7.5, 0.05, m['dark'], n=32)
    parts.append(disc)

    # ---------------------------------------------------- the metal plates
    top = Part('top_plate', (25, 10, 45), 'The top metal plate, over the one board.')
    top.box(8, 200, 12, 146, 10.6, 11.1, m['zinc'])
    top.box(44, 96, 56, 100, 11.1, 12.6, m['steel'], bevel=0.3)
    parts.append(top)

    bot = Part('bottom_plate', (10, 5, -55), 'The bottom plate. On the slim it also holds the cooler to the chip.')
    bot.box(8, 200, 12, 146, BOT + 1.2, BOT + 1.7, m['zinc'])
    parts.append(bot)

    # ---------------------------------------------------- the one board
    brd = Part('main_board', (10, 0, 8), 'One board and, in the later slims, one chip: the Emotion Engine and Graphics Synthesizer on a single die. Exactly what a compatibility test has to treat as one machine.')
    bz = 6.6
    brd.box(8, 204, 13, 148, bz - 1.2, bz - 0.02, m['pcb'])
    brd.textured_quad(8, 204, 13, 148, bz, m['board'])
    # the EE+GS, then RDRAM and the IOP, as the keepouts on its picture
    bm2 = 196 / 1024
    def on_board(px0, py0, px1, py1):
        return 8 + px0 * bm2, 8 + px1 * bm2, 148 - py1 * 138 / 720, 148 - py0 * 138 / 720
    x0, x1, y0b, y1b = on_board(330, 230, 620, 500)
    brd.box(x0, x1, y0b, y1b, bz, bz + 1.4, m['chip'], bevel=0.2)
    brd.box(x0 + 5, x1 - 5, y0b + 5, y1b - 5, bz + 1.4, bz + 2.2, m['chiplid'], bevel=0.2)
    brd.text('EE + GS', 'arialbd.ttf', 5, plane(((x0 + x1) / 2, (y0b + y1b) / 2 - 1, bz + 2.23), (1, 0, 0), (0, 1, 0)), m['chipdark'], align='CENTER', depth=0.02)
    x0, x1, y0b, y1b = on_board(660, 250, 760, 350)
    brd.box(x0, x1, y0b, y1b, bz, bz + 1.3, m['chip'], bevel=0.15)
    brd.text('IOP', 'arialbd.ttf', 4, plane(((x0 + x1) / 2, (y0b + y1b) / 2 - 1.4, bz + 1.33), (1, 0, 0), (0, 1, 0)), m['chipprint'], align='CENTER', depth=0.02)
    x0, x1, y0b, y1b = on_board(680, 400, 800, 490)
    brd.box(x0, x1, y0b, y1b, bz, bz + 1.1, m['chiplid'], bevel=0.15)
    for x, y, r, h in ((30, 40, 2.6, 3.6), (38, 40, 2.6, 3.6), (178, 120, 2.6, 3.6), (186, 120, 2.6, 3.6), (150, 40, 2.2, 3.2), (160, 36, 2.2, 3.2)):
        brd.cyl((x, y, bz), 'z', r, h, m['cap'], n=14)
    parts.append(brd)

    # ---------------------------------------------------- the battery in its boot, and the fan
    bat = Part('battery', (95, -35, 45), 'The clock battery in its black boot, on two wires: the RTC RIPPCSX2 keeps in its own settings.', spin=1.6)
    bat.cyl((186, 70, 10), 'z', 11, 3.6, m['boot'], n=32)
    bat.text('CR2032', 'arial.ttf', 3.0, plane((186, 69, 13.62), (1, 0, 0), (0, 1, 0)), m['label'], align='CENTER', depth=0.02)
    bat.box(176, 178, 70, 70.6, 9, 10, m['wire_r'])
    parts.append(bat)

    fan = Part('fan', (90, 80, 40), 'The slim\'s small blower, under its cover at the back right.', spin=1.8)
    cx, cy = 176, 120
    fan.box(155, 200, 98, 146, 11.2, 12.0, m['fan'])
    fan.cyl((cx, cy, 12), 'z', 19, 0.04, m['dark'], n=40, smooth=False)
    fan.cyl((cx, cy, 12), 'z', 7, 2.4, m['fan'], n=20)
    for i in range(11):
        a = i * 2 * math.pi / 11
        c, s = math.cos(a), math.sin(a)
        fan.poly([(7, -1), (18, -3.4), (18, 1.2), (7, 1)], plane((cx, cy, 13), (c, s, 0), (-s, c, 0)), m['fan'], depth=0.6)
    parts.append(fan)

    return [p.finish(col) for p in parts]
