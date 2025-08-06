from pathlib import Path
import pytest

from gpt_fusion.analysis import (
    average_from_csv,
    load_numbers_from_csv,
    median_from_csv,
)

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "numbers.csv"


def test_load_numbers_from_csv():
    values = load_numbers_from_csv(DATA_PATH)
    assert values == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_average_from_csv():
    assert average_from_csv(DATA_PATH) == 3.0


def test_median_from_csv():
    assert median_from_csv(DATA_PATH) == 3.0


def test_load_numbers_from_csv_skips_invalid(tmp_path):
    csv_path = tmp_path / "nums.csv"
    csv_path.write_text("value\n1\ninvalid\n2\n\n3\n", encoding="utf-8")

    assert load_numbers_from_csv(csv_path) == [1.0, 2.0, 3.0]


def test_load_numbers_from_csv_missing_file(tmp_path):
    missing_path = tmp_path / "nope.csv"
    with pytest.raises(FileNotFoundError):
        load_numbers_from_csv(missing_path)
