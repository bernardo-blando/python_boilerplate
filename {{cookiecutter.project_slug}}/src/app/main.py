{% if cookiecutter.framework == 'fastapi' %}
"""FastAPI application entry point.

Run with: make run
Or: uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.models import GreetingResponse, HealthResponse, MessageResponse
from {{ cookiecutter.package_name }} import greet
from {{ cookiecutter.package_name }}.config import config

app = FastAPI(
    title=config.app_name,
    description="{{ cookiecutter.project_description }}",
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
{% elif cookiecutter.framework == 'gradio' %}
"""Gradio application entry point.

Run with: make run
Or: python -m app.main
"""

import gradio as gr

from {{ cookiecutter.package_name }} import greet
from {{ cookiecutter.package_name }}.config import config


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
{% elif cookiecutter.framework == 'streamlit' %}
"""Streamlit application entry point.

Run with: make run
Or: streamlit run src/app/main.py --server.port 8000
"""

import streamlit as st

from {{ cookiecutter.package_name }} import greet
from {{ cookiecutter.package_name }}.config import config

st.set_page_config(
    page_title=config.app_name,
    page_icon=":wave:",
    layout="centered",
)

st.title(config.app_name)
st.write("Enter your name to receive a greeting.")

with st.sidebar:
    st.header("About")
    st.write(f"Version: {config.app_version}")
    st.write(f"Debug: {config.debug}")

name = st.text_input("Your Name", placeholder="Enter your name...")

if st.button("Greet"):
    if name:
        greeting = greet(name)
        st.success(greeting.message)
    else:
        greeting = greet("World")
        st.info(greeting.message)
{% elif cookiecutter.framework == 'fasthtml' %}
"""FastHTML application entry point.

Run with: make run
Or: python -m app.main
"""

from fasthtml.common import (
    H1,
    Button,
    Div,
    Form,
    Input,
    P,
    Script,
    fast_app,
    serve,
)

from {{ cookiecutter.package_name }} import greet
from {{ cookiecutter.package_name }}.config import config

app, rt = fast_app(
    hdrs=(Script(src="https://unpkg.com/htmx.org@1.9.10"),),
)


@rt("/")
def get():
    """Render the main page."""
    return Div(
        H1(config.app_name),
        P("Enter your name to receive a greeting."),
        Form(
            Input(
                type="text",
                name="name",
                placeholder="Your name...",
                required=True,
            ),
            Button("Greet", type="submit"),
            hx_post="/greet",
            hx_target="#result",
            hx_swap="innerHTML",
        ),
        Div(id="result"),
    )


@rt("/greet")
def post(name: str):
    """Handle the greeting form submission."""
    greeting = greet(name)
    return P(greeting.message, style="color: green; font-weight: bold;")


if __name__ == "__main__":
    serve(host=config.host, port=config.port)
{% endif %}
