from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean, median
from typing import Iterator

from .exceptions import DataError, SecurityError


def _validate_csv_path(path: str | Path) -> Path:
    """Validate and resolve CSV file path.

    Args:
        path: Path to validate

    Returns:
        Resolved path object

    Raises:
        SecurityError: If path attempts directory traversal
        FileNotFoundError: If file doesn't exist
    """
    # Prevent path traversal attacks - check before resolving
    if ".." in str(path):
        raise SecurityError(f"Path traversal detected: {path}")

    path = Path(path).resolve()

    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")

    return path


def load_numbers_from_csv_stream(
    path: str | Path, chunk_size: int = 1000
) -> Iterator[float]:
    """Stream numbers from a CSV file with a ``value`` column.

    Memory-efficient alternative to load_numbers_from_csv for large files.

    Args:
        path: Path to the CSV file to load
        chunk_size: Number of rows to process at once

    Yields:
        Float values from the 'value' column

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        SecurityError: If path attempts directory traversal
    """
    path = _validate_csv_path(path)

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        chunk = []

        for row in reader:
            value = row.get("value")
            if value is None:
                continue

            try:
                chunk.append(float(value))
            except ValueError:
                # Ignore rows that cannot be converted to float
                continue

            if len(chunk) >= chunk_size:
                yield from chunk
                chunk = []

        # Yield remaining values
        if chunk:
            yield from chunk


def load_numbers_from_csv(
    path: str | Path, use_streaming: bool = False, chunk_size: int = 1000
) -> list[float]:
    """Load numbers from a CSV file with a ``value`` column.

    Args:
        path: Path to the CSV file to load
        use_streaming: If True, use streaming for large files
            (default: False for compatibility)
        chunk_size: Number of rows to process at once when streaming

    Returns:
        List of float values from the 'value' column

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        SecurityError: If path attempts directory traversal
        DataError: If CSV file has no valid data
    """
    if use_streaming:
        return list(load_numbers_from_csv_stream(path, chunk_size))

    path = _validate_csv_path(path)

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


def average_from_csv(path: str | Path, use_streaming: bool = False) -> float:
    """Return the average of the ``value`` column in *path*.

    Args:
        path: Path to the CSV file
        use_streaming: If True, calculate average without loading entire file
            into memory

    Returns:
        Average of numeric values in the 'value' column

    Raises:
        DataError: If no valid numeric values found
    """
    if use_streaming:
        # Memory-efficient streaming calculation
        total = 0.0
        count = 0

        for value in load_numbers_from_csv_stream(path):
            total += value
            count += 1

        if count == 0:
            raise DataError(f"No valid numeric values found in {path}")

        return total / count

    values = load_numbers_from_csv(path)
    if not values:
        raise DataError(f"No valid numeric values found in {path}")
    return mean(values)


def median_from_csv(path: str | Path, use_streaming: bool = False) -> float:
    """Return the median of the ``value`` column in *path*.

    Args:
        path: Path to the CSV file
        use_streaming: If True, use streaming (still loads all values for
            median calculation)

    Returns:
        Median of numeric values in the 'value' column

    Raises:
        DataError: If no valid numeric values found

    Note:
        Median calculation requires all values in memory regardless of streaming mode.
        For very large files, consider using average_from_csv with streaming instead.
    """
    # Note: Median requires all values to be loaded for sorting
    # Streaming doesn't provide memory benefits for median calculation
    values = load_numbers_from_csv(path, use_streaming=use_streaming)
    if not values:
        raise DataError(f"No valid numeric values found in {path}")
    return median(values)
