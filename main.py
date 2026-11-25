#!/usr/bin/env python3
"""Entry point for the news-image-20261124 submission.

Copies entry.png into the output directory the platform provides
($MAKEFUN_OUTPUT_DIR, default /output), then verifies the copy: the file
must be a PNG of at most 1 MiB and its SHA-256 must match the source.
Exits non-zero on any mismatch so a bad run fails loudly.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576  # 1 MiB
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(src):
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    with open(src, "rb") as f:
        header = f.read(len(PNG_MAGIC) + 25)
    if header[: len(PNG_MAGIC)] != PNG_MAGIC:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    # IHDR chunk: length (4) + "IHDR" (4) + width (4) + height (4), big-endian.
    if header[12:16] != b"IHDR":
        print("error: entry.png has no IHDR chunk", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"error: entry.png is {width}x{height}, over the "
              f"{MAX_SIDE}x{MAX_SIDE} limit", file=sys.stderr)
        return 1

    size = os.path.getsize(src)
    if size > MAX_BYTES:
        print(f"error: entry.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1

    expected = sha256(src)
    shutil.copyfile(src, dst)
    got = sha256(dst)
    if got != expected:
        print(f"error: checksum mismatch after copy: {got} != {expected}",
              file=sys.stderr)
        return 1

    print(f"entry.png: {width}x{height}, {size} bytes, sha256={expected}")
    print(f"copied to {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
