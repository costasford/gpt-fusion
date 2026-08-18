import pytest

from gpt_fusion.exceptions import ValidationError
from gpt_fusion.utils import (
    ChatHistory,
    add_numbers,
    divide_numbers,
    multiply_numbers,
    subtract_numbers,
)


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    assert subtract_numbers(5, 2) == 3


def test_multiply_numbers():
    assert multiply_numbers(2, 4) == 8


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)


@pytest.mark.parametrize(
    "func",
    [add_numbers, subtract_numbers, multiply_numbers, divide_numbers],
)
def test_arithmetic_rejects_non_numeric_input(func):
    """Regression test: these silently did Python's operator overloading
    on wrong-typed input instead of raising - multiply_numbers("ab", 3)
    returned "ababab", add_numbers("2", "3") returned "23"."""
    with pytest.raises(ValidationError):
        func("2", 3)


def test_chat_history():
    history = ChatHistory(messages=[])
    history.add_message("hello")
    history.add_message("world")
    assert history.last_message() == "world"


def test_clear_chat_history():
    history = ChatHistory(messages=["hello", "world"])
    history.clear()
    assert history.messages == []
    assert history.last_message() is None


def test_last_message_empty_returns_none():
    history = ChatHistory(messages=[])
    assert history.last_message() is None


def test_chathistory_defaults_to_empty_list():
    history = ChatHistory()
    assert history.messages == []
    history.add_message("hi")
    assert history.last_message() == "hi"
