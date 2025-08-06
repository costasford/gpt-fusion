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
