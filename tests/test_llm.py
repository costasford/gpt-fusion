from unittest.mock import Mock, patch

"""LLM client tests requiring the requests library."""

import pytest

pytest.importorskip("requests")

import requests  # noqa: E402

from gpt_fusion.exceptions import (  # noqa: E402
    APIError,
    ConfigurationError,
    ValidationError,
)
from gpt_fusion.llm import LLMClient, ask  # noqa: E402


def mock_chat_response(mock_session: Mock, content: str = "Hello there!") -> Mock:
    response = Mock()
    response.json.return_value = {
        "choices": [{"message": {"role": "assistant", "content": content}}]
    }
    response.raise_for_status = Mock()
    mock_session.post.return_value = response
    return response


def test_chat_with_string_prompt_returns_reply():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_chat_response(mock_session)

        client = LLMClient(api_key="sk-test")
        reply = client.chat("Hi!")

        assert reply == "Hello there!"
        call_kwargs = mock_session.post.call_args.kwargs
        assert call_kwargs["json"]["messages"] == [{"role": "user", "content": "Hi!"}]
        assert call_kwargs["headers"]["Authorization"] == "Bearer sk-test"


def test_chat_with_message_list_passes_through():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_chat_response(mock_session)

        messages = [
            {"role": "system", "content": "Be terse."},
            {"role": "user", "content": "Hi!"},
        ]
        client = LLMClient(api_key="sk-test")
        client.chat(messages)

        call_kwargs = mock_session.post.call_args.kwargs
        assert call_kwargs["json"]["messages"] == messages


def test_missing_api_key_raises_configuration_error(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ConfigurationError):
        LLMClient()


def test_api_key_from_env_var(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-from-env")
    client = LLMClient()
    assert client.api_key == "sk-from-env"


@pytest.mark.parametrize(
    "bad_messages",
    ["", "   ", [], {"role": "user"}, [{"role": "user"}], [{"content": "hi"}], 42],
)
def test_invalid_messages_raise_validation_error(bad_messages):
    client = LLMClient(api_key="sk-test")
    with pytest.raises(ValidationError):
        client.chat(bad_messages)


def test_request_exception_raises_api_error():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_session.post.side_effect = requests.exceptions.ConnectionError("boom")

        client = LLMClient(api_key="sk-test")
        with pytest.raises(APIError):
            client.chat("Hi!")


def test_unexpected_response_shape_raises_api_error():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        response = Mock()
        response.json.return_value = {"error": "rate limited"}
        response.raise_for_status = Mock()
        mock_session.post.return_value = response

        client = LLMClient(api_key="sk-test")
        with pytest.raises(APIError):
            client.chat("Hi!")


def test_non_json_response_raises_api_error():
    """Regression test: a 200 response with a non-JSON body (a proxy error
    page, an empty body from a flaky local server) used to raise a raw
    ValueError/JSONDecodeError instead of the documented APIError."""
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        response = Mock()
        response.json.side_effect = ValueError("Expecting value: line 1 column 1")
        response.raise_for_status = Mock()
        mock_session.post.return_value = response

        client = LLMClient(api_key="sk-test")
        with pytest.raises(APIError):
            client.chat("Hi!")


def test_session_retries_post_on_transient_errors():
    """Regression test: max_retries=2 was passed as a bare int, which
    urllib3 turns into a Retry whose default allowed_methods excludes
    POST - this client only ever POSTs, so retries were silently a
    no-op."""
    client = LLMClient(api_key="sk-test")
    adapter = client._get_session().get_adapter("https://api.openai.com/v1")
    assert "POST" in adapter.max_retries.allowed_methods
    client.close()


def test_custom_model_and_base_url_are_used():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_chat_response(mock_session)

        client = LLMClient(
            api_key="sk-test",
            base_url="http://localhost:11434/v1",
            model="llama3",
        )
        client.chat("Hi!")

        call_args = mock_session.post.call_args
        assert call_args.args[0] == "http://localhost:11434/v1/chat/completions"
        assert call_args.kwargs["json"]["model"] == "llama3"


def test_per_call_model_overrides_client_default():
    with patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session:
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_chat_response(mock_session)

        client = LLMClient(api_key="sk-test", model="gpt-4o-mini")
        client.chat("Hi!", model="gpt-4o")

        assert mock_session.post.call_args.kwargs["json"]["model"] == "gpt-4o"


def test_ask_convenience_function_closes_client():
    with (
        patch("gpt_fusion.llm.LLMClient._get_session") as mock_get_session,
        patch("gpt_fusion.llm.LLMClient.close") as mock_close,
    ):
        mock_session = Mock()
        mock_get_session.return_value = mock_session
        mock_chat_response(mock_session, content="42")

        reply = ask("What is 6 * 7?", api_key="sk-test")

        assert reply == "42"
        mock_close.assert_called_once()


def test_close_is_idempotent_and_resets_session():
    client = LLMClient(api_key="sk-test")
    client._session = Mock()
    client.close()
    assert client._session is None
    client.close()  # should not raise
