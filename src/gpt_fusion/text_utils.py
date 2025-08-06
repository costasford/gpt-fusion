from __future__ import annotations

"""Utility functions for basic text manipulation."""

import re
import string
from collections import Counter

__all__ = [
    "word_count",
    "unique_words",
    "reverse_words",
    "count_characters",
    "remove_punctuation",
    "most_common_word",
    "to_title_case",
    "is_palindrome",
]


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def unique_words(text: str) -> set[str]:
    """Return a set of unique whitespace-separated words from *text*."""
    return set(text.split())


def reverse_words(text: str) -> str:
    """Return *text* with the order of whitespace-separated words reversed."""
    return " ".join(reversed(text.split()))


def count_characters(text: str) -> int:
    """Return the number of characters in *text*."""
    return len(text)


def remove_punctuation(text: str) -> str:
    """Return *text* with ASCII punctuation characters removed."""
    return text.translate(str.maketrans("", "", string.punctuation))


def most_common_word(text: str, case_sensitive: bool = True) -> str:
    """Return the most frequently occurring whitespace-separated word.

    Args:
        text: Input text to analyze
        case_sensitive: Whether to treat words with different cases as different

    Returns:
        Most common word, or empty string if no words found

    Note:
        If multiple words have the same highest frequency, returns the first one
        encountered in alphabetical order for deterministic behavior.
    """
    if not text or not text.strip():
        return ""

    words = text.split()
    if not case_sensitive:
        words = [word.lower() for word in words]

    counts = Counter(words)
    # Sort by count (descending) then alphabetically for deterministic results
    most_common = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return most_common[0][0]


def to_title_case(text: str) -> str:
    """Return *text* in title case."""
    return text.title()


def is_palindrome(text: str) -> bool:
    """Return ``True`` if *text* is a palindrome.

    Comparison ignores case and punctuation.
    """
    cleaned = re.sub(r"[^A-Za-z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]
