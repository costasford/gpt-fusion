"""Test the __main__ module."""

import subprocess
import sys


def test_main_module(tmp_path):
    """Test running the module with -m flag."""
    result = subprocess.run(
        [sys.executable, "-m", "gpt_fusion", "create_csv_app", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert (tmp_path / "app.py").is_file()
    assert (tmp_path / "numbers.csv").is_file()


def test_console_script_entry_point_is_importable():
    """pyproject.toml's [project.scripts] entry (gpt_fusion.__main__:main)
    must resolve to a callable, or the installed `gpt-fusion` command
    crashes with an ImportError before running a single line of user code.
    `python -m gpt_fusion` alone doesn't exercise this - it only hits the
    `if __name__ == "__main__"` guard, not the `main` attribute pip's
    console-script wrapper actually imports.
    """
    from gpt_fusion.__main__ import main

    assert callable(main)
