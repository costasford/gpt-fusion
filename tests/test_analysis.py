from pathlib import Path

from gpt_fusion.analysis import load_numbers_from_csv, average_from_csv


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "numbers.csv"


def test_load_numbers_from_csv():
    values = load_numbers_from_csv(DATA_PATH)
    assert values == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_average_from_csv():
    assert average_from_csv(DATA_PATH) == 3.0
