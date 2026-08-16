from __future__ import annotations

import ipaddress
import logging
import socket
from urllib.parse import urljoin, urlparse
from typing import Optional

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from .exceptions import ValidationError
from .config import get_config

logger = logging.getLogger(__name__)

# Global session for connection pooling
_session: Optional[requests.Session] = None

# Redirects are followed manually (not via requests' allow_redirects=True)
# so each hop can be re-validated - otherwise a URL that passes validation
# can 30x to an internal address and requests would follow it straight
# there.
_MAX_REDIRECTS = 5
_REDIRECT_STATUS_CODES = {301, 302, 303, 307, 308}


def _get_session() -> requests.Session:
    """Get or create a requests session with connection pooling.

    Returns:
        Configured requests session with connection pooling
    """
    global _session
    if _session is None:
        _session = requests.Session()
        # Configure connection pooling using centralized config
        config = get_config()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=config.HTTP_POOL_CONNECTIONS,
            pool_maxsize=config.HTTP_POOL_MAXSIZE,
            max_retries=config.HTTP_MAX_RETRIES,
            pool_block=False,
        )
        _session.mount("http://", adapter)
        _session.mount("https://", adapter)

        # Set default headers using centralized config
        _session.headers.update({"User-Agent": config.USER_AGENT})

    return _session


def close_session() -> None:
    """Close the global session and clean up connections.

    Call this when shutting down or when done with web scraping operations.
    """
    global _session
    if _session:
        _session.close()
        _session = None


def _resolve_addresses(hostname: str) -> list[str]:
    """Resolve *hostname* to its IP addresses.

    Split out from _ensure_public_url so tests can stub DNS resolution
    without depending on the network.
    """
    try:
        return [info[4][0] for info in socket.getaddrinfo(hostname, None)]
    except socket.gaierror as e:
        raise ValidationError(f"Could not resolve host: {hostname}") from e


def _ensure_public_url(url: str) -> None:
    """Raise ValidationError unless *url* is http(s) and resolves only to
    public addresses.

    Blocks SSRF against cloud metadata endpoints (e.g. 169.254.169.254),
    loopback, and other internal/reserved network ranges.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValidationError(f"Only HTTP/HTTPS URLs are allowed, got: {parsed.scheme}")

    hostname = parsed.hostname
    if not hostname:
        raise ValidationError(f"Invalid URL format: {url}")

    for addr in _resolve_addresses(hostname):
        ip = ipaddress.ip_address(addr)
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
            or ip.is_unspecified
        ):
            raise ValidationError(
                f"Refusing to request {hostname!r}: resolves to non-public "
                f"address {ip}"
            )


def _get_with_safe_redirects(
    session: requests.Session, url: str, timeout: Optional[int]
) -> requests.Response:
    """GET *url*, following redirects manually so each hop is re-validated."""
    for _ in range(_MAX_REDIRECTS + 1):
        logger.info(f"Scraping URL: {url}")
        response = session.get(url, timeout=timeout, allow_redirects=False)
        if response.status_code not in _REDIRECT_STATUS_CODES:
            return response

        location = response.headers.get("Location")
        if not location:
            return response

        url = urljoin(url, location)
        _ensure_public_url(url)

    raise ValidationError(f"Too many redirects while scraping (max {_MAX_REDIRECTS})")


def scrape(
    url: str, css_selector: str = "*", timeout: Optional[int] = None
) -> list[str]:
    """Return text content of elements matching *css_selector* from *url*.

    Args:
        url: The URL to scrape content from (must be HTTP/HTTPS)
        css_selector: CSS selector for elements to extract (default: all elements)
        timeout: Request timeout in seconds (default: from config)

    Returns:
        List of text content from matching elements

    Raises:
        ValidationError: If URL is invalid, uses an unsupported scheme, or
            resolves (directly or via redirect) to a non-public address
        RequestException: If the HTTP request fails
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValidationError("URL must be a non-empty string")

    url = url.strip()
    parsed = urlparse(url)
    if not parsed.scheme:
        raise ValidationError(f"Invalid URL format: {url}")

    if parsed.scheme not in ("http", "https"):
        raise ValidationError(f"Only HTTP/HTTPS URLs are allowed, got: {parsed.scheme}")

    if not parsed.netloc:
        raise ValidationError(f"Invalid URL format: {url}")

    _ensure_public_url(url)

    # Use session with connection pooling
    session = _get_session()

    # Use timeout from config if not specified
    if timeout is None:
        timeout = get_config().HTTP_TIMEOUT

    try:
        response = _get_with_safe_redirects(session, url, timeout)
        response.raise_for_status()
    except RequestException as e:
        logger.error(f"Failed to scrape {url}: {e}")
        raise

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.select(css_selector)
        result = [element.get_text(strip=True) for element in elements]
        logger.info(f"Successfully scraped {len(result)} elements from {url}")
        return result
    except Exception as e:
        logger.error(f"Failed to parse content from {url}: {e}")
        raise ValidationError(f"Failed to parse HTML content: {e}") from e
