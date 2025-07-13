---
layout: default
title: Contribute
---

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

# Contributing

We welcome improvements to **gpt-fusion**! Please follow these guidelines to keep
things consistent. The full instructions used by Codex are listed on the
[Guidelines](guidelines.md) page.

## Development workflow

- Create a virtual environment and install dev dependencies:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements-dev.txt
  ```
- Run `pre-commit install` so formatting and linting trigger on each commit.
- Format code with `black .` and lint with `flake8`.
- Execute the test suite using `pytest -q` before committing.

## Pull requests

Keep changes focused and document your intent. Passing tests and clean linting
are required before a PR is merged. Summaries should explain the high level goal
and mention the commands you ran.

<script src="assets/js/external-links.js"></script>
<script src="assets/js/anchor-links.js"></script>
<script src="assets/js/toc.js"></script>
