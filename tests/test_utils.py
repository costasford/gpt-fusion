import pytest

from gpt_fusion.utils import (ChatHistory, add_numbers, divide_numbers,
                              multiply_numbers, subtract_numbers)


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


def test_chat_history():
    history = ChatHistory(messages=[])
    history.add_message("hello")
    history.add_message("world")
    assert history.last_message() == "world"
