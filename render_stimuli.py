"""Render the stimulus clips: a baseline and a low/high pair per property, per scene.

    uv run python render_stimuli.py --calibrate                 # check each scene's camera constants
    uv run python render_stimuli.py --preview                   # one still per clip, as a contact sheet
    uv run python render_stimuli.py --check                     # flag pairs that barely differ in a scene
    uv run python render_stimuli.py                             # all clips -> public/stimuli/
    uv run python render_stimuli.py --scene pedestrian_crossing --property path_width

Every clip of a scene starts from the baseline display in study/properties.json; the
low and high clip of a property change only that property's settings (its ``render``
block). Clips are H.264 so browsers can play them. Previews and calibration images go
to data/previews/.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np

from avprops.clip_render import ClipRenderer, Style, read_frames, read_geometry, render_variants, path_on_ground
from avprops.common import load_config, load_properties, load_scenes, resolve, PROJECT_ROOT

TIMING_KEYS = {"show_when", "lead_time_s", "fade_s"}


def baseline_style(config: dict) -> Style:
    with resolve(config["properties"]).open(encoding="utf-8") as fh:
        overrides = {k: v for k, v in json.load(fh).get("baseline", {}).items() if not k.startswith("_")}
    return Style.from_overrides(Style(), overrides)


def variants(properties: list[dict], base: Style) -> list[tuple[str, Style]]:
    """(file name, style) for the baseline and both levels of every property."""
    out = [("baseline", base)]
    for prop in properties:
        if "render" not in prop:
            raise SystemExit(f"{prop['id']} has no render block, so it cannot be made as a clip; screen it out")
        for level in ("low", "high"):
            out.append((f"{prop['id']}_{level}", Style.from_overrides(base, prop["render"][level])))
    return out


def geometry_for(scene: dict):
    path = resolve(scene["geometry"]) if scene.get("geometry") else \
        PROJECT_ROOT / "data" / "geometry" / f"{scene['id']}_geometry.jsonl.gz"
    if not path.exists():
        raise FileNotFoundError(f"no geometry for {scene['id']} ({path}); run extract_geometry.py")
    return read_geometry(path)


def frame_at(clip: Path, index: int, size) -> np.ndarray:
    return next(read_frames(clip, index, 1, size=size))


def calibrate(scene: dict, geometry, out: Path) -> None:
    """Horizon, vanishing point, metre ticks and the path on one frame of the scene."""
    renderer = ClipRenderer(geometry, scene)
    index = int(round((scene["start_s"] + 1.0) * geometry.fps))
    image = frame_at(resolve(scene["clip"]), index, geometry.size)
    cam = renderer.camera
    cv2.line(image, (0, int(cam.horizon)), (image.shape[1], int(cam.horizon)), (0, 255, 255), 1)
    cv2.circle(image, (int(cam.vanish), int(cam.horizon)), 6, (0, 255, 255), 2)
    for d in (5, 10, 20, 30):
        for x in (-1.75, 1.75):  # lane edges of a 3.5 m lane
            u, v = cam.to_image(np.array([[x, d]]))[0]
            cv2.circle(image, (int(u), int(v)), 4, (0, 0, 255), -1)
        u, v = cam.to_image(np.array([[1.9, d]]))[0]
        cv2.putText(image, f"{d} m", (int(u) + 6, int(v) + 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    ground = path_on_ground(cam, geometry.frames[index].get("ribbon"), 40)
    if ground is not None:
        cv2.polylines(image, [cam.to_image(ground).round().astype(np.int32)], False, (255, 200, 0), 2)
    out.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out), image)


def preview(scene: dict, geometry, styles: list[tuple[str, Style]], out: Path) -> None:
    """One still per clip, tiled with its name: a quick check that each pair differs."""
    renderer = ClipRenderer(geometry, scene)
    fps = geometry.fps
    in_event = int(round(np.mean(scene.get("event_s") or [scene["start_s"] + scene["duration_s"] / 2]) * fps))
    before = int(round(scene["start_s"] * fps))
    clip = resolve(scene["clip"])
    tiles = []
    for name, style in styles:
        timing = any(getattr(style, k) != getattr(styles[0][1], k) for k in TIMING_KEYS) or name.startswith("show_when")
        index = before if timing else in_event
        strength = float(renderer.visibility(style)[index])
        image = renderer.render_frame(frame_at(clip, index, geometry.size), index, style, strength)
        image = cv2.resize(image, (480, 270), interpolation=cv2.INTER_AREA)
        cv2.rectangle(image, (0, 0), (480, 22), (0, 0, 0), -1)
        cv2.putText(image, f"{name}  t={index / fps:.1f}s", (6, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        tiles.append(image)
    columns = 3
    while len(tiles) % columns:
        tiles.append(np.zeros_like(tiles[0]))
    sheet = np.vstack([np.hstack(tiles[r:r + columns]) for r in range(0, len(tiles), columns)])
    out.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out), sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])


def check(scene: dict, geometry, styles: list[tuple[str, Style]], step_s: float = 0.5,
          min_changed: float = 0.002) -> list[tuple[str, float, bool]]:
    """Share of pixels that differ between the low and high clip of each property, sampled
    every step_s seconds. A property whose pair barely differs in this scene has nothing
    to act on here (no moving road users, no vehicles, no event) and needs another scene."""
    renderer = ClipRenderer(geometry, scene)
    fps = geometry.fps
    start = int(round(scene["start_s"] * fps))
    stop = min(len(geometry.frames), start + int(round(scene["duration_s"] * fps)))
    indices = list(range(start, stop, max(1, int(round(step_s * fps)))))
    frames = {i: frame_at(resolve(scene["clip"]), i, geometry.size) for i in indices}
    by_name = dict(styles)
    results = []
    for name in [n[:-4] for n, _ in styles if n.endswith("_low")]:
        low, high = by_name[name + "_low"], by_name[name + "_high"]
        vis_low, vis_high = renderer.visibility(low), renderer.visibility(high)
        changed = []
        for i in indices:
            a = renderer.render_frame(frames[i], i, low, float(vis_low[i]))
            b = renderer.render_frame(frames[i], i, high, float(vis_high[i]))
            changed.append(float((np.abs(a.astype(int) - b.astype(int)).max(axis=2) > 12).mean()))
        share = float(np.mean(changed))
        results.append((name, share, share >= min_changed))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scene", nargs="+", help="scene ids (default: every scene with a clip)")
    parser.add_argument("--property", nargs="+", help="property ids (default: every screened-in property)")
    parser.add_argument("--reserves", action="store_true", help="also the screened-out properties that can be rendered")
    parser.add_argument("--preview", action="store_true", help="contact sheet of stills instead of videos")
    parser.add_argument("--calibrate", action="store_true", help="camera calibration image per scene")
    parser.add_argument("--check", action="store_true",
                        help="report how much each pair differs in each scene, without rendering videos")
    args = parser.parse_args()

    config = load_config()
    props = load_properties(config, screened_only=not args.reserves and not args.property)
    if args.reserves:
        props = [p for p in props if "render" in p]
    if args.property:
        props = [p for p in props if p["id"] in args.property]
    styles = variants(props, baseline_style(config))
    scenes = [s for s in load_scenes(config) if s.get("clip")]
    if args.scene:
        scenes = [s for s in scenes if s["id"] in args.scene]

    check_path = PROJECT_ROOT / "data" / "stimulus_check.json"
    checked = json.loads(check_path.read_text()) if check_path.exists() else {}
    for scene in scenes:
        geometry = geometry_for(scene)
        previews = PROJECT_ROOT / "data" / "previews"
        if args.calibrate:
            calibrate(scene, geometry, previews / f"{scene['id']}_calibration.jpg")
            print(f"{scene['id']}: {previews / (scene['id'] + '_calibration.jpg')}")
            continue
        if args.check:
            print(f"{scene['id']}: share of pixels that differ between low and high (mean over the clip)")
            results = check(scene, geometry, styles)
            for name, share, ok in results:
                print(f"  {'ok  ' if ok else 'WEAK'} {name:<22} {share:7.2%}")
            checked[scene["id"]] = {name: {"changed": round(share, 5), "ok": ok} for name, share, ok in results}
            check_path.parent.mkdir(parents=True, exist_ok=True)
            check_path.write_text(json.dumps(checked, indent=1))
            continue
        if args.preview:
            preview(scene, geometry, styles, previews / f"{scene['id']}_properties.jpg")
            print(f"{scene['id']}: {previews / (scene['id'] + '_properties.jpg')}")
            continue
        out_dir = PROJECT_ROOT / "public" / "stimuli" / scene["id"]
        frames = render_variants(geometry, resolve(scene["clip"]), styles, out_dir,
                                 scene["start_s"], scene["duration_s"], scene)
        print(f"{scene['id']}: {len(styles)} clips of {frames} frames in {out_dir.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
