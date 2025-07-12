from __future__ import annotations

"""Utility functions for basic text manipulation."""

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
    import string

    return text.translate(str.maketrans("", "", string.punctuation))


def most_common_word(text: str) -> str:
    """Return the most frequently occurring whitespace-separated word."""
    from collections import Counter

    words = text.split()
    if not words:
        return ""
    counts = Counter(words)
    return counts.most_common(1)[0][0]


def to_title_case(text: str) -> str:
    """Return *text* in title case."""
    return text.title()


def is_palindrome(text: str) -> bool:
    """Return ``True`` if *text* is a palindrome.

    Comparison ignores case and punctuation.
    """
    import re

    cleaned = re.sub(r"[^A-Za-z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]
