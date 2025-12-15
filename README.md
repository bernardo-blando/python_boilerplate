# Project Name

> **TODO:** Replace "Project Name" with your project's name and update this description.

Brief description of what this project does and why it exists.

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd <project-directory>

# Install dependencies (requires uv - https://docs.astral.sh/uv/)
make setup

# Run the development server
make run

# Run tests
make test
```

## Project Structure

```
├── src/
│   ├── core/           # Business logic layer
│   │   ├── __init__.py
│   │   └── hello.py    # Example module
│   └── api/            # API/Web layer
│       ├── __init__.py
│       └── main.py     # FastAPI application
├── tests/
│   ├── conftest.py     # Shared test fixtures
│   ├── test_core/      # Tests for business logic
│   └── test_api/       # Tests for API endpoints
├── pyproject.toml      # Project configuration
├── Makefile            # Development commands
└── standards.md        # Coding standards
```

## Development

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager

### Setup

```bash
# Install all dependencies including dev tools
make install-dev

# Install pre-commit hooks
make install-hooks

# Or do both at once
make setup
```

### Available Commands

| Command | Description |
|---------|-------------|
| `make install` | Install production dependencies |
| `make install-dev` | Install all dependencies including dev tools |
| `make setup` | Full development setup (deps + hooks) |
| `make test` | Run tests |
| `make test-cov` | Run tests with coverage report |
| `make lint` | Run ruff and mypy |
| `make format` | Format code with ruff |
| `make run` | Start development server |
| `make clean` | Remove generated files |

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific tests
make test-k PATTERN=test_greet
```

### Code Quality

This project uses:
- **Ruff** for linting and formatting
- **Mypy** for type checking
- **Pre-commit** hooks to run checks automatically

```bash
# Run all checks
make lint

# Format code
make format
```

## API Documentation

When the server is running, access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Configuration

> **TODO:** Document environment variables and configuration options.

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8000` |

## Contributing

> **TODO:** Update with your contribution guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make all`)
5. Commit your changes (see [Commit Guidelines](standards.md#git-commit-messages))
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please read [standards.md](standards.md) for our coding standards.

## License

> **TODO:** Add license information.

This project is licensed under the [LICENSE NAME] - see the [LICENSE](LICENSE) file for details.

---

> **Note to developers:** Remove all `TODO` comments and update placeholder text before using this README for your project.
