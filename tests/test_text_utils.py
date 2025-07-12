from gpt_fusion.text_utils import (
    count_characters,
    is_palindrome,
    most_common_word,
    remove_punctuation,
    reverse_words,
    to_title_case,
    unique_words,
    word_count,
)


def test_word_count():
    assert word_count("hello world") == 2


def test_unique_words():
    assert unique_words("hello hello world") == {"hello", "world"}


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


def test_count_characters():
    assert count_characters("abc") == 3


def test_remove_punctuation():
    assert remove_punctuation("hello, world!") == "hello world"


def test_most_common_word():
    assert most_common_word("a b a c a") == "a"


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
