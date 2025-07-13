---
layout: default
title: Agent Guidelines
---

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

This page mirrors the instructions in [AGENTS.md](../AGENTS.md) for AI-based contributors.

## Setup

- Use Python 3.8 or newer.
- Install development dependencies:
  ```bash
  pip install -r requirements-dev.txt
  npm install  # install JS tooling
  pre-commit install  # sets up hooks to run formatting and linting automatically
  ```

## Testing and quality checks

1. Format and lint the project using `pre-commit`:
   ```bash
   pre-commit run --all-files
   ```
2. Run the unit tests:
   ```bash
   pytest -q
   ```
3. Build the docs from the `docs/` directory to verify pages render:
   ```bash
   jekyll build
   ```
   Fix any issues before committing.

## Pull requests

- Summaries should describe the high level goal of the change.
- Include a **Testing** section listing the commands run and whether they succeeded.

## Project direction

- Keep modules small and focused.
- Document new interfaces with docstrings and examples.
- Maintain cross-platform compatibility where reasonable.
- Expand the test suite for new functionality.
- Write helpful commit messages and PR summaries explaining the intent of your changes.

If this page diverges from [AGENTS.md](../AGENTS.md), please update both files so the instructions stay consistent.
