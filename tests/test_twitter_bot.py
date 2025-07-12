from unittest.mock import patch

from gpt_fusion.twitter_bot import TwitterBot


def test_post_tweet_invokes_tweepy():
    with patch("tweepy.OAuth1UserHandler") as mock_handler, patch(
        "tweepy.API"
    ) as mock_api:
        api_instance = mock_api.return_value
        bot = TwitterBot("k", "s", "t", "c")
        bot.post_tweet("hello")
        api_instance.update_status.assert_called_once_with("hello")
        mock_handler.assert_called_once()
