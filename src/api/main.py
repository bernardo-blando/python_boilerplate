"""FastAPI application entry point."""

from fastapi import FastAPI

from core import greet

app = FastAPI(
    title="Boilerplate API",
    description="A minimal API boilerplate",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the API"}


@app.get("/greet/{name}")
def greet_endpoint(name: str) -> dict[str, str]:
    """Greet a user by name.

    Args:
        name: The name to greet.

    Returns:
        A dictionary with the greeting message.
    """
    return {"message": greet(name)}


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
