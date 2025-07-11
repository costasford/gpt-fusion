import sys
from pathlib import Path

# Ensure src/ is on the import path for tests without installation
SRC_PATH = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_PATH))
