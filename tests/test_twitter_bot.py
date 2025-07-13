from unittest.mock import patch

"""Twitter bot tests that depend on Tweepy."""

import pytest

pytest.importorskip("tweepy")

from gpt_fusion.twitter_bot import TwitterBot  # noqa: E402


def test_post_tweet_invokes_tweepy():
    with (
        patch("tweepy.OAuth1UserHandler") as mock_handler,
        patch("tweepy.API") as mock_api,
    ):
        api_instance = mock_api.return_value
        bot = TwitterBot("k", "s", "t", "c")
        bot.post_tweet("hello")
        api_instance.update_status.assert_called_once_with("hello")
        mock_handler.assert_called_once()


def test_post_tweet_long_message_raises_error():
    with patch("tweepy.OAuth1UserHandler"), patch("tweepy.API"):
        bot = TwitterBot("k", "s", "t", "c")
        with pytest.raises(ValueError):
            bot.post_tweet("x" * 281)
