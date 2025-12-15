"""FastHTML application entry point.

Run with: make run-fasthtml
Or: python -m fasthtml_app.main

FastHTML is great for:
- Hypermedia-driven apps (HTMX)
- Server-rendered web apps
- Progressive enhancement
"""

from fasthtml.common import (
    H1,
    Button,
    Div,
    Form,
    Input,
    P,
    Script,
    Style,
    fast_app,
    serve,
)

from project_core import greet
from project_core.settings import settings

app, rt = fast_app(
    hdrs=(
        Style(
            """
            body { font-family: system-ui; max-width: 600px; margin: 2rem auto; padding: 1rem; }
            .greeting { padding: 1rem; background: #e8f5e9; border-radius: 8px; margin-top: 1rem; }
            input { padding: 0.5rem; font-size: 1rem; width: 200px; }
            button { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; }
            """
        ),
        Script(src="https://unpkg.com/htmx.org@2.0.0"),
    ),
)


@rt("/")
def home():
    """Render the home page."""
    return (
        H1(settings.app_name),
        P("A simple greeting demo using FastHTML"),
        Form(
            Input(
                type="text",
                name="name",
                placeholder="Enter your name...",
                value="World",
            ),
            Button("Greet", type="submit"),
            hx_post="/greet",
            hx_target="#result",
            hx_swap="innerHTML",
        ),
        Div(id="result"),
    )


@rt("/greet", methods=["POST"])
def greet_user(name: str = "World"):
    """Handle the greet form submission."""
    if not name.strip():
        name = "World"
    greeting = greet(name)
    return Div(greeting.message, cls="greeting")


if __name__ == "__main__":
    serve(host=settings.host, port=settings.port)
