"""Detect and track road users in each scene's source clip and write overlay geometry.

    uv sync --extra extract
    uv run python extract_geometry.py                      # every scene with a clip
    uv run python extract_geometry.py --scene pedestrian_crossing --device mps

Writes data/geometry/<scene>_geometry.jsonl.gz and <scene>_occlusion.mp4, the geometry
format the clip renderer reads. A scene whose ``geometry`` field in study/scenes.json
points at existing geometry does not need this step. See avprops/extract.py for
what this simpler model of the scene does and does not do.
"""

from __future__ import annotations

import argparse

from avprops.common import load_config, load_scenes, resolve, PROJECT_ROOT
from avprops.extract import extract


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scene", nargs="+", help="scene ids (default: every scene with a clip)")
    parser.add_argument("--model", default="yolo26m-seg.pt", help="ultralytics segmentation model")
    parser.add_argument("--device", default=None, help="cpu, mps or cuda:0 (default: chosen by ultralytics)")
    args = parser.parse_args()

    scenes = [s for s in load_scenes(load_config()) if s.get("clip")]
    if args.scene:
        scenes = [s for s in scenes if s["id"] in args.scene]
    if not scenes:
        raise SystemExit("no scene with a clip selected")
    for scene in scenes:
        clip = resolve(scene["clip"])
        if not clip.exists():
            print(f"skip {scene['id']}: {clip} not found")
            continue
        path = extract(scene, clip, PROJECT_ROOT / "data" / "geometry", args.model, args.device)
        print(f"{scene['id']}: {path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
