"""Chat completions client for OpenAI-compatible LLM APIs.

Works with OpenAI directly, or any OpenAI-compatible endpoint (Groq, a
local Ollama server, etc.) by overriding *base_url*.
"""

from __future__ import annotations

import os
from typing import Any, Optional, Union

import requests
from urllib3.util.retry import Retry

from .exceptions import APIError, ConfigurationError, ValidationError

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-4o-mini"

Message = dict[str, str]


def _normalize_messages(messages: Union[str, list[Message]]) -> list[Message]:
    """Validate *messages* and coerce a plain string into a single user message."""
    if isinstance(messages, str):
        if not messages.strip():
            raise ValidationError("messages string must not be empty")
        return [{"role": "user", "content": messages}]

    if isinstance(messages, list):
        if not messages:
            raise ValidationError("messages list must not be empty")
        for message in messages:
            if (
                not isinstance(message, dict)
                or "role" not in message
                or "content" not in message
            ):
                raise ValidationError(
                    "each message must be a dict with 'role' and 'content' keys"
                )
        return messages

    raise ValidationError("messages must be a string or a list of role/content dicts")


class LLMClient:
    """Reusable client for an OpenAI-compatible chat completions endpoint."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        model: str = DEFAULT_MODEL,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ConfigurationError(
                "No API key provided - pass api_key= or set the OPENAI_API_KEY "
                "environment variable"
            )
        self.base_url = base_url.rstrip("/")
        self.model = model
        self._session: Optional[requests.Session] = None

    def _get_session(self) -> requests.Session:
        """Get or create a requests session with connection pooling."""
        if self._session is None:
            self._session = requests.Session()
            # urllib3's Retry excludes POST from its allowed_methods by
            # default (it isn't idempotent in general) - this client only
            # ever POSTs to /chat/completions, so a bare max_retries=2
            # silently never retried anything. Add POST explicitly so
            # transient connection errors/429/5xx actually get retried.
            retry = Retry(
                total=2,
                backoff_factor=0.5,
                status_forcelist=(429, 500, 502, 503, 504),
                allowed_methods=Retry.DEFAULT_ALLOWED_METHODS | frozenset({"POST"}),
            )
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=5, pool_maxsize=10, max_retries=retry, pool_block=False
            )
            self._session.mount("http://", adapter)
            self._session.mount("https://", adapter)
        return self._session

    def close(self) -> None:
        """Close the session and clean up connections."""
        if self._session:
            self._session.close()
            self._session = None

    def chat(
        self,
        messages: Union[str, list[Message]],
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        timeout: int = 30,
    ) -> str:
        """Send a chat completion request and return the assistant's reply text.

        Args:
            messages: Either a plain string (sent as a single user message) or
                a list of ``{"role": ..., "content": ...}`` dicts for
                multi-turn context.
            model: Overrides the client's default model for this call.
            temperature: Sampling temperature passed through to the API.
            max_tokens: Optional cap on the completion length.
            timeout: Request timeout in seconds.

        Returns:
            The assistant's reply text.

        Raises:
            ValidationError: If *messages* is empty or malformed.
            APIError: If the request fails or the response is unexpected.
        """
        payload: dict[str, Any] = {
            "model": model or self.model,
            "messages": _normalize_messages(messages),
            "temperature": temperature,
        }
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens

        session = self._get_session()
        try:
            response = session.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=timeout,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise APIError(f"LLM API request failed: {e}") from e

        try:
            data = response.json()
        except ValueError as e:
            raise APIError(f"LLM API returned a non-JSON response: {e}") from e

        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as e:
            raise APIError(f"Unexpected response shape from LLM API: {data!r}") from e


def ask(
    prompt: str,
    api_key: str | None = None,
    model: str = DEFAULT_MODEL,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs: Any,
) -> str:
    """One-shot convenience wrapper: send *prompt* and return the reply text.

    Creates a throwaway :class:`LLMClient` under the hood. For multiple calls,
    create an :class:`LLMClient` directly so the underlying connection is
    reused.
    """
    client = LLMClient(api_key=api_key, base_url=base_url, model=model)
    try:
        return client.chat(prompt, **kwargs)
    finally:
        client.close()
