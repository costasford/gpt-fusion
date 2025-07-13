# gpt-fusion
[![CI Status](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml)
[![Coverage Status](https://img.shields.io/coveralls/github/costasford/gpt-fusion?branch=main)](https://coveralls.io/github/costasford/gpt-fusion?branch=main)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/costasford/gpt-fusion)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/gpt-fusion.svg)](https://pypi.org/project/gpt-fusion/)

"Practical demos of human-AI collaboration"

GPT Fusion is a small sandbox for developers curious about mixing traditional
programming with AI assistance. It bundles CSV analysis utilities, a sample
FastAPI backend, web scraping helpers and demo apps like a Firebase auth UI and
a Unity prototype. The project targets tinkerers who want clear examples of how
humans and ChatGPT can iteratively build software together.

## Features

- Python utilities for math and CSV summaries
- Simple web scraper and text helpers
- Optional FastAPI backend and Twitter bot modules
- Demo front-end with Firebase authentication
- Unity project showcasing basic movement scripts

## Installation & Usage

Clone the repo and install the development dependencies:

```bash
git clone https://github.com/costasford/gpt-fusion.git
cd gpt-fusion
pip install -r requirements-dev.txt
```

Run the test suite to confirm everything works:

```bash
pytest
```

Try the example script which loads numbers from `data/numbers.csv`:

```bash
python examples/tutorial.py
```

You can also preview the auth UI demo by serving the `auth-ui-kit` folder:

```bash
python -m http.server --directory auth-ui-kit
```

![Auth UI screenshot](auth-ui-screenshot.png)

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

## Documentation

Detailed guides live in [`docs/`](docs). Build the site locally with

```bash
cd docs
jekyll serve
```

and open <http://localhost:4000> to browse the tutorials.

## Contributing

Development guidelines are recorded in [AGENTS.md](AGENTS.md).
Please open issues and pull requests via GitHub.

## Repository topics and labels

To help others discover this project, tag the repository with relevant topics
such as `ai`, `tailwindcss`, `pytest` and `unity3d`.  Issues should use
standard labels like `bug`, `enhancement` and `help wanted` so contributors can
quickly triage requests.

## License & Contact

This project is licensed under the [MIT License](LICENSE).
For questions or support, open an issue or reach the maintainer at
[costasford@yahoo.com](mailto:costasford@yahoo.com).

