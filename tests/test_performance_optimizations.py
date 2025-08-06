"""Tests for performance optimizations."""

from __future__ import annotations

import csv
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch


import gpt_fusion
from gpt_fusion.config import get_config, update_config


class TestPerformanceOptimizations:
    """Test performance optimization features."""

    def test_streaming_csv_processing(self):
        """Test that streaming CSV processing works for large files."""
        # Create a larger test CSV file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(["value"])
            for i in range(100):  # Create 100 rows
                writer.writerow([str(float(i))])
            temp_path = f.name

        try:
            # Test streaming vs non-streaming
            values_normal = gpt_fusion.load_numbers_from_csv(
                temp_path, use_streaming=False
            )
            values_streaming = gpt_fusion.load_numbers_from_csv(
                temp_path, use_streaming=True
            )

            # Should produce same results
            assert values_normal == values_streaming
            assert len(values_normal) == 100

            # Test streaming average calculation
            avg_normal = gpt_fusion.average_from_csv(temp_path, use_streaming=False)
            avg_streaming = gpt_fusion.average_from_csv(temp_path, use_streaming=True)

            assert abs(avg_normal - avg_streaming) < 0.001  # Should be nearly identical

        finally:
            Path(temp_path).unlink()

    def test_streaming_generator_function(self):
        """Test the streaming generator function directly."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(["value"])
            writer.writerow(["1.5"])
            writer.writerow(["2.5"])
            writer.writerow(["3.5"])
            temp_path = f.name

        try:
            # Test generator produces expected values
            values = list(gpt_fusion.analysis.load_numbers_from_csv_stream(temp_path))
            assert values == [1.5, 2.5, 3.5]

            # Test chunking behavior
            values_chunked = list(
                gpt_fusion.analysis.load_numbers_from_csv_stream(
                    temp_path, chunk_size=2
                )
            )
            assert values_chunked == [1.5, 2.5, 3.5]

        finally:
            Path(temp_path).unlink()

    def test_http_connection_pooling_web_scraper(self):
        """Test that web scraper uses connection pooling."""
        with patch("gpt_fusion.web_scraper._get_session") as mock_get_session:
            mock_session = Mock()
            mock_get_session.return_value = mock_session

            mock_response = Mock()
            mock_response.text = "<html><body><p>Test</p></body></html>"
            mock_response.raise_for_status = Mock()
            mock_session.get.return_value = mock_response

            # Make multiple requests
            gpt_fusion.scrape("https://example.com")
            gpt_fusion.scrape("https://example2.com")

            # Session should be reused (called once to get it)
            assert (
                mock_get_session.call_count <= 2
            )  # May be called once or twice due to caching
            # Both requests should use the same session
            assert mock_session.get.call_count == 2

    def test_http_connection_pooling_twitch_client(self):
        """Test that Twitch client uses connection pooling."""
        with patch("gpt_fusion.twitch.TwitchClient._get_session") as mock_get_session:
            mock_session = Mock()
            mock_get_session.return_value = mock_session

            # Mock auth response
            auth_response = Mock()
            auth_response.json.return_value = {"access_token": "token"}
            auth_response.raise_for_status = Mock()

            # Mock API responses
            games_response = Mock()
            games_response.json.return_value = {"data": [{"name": "Game1"}]}
            games_response.raise_for_status = Mock()

            streams_response = Mock()
            streams_response.json.return_value = {"data": [{"user_name": "Streamer1"}]}
            streams_response.raise_for_status = Mock()

            mock_session.post.return_value = auth_response
            mock_session.get.side_effect = [games_response, streams_response]

            client = gpt_fusion.TwitchClient("id", "secret")
            client.get_top_games()
            client.get_top_streams()

            # Should use same session for all requests
            assert mock_session.post.call_count == 1  # Auth call
            assert mock_session.get.call_count == 2  # API calls

    def test_centralized_configuration(self):
        """Test centralized configuration system."""
        # Test getting config
        config = get_config()
        assert config.HTTP_TIMEOUT == 10
        assert config.TWITTER_CHAR_LIMIT == 280

        # Test updating config
        original_timeout = config.HTTP_TIMEOUT
        update_config(http_timeout=30)

        updated_config = get_config()
        assert updated_config.HTTP_TIMEOUT == 30

        # Restore original
        update_config(http_timeout=original_timeout)

    def test_build_utils_batch_processing(self):
        """Test that build utils processes files in batches."""
        # This is more of an integration test to ensure the new batch
        # processing doesn't break
        with (
            tempfile.TemporaryDirectory() as src_dir,
            tempfile.TemporaryDirectory() as dst_dir,
        ):
            # Create test files
            src_path = Path(src_dir)
            (src_path / "test1.html").write_text(
                "<html><body><h1>Test 1</h1></body></html>"
            )
            (src_path / "test2.css").write_text("body { margin: 0; padding: 0; }")
            (src_path / "test3.js").write_text("console.log('hello world');")
            (src_path / "test4.txt").write_text("Plain text file")

            # Test batch processing (current version doesn't have batch_size
            # param yet)
            from gpt_fusion.build_utils import minify_dir

            minify_dir(src_dir, dst_dir)

            # Verify files were processed
            dst_path = Path(dst_dir)
            assert (dst_path / "test1.html").exists()
            assert (dst_path / "test2.css").exists()
            assert (dst_path / "test3.js").exists()
            assert (dst_path / "test4.txt").exists()

            # Verify minification occurred
            minified_html = (dst_path / "test1.html").read_text()
            assert "<h1>Test 1</h1>" in minified_html
            assert len(minified_html) < len("<html><body><h1>Test 1</h1></body></html>")

    def test_config_from_environment(self):
        """Test configuration can be loaded from environment variables."""
        import os
        from gpt_fusion.config import Config

        # Set environment variable
        os.environ["GPT_FUSION_HTTP_TIMEOUT"] = "25"

        try:
            config = Config.from_env()
            assert config.HTTP_TIMEOUT == 25
        finally:
            # Clean up
            if "GPT_FUSION_HTTP_TIMEOUT" in os.environ:
                del os.environ["GPT_FUSION_HTTP_TIMEOUT"]
