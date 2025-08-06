from __future__ import annotations

import logging
from urllib.parse import urlparse

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from .exceptions import ValidationError

logger = logging.getLogger(__name__)


def scrape(url: str, css_selector: str = "*") -> list[str]:
    """Return text content of elements matching *css_selector* from *url*.

    Args:
        url: The URL to scrape content from (must be HTTP/HTTPS)
        css_selector: CSS selector for elements to extract (default: all elements)

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
    # Make request with proper headers
    headers = {
        "User-Agent": "gpt-fusion/0.0.1a0 (https://github.com/costasford/gpt-fusion)"
    }

    try:
        logger.info(f"Scraping URL: {url}")
        response = requests.get(url, timeout=10, headers=headers)
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
