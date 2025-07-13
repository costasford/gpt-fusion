import pytest

"""Test optional imports are lazy-loaded when deps installed."""

pytest.importorskip("requests")
pytest.importorskip("bs4")
pytest.importorskip("tweepy")


def test_optional_modules_lazy_loaded():
    import gpt_fusion

    assert "scrape" not in gpt_fusion.__dict__
    assert "TwitterBot" not in gpt_fusion.__dict__

    _ = gpt_fusion.scrape
    _ = gpt_fusion.TwitterBot

    assert "scrape" in gpt_fusion.__dict__
    assert "TwitterBot" in gpt_fusion.__dict__
