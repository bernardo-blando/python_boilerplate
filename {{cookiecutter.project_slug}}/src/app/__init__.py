{% if cookiecutter.framework == 'fastapi' %}
"""Application package (FastAPI)."""

from app.main import app

__all__ = ["app"]
{% else %}
"""Application package ({{ cookiecutter.framework | capitalize }})."""
{% endif %}
