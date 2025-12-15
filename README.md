# Project Name

Brief description of what this project does and why it exists.

## Quick Start

```bash
git clone <repository-url>
cd <project-directory>

# Install dependencies
make setup

# Run the app
make run

# Run tests
make test
```

## Project Structure

```
src/
├── project_core/       # Business logic (shared across frameworks)
└── app/                # Web application (FastAPI by default)
tests/
├── test_core/          # Business logic tests
└── test_apps/          # App tests
```

## Switching Frameworks

This boilerplate uses FastAPI by default. Ready-to-use alternatives are in `app_alternatives/`:

```bash
# Switch to Gradio
rm -rf src/app && cp -r app_alternatives/gradio src/app

# Switch to Streamlit
rm -rf src/app && cp -r app_alternatives/streamlit src/app

# Switch to FastHTML
rm -rf src/app && cp -r app_alternatives/fasthtml src/app
```

Then update dependencies in `pyproject.toml` and run `uv sync`.

See [app_alternatives/README.md](app_alternatives/README.md) for full instructions.

## Development

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Commands

| Command | Description |
|---------|-------------|
| `make setup` | Install dependencies and pre-commit hooks |
| `make test` | Run tests |
| `make lint` | Run linting (ruff + mypy) |
| `make format` | Format code |
| `make run` | Start the application |

## Configuration

Environment variables (set in `.env` or environment):

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | `Boilerplate API` |
| `DEBUG` | Enable debug mode | `false` |
| `PORT` | Server port | `8000` |

## Contributing

1. Create a feature branch
2. Make changes
3. Run `make all` (lint + test)
4. Open a Pull Request

See [standards.md](standards.md) for coding conventions.

## License

[Add license information]
