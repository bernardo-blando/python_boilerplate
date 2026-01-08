# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

```bash
git clone <repository-url>
cd {{ cookiecutter.project_slug }}

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
├── {{ cookiecutter.package_name }}/    # Business logic (framework-agnostic)
└── app/                                # {{ cookiecutter.framework | capitalize }} application
tests/
├── test_core/                          # Business logic tests
└── test_app/                           # App tests
```

## Development

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://docs.astral.sh/uv/)

### Commands

| Command | Description |
|---------|-------------|
| `make setup` | Install dependencies and pre-commit hooks |
| `make test` | Run tests |
| `make lint` | Run linting (ruff + mypy) |
| `make format` | Format code |
| `make run` | Start the application |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |

## Configuration

Environment variables (set in `.env` or environment):

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | `{{ cookiecutter.project_name }}` |
| `DEBUG` | Enable debug mode | `false` |
| `PORT` | Server port | `8000` |

## Docker

Build and run with Docker:

```bash
# Build the image
make docker-build

# Run the container
make docker-run
```

Or manually:

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```

## Contributing

1. Create a feature branch
2. Make changes
3. Run `make all` (lint + test)
4. Open a Pull Request

See [standards.md](standards.md) for coding conventions.

