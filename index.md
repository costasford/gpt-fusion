---
layout: default
title: GPT Fusion - Human-AI Collaboration Toolkit
description: Practical demos of human-AI collaboration with Python utilities, web scraping, FastAPI backend, and more
---

# GPT Fusion

**Practical demos of human-AI collaboration**

A Python toolkit for building AI-assisted applications with utilities for text processing, web scraping, FastAPI backends, and interactive demos.

[![CI](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.4.4-brightgreen.svg)](https://github.com/costasford/gpt-fusion/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/costasford/gpt-fusion/blob/main/LICENSE)
[![Tests](https://img.shields.io/badge/tests-80%2B%20passed-brightgreen.svg)](https://github.com/costasford/gpt-fusion/actions)
[![Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen.svg)](https://github.com/costasford/gpt-fusion)

🌐 **[Live Documentation](https://costasford.github.io/gpt-fusion/)** • 🎮 **[Try Live Demo](https://costasford.github.io/gpt-fusion/demo.html)** • 📁 **[View Source](https://github.com/costasford/gpt-fusion)**

## 🚀 Quick Start

### Install
```bash
pip install gpt-fusion
```

### Basic Usage
```python
import gpt_fusion

# Text utilities
print(gpt_fusion.greet('World'))
print(gpt_fusion.word_count('Hello world'))
print(gpt_fusion.reverse_words('Hello world'))

# Math helpers  
numbers = gpt_fusion.load_numbers_from_csv('data/numbers.csv')
print(f"Average: {gpt_fusion.average_from_csv('data/numbers.csv')}")

# Generate starter projects
gpt_fusion.create_csv_app('my-csv-demo')
gpt_fusion.create_tailwind_ui('my-ui-demo')
```

### Advanced Features
Install with optional extras for full functionality:
```bash
pip install "gpt-fusion[web,twitter,backend,build]"
```

## ✨ Features

### 🐍 Python Utilities
Core text processing, math helpers, and CSV analysis tools.
```python
import gpt_fusion

# Text processing
gpt_fusion.word_count("Hello world")  # 2
gpt_fusion.reverse_words("Hello world")  # "world Hello"
gpt_fusion.is_palindrome("racecar")  # True

# Math & CSV
gpt_fusion.average_from_csv("data.csv")
gpt_fusion.median_from_csv("data.csv")
```

### 🌐 Web Scraping
Simple web scraping utilities with BeautifulSoup integration.
```python
# Install: pip install "gpt-fusion[web]"
import gpt_fusion

html = gpt_fusion.scrape("https://example.com")
# Returns clean text content
```

### 🚀 FastAPI Backend
Ready-to-deploy API server with auto-generated docs.
```python
# Install: pip install "gpt-fusion[backend]"
import uvicorn
import gpt_fusion

# Start server
uvicorn.run(gpt_fusion.backend_app, port=8000)
```

### 🐦 Twitter Integration
Twitter bot utilities with OAuth support.
```python
# Install: pip install "gpt-fusion[twitter]"
# Reads TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, and
# TWITTER_ACCESS_SECRET from the environment if not passed explicitly.
from gpt_fusion import TwitterBot

bot = TwitterBot()
bot.post_tweet("Hello from GPT Fusion!")
```

## 🎮 Demo Projects

### 🔐 Auth UI Kit
Beautiful Tailwind CSS login form with Firebase authentication. Includes email/password and Google OAuth flows.

[→ View Source](https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit)

### 🎯 Unity 3D Demo
Interactive 3D game prototype with movement, items, and basic gameplay mechanics.

[→ View Unity Scripts](https://github.com/costasford/gpt-fusion/tree/main/unity-prototype)

### 📊 CSV Analysis
Data processing and analysis examples with built-in sample datasets.
```bash
$ python examples/tutorial.py
Values: [1.0, 2.0, 3.0, 4.0, 5.0]
Average: 3.0
Median: 3.0
```

### 🛠️ Starter Kit Generator
Generate new projects with pre-configured templates.
```bash
# Create a CSV analysis app
python -m gpt_fusion.starter_kits create_csv_app my-app

# Create a Tailwind UI demo  
python -m gpt_fusion.starter_kits create_tailwind_ui my-ui
```

## 🔌 API & Deployment

### Local Development
```bash
pip install "gpt-fusion[backend]"
uvicorn gpt_fusion.backend:app --reload
```

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /greet/{name} | Personalized greeting |
| GET | /projects | List of demo projects |
| GET | /health | Health check endpoint |

### Deploy to Render
1. Create a new Web Service from your GitHub repo
2. Build Command: `pip install "gpt-fusion[backend]"`
3. Start Command: `uvicorn gpt_fusion.backend:app --host 0.0.0.0 --port $PORT`

### Deploy to Heroku
Create a `Procfile`:
```
web: uvicorn gpt_fusion.backend:app --host 0.0.0.0 --port $PORT
```

##
 🤝 Contributing

### Development Setup
```bash
git clone https://github.com/costasford/gpt-fusion.git
cd gpt-fusion
pip install -r requirements-dev.txt
pip install -e .
```

### Run Tests
```bash
pytest --cov=src/gpt_fusion --cov-report=term-missing
```

### Code Quality
```bash
python scripts/run_checks.py
```

This runs:
- **Black** - Code formatting
- **Flake8** - Linting
- **Pytest** - Test suite with 93% coverage

### Project Structure
```
src/gpt_fusion/     # Main package
├── core.py         # Basic utilities  
├── text_utils.py   # Text processing
├── analysis.py     # CSV/data tools
├── web_scraper.py  # Web scraping (optional)
├── backend.py      # FastAPI server (optional)
├── twitter_bot.py  # Twitter integration (optional)
└── starter_kits.py # Project templates

tests/              # Comprehensive test suite
docs/               # Jekyll documentation
examples/           # Usage examples
```

### Links
📖 [GitHub Repository](https://github.com/costasford/gpt-fusion) • 🐛 [Report Issues](https://github.com/costasford/gpt-fusion/issues) • 📄 [MIT License](https://github.com/costasford/gpt-fusion/blob/main/LICENSE)

---

*GPT Fusion - Practical demos of human-AI collaboration. Built with ❤️ and Python.*
