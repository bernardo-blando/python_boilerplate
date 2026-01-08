# syntax=docker/dockerfile:1

FROM python:{{ cookiecutter.python_version }}-slim AS base

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --frozen --no-dev --no-install-project

# Copy source code
COPY src/ ./src/

# Install the project
RUN uv sync --frozen --no-dev

# Expose port
EXPOSE 8000

{% if cookiecutter.framework == 'fastapi' %}
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
{% elif cookiecutter.framework == 'gradio' %}
CMD ["uv", "run", "python", "-m", "app.main"]
{% elif cookiecutter.framework == 'streamlit' %}
CMD ["uv", "run", "streamlit", "run", "src/app/main.py", "--server.port", "8000", "--server.address", "0.0.0.0"]
{% elif cookiecutter.framework == 'fasthtml' %}
CMD ["uv", "run", "python", "-m", "app.main"]
{% endif %}
