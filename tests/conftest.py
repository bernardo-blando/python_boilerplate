"""Shared test fixtures and configuration."""

from collections.abc import Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture
def client() -> Generator[TestClient]:
    """Create a test client for the FastAPI application.

    Yields:
        A TestClient instance for making test requests.
    """
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def mock_service() -> MagicMock:
    """Example mock fixture for external services.

    This demonstrates how to create mock fixtures for testing.
    Replace this with actual mocks for your external dependencies.

    Returns:
        A MagicMock instance configured for testing.
    """
    mock = MagicMock()
    mock.get_data.return_value = {"key": "value"}
    mock.is_available.return_value = True
    return mock


@pytest.fixture
def sample_user_data() -> dict[str, str]:
    """Provide sample user data for testing.

    Returns:
        A dictionary with sample user information.
    """
    return {
        "name": "Test User",
        "email": "test@example.com",
    }
