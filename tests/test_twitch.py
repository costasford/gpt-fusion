from unittest.mock import Mock, patch

"""Twitch client tests requiring the requests library."""

import pytest

pytest.importorskip("requests")

from gpt_fusion.twitch import TwitchClient  # noqa: E402


def mock_auth(mock_post: Mock) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"access_token": "token"}
    mock_response.raise_for_status = Mock()
    mock_post.return_value = mock_response


def test_get_top_games_returns_data():
    with patch("requests.post") as mock_post, patch(
        "requests.get",
    ) as mock_get:
        mock_auth(mock_post)
        get_response = Mock()
        get_response.json.return_value = {"data": [{"name": "Game"}]}
        get_response.raise_for_status = Mock()
        mock_get.return_value = get_response

        client = TwitchClient("id", "secret")
        games = client.get_top_games()

        assert games == [{"name": "Game"}]
        mock_get.assert_called_once()


def test_missing_credentials_raise_error():
    with pytest.raises(ValueError):
        TwitchClient(client_id=None, client_secret=None)
