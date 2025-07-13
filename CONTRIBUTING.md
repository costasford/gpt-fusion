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

We follow standard Python conventions inspired by [PEP 8](https://peps.python.org/pep-0008/).

- Format code with `black`.
- Lint using `flake8`.
- Run `pre-commit run --all-files` before committing.
- Include unit tests with `pytest` for any new functionality.

Commit messages should use the `feat:`, `fix:`, or `docs:` prefixes so GitHub
Actions and reviewers can quickly understand the intent of the change.

## Pull requests

- Keep PRs focused and reference related issues.
- Run `pytest` locally and ensure all tests pass.
- Verify that `pre-commit` checks succeed.
- Update documentation when behavior changes.
- PR titles should match the commit style noted above.
- GitHub Actions will verify builds and linting automatically.

See the [Code of Conduct](CODE_OF_CONDUCT.md) for expectations around respectful
communication. Good discussions lead to better code!
