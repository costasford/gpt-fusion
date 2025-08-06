"""Top-level package for gpt-fusion."""

from __future__ import annotations

import importlib
from typing import Any

from .analysis import average_from_csv, load_numbers_from_csv, median_from_csv
from .config import config, get_config, update_config
from .core import greet
from .exceptions import (
    ConfigurationError,
    DataError,
    GPTFusionError,
    SecurityError,
    ValidationError,
)

from .starter_kits import create_csv_app, create_tailwind_ui
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
    "minify_dir": ("build_utils", "minify_dir"),
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
    "create_csv_app",
    "create_tailwind_ui",
    "ChatHistory",
    "add_numbers",
    "divide_numbers",
    "multiply_numbers",
    "subtract_numbers",
    "average_from_csv",
    "load_numbers_from_csv",
    "median_from_csv",
    "is_palindrome",
    "most_common_word",
    "word_count",
    "unique_words",
    "reverse_words",
    "count_characters",
    "remove_punctuation",
    "to_title_case",
    "scrape",
    "minify_dir",
    "TwitterBot",
    "TwitchClient",
    "backend_app",
    "Project",
    "PROJECTS",
    # Configuration
    "config",
    "get_config",
    "update_config",
    # Exceptions
    "GPTFusionError",
    "ValidationError",
    "DataError",
    "SecurityError",
    "ConfigurationError",
]
