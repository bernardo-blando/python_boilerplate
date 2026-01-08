#!/usr/bin/env python
"""Post-generation hook to clean up based on user choices."""

import os
import shutil
from pathlib import Path

# Configuration from cookiecutter
FRAMEWORK = "{{ cookiecutter.framework }}"

PROJECT_ROOT = Path.cwd()


def remove_file(filepath: Path) -> None:
    """Remove a file if it exists."""
    if filepath.exists():
        filepath.unlink()
        print(f"Removed: {filepath}")


def remove_dir(dirpath: Path) -> None:
    """Remove a directory if it exists."""
    if dirpath.exists():
        shutil.rmtree(dirpath)
        print(f"Removed: {dirpath}")


def main() -> None:
    """Main cleanup logic."""

    # Handle FastAPI-specific files
    if FRAMEWORK != "fastapi":
        # Remove FastAPI-specific models
        remove_file(PROJECT_ROOT / "src" / "app" / "models.py")
        remove_file(PROJECT_ROOT / "tests" / "test_app" / "test_models.py")


    # Clean up any empty directories
    for dirpath in PROJECT_ROOT.rglob("*"):
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            dirpath.rmdir()
            print(f"Removed empty directory: {dirpath}")

    print("\n" + "=" * 50)
    print(f"Project '{{ cookiecutter.project_slug }}' generated successfully!")
    print("=" * 50)
    print("\nNext steps:")
    print(f"  cd {{ cookiecutter.project_slug }}")
    print("  make setup")
    print("  make run")
    print("\nHappy coding!")


if __name__ == "__main__":
    main()
