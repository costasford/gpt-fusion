"""Top-level package for gpt-fusion."""

from __future__ import annotations

import importlib
from typing import Any

from .analysis import average_from_csv, load_numbers_from_csv, median_from_csv
from .core import greet
from .utils import (
    ChatHistory,
    add_numbers,
    divide_numbers,
    multiply_numbers,
    subtract_numbers,
)
from .text_utils import (
    is_palindrome,
    most_common_word,
    remove_punctuation,
    reverse_words,
    to_title_case,
    unique_words,
    word_count,
    count_characters,
)

_OPTIONAL_ATTRS: dict[str, tuple[str, str]] = {
    "scrape": ("web_scraper", "scrape"),
    "backend_app": ("backend", "app"),
    "TwitterBot": ("twitter_bot", "TwitterBot"),
    "TwitchClient": ("twitch", "TwitchClient"),
    "Project": ("projects", "Project"),
    "PROJECTS": ("projects", "PROJECTS"),
}


def __getattr__(name: str) -> Any:
    """Lazily import optional components."""
    if name in _OPTIONAL_ATTRS:
        module_name, attr_name = _OPTIONAL_ATTRS[name]
        module = importlib.import_module(f".{module_name}", __name__)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name}")


__all__ = [
    "greet",
    "ChatHistory",
    "add_numbers",
    "multiply_numbers",
    "subtract_numbers",
    "divide_numbers",
    "load_numbers_from_csv",
    "average_from_csv",
    "scrape",
    "median_from_csv",
    "word_count",
    "unique_words",
    "reverse_words",
    "count_characters",
    "remove_punctuation",
    "most_common_word",
    "to_title_case",
    "is_palindrome",
    "TwitterBot",
    "TwitchClient",
    "backend_app",
    "Project",
    "PROJECTS",
]
