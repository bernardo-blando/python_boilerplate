{% if cookiecutter.framework == 'fastapi' %}
"""Tests for the FastAPI application endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_greet_endpoint() -> None:
    """Test the greet endpoint with a name."""
    response = client.get("/greet/Alice")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Alice!"
    assert data["name"] == "Alice"


def test_greet_endpoint_special_characters() -> None:
    """Test the greet endpoint with special characters."""
    response = client.get("/greet/John%20Doe")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, John Doe!"
    assert data["name"] == "John Doe"


def test_health_endpoint() -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
{% else %}
"""Tests for the {{ cookiecutter.framework | capitalize }} application.

Note: {{ cookiecutter.framework | capitalize }} applications typically require
different testing approaches. Add framework-specific tests as needed.
"""


def test_placeholder() -> None:
    """Placeholder test - replace with framework-specific tests."""
    assert True
{% endif %}
