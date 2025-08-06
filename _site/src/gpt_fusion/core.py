"""Core functionality for gpt_fusion.

Currently this module contains a simple greeting helper which can be
expanded as the project grows.
"""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"Hello, {name}! Welcome to gpt-fusion."
