"""FastAPI application entry point."""

from fastapi import FastAPI

from api.schemas import GreetingResponse, HealthResponse, MessageResponse
from project_core import greet
from project_core.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="A minimal API boilerplate",
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/", response_model=MessageResponse)
def root() -> MessageResponse:
    """Root endpoint returning a welcome message."""
    return MessageResponse(message="Welcome to the API")


@app.get("/greet/{name}", response_model=GreetingResponse)
def greet_endpoint(name: str) -> GreetingResponse:
    """Greet a user by name.

    Args:
        name: The name to greet.

    Returns:
        A GreetingResponse with the greeting message.
    """
    greeting = greet(name)
    return GreetingResponse(message=greeting.message, name=greeting.name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy")
