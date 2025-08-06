from __future__ import annotations

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def scrape(url: str, css_selector: str) -> list[str]:
    """Return text content of elements matching *css_selector* from *url*.

    Returns an empty list if the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except RequestException:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(css_selector)
    return [element.get_text(strip=True) for element in elements]
