"""Tests for the hello module."""

from unittest.mock import MagicMock

from core.hello import greet


def test_greet_default() -> None:
    """Test greet with default argument."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_with_name() -> None:
    """Test greet with a custom name."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_with_empty_string() -> None:
    """Test greet with an empty string."""
    result = greet("")
    assert result == "Hello, !"


def test_greet_with_mock_service(mock_service: MagicMock) -> None:
    """Example test demonstrating fixture usage.

    This test shows how to use the mock_service fixture from conftest.py.
    In real scenarios, you would inject this mock into your business logic.
    """
    # Verify the mock fixture is properly configured
    assert mock_service.is_available() is True
    assert mock_service.get_data() == {"key": "value"}

    # Your actual test logic would go here
    result = greet("Mock User")
    assert result == "Hello, Mock User!"
