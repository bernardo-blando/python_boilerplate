"""Tests for the main API endpoints."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_greet_endpoint(client: TestClient) -> None:
    """Test the greet endpoint with a name."""
    response = client.get("/greet/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}


def test_greet_endpoint_special_characters(client: TestClient) -> None:
    """Test the greet endpoint with special characters."""
    response = client.get("/greet/John%20Doe")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John Doe!"}


def test_health_endpoint(client: TestClient) -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
