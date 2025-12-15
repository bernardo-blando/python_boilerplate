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

from project_core import greet
from project_core.config import config

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
