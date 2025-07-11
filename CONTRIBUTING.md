# Contributing to gpt-fusion

We welcome contributions! To keep things tidy, please follow these guidelines.

## Setup

1. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
  ```
   There are no third-party runtime packages, so installing the dev
   requirements is all you need.
   After installing dependencies, run `pre-commit install` to enable automatic
   formatting and linting on each commit.

## Coding standards

- Format code using `black`.
- Run `flake8` for linting.
- Include unit tests with `pytest`.

## Pull requests

- Keep PRs focused and reference related issues.
- Ensure all tests pass with `pytest`.
- We use GitHub Actions to verify builds automatically.
