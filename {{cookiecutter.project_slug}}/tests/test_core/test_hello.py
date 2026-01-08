"""Tests for the hello module."""

from unittest.mock import MagicMock

from {{ cookiecutter.package_name }}.hello import greet
from {{ cookiecutter.package_name }}.models import Greeting


def test_greet_default() -> None:
    """Test greet with default argument returns a Greeting model."""
    result = greet()
    assert isinstance(result, Greeting)
    assert result.message == "Hello, World!"
    assert result.name == "World"


def test_greet_with_name() -> None:
    """Test greet with a custom name."""
    result = greet("Alice")
    assert result.message == "Hello, Alice!"
    assert result.name == "Alice"


def test_greet_with_empty_string() -> None:
    """Test greet with an empty string."""
    result = greet("")
    assert result.message == "Hello, !"
    assert result.name == ""


def test_greet_with_mock_service(mock_service: MagicMock) -> None:
    """Example test demonstrating fixture usage."""
    assert mock_service.is_available() is True
    assert mock_service.get_data() == {"key": "value"}

    result = greet("Mock User")
    assert result.message == "Hello, Mock User!"
