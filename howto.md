# How to Use This Template

This guide explains how to use this boilerplate to start a new Python project.

## 1. Create Your Project

```bash
# Option A: Clone directly
git clone <this-repo-url> my-project
cd my-project
rm -rf .git
git init

# Option B: Use GitHub template feature (if available)
# Click "Use this template" on GitHub
```

## 2. Rename the Core Package

Rename `project_core` to match your project:

```bash
# Rename the directory
mv src/project_core src/myproject

# Update all imports (replace 'myproject' with your name)
find src tests -name "*.py" -exec sed -i '' 's/project_core/myproject/g' {} +

# Update pyproject.toml
sed -i '' 's/project_core/myproject/g' pyproject.toml
```

## 3. Choose Your Framework

Keep only the app(s) you need:

```bash
# Example: Keep only FastAPI
rm -rf src/gradio_app src/streamlit_app src/fasthtml_app
rm -rf tests/test_apps/test_gradio tests/test_apps/test_streamlit tests/test_apps/test_fasthtml
```

Then update `pyproject.toml` to remove unused dependencies:

```toml
# Remove the frameworks you deleted
dependencies = [
    "pydantic-settings>=2.6.0",
    "fastapi>=0.115.0",        # Keep
    "uvicorn[standard]>=0.32.0", # Keep
    # "gradio>=5.0.0",          # Remove
    # "streamlit>=1.40.0",      # Remove
    # "python-fasthtml>=0.6.0", # Remove
]
```

Also update `[tool.hatch.build.targets.wheel]` and `[tool.ruff.lint.isort]` sections.

## 4. Update Project Metadata

Edit `pyproject.toml`:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "What your project does"
```

## 5. Set Up Development Environment

```bash
# Install dependencies
make setup

# Verify everything works
make test
make lint
```

## 6. Write Your README

Edit `README.md` - it's a template with placeholders. Replace:
- Project name and description
- Update the Quick Start section for your app
- Update the project structure
- Add your configuration variables
- Set your license

## 7. Start Building

### Add Business Logic

All business logic goes in `src/myproject/`:

```python
# src/myproject/services.py
from myproject.models import MyModel

def my_business_function(data: str) -> MyModel:
    # Your logic here
    return MyModel(result=data.upper())
```

### Add Pydantic Models

Domain models go in `src/myproject/models.py`:

```python
from pydantic import BaseModel, Field

class MyModel(BaseModel):
    result: str = Field(..., description="The result")
```

### Add Configuration

Settings go in `src/myproject/settings.py`:

```python
class Settings(BaseSettings):
    # Add your settings
    database_url: str = Field(default="sqlite:///./app.db")
    api_key: str | None = Field(default=None)
```

### Connect to Your App

Import your business logic in the app layer:

```python
# src/fastapi_app/main.py
from myproject.services import my_business_function
from myproject.settings import settings

@app.get("/process/{data}")
def process(data: str):
    result = my_business_function(data)
    return {"result": result.result}
```

## Project Structure

```
src/
├── myproject/           # Your business logic (rename from project_core)
│   ├── __init__.py      # Exports
│   ├── models.py        # Pydantic domain models
│   ├── settings.py      # Configuration
│   └── services.py      # Add your business logic here
└── fastapi_app/         # Your chosen framework (or gradio_app, etc.)
    ├── __init__.py
    ├── main.py          # App entry point
    └── schemas.py       # API-specific schemas
```

## Common Tasks

| Task | Command |
|------|---------|
| Run the app | `make run-fastapi` (or `run-gradio`, etc.) |
| Run tests | `make test` |
| Run linting | `make lint` |
| Format code | `make format` |
| Full check | `make all` |

## Framework Reference

| Framework | Best For | Docs |
|-----------|----------|------|
| FastAPI | REST APIs, microservices | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| Gradio | ML demos, quick UIs | [gradio.app](https://gradio.app) |
| Streamlit | Data dashboards | [streamlit.io](https://streamlit.io) |
| FastHTML | Server-rendered, HTMX | [fastht.ml](https://fastht.ml) |

## Checklist

- [ ] Renamed `project_core` to your project name
- [ ] Removed unused framework apps
- [ ] Updated `pyproject.toml` (name, deps, build config)
- [ ] Updated `README.md` with your project info
- [ ] Ran `make setup` and `make test`
- [ ] Deleted this `howto.md` file
