from gpt_fusion.core import greet


def test_greet():
    assert greet("World") == "Hello, World! Welcome to gpt-fusion."
