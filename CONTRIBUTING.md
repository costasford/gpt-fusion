# Contributing to gpt-fusion

We welcome contributions! To keep things tidy, please follow these guidelines.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```

## Coding standards

- Format code using `black`.
- Run `flake8` for linting.
- Include unit tests with `pytest`.

## Pull requests

- Keep PRs focused and reference related issues.
- Ensure all tests pass with `pytest`.
- We use GitHub Actions to verify builds automatically.
