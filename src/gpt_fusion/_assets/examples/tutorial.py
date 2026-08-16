"""Load sample data and display basic statistics."""

from pathlib import Path
from gpt_fusion import load_numbers_from_csv, average_from_csv, median_from_csv


def _find_csv_path() -> Path:
    """Locate numbers.csv. In the repo checkout this script sits at
    examples/tutorial.py with data at ../data/numbers.csv, but
    create_csv_app copies it as app.py next to a flat numbers.csv in the
    same directory. Check both."""
    here = Path(__file__).resolve().parent
    for candidate in (here / "numbers.csv", here.parent / "data" / "numbers.csv"):
        if candidate.is_file():
            return candidate
    return here / "numbers.csv"


def main() -> None:
    csv_path = _find_csv_path()
    values = load_numbers_from_csv(csv_path)
    print("Values:", values)
    print("Average:", average_from_csv(csv_path))
    print("Median:", median_from_csv(csv_path))


if __name__ == "__main__":
    main()
