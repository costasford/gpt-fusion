#!/usr/bin/env python3
# GENERATED - DO NOT EDIT DIRECTLY
"""Run formatting, tests, and docs build like the CI workflow."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(cmd: str) -> None:
    """Execute *cmd* and exit on failure."""
    print(f"--> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    run("pre-commit run --all-files")
    run("pytest --cov=src --cov-report=xml -q")
    docs_dir = project_root / "docs"
    if docs_dir.is_dir():
        run("JEKYLL_ENV=production jekyll build -s docs -d docs/_site")
        run("PYTHONPATH=src python -m gpt_fusion.build_utils docs/_site docs/_site_tmp")
        run("rm -rf docs/_site")
        run("mv docs/_site_tmp docs/_site")
    print("All checks passed.")


if __name__ == "__main__":
    main()
