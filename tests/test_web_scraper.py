from unittest.mock import Mock, patch

"""Web scraper tests requiring requests and BeautifulSoup."""

import pytest

pytest.importorskip("requests")
pytest.importorskip("bs4")

import requests  # noqa: E402

from gpt_fusion.web_scraper import scrape  # noqa: E402


def test_scrape_parses_text():
    html = (
        "<html><body>"
        "<p class='msg'>Hello</p>"
        "<p class='msg'>World</p>"
        "</body></html>"
    )

    with patch("gpt_fusion.web_scraper._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session

        mock_response = Mock()
        mock_response.text = html
        mock_response.raise_for_status = Mock()
        mock_session.get.return_value = mock_response

        result = scrape("http://example.com", "p.msg")
        mock_session.get.assert_called_once_with(
            "http://example.com",
            timeout=10,
        )

    assert result == ["Hello", "World"]


def test_scrape_connection_error_raises_exception():
    with patch("gpt_fusion.web_scraper._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.side_effect = requests.exceptions.RequestException

        with pytest.raises(requests.exceptions.RequestException):
            scrape("http://example.com", "p.msg")
        mock_session.get.assert_called_once_with(
            "http://example.com",
            timeout=10,
        )
