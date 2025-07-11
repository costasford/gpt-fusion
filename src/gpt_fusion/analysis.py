from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean


def load_numbers_from_csv(path: str | Path) -> list[float]:
    """Load numbers from a CSV file with a ``value`` column."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [float(row["value"]) for row in reader]


def average_from_csv(path: str | Path) -> float:
    """Return the average of the ``value`` column in *path*."""
    values = load_numbers_from_csv(path)
    return mean(values) if values else 0.0
