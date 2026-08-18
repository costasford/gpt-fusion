from __future__ import annotations

from dataclasses import dataclass, field

from .exceptions import ValidationError


def _validate_numbers(a: object, b: object) -> None:
    """Reject non-numeric input instead of letting Python's operator
    overloading silently do the wrong thing (e.g. multiply_numbers("ab", 3)
    returning "ababab", or add_numbers("2", "3") returning "23")."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValidationError(
            f"Expected numeric arguments, got {type(a).__name__!r} and "
            f"{type(b).__name__!r}"
        )


def add_numbers(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    _validate_numbers(a, b)
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Return the difference of *a* and *b*."""
    _validate_numbers(a, b)
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    _validate_numbers(a, b)
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Return the quotient of *a* and *b*."""
    _validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


@dataclass
class ChatHistory:
    """Simple container for tracking conversation messages."""

    messages: list[str] = field(default_factory=list)

    def add_message(self, text: str) -> None:
        """Append *text* to the history."""
        self.messages.append(text)

    def last_message(self) -> str | None:
        """Return the most recent message or ``None`` if empty."""
        return self.messages[-1] if self.messages else None

    def clear(self) -> None:
        """Remove all messages from the history."""
        self.messages.clear()
