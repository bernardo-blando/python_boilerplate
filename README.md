# Python Project Cookiecutter Template

A modern Python project template with best practices baked in.

## Features

- **Multiple framework support**: FastAPI, Gradio, Streamlit, or FastHTML
- **Modern tooling**: uv, Ruff, MyPy, pytest
- **Docker ready**: Dockerfile included
- **CI/CD**: GitHub Actions workflow
- **Clean architecture**: Separation of business logic from framework code
- **Type-safe**: Strict MyPy configuration
- **Pre-commit hooks**: Automated code quality checks

## Quick Start

```bash
# Install cookiecutter
pip install cookiecutter

# Generate a new project
cookiecutter gh:your-username/python-boilerplate

# Or from local directory
cookiecutter /path/to/python_boilerplate
```

## Template Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | "My Python Project" |
| `project_slug` | Directory/package name (kebab-case) | Auto-generated |
| `package_name` | Python package name (snake_case) | Auto-generated |
| `project_description` | Short description | "A Python project..." |
| `author_name` | Your name | "Your Name" |
| `author_email` | Your email | "your.email@example.com" |
| `python_version` | Python version | 3.13, 3.12, or 3.11 |
| `framework` | Web framework | fastapi, gradio, streamlit, or fasthtml |

## Generated Project Structure

```
my-python-project/
├── src/
│   ├── my_python_project/    # Business logic (framework-agnostic)
│   │   ├── __init__.py
│   │   ├── config.py         # Pydantic settings
│   │   ├── hello.py          # Example module
│   │   └── models.py         # Domain models
│   └── app/                  # Web application
│       ├── __init__.py
│       └── main.py           # Framework entry point
├── tests/
│   ├── test_core/            # Business logic tests
│   └── test_app/             # App tests
├── .github/workflows/ci.yml  # GitHub Actions
├── Dockerfile
├── Makefile
├── pyproject.toml
├── README.md
└── standards.md
```

## Framework Examples

### FastAPI (default)

```bash
cookiecutter . --no-input framework=fastapi
cd my-python-project
make setup && make run
# Visit http://localhost:8000/docs
```

### Gradio

```bash
cookiecutter . --no-input framework=gradio
cd my-python-project
make setup && make run
# Visit http://localhost:7860
```

### Streamlit

```bash
cookiecutter . --no-input framework=streamlit
cd my-python-project
make setup && make run
# Visit http://localhost:8501
```

### FastHTML

```bash
cookiecutter . --no-input framework=fasthtml
cd my-python-project
make setup && make run
# Visit http://localhost:8000
```

## Development

After generating a project:

```bash
cd my-python-project

# Install dependencies and pre-commit hooks
make setup

# Run linting
make lint

# Run tests
make test

# Start the application
make run

# Build Docker image
make docker-build
```

## License

This template is available under the MIT License.
