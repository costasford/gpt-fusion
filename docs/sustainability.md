---
layout: default
title: Sustainability Guide
---

{% include nav.html %}

# Long-term maintenance

Keeping the repository healthy ensures others can reuse these examples far into the future. Follow these practices to sustain the project over time.

## Regular upkeep

- **Keep dependencies current**. Run `pip list --outdated` and update packages in `requirements-dev.txt` when new versions are released.
- **Check for security issues**. Tools like `pip-audit` or GitHub's Dependabot can highlight potential vulnerabilities.
- **Verify builds**. Always run `pre-commit run --all-files`, `pytest -q`, and `jekyll build` before merging changes.
- **Document significant changes**. Update the relevant markdown files and docstrings so new contributors understand the latest behaviour.
- **Tag releases following [Semantic Versioning](https://semver.org)**. GitHub's Release Drafter action compiles notes automatically when a tag is pushed.

## Project health

- Aim for small, focused modules with clear tests.
- Keep the CI workflow green. Fix failing jobs quickly to avoid regressions.
- Enable branch protection on `main` so merges only land when the CI workflow succeeds.
- Review pull requests thoroughly to maintain code quality.

With routine attention the project can serve as a lasting reference for human–AI collaboration.
