# Plan: provide simple cookie-cutter helpers for demo apps.
# 1. create_csv_app() copies the tutorial script and sample data into a
#    destination folder, renaming the script to app.py.
# 2. create_tailwind_ui() copies the auth-ui-kit directory to the
#    destination folder.
# 3. Both functions return the path to the created directory.

from __future__ import annotations

from pathlib import Path
import shutil


def create_csv_app(dst: str | Path) -> Path:
    """Create a minimal CSV demo in *dst* and return the path."""
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parents[2]
    shutil.copy2(root / "examples" / "tutorial.py", dst_path / "app.py")
    shutil.copy2(root / "data" / "numbers.csv", dst_path / "numbers.csv")
    return dst_path


def create_tailwind_ui(dst: str | Path) -> Path:
    """Copy the Tailwind auth demo into *dst* and return the path."""
    dst_path = Path(dst)
    src = Path(__file__).resolve().parents[2] / "auth-ui-kit"
    shutil.copytree(src, dst_path, dirs_exist_ok=True)
    return dst_path


__all__ = ["create_csv_app", "create_tailwind_ui"]


def _main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate starter kit demos")
    sub = parser.add_subparsers(dest="cmd", required=True)

    csv_p = sub.add_parser("create_csv_app", help="Create the CSV demo")
    csv_p.add_argument("dest")

    ui_p = sub.add_parser("create_tailwind_ui", help="Create the Tailwind demo")
    ui_p.add_argument("dest")

    args = parser.parse_args()
    if args.cmd == "create_csv_app":
        create_csv_app(args.dest)
    else:
        create_tailwind_ui(args.dest)


if __name__ == "__main__":
    _main()
