from __future__ import annotations

"""Centralized configuration management for gpt-fusion package."""

import logging
import os
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version as _pkg_version

logger = logging.getLogger(__name__)


def _default_user_agent() -> str:
    try:
        pkg_version = _pkg_version("gpt-fusion")
    except PackageNotFoundError:
        pkg_version = "0.0.0"
    return f"gpt-fusion/{pkg_version} (https://github.com/costasford/gpt-fusion)"


def _int_env(name: str, default: int) -> int:
    """Read *name* from the environment as an int, falling back to
    *default* (with a warning) instead of raising on a malformed value -
    this is read at import time, so a raised exception here would take
    down `import gpt_fusion` entirely."""
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        logger.warning(
            "Ignoring invalid value for %s=%r; using default %r", name, raw, default
        )
        return default


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
    USER_AGENT: str = field(default_factory=_default_user_agent)

    # Logging
    LOG_LEVEL: str = "INFO"

    @classmethod
    def from_env(cls) -> Config:
        """Create config from environment variables with fallback to defaults."""
        return cls(
            HTTP_TIMEOUT=_int_env("GPT_FUSION_HTTP_TIMEOUT", cls.HTTP_TIMEOUT),
            HTTP_POOL_CONNECTIONS=_int_env(
                "GPT_FUSION_POOL_CONNECTIONS", cls.HTTP_POOL_CONNECTIONS
            ),
            HTTP_POOL_MAXSIZE=_int_env(
                "GPT_FUSION_POOL_MAXSIZE", cls.HTTP_POOL_MAXSIZE
            ),
            HTTP_MAX_RETRIES=_int_env("GPT_FUSION_MAX_RETRIES", cls.HTTP_MAX_RETRIES),
            TWITTER_CHAR_LIMIT=_int_env(
                "GPT_FUSION_TWITTER_LIMIT", cls.TWITTER_CHAR_LIMIT
            ),
            CSV_CHUNK_SIZE=_int_env("GPT_FUSION_CSV_CHUNK_SIZE", cls.CSV_CHUNK_SIZE),
            BUILD_BATCH_SIZE=_int_env(
                "GPT_FUSION_BUILD_BATCH_SIZE", cls.BUILD_BATCH_SIZE
            ),
            USER_AGENT=os.getenv("GPT_FUSION_USER_AGENT", _default_user_agent()),
            LOG_LEVEL=os.getenv("GPT_FUSION_LOG_LEVEL", cls.LOG_LEVEL),
        )


# Global configuration instance
config = Config.from_env()


def get_config() -> Config:
    """Get the global configuration instance."""
    return config


def update_config(**kwargs) -> None:
    """Update global configuration with new values.

    Raises:
        ValueError: If a key doesn't match a known configuration field.
        TypeError: If a value's type doesn't match the field it's setting.
    """
    for key, value in kwargs.items():
        attr = key.upper()
        if not hasattr(config, attr):
            raise ValueError(f"Unknown configuration key: {key}")
        expected_type = type(getattr(config, attr))
        if not isinstance(value, expected_type):
            raise TypeError(
                f"{key} expects {expected_type.__name__}, got "
                f"{type(value).__name__}"
            )
        setattr(config, attr, value)
