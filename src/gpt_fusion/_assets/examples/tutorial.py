"""Load sample data and display basic statistics."""

from pathlib import Path
from gpt_fusion import load_numbers_from_csv, average_from_csv, median_from_csv


def main() -> None:
    csv_path = Path(__file__).resolve().parents[1] / "data" / "numbers.csv"
    values = load_numbers_from_csv(csv_path)
    print("Values:", values)
    print("Average:", average_from_csv(csv_path))
    print("Median:", median_from_csv(csv_path))


if __name__ == "__main__":
    main()
