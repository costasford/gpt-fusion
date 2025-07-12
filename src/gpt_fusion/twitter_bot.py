from __future__ import annotations

"""Simple Twitter bot utilities."""

import os
from dataclasses import dataclass

import tweepy


@dataclass
class TwitterBot:
    """A small wrapper around Tweepy for posting tweets."""

    api_key: str | None = None
    api_secret: str | None = None
    access_token: str | None = None
    access_secret: str | None = None

    def __post_init__(self) -> None:
        self.api_key = self.api_key or os.getenv("TWITTER_API_KEY")
        self.api_secret = self.api_secret or os.getenv("TWITTER_API_SECRET")
        self.access_token = self.access_token or os.getenv(
            "TWITTER_ACCESS_TOKEN"
        )  # noqa: E501
        self.access_secret = self.access_secret or os.getenv(
            "TWITTER_ACCESS_SECRET"
        )  # noqa: E501

        if not all(
            [
                self.api_key,
                self.api_secret,
                self.access_token,
                self.access_secret,
            ]
        ):
            raise ValueError("Twitter credentials are not fully specified")

        auth = tweepy.OAuth1UserHandler(
            self.api_key,
            self.api_secret,
            self.access_token,
            self.access_secret,
        )
        self.client = tweepy.API(auth)

    def post_tweet(self, message: str) -> None:
        """Post *message* to Twitter."""
        self.client.update_status(message)
