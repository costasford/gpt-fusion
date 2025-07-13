# AGENTS instructions for gpt-fusion

Codex should follow these guidelines when contributing to this repository.

## Testing

Always run the unit tests with `pytest -q` before committing changes.

## Formatting and linting

Run `black .` to format code and `flake8` to lint. Fix any issues before committing.

## Documentation

Keep the README and docs in sync with new features. Build the site with
`jekyll build` to verify pages render. A copy of these guidelines is published
at [docs/guidelines.md](docs/guidelines.md).

## Pull request messages

Summaries should describe the high level goal of the change. Include a short **Testing** section that lists the commands run and whether they succeeded.

## Project direction

The goal of *gpt-fusion* is to demonstrate how human and AI contributions can
blend into clear, maintainable tooling. When adding features or fixing bugs,
keep the following principles in mind:

- Keep modules small and focused so others can easily reuse them.
- Document new interfaces with docstrings and practical examples.
- Maintain cross-platform compatibility where reasonable.
- Expand the test suite for any new functionality.
- Write helpful commit messages and PR summaries explaining the intent of your
  changes.
