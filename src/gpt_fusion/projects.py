from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Project:
    """Small description of a demo project."""

    id: str
    name: str
    description: str


PROJECTS: list[Project] = [
    Project(
        id="python-utilities",
        name="Python utilities",
        description=(
            "Greeting helpers, math functions, text utilities and a small CSV "
            "reader. Includes a web scraper, Twitter bot and optional FastAPI backend."
        ),
    ),
    Project(
        id="auth-ui-kit",
        name="Auth UI Kit",
        description=(
            "Tailwind-styled login form powered by Firebase for experimenting with "
            "email/password and Google sign in flows."
        ),
    ),
    Project(
        id="unity-prototype",
        name="Unity prototype",
        description=(
            "Basic 3D scene demonstrating player movement, item pickups and simple "
            "enemy AI."
        ),
    ),
    Project(
        id="top-viewer-games",
        name="Top Viewer Games",
        description=(
            "Shows current popular Twitch channels and games using the Twitch API."
        ),
    ),
    Project(
        id="tutorial",
        name="Tutorial",
        description="Walkthrough for loading sample data and computing averages.",
    ),
]

__all__ = ["Project", "PROJECTS"]
