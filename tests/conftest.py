import sys
from pathlib import Path

# If gpt_fusion is already installed (e.g. a real wheel install being
# tested), leave sys.path alone so tests exercise that install rather than
# silently falling back to the source tree. Only add src/ when running
# straight from a checkout without installing the package first.
try:
    import gpt_fusion  # noqa: F401
except ImportError:
    SRC_PATH = Path(__file__).resolve().parents[1] / "src"
    sys.path.insert(0, str(SRC_PATH))
