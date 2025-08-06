from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean, median


def load_numbers_from_csv(path: str | Path) -> list[float]:
    """Load numbers from a CSV file with a ``value`` column."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        values: list[float] = []
        for row in reader:
            value = row.get("value")
            if value is None:
                continue
            try:
                values.append(float(value))
            except ValueError:
                # Ignore rows that cannot be converted to float
                continue
        return values


def average_from_csv(path: str | Path) -> float:
    """Return the average of the ``value`` column in *path*."""
    values = load_numbers_from_csv(path)
    return mean(values) if values else 0.0


def median_from_csv(path: str | Path) -> float:
    """Return the median of the ``value`` column in *path*."""
    values = load_numbers_from_csv(path)
    return median(values) if values else 0.0
