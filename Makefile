.PHONY: all install install-dev test test-cov lint format check run clean help

# Default target
all: lint test

# =============================================================================
# Installation
# =============================================================================

## Install production dependencies
install:
	uv sync

## Install all dependencies including dev tools
install-dev:
	uv sync --all-extras

## Install pre-commit hooks
install-hooks:
	uv run pre-commit install

## Full development setup
setup: install-dev install-hooks

# =============================================================================
# Testing
# =============================================================================

## Run tests
test:
	uv run pytest

## Run tests with coverage report
test-cov:
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html

## Run tests matching a pattern (usage: make test-k PATTERN=test_name)
test-k:
	uv run pytest -k "$(PATTERN)"

# =============================================================================
# Code Quality
# =============================================================================

## Run all linting checks (ruff + mypy)
lint: lint-ruff lint-mypy

## Run ruff linter
lint-ruff:
	uv run ruff check src tests

## Run mypy type checker
lint-mypy:
	uv run mypy src

## Format code with ruff
format:
	uv run ruff format src tests
	uv run ruff check --fix src tests

## Check formatting without making changes
check:
	uv run ruff format --check src tests
	uv run ruff check src tests
	uv run mypy src

# =============================================================================
# Running the Application
# =============================================================================

## Run the API server (development mode with auto-reload)
run:
	uv run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

## Run the API server (production mode)
run-prod:
	uv run uvicorn api.main:app --host 0.0.0.0 --port 8000

## Run the CLI entry point (if configured)
run-cli:
	uv run python -m core.hello

# =============================================================================
# Maintenance
# =============================================================================

## Remove all generated files
clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf src/*.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

## Update dependencies
update:
	uv lock --upgrade

# =============================================================================
# Help
# =============================================================================

## Show this help message
help:
	@echo "Available targets:"
	@echo ""
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/## /  /'
	@echo ""
	@echo "Usage: make [target]"
