import pytest

from gpt_fusion.config import Config, get_config, update_config


def test_from_env_malformed_int_falls_back_to_default(monkeypatch, caplog):
    """Regression test: a malformed env var used to raise ValueError at
    import time (`config = Config.from_env()` runs on module import), which
    took down `import gpt_fusion` entirely rather than failing just the one
    setting."""
    monkeypatch.setenv("GPT_FUSION_HTTP_TIMEOUT", "not-a-number")

    with caplog.at_level("WARNING"):
        config = Config.from_env()

    assert config.HTTP_TIMEOUT == Config.HTTP_TIMEOUT
    assert "GPT_FUSION_HTTP_TIMEOUT" in caplog.text


def test_from_env_empty_string_falls_back_to_default(monkeypatch):
    monkeypatch.setenv("GPT_FUSION_POOL_MAXSIZE", "")

    config = Config.from_env()

    assert config.HTTP_POOL_MAXSIZE == Config.HTTP_POOL_MAXSIZE


def test_from_env_reads_valid_int_env_var(monkeypatch):
    monkeypatch.setenv("GPT_FUSION_HTTP_TIMEOUT", "25")

    config = Config.from_env()

    assert config.HTTP_TIMEOUT == 25


def test_default_user_agent_includes_installed_version():
    from importlib.metadata import version

    config = Config()

    assert version("gpt-fusion") in config.USER_AGENT


def test_update_config_unknown_key_raises_value_error():
    with pytest.raises(ValueError, match="Unknown configuration key"):
        update_config(not_a_real_setting=1)


def test_update_config_wrong_type_raises_type_error():
    original = get_config().HTTP_TIMEOUT
    try:
        with pytest.raises(TypeError, match="http_timeout expects int"):
            update_config(http_timeout="30")
    finally:
        update_config(http_timeout=original)


def test_update_config_leaves_config_unchanged_on_type_error():
    original = get_config().HTTP_TIMEOUT

    with pytest.raises(TypeError):
        update_config(http_timeout="30")

    assert get_config().HTTP_TIMEOUT == original
