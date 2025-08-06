from __future__ import annotations

import os
from typing import Any, Optional

import requests


class TwitchClient:
    """Simple client for the public Twitch API with connection pooling."""

    def __init__(
        self, client_id: str | None = None, client_secret: str | None = None
    ) -> None:
        self.client_id = client_id or os.getenv("TWITCH_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("TWITCH_CLIENT_SECRET")
        if not self.client_id or not self.client_secret:
            raise ValueError("Twitch credentials are not fully specified")
        self._token: str | None = None
        self._session: Optional[requests.Session] = None

    def _get_session(self) -> requests.Session:
        """Get or create a requests session with connection pooling."""
        if self._session is None:
            self._session = requests.Session()
            # Configure connection pooling
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=5, pool_maxsize=10, max_retries=2, pool_block=False
            )
            self._session.mount("http://", adapter)
            self._session.mount("https://", adapter)
        return self._session

    def close(self) -> None:
        """Close the session and clean up connections."""
        if self._session:
            self._session.close()
            self._session = None

    def _authenticate(self) -> None:
        if self._token:
            return
        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        session = self._get_session()
        response = session.post(url, params=params, timeout=10)
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
        session = self._get_session()
        response = session.get(
            url, headers=self._headers(), params={"first": first}, timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])

    def get_top_streams(self, first: int = 5) -> list[dict[str, Any]]:
        url = "https://api.twitch.tv/helix/streams"
        session = self._get_session()
        response = session.get(
            url, headers=self._headers(), params={"first": first}, timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])
