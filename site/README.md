# RIPPCSX2's website

**[akilluminati47.github.io/RIPPCSX2](https://akilluminati47.github.io/RIPPCSX2/)**: a PS2 you can take apart or blow up, and everything about RIPPCSX2 in its Info panel. A cousin of [BIBLE's site](https://akilluminati47.github.io/BIBLE/): the same sky, floor, towers and fire, with real models in place of the TVs. Blow up the fat and you get the slim, and back.

It is a plain static site: no build step, no trackers, no accounts, nothing from another server. To try it on your PC:

```bash
python tools/site/serve.py
```

Then open http://localhost:8335/.

## The consoles

`site/models/ps2-fat.glb` and `ps2-slim.glb` are modelled in Blender, by scripts, in real millimetres:

| File | What it is |
|---|---|
| `tools/site/blender/ps2kit.py` | The kit: boxes with chamfered edges, cylinders, rings, flat art and text as real geometry, and `Part`, one thing that comes away in the exploded view with its own origin, explode vector and caption |
| `tools/site/blender/fat.py` | The fat, 301 x 182 x 78 mm from Sony's manual |
| `tools/site/blender/slim.py` | The slim, 230 x 152 x 28 mm |
| `tools/site/blender/gen_textures.py` | The surface textures and boards, all generated, nothing traced |
| `tools/site/blender/build_models.py` | Builds them and writes the .glb files |

```bash
python tools/site/blender/gen_textures.py
blender -b --python tools/site/blender/build_models.py -- fat slim
```

Every position was measured, not guessed: each reference photograph's camera was solved from the console's known corners (square pixels, Levenberg-Marquardt from a DLT), each face was rectified through that camera to a true elevation with a millimetre grid, and each pass of the model was rendered through the same camera and compared with the photograph, band by band, as brightness along a line. The rails on both consoles now land within about half a millimetre of the photographs. That is how the fat's front rows came out 7.6 mm apart with 3.4 mm slits and a thick bottom row, how its lower block came out standing 14 mm behind the fins, and how the slim's plates came out 2.8 mm thick with 3 mm slits, its left end and the back of its right half flat walls, and its rear ports high under the lid. The photographs were only measured: none of them is here, and no texture comes from one. The insides follow published teardowns.

A web render has no shadows, so what a photograph shows as shade is built in: the floors and roofs of the slits and vents are black, the expansion bay gets darker in steps as it goes in, and the thin lines of light along the rounded edges are real strips.

To measure again, `tools/site/measure` holds the scripts: `camfit.py` solves the cameras from corner picks, `render.sh` renders through them, `compare.py` puts photo and render side by side, `elev.py` rectifies a face of each to a millimetre grid, and `bands.py` reads the bands of dark and light as numbers. They expect a `refs/` folder of your own with clear photographs of a fat from the front left and the back and a slim from the front left and back right, and the corner picks in `camfit.py` will want redoing for yours. Those are not in the repo, and should not be.

## What is real and what is not

What the page says RIPPCSX2 does today was checked in the lab. What it says RIPPCSX2 is going towards is marked as that, in the panel's **Where it is going** column. The explosions are synthesised, and there is no Sony audio.

Unofficial fan project. Both consoles are fan-made from published sizes and photographs. Sony, PlayStation, PS2, DVD and MagicGate are trademarks of their owners. RIPPCSX2 is a GPL-3.0 fork of PCSX2, not affiliated with the PCSX2 team or with Sony.
