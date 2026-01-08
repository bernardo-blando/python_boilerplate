#!/usr/bin/env python
"""Pre-generation hook to validate cookiecutter inputs."""

import re
import sys

# Validate package name is a valid Python identifier
package_name = "{{ cookiecutter.package_name }}"
if not re.match(r"^[a-z][a-z0-9_]*$", package_name):
    print(f"ERROR: '{package_name}' is not a valid Python package name.")
    print("Package names must:")
    print("  - Start with a lowercase letter")
    print("  - Contain only lowercase letters, numbers, and underscores")
    sys.exit(1)

# Validate project slug
project_slug = "{{ cookiecutter.project_slug }}"
if not re.match(r"^[a-z][a-z0-9-]*$", project_slug):
    print(f"ERROR: '{project_slug}' is not a valid project slug.")
    print("Project slugs must:")
    print("  - Start with a lowercase letter")
    print("  - Contain only lowercase letters, numbers, and hyphens")
    sys.exit(1)

# Validate Python version format
python_version = "{{ cookiecutter.python_version }}"
if not re.match(r"^3\.\d{1,2}$", python_version):
    print(f"ERROR: '{python_version}' is not a valid Python version format.")
    print("Expected format: 3.11, 3.12, 3.13, etc.")
    sys.exit(1)

# Check Python version is supported
major, minor = map(int, python_version.split("."))
if minor < 11:
    print(f"WARNING: Python {python_version} may not support all features.")
    print("Python 3.11+ is recommended.")

print(f"Generating project: {project_slug}")
print(f"Package name: {package_name}")
print(f"Framework: {{ cookiecutter.framework }}")
print(f"Python version: {python_version}")
