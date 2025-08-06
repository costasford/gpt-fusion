from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean, median

from .exceptions import DataError, SecurityError


def load_numbers_from_csv(path: str | Path) -> list[float]:
    """Load numbers from a CSV file with a ``value`` column.

    Args:
        path: Path to the CSV file to load

    Returns:
        List of float values from the 'value' column

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        SecurityError: If path attempts directory traversal
        DataError: If CSV file has no valid data
    """
    # Prevent path traversal attacks - check before resolving
    if ".." in str(path):
        raise SecurityError(f"Path traversal detected: {path}")

    path = Path(path).resolve()

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
    """Return the average of the ``value`` column in *path*.

    Args:
        path: Path to the CSV file

    Returns:
        Average of numeric values in the 'value' column

    Raises:
        DataError: If no valid numeric values found
    """
    values = load_numbers_from_csv(path)
    if not values:
        raise DataError(f"No valid numeric values found in {path}")
    return mean(values)


def median_from_csv(path: str | Path) -> float:
    """Return the median of the ``value`` column in *path*.

    Args:
        path: Path to the CSV file

    Returns:
        Median of numeric values in the 'value' column

    Raises:
        DataError: If no valid numeric values found
    """
    values = load_numbers_from_csv(path)
    if not values:
        raise DataError(f"No valid numeric values found in {path}")
    return median(values)
