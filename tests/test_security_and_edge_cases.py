"""Tests for security fixes and edge cases."""

from __future__ import annotations

import csv
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

import gpt_fusion
from gpt_fusion.exceptions import DataError, SecurityError, ValidationError


class TestSecurityFixes:
    """Test security vulnerability fixes."""

    def test_path_traversal_prevention(self):
        """Test that path traversal attacks are prevented."""
        with pytest.raises(SecurityError, match="Path traversal detected"):
            gpt_fusion.load_numbers_from_csv("../../../etc/passwd")

    def test_path_traversal_prevention_relative(self):
        """Test that relative path traversal attempts are prevented."""
        with pytest.raises(SecurityError, match="Path traversal detected"):
            gpt_fusion.load_numbers_from_csv("../../../../sensitive_file.csv")

    def test_web_scraper_url_validation(self):
        """Test that web scraper validates URLs properly."""
        # Invalid schemes
        with pytest.raises(ValidationError, match="Only HTTP/HTTPS URLs are allowed"):
            gpt_fusion.scrape("ftp://example.com")

        with pytest.raises(ValidationError, match="Only HTTP/HTTPS URLs are allowed"):
            gpt_fusion.scrape("file:///etc/passwd")

        # Invalid URL format
        with pytest.raises(ValidationError, match="Invalid URL format"):
            gpt_fusion.scrape("not-a-url")

        # Empty URL
        with pytest.raises(ValidationError, match="URL must be a non-empty string"):
            gpt_fusion.scrape("")

    def test_csv_file_validation(self):
        """Test that CSV functions validate file existence."""
        with pytest.raises(FileNotFoundError, match="CSV file not found"):
            gpt_fusion.load_numbers_from_csv("nonexistent.csv")


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_word_count_edge_cases(self):
        """Test word_count with edge cases."""
        assert gpt_fusion.word_count("") == 0
        assert gpt_fusion.word_count("   ") == 0
        assert gpt_fusion.word_count("\n\t  ") == 0
        assert gpt_fusion.word_count("single") == 1
        assert gpt_fusion.word_count("  multiple   spaces  between   words  ") == 4

    def test_most_common_word_edge_cases(self):
        """Test most_common_word with edge cases."""
        # Empty string
        assert gpt_fusion.most_common_word("") == ""

        # Single word
        assert gpt_fusion.most_common_word("hello") == "hello"

        # Tie - should be deterministic
        result = gpt_fusion.most_common_word("a b a b")
        assert result == "a"  # Alphabetical order for determinism

        # Case sensitivity
        result_sensitive = gpt_fusion.most_common_word(
            "Apple apple APPLE", case_sensitive=True
        )
        # Should return first alphabetically among the tied options
        assert result_sensitive in ["APPLE", "Apple", "apple"]

        result_insensitive = gpt_fusion.most_common_word(
            "Apple apple APPLE", case_sensitive=False
        )
        assert result_insensitive == "apple"  # All converted to lowercase

    def test_empty_csv_handling(self):
        """Test CSV functions with empty data."""
        # Create empty CSV file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(["value"])  # Header only
            temp_path = f.name

        try:
            with pytest.raises(DataError, match="No valid numeric values found"):
                gpt_fusion.average_from_csv(temp_path)

            with pytest.raises(DataError, match="No valid numeric values found"):
                gpt_fusion.median_from_csv(temp_path)
        finally:
            Path(temp_path).unlink()

    def test_csv_with_invalid_values(self):
        """Test CSV functions with mixed valid/invalid data."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(["value"])
            writer.writerow(["1.5"])
            writer.writerow(["not-a-number"])
            writer.writerow(["2.5"])
            writer.writerow([""])
            writer.writerow(["3.5"])
            temp_path = f.name

        try:
            values = gpt_fusion.load_numbers_from_csv(temp_path)
            assert values == [1.5, 2.5, 3.5]

            avg = gpt_fusion.average_from_csv(temp_path)
            assert avg == 2.5

            median = gpt_fusion.median_from_csv(temp_path)
            assert median == 2.5
        finally:
            Path(temp_path).unlink()

    @patch("gpt_fusion.web_scraper.requests.get")
    def test_web_scraper_with_valid_url(self, mock_get):
        """Test web scraper with valid URL and proper headers."""
        # Mock successful response
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.text = "<html><body><p>Test content</p></body></html>"

        gpt_fusion.scrape("https://example.com", "p")

        # Verify request was made with proper headers
        mock_get.assert_called_once_with(
            "https://example.com",
            timeout=10,
            headers={
                "User-Agent": (
                    "gpt-fusion/0.0.1a0 " "(https://github.com/costasford/gpt-fusion)"
                )
            },
        )

    def test_palindrome_edge_cases(self):
        """Test palindrome detection with edge cases."""
        # Empty string should be considered a palindrome
        assert gpt_fusion.is_palindrome("") is True

        # Single character
        assert gpt_fusion.is_palindrome("a") is True

        # Only punctuation
        assert gpt_fusion.is_palindrome("!@#$%^&*()") is True

        # Mixed case and punctuation
        assert gpt_fusion.is_palindrome("A man, a plan, a canal: Panama") is True

    def test_unique_words_edge_cases(self):
        """Test unique_words function with edge cases."""
        # Empty string
        assert gpt_fusion.unique_words("") == set()

        # Single word
        assert gpt_fusion.unique_words("hello") == {"hello"}

        # Repeated words
        assert gpt_fusion.unique_words("hello world hello") == {"hello", "world"}


class TestExceptionHierarchy:
    """Test that custom exceptions work properly."""

    def test_exception_inheritance(self):
        """Test that custom exceptions inherit properly."""
        assert issubclass(ValidationError, gpt_fusion.GPTFusionError)
        assert issubclass(DataError, gpt_fusion.GPTFusionError)
        assert issubclass(SecurityError, gpt_fusion.GPTFusionError)
        assert issubclass(gpt_fusion.ConfigurationError, gpt_fusion.GPTFusionError)

    def test_exception_messages(self):
        """Test that exceptions carry proper messages."""
        try:
            raise ValidationError("Test validation error")
        except ValidationError as e:
            assert str(e) == "Test validation error"

        try:
            raise DataError("Test data error")
        except DataError as e:
            assert str(e) == "Test data error"
