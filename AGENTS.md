# Agent guidelines for gpt-fusion

Codex must follow these steps when contributing to this repository.

## Setup

- Use Python 3.8 or newer.
- Install development dependencies:
  ```bash
  pip install -r requirements-dev.txt
  pre-commit install  # sets up hooks to run formatting and linting automatically
  ```

## Testing and quality checks

1. Format and lint the project. The `pre-commit` hook will run these checks:
   ```bash
   pre-commit run --all-files
   ```
   You can also run `black .` and `flake8` directly.
2. Run the unit tests:
   ```bash
   pytest -q
   ```
3. Build the documentation from the `docs/` directory:
   ```bash
   jekyll build
   ```
   Fix any issues before committing.

## Pull requests

- Summaries should describe the high level goal of the change.
- Include a **Testing** section listing the commands run and whether they succeeded.

## Project direction

- Keep modules small and focused so others can easily reuse them.
- Document new interfaces with docstrings and practical examples.
- Maintain cross-platform compatibility where reasonable.
- Expand the test suite for any new functionality.
- Write helpful commit messages and PR summaries explaining the intent of your changes.

If you modify this file, update [docs/guidelines.md](docs/guidelines.md) to keep the website in sync.

A copy of these guidelines is available at [docs/guidelines.md](docs/guidelines.md).
