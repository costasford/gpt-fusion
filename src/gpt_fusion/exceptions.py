"""Custom exceptions for gpt-fusion package."""

from __future__ import annotations


class GPTFusionError(Exception):
    """Base exception for gpt-fusion package."""

    pass


class ValidationError(GPTFusionError):
    """Raised when input validation fails."""

    pass


class ConfigurationError(GPTFusionError):
    """Raised when configuration is invalid."""

    pass


class SecurityError(GPTFusionError):
    """Raised when a security violation is detected."""

    pass


class DataError(GPTFusionError):
    """Raised when data processing fails."""

    pass
