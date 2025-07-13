---
layout: default
title: Agent Guidelines
---

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

This page summarizes the instructions in [AGENTS.md](../AGENTS.md) for AI-based contributors.

## Testing

Always run `pytest -q` before committing changes.

## Formatting and linting

Run `black .` to format code and `flake8` to lint. Fix any issues before committing.

## Pull requests

Summaries should describe the high level goal of the change and include a short **Testing** section listing the commands run and whether they succeeded.

## Project direction

- Keep modules small and focused.
- Document new interfaces with docstrings and examples.
- Maintain cross-platform compatibility where reasonable.
- Expand the test suite for new functionality.
- Write helpful commit messages and PR summaries explaining the intent of your changes.

