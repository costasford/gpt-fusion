from __future__ import annotations

import logging
from urllib.parse import urlparse
from typing import Optional

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from .exceptions import ValidationError
from .config import get_config

logger = logging.getLogger(__name__)

# Global session for connection pooling
_session: Optional[requests.Session] = None


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
        ValidationError: If URL is invalid or uses unsupported scheme
        RequestException: If the HTTP request fails
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValidationError("URL must be a non-empty string")

    parsed = urlparse(url.strip())
    if not parsed.scheme:
        raise ValidationError(f"Invalid URL format: {url}")

    if parsed.scheme not in ("http", "https"):
        raise ValidationError(f"Only HTTP/HTTPS URLs are allowed, got: {parsed.scheme}")

    if not parsed.netloc:
        raise ValidationError(f"Invalid URL format: {url}")

    # Use session with connection pooling
    session = _get_session()

    # Use timeout from config if not specified
    if timeout is None:
        timeout = get_config().HTTP_TIMEOUT

    try:
        logger.info(f"Scraping URL: {url}")
        response = session.get(url, timeout=timeout)
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
