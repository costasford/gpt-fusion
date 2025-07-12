from __future__ import annotations

from dataclasses import dataclass


def add_numbers(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Return the difference of *a* and *b*."""
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Return the quotient of *a* and *b*."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


@dataclass
class ChatHistory:
    """Simple container for tracking conversation messages."""

    messages: list[str]

    def add_message(self, text: str) -> None:
        """Append *text* to the history."""
        self.messages.append(text)

    def last_message(self) -> str | None:
        """Return the most recent message or ``None`` if empty."""
        return self.messages[-1] if self.messages else None

    def clear(self) -> None:
        """Remove all messages from the history."""
        self.messages.clear()
