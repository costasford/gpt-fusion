from __future__ import annotations

import os
from typing import Any

import requests


class TwitchClient:
    """Simple client for the public Twitch API."""

    def __init__(
        self, client_id: str | None = None, client_secret: str | None = None
    ) -> None:
        self.client_id = client_id or os.getenv("TWITCH_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("TWITCH_CLIENT_SECRET")
        if not self.client_id or not self.client_secret:
            raise ValueError("Twitch credentials are not fully specified")
        self._token: str | None = None

    def _authenticate(self) -> None:
        if self._token:
            return
        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        response = requests.post(url, params=params, timeout=10)
        response.raise_for_status()
        self._token = response.json()["access_token"]

    def _headers(self) -> dict[str, str]:
        self._authenticate()
        assert self._token
        return {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self._token}",
        }

    def get_top_games(self, first: int = 5) -> list[dict[str, Any]]:
        url = "https://api.twitch.tv/helix/games/top"
        response = requests.get(
            url, headers=self._headers(), params={"first": first}, timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])

    def get_top_streams(self, first: int = 5) -> list[dict[str, Any]]:
        url = "https://api.twitch.tv/helix/streams"
        response = requests.get(
            url, headers=self._headers(), params={"first": first}, timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])
