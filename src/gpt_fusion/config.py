from __future__ import annotations

"""Centralized configuration management for gpt-fusion package."""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Centralized configuration settings for gpt-fusion package."""

    # HTTP/Network settings
    HTTP_TIMEOUT: int = 10
    HTTP_POOL_CONNECTIONS: int = 10
    HTTP_POOL_MAXSIZE: int = 20
    HTTP_MAX_RETRIES: int = 3

    # Social media limits
    TWITTER_CHAR_LIMIT: int = 280

    # File processing settings
    CSV_CHUNK_SIZE: int = 1000
    BUILD_BATCH_SIZE: int = 50

    # User agent for web requests
    USER_AGENT: str = "gpt-fusion/0.0.1a0 (https://github.com/costasford/gpt-fusion)"

    # Logging
    LOG_LEVEL: str = "INFO"

    @classmethod
    def from_env(cls) -> Config:
        """Create config from environment variables with fallback to defaults."""
        return cls(
            HTTP_TIMEOUT=int(os.getenv("GPT_FUSION_HTTP_TIMEOUT", cls.HTTP_TIMEOUT)),
            HTTP_POOL_CONNECTIONS=int(
                os.getenv("GPT_FUSION_POOL_CONNECTIONS", cls.HTTP_POOL_CONNECTIONS)
            ),
            HTTP_POOL_MAXSIZE=int(
                os.getenv("GPT_FUSION_POOL_MAXSIZE", cls.HTTP_POOL_MAXSIZE)
            ),
            HTTP_MAX_RETRIES=int(
                os.getenv("GPT_FUSION_MAX_RETRIES", cls.HTTP_MAX_RETRIES)
            ),
            TWITTER_CHAR_LIMIT=int(
                os.getenv("GPT_FUSION_TWITTER_LIMIT", cls.TWITTER_CHAR_LIMIT)
            ),
            CSV_CHUNK_SIZE=int(
                os.getenv("GPT_FUSION_CSV_CHUNK_SIZE", cls.CSV_CHUNK_SIZE)
            ),
            BUILD_BATCH_SIZE=int(
                os.getenv("GPT_FUSION_BUILD_BATCH_SIZE", cls.BUILD_BATCH_SIZE)
            ),
            USER_AGENT=os.getenv("GPT_FUSION_USER_AGENT", cls.USER_AGENT),
            LOG_LEVEL=os.getenv("GPT_FUSION_LOG_LEVEL", cls.LOG_LEVEL),
        )


# Global configuration instance
config = Config.from_env()


def get_config() -> Config:
    """Get the global configuration instance."""
    return config


def update_config(**kwargs) -> None:
    """Update global configuration with new values."""
    global config
    for key, value in kwargs.items():
        if hasattr(config, key.upper()):
            setattr(config, key.upper(), value)
        else:
            raise ValueError(f"Unknown configuration key: {key}")
    # Re-assign to global to satisfy linter
    config = config
