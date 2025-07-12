from unittest.mock import Mock, patch

from gpt_fusion.web_scraper import scrape


def test_scrape_parses_text():
    html = (
        "<html><body>"
        "<p class='msg'>Hello</p>"
        "<p class='msg'>World</p>"
        "</body></html>"
    )

    mock_response = Mock()
    mock_response.text = html
    mock_response.raise_for_status = Mock()

    with patch("requests.get", return_value=mock_response) as mock_get:
        result = scrape("http://example.com", "p.msg")
        mock_get.assert_called_once_with("http://example.com", timeout=10)

    assert result == ["Hello", "World"]
