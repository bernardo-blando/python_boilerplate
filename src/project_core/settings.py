"""Application settings using pydantic-settings.

This module demonstrates the recommended pattern for configuration management.
Settings are loaded from environment variables with type validation.

Usage:
    from core.settings import settings
    print(settings.app_name)
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    Environment variables can be set directly or via a .env file.
    Variable names are case-insensitive and can use either format:
    - APP_NAME=MyApp
    - app_name=MyApp

    To add new settings, simply add a new field:

        database_url: str = Field(
            default="sqlite:///./app.db",
            description="Database connection URL",
        )
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = Field(
        default="Boilerplate API",
        description="Application name shown in docs",
    )
    app_version: str = Field(
        default="0.1.0",
        description="Application version",
    )
    debug: bool = Field(
        default=False,
        description="Enable debug mode",
    )

    # Server
    host: str = Field(
        default="0.0.0.0",
        description="Server host",
    )
    port: int = Field(
        default=8000,
        ge=1,
        le=65535,
        description="Server port",
    )


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance.

    Using lru_cache ensures settings are only loaded once.

    Returns:
        The application settings.
    """
    return Settings()


# Convenience alias for direct import
settings = get_settings()
