"""Gradio application entry point.

Run with: make run
Or: python -m app.main
"""

import gradio as gr

from project_core import greet
from project_core.config import config


def greet_user(name: str) -> str:
    """Greet a user by name."""
    if not name:
        name = "World"
    greeting = greet(name)
    return greeting.message


demo = gr.Interface(
    fn=greet_user,
    inputs=gr.Textbox(label="Your Name", placeholder="Enter your name..."),
    outputs=gr.Textbox(label="Greeting"),
    title=config.app_name,
    description="Enter your name to receive a greeting.",
)

if __name__ == "__main__":
    demo.launch(server_name=config.host, server_port=config.port)
