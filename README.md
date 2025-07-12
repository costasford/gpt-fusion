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
2. **Dependencies**: The core library uses only the Python standard library. The optional Twitter bot requires [tweepy](https://www.tweepy.org/).
3. **Style**: Format code with [black](https://github.com/psf/black) and lint with [flake8](https://github.com/PyCQA/flake8). A [pre-commit](https://pre-commit.com) hook runs these automatically.
4. **Tests**: Run `pytest` before submitting changes.
5. **Hooks**: After installing dependencies, run `pre-commit install` so formatting and linting run on each commit.
6. **CI**: GitHub Actions runs formatting checks and the test suite on every pull request.
7. **Contributions**: Please open issues and pull requests via GitHub. Keep commits clear and focused.

Enjoy fusing ideas with code!

## Sample apps

Check out `auth-ui-kit/` for a Firebase-based login demo with sign-up, password reset,
and Google authentication. You can also explore `twitter_bot.py` for posting project
updates to Twitter, and `unity-prototype/` for a basic Unity setup.

## Data

The `data/` directory contains a small `numbers.csv` file used in tutorials and
tests. Feel free to replace it with your own datasets when experimenting with
the CSV utilities.

## Documentation

Comprehensive guides and examples live in the [`docs/`](docs) folder. The
markdown files there are rendered with [Jekyll](https://jekyllrb.com/). To preview
the site locally:

1. Install Ruby and the Jekyll gem: `gem install jekyll`.
2. Run `jekyll serve` from the `docs/` directory.
3. Open <http://localhost:4000> in your browser to explore the docs.
