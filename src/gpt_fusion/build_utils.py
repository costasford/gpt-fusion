from __future__ import annotations

"""Utilities for minifying and compressing static files."""

from pathlib import Path
import gzip
import shutil

import brotli
import htmlmin
from csscompressor import compress
from jsmin import jsmin


def _compress_file(path: Path) -> None:
    """Create gzip and brotli versions of *path* in the same directory."""
    data = path.read_bytes()
    with gzip.open(path.with_suffix(path.suffix + ".gz"), "wb") as gz_file:
        gz_file.write(data)
    path.with_suffix(path.suffix + ".br").write_bytes(brotli.compress(data))


def minify_dir(src_dir: str | Path, dst_dir: str | Path) -> None:
    """Minify HTML/CSS/JS files from *src_dir* into *dst_dir* and compress them."""
    src = Path(src_dir)
    dst = Path(dst_dir)
    for file in src.rglob("*"):
        if file.is_dir():
            continue
        target = dst / file.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        text: str | bytes
        if file.suffix.lower() in {".html", ".htm"}:
            text = htmlmin.minify(file.read_text(encoding="utf-8"), remove_comments=True)
            target.write_text(text, encoding="utf-8")
        elif file.suffix.lower() == ".css":
            text = compress(file.read_text(encoding="utf-8"))
            target.write_text(text, encoding="utf-8")
        elif file.suffix.lower() == ".js":
            text = jsmin(file.read_text(encoding="utf-8"))
            target.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(file, target)
            continue
        _compress_file(target)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Minify and compress static files")
    parser.add_argument("src", help="Source directory")
    parser.add_argument("dst", help="Destination directory")
    args = parser.parse_args()
    minify_dir(args.src, args.dst)
