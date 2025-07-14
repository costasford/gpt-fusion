---
layout: default
title: Contribute
---

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

# Contributing

We welcome improvements to **gpt-fusion**! Please follow these guidelines to maintain consistency. The full instructions used by Codex are listed on the
[Guidelines](guidelines.md) page.

## Development workflow

- Create a virtual environment and install dev dependencies:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements-dev.txt
  ```
- Run `pre-commit install` so formatting and linting trigger on each commit.
- Run `pre-commit run --all-files` to format and lint the code.
- Execute the test suite using `pytest -q` before committing.
- Build the docs with `jekyll build` to ensure pages render.

## Pull requests

Keep changes focused and document your intent. Passing tests and clean linting
are required before a PR is merged. Summaries should explain the high level goal
and mention the commands you ran.
- The `main` branch is protected; CI must succeed before your pull request can be merged.
- Releases use [Release Drafter](https://github.com/marketplace/release-drafter) and follow Semantic Versioning.

<script src="assets/js/bundle.js"></script>
