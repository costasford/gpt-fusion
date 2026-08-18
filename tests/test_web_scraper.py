import socket
from unittest.mock import Mock, patch

"""Web scraper tests requiring requests and BeautifulSoup."""

import pytest

pytest.importorskip("requests")
pytest.importorskip("bs4")

import requests  # noqa: E402

from gpt_fusion.exceptions import ValidationError  # noqa: E402
from gpt_fusion.web_scraper import scrape  # noqa: E402


def _mock_response(status_code=200, text="", location=None):
    response = Mock()
    response.status_code = status_code
    response.headers = {"Location": location} if location else {}
    response.text = text
    response.raise_for_status = Mock()
    return response


def test_scrape_parses_text():
    html = (
        "<html><body>"
        "<p class='msg'>Hello</p>"
        "<p class='msg'>World</p>"
        "</body></html>"
    )

    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.return_value = _mock_response(text=html)

        result = scrape("http://example.com", "p.msg")
        mock_session.get.assert_called_once_with(
            "http://example.com",
            timeout=10,
            allow_redirects=False,
        )

    assert result == ["Hello", "World"]


def test_scrape_connection_error_raises_exception():
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.side_effect = requests.exceptions.RequestException

        with pytest.raises(requests.exceptions.RequestException):
            scrape("http://example.com", "p.msg")
        mock_session.get.assert_called_once_with(
            "http://example.com",
            timeout=10,
            allow_redirects=False,
        )


@pytest.mark.parametrize(
    "address",
    [
        "127.0.0.1",  # loopback
        "169.254.169.254",  # link-local / cloud metadata endpoint
        "10.0.0.5",  # RFC1918 private
        "172.16.0.5",  # RFC1918 private
        "192.168.1.5",  # RFC1918 private
        "0.0.0.0",  # unspecified
        "::1",  # IPv6 loopback
    ],
)
def test_scrape_blocks_non_public_targets(address):
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch("gpt_fusion.web_scraper._resolve_addresses", return_value=[address]),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session

        with pytest.raises(ValidationError):
            scrape("http://internal.example", "p")

        mock_session.get.assert_not_called()


def test_scrape_blocks_redirect_to_internal_address():
    """A URL that resolves publicly must not be followed if it redirects
    somewhere internal - requests' default allow_redirects=True would do
    exactly that."""
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch("gpt_fusion.web_scraper._resolve_addresses") as mock_resolve,
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.return_value = _mock_response(
            status_code=302, location="http://internal.example/secret"
        )

        def resolve(hostname):
            return ["10.0.0.5"] if hostname == "internal.example" else ["93.184.216.34"]

        mock_resolve.side_effect = resolve

        with pytest.raises(ValidationError):
            scrape("http://public.example", "p")

        mock_session.get.assert_called_once()


def test_scrape_follows_redirect_to_public_address():
    html = "<p class='msg'>Hello</p>"
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.side_effect = [
            _mock_response(status_code=301, location="http://public.example/new"),
            _mock_response(text=html),
        ]

        result = scrape("http://public.example", "p.msg")

        assert result == ["Hello"]
        assert mock_session.get.call_count == 2


def test_scrape_too_many_redirects_raises():
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.return_value = _mock_response(
            status_code=302, location="http://public.example/loop"
        )

        with pytest.raises(ValidationError):
            scrape("http://public.example", "p")


def test_scrape_unresolvable_host_raises_validation_error():
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses",
            side_effect=ValidationError("Could not resolve host: nope.invalid"),
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session

        with pytest.raises(ValidationError):
            scrape("http://nope.invalid", "p")

        mock_session.get.assert_not_called()


def test_scrape_raises_on_redirect_with_no_location_header():
    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.return_value = _mock_response(status_code=302)

        with pytest.raises(ValidationError, match="no Location header"):
            scrape("http://public.example", "p")


def test_scrape_pins_dns_during_request_and_restores_afterward():
    """Regression test for the DNS-rebinding TOCTOU gap: _ensure_public_url
    validates a hostname's addresses, but requests/urllib3 re-resolve the
    same hostname independently when actually connecting - an attacker
    controlling DNS for the target could answer the two lookups
    differently. The connection must be pinned to the addresses that were
    actually validated."""
    seen_during_request = {}
    real_getaddrinfo = socket.getaddrinfo

    def fake_get(*args, **kwargs):
        # Simulate what happens during the real connection: something
        # calls socket.getaddrinfo for the target host while the request
        # is "in flight". It must resolve to the pinned address, not
        # whatever the real resolver would say.
        seen_during_request["result"] = socket.getaddrinfo("public.example", 443)
        return _mock_response(text="<p>hi</p>")

    with (
        patch("gpt_fusion.web_scraper._get_session") as mock_get_session,
        patch(
            "gpt_fusion.web_scraper._resolve_addresses", return_value=["93.184.216.34"]
        ),
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.get.side_effect = fake_get

        scrape("http://public.example", "p")

    assert seen_during_request["result"][0][4][0] == "93.184.216.34"
    # The patch must not leak past the request.
    assert socket.getaddrinfo is real_getaddrinfo
