from gpt_fusion.utils import add_numbers, multiply_numbers, ChatHistory


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_multiply_numbers():
    assert multiply_numbers(2, 4) == 8


def test_chat_history():
    history = ChatHistory(messages=[])
    history.add_message("hello")
    history.add_message("world")
    assert history.last_message() == "world"
