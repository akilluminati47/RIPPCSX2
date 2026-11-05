#!/bin/bash
# render.sh <fat|slim> [samples]: rebuilds a console and renders it through the solved photo cameras into r/, for compare.py, elev.py and bands.py.
# Run it in a folder of its own holding refs/ (see ../../../site/README.md). BLENDER names your Blender.
BLENDER="${BLENDER:-blender}"
HERE="$(cd "$(dirname "$0")" && pwd)"
"$BLENDER" -b --python "$HERE/../blender/build_models.py" -- "$1" --glb glb --renders r --cams refs/cams.json --samples "${2:-48}" 2>&1 | grep -E "BUILT|Error|Traceback"
