# gpt-fusion
[![CI Status](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml)

"Human charm meets algorithmic arm"

This repository is a playful collaboration between Costas and ChatGPT. We mix code and conversation to explore how human ingenuity and AI assistance can fuse into something greater than either alone. Stick around as we experiment with new ideas, tools, and witty back-and-forth.

## Goals

- Provide a small playground for exploring human–AI collaboration.
- Offer simple, reusable modules that demonstrate practical uses of AI-assisted tooling.
- Maintain code quality and encourage contributions through clear guidelines and tests.

## Project layout

```
src/            # Python package source
  gpt_fusion/   # package implementation
    core.py     # greeting helper
    utils.py    # math helpers and chat history container
    analysis.py # simple CSV helpers

tests/          # pytest-based unit tests

docs/           # documentation with examples and tutorials
data/           # sample data
```

## Development workflow

1. **Environment**: Use Python 3.8+.
2. **Dependencies**: The project relies only on the Python standard library, so there are no runtime packages to install.
3. **Style**: Format code with [black](https://github.com/psf/black) and lint with [flake8](https://github.com/PyCQA/flake8).
4. **Tests**: Run `pytest` before submitting changes.
5. **CI**: GitHub Actions runs formatting checks and the test suite on every pull request.
6. **Contributions**: Please open issues and pull requests via GitHub. Keep commits clear and focused.

Enjoy fusing ideas with code!

## Sample apps

Check out `auth-ui-kit/` for a simple web login example and `unity-prototype/` for a basic Unity setup.

## Data

The `data/` directory contains a small `numbers.csv` file used in tutorials and
tests. Feel free to replace it with your own datasets when experimenting with
the CSV utilities.
