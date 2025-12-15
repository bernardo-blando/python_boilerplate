# Alternative Framework Implementations

This folder contains ready-to-use implementations for different web frameworks.
The default boilerplate uses **FastAPI**. To switch, follow the steps below.

## Switching Frameworks

### 1. Copy the alternative to `src/app/`

```bash
# For Gradio
rm -rf src/app && cp -r app_alternatives/gradio src/app

# For Streamlit
rm -rf src/app && cp -r app_alternatives/streamlit src/app

# For FastHTML
rm -rf src/app && cp -r app_alternatives/fasthtml src/app
```

### 2. Update `pyproject.toml` dependencies

```toml
# FastAPI (default)
dependencies = [
    "pydantic-settings>=2.6.0",
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
]

# Gradio
dependencies = [
    "pydantic-settings>=2.6.0",
    "gradio>=5.0.0",
]

# Streamlit
dependencies = [
    "pydantic-settings>=2.6.0",
    "streamlit>=1.40.0",
]

# FastHTML
dependencies = [
    "pydantic-settings>=2.6.0",
    "python-fasthtml>=0.6.0",
]
```

### 3. Update `Makefile` run target

```makefile
# FastAPI (default)
run:
	uv run uvicorn app.main:app --reload --host $(HOST) --port $(PORT)

# Gradio
run:
	uv run python -m app.main

# Streamlit
run:
	uv run streamlit run src/app/main.py --server.port $(PORT)

# FastHTML
run:
	uv run python -m app.main
```

### 4. Sync dependencies

```bash
uv sync
```

## Framework Comparison

| Framework | Best For | Docs |
|-----------|----------|------|
| FastAPI | REST APIs, microservices | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| Gradio | ML demos, quick UIs | [gradio.app](https://gradio.app) |
| Streamlit | Data dashboards | [streamlit.io](https://streamlit.io) |
| FastHTML | Server-rendered, HTMX | [fastht.ml](https://fastht.ml) |
