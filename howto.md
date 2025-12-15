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

## 3. Choose Your Framework (Optional)

The boilerplate uses FastAPI by default. Ready-to-use alternatives are in `app_alternatives/`:

```bash
# Switch to Gradio, Streamlit, or FastHTML
rm -rf src/app && cp -r app_alternatives/gradio src/app
```

Then update `pyproject.toml` dependencies and `Makefile`. See [app_alternatives/README.md](app_alternatives/README.md).

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

Config goes in `src/myproject/config.py`:

```python
class Config(BaseSettings):
    # Add your config
    database_url: str = Field(default="sqlite:///./app.db")
    api_key: str | None = Field(default=None)
```

### Connect to Your App

Import your business logic in the app layer:

```python
# src/app/main.py
from myproject.services import my_business_function
from myproject.config import config

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
│   ├── config.py        # Configuration
│   └── services.py      # Add your business logic here
└── app/                 # Web application (FastAPI by default)
    ├── __init__.py
    ├── main.py          # App entry point
    └── schemas.py       # API-specific schemas (FastAPI)
```

## Common Tasks

| Task | Command |
|------|---------|
| Run the app | `make run` |
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
- [ ] Updated `pyproject.toml` (name, deps, build config)
- [ ] Updated `README.md` with your project info
- [ ] Ran `make setup` and `make test`
- [ ] Deleted this `howto.md` file
