"""FastAPI application entry point.

Run with: make run
Or: uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.models import GreetingResponse, HealthResponse, MessageResponse
from project_core import greet
from project_core.config import config

app = FastAPI(
    title=config.app_name,
    description="A minimal API boilerplate",
    version=config.app_version,
    debug=config.debug,
)


@app.get("/", response_model=MessageResponse)
def root() -> MessageResponse:
    """Root endpoint returning a welcome message."""
    return MessageResponse(message="Welcome to the API")


@app.get("/greet/{name}", response_model=GreetingResponse)
def greet_endpoint(name: str) -> GreetingResponse:
    """Greet a user by name."""
    greeting = greet(name)
    return GreetingResponse(message=greeting.message, name=greeting.name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy")
