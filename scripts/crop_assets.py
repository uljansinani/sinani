#!/usr/bin/env python3
"""Pixel-detected crop for portfolio image assets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "notebook" / "media" / "sources"
ASSETS = ROOT / "assets"

LUM_THRESHOLD = 60
INSET_START = 6
INSET_STEP = 2
MAX_ATTEMPTS = 5
BORDER_PX = 3
BORDER_MIN_LUM = 40


def luminance(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return (0.299 * r + 0.587 * g + 0.114 * b).astype(np.float32)


def content_bbox(gray: np.ndarray, threshold: float) -> tuple[int, int, int, int]:
    ys, xs = np.where(gray > threshold)
    if len(xs) == 0:
        raise ValueError("no content pixels found above luminance threshold")
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def inset_box(box: tuple[int, int, int, int], inset: int, w: int, h: int) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    left = min(max(0, left + inset), w - 1)
    top = min(max(0, top + inset), h - 1)
    right = max(left + 1, min(w, right - inset))
    bottom = max(top + 1, min(h, bottom - inset))
    return left, top, right, bottom


def assert_border_luminance(gray: np.ndarray, border_px: int, min_lum: float) -> None:
    h, w = gray.shape
    if h < border_px * 2 or w < border_px * 2:
        raise AssertionError(f"image too small for {border_px}px border check")
    regions = [
        gray[:border_px, :].ravel(),
        gray[-border_px:, :].ravel(),
        gray[border_px:-border_px, :border_px].ravel(),
        gray[border_px:-border_px, -border_px:].ravel(),
    ]
    border = np.concatenate(regions)
    dark = border[border < min_lum]
    if len(dark) > 0:
        raise AssertionError(
            f"border assertion failed: {len(dark)} pixels in outer {border_px}px "
            f"have luminance < {min_lum} (min={float(dark.min()):.1f})"
        )


def crop_with_assertion(im: Image.Image, inset_start: int = INSET_START) -> Image.Image:
    rgb = np.array(im.convert("RGB"))
    gray = luminance(rgb)
    h, w = gray.shape
    box = content_bbox(gray, LUM_THRESHOLD)

    for attempt in range(MAX_ATTEMPTS):
        inset = inset_start + attempt * INSET_STEP
        crop_box = inset_box(box, inset, w, h)
        cropped = im.crop(crop_box)
        crop_gray = luminance(np.array(cropped.convert("RGB")))
        try:
            assert_border_luminance(crop_gray, BORDER_PX, BORDER_MIN_LUM)
            print(f"crop ok: inset={inset}px box={crop_box}", file=sys.stderr)
            return cropped
        except AssertionError as exc:
            print(f"attempt {attempt + 1}: {exc}", file=sys.stderr)

    raise SystemExit("border assertion failed after max attempts; assets not updated")


def export_dcam(im: Image.Image) -> tuple[int, int]:
    jpg_path = ASSETS / "dcam-linedrone-hydroquebec.jpg"
    webp_path = ASSETS / "dcam-linedrone-hydroquebec.webp"
    rgb = im.convert("RGB")

    for q in (82, 78, 75, 70):
        rgb.save(jpg_path, "JPEG", quality=q, optimize=True)
        if jpg_path.stat().st_size < 150_000:
            break

    rgb.save(webp_path, "WEBP", quality=82, method=6)
    print(f"exported {jpg_path.name}: {jpg_path.stat().st_size}B q~{q}")
    print(f"exported {webp_path.name}: {webp_path.stat().st_size}B")
    return rgb.size


def crop_dcam() -> tuple[int, int]:
    src = SOURCES / "dcam-linedrone-hydroquebec.png"
    if not src.exists():
        raise SystemExit(f"missing source: {src}")
    im = Image.open(src)
    cropped = crop_with_assertion(im)
    return export_dcam(cropped)


def headshot() -> None:
    """Future: crop Headshot-photo.png when restored to notebook/media/sources/.

    - Bbox of pixels with luminance > 45
    - Scale crop region down 6% about center
    - Export 480x480 jpg <60KB with border-luminance assertion
    """
    raise NotImplementedError("headshot source PNG not available; CSS-only change for now")


def main() -> None:
    parser = argparse.ArgumentParser(description="Crop portfolio image assets")
    parser.add_argument("--dcam", action="store_true", help="Re-crop DCAM field photo")
    args = parser.parse_args()
    if not args.dcam:
        parser.error("specify --dcam")
    w, h = crop_dcam()
    print(f"{w}x{h}")


if __name__ == "__main__":
    main()
