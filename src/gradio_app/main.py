"""Gradio application entry point.

Run with: make run-gradio
Or: python -m gradio_app.main

Gradio is great for:
- ML model demos
- Quick prototypes
- Shareable interfaces
"""

import gradio as gr

from project_core import greet
from project_core.settings import settings


def greet_user(name: str) -> str:
    """Greet a user by name using core business logic."""
    if not name.strip():
        name = "World"
    greeting = greet(name)
    return greeting.message


# Build the Gradio interface
app = gr.Interface(
    fn=greet_user,
    inputs=gr.Textbox(
        label="Your Name",
        placeholder="Enter your name...",
        value="World",
    ),
    outputs=gr.Textbox(label="Greeting"),
    title=settings.app_name,
    description="A simple greeting demo using Gradio",
    examples=[["Alice"], ["Bob"], ["World"]],
    theme=gr.themes.Soft(),
)


if __name__ == "__main__":
    app.launch(
        server_name=settings.host,
        server_port=settings.port,
    )
