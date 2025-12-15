"""Hello world module demonstrating basic business logic."""


def greet(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Entry point for the hello module."""
    print(greet())


if __name__ == "__main__":
    main()
