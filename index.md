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
[![Tests](https://img.shields.io/badge/tests-135%20passed-brightgreen.svg)](https://github.com/costasford/gpt-fusion/actions)
[![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen.svg)](https://github.com/costasford/gpt-fusion)

🌐 **[Live Documentation](https://costasford.github.io/gpt-fusion/)** • 🎮 **[Try Interactive Demos](#interactive-demos)** • 📁 **[View Source](https://github.com/costasford/gpt-fusion)**

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

## 🎮 Interactive Demos {#interactive-demos}

Try the core utilities right here, no install required.

<div class="demo-card bg-white rounded-xl shadow-lg p-6 mb-6">
  <h3 class="text-xl font-bold mb-1">🔤 Text Processing</h3>
  <p class="text-sm text-gray-600 mb-4">Smart text utilities with instant results</p>

  <div class="grid md:grid-cols-2 gap-6">
    <div>
      <label for="text-input" class="block text-sm font-medium mb-2">Enter text to process:</label>
      <textarea id="text-input"
                class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                rows="4"
                placeholder="Type something here...">The quick brown fox jumps over the lazy dog</textarea>
      <div class="flex flex-wrap gap-2 mt-4">
        <button type="button" onclick="processText('word_count')" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">Count Words</button>
        <button type="button" onclick="processText('reverse_words')" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition">Reverse Words</button>
        <button type="button" onclick="processText('palindrome')" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition">Check Palindrome</button>
      </div>
    </div>

    <div>
      <label class="block text-sm font-medium mb-2">Output:</label>
      <div id="text-output" class="bg-gray-900 text-white p-4 rounded-lg min-h-32 font-mono">
        Click a button to see the magic! ✨
      </div>
      <div class="mt-4">
        <label class="block text-sm font-medium mb-2">Python Code:</label>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto"><code id="text-code">import gpt_fusion

# Try the functions above!
text = "Your input here"
gpt_fusion.word_count(text)
gpt_fusion.reverse_words(text)
gpt_fusion.is_palindrome(text)</code></pre>
      </div>
    </div>
  </div>
</div>

<div class="demo-card bg-white rounded-xl shadow-lg p-6 mb-6">
  <h3 class="text-xl font-bold mb-1">📊 CSV Data Analysis</h3>
  <p class="text-sm text-gray-600 mb-4">Powerful data processing with streaming support</p>

  <div class="grid md:grid-cols-2 gap-6">
    <div>
      <label for="csv-input" class="block text-sm font-medium mb-2">Enter CSV data (comma-separated values):</label>
      <textarea id="csv-input"
                class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                rows="6"
                placeholder="value&#10;1.5&#10;2.8&#10;3.2&#10;4.1&#10;5.7">value
1.5
2.8
3.2
4.1
5.7</textarea>
      <div class="flex flex-wrap gap-2 mt-4">
        <button type="button" onclick="analyzeCSV('average')" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">Calculate Average</button>
        <button type="button" onclick="analyzeCSV('median')" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition">Find Median</button>
        <button type="button" onclick="analyzeCSV('stats')" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition">Full Stats</button>
      </div>
    </div>

    <div>
      <label class="block text-sm font-medium mb-2">Analysis Results:</label>
      <div id="csv-output" class="bg-gray-900 text-white p-4 rounded-lg min-h-32 font-mono whitespace-pre-line">
        Enter CSV data to see analysis! 📈
      </div>
      <div class="mt-4">
        <label class="block text-sm font-medium mb-2">Python Code:</label>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto"><code>import gpt_fusion

# Load data from CSV file
data = gpt_fusion.load_numbers_from_csv('data.csv')

# Fast streaming for large files
avg = gpt_fusion.average_from_csv('data.csv', use_streaming=True)
med = gpt_fusion.median_from_csv('data.csv')

print(f"Average: {avg}")
print(f"Median: {med}")</code></pre>
      </div>
    </div>
  </div>
</div>

<div class="demo-card bg-white rounded-xl shadow-lg p-6 mb-6">
  <h3 class="text-xl font-bold mb-1">🛠️ Project Generator</h3>
  <p class="text-sm text-gray-600 mb-4">Generate production-ready projects instantly</p>

  <div class="grid md:grid-cols-3 gap-4">
    <div class="border border-gray-200 rounded-lg p-4 hover:border-blue-500 transition cursor-pointer" onclick="showProjectCode('csv')">
      <div class="text-center">
        <div class="text-3xl mb-2">📊</div>
        <h4 class="font-semibold">CSV Analytics App</h4>
        <p class="text-sm text-gray-600 mt-2">FastAPI backend with data visualization</p>
      </div>
    </div>

    <div class="border border-gray-200 rounded-lg p-4 hover:border-blue-500 transition cursor-pointer" onclick="showProjectCode('ui')">
      <div class="text-center">
        <div class="text-3xl mb-2">🎨</div>
        <h4 class="font-semibold">Tailwind UI Kit</h4>
        <p class="text-sm text-gray-600 mt-2">Modern responsive web interface</p>
      </div>
    </div>

    <div class="border border-gray-200 rounded-lg p-4 hover:border-blue-500 transition cursor-pointer" onclick="showProjectCode('fullstack')">
      <div class="text-center">
        <div class="text-3xl mb-2">🚀</div>
        <h4 class="font-semibold">Full-Stack App</h4>
        <p class="text-sm text-gray-600 mt-2">Complete app with auth &amp; database</p>
      </div>
    </div>
  </div>

  <div class="mt-6">
    <label class="block text-sm font-medium mb-2">Generated Command:</label>
    <div id="project-output" class="bg-gray-900 text-white p-4 rounded-lg font-mono">
      Click a project type above to see the generation command! 🎯
    </div>
  </div>
</div>

<script src="{{ '/assets/js/demo.js' | relative_url }}"></script>

## 🔗 More Demos

### 🔐 Auth UI Kit
Beautiful Tailwind CSS login form with Firebase authentication. Includes email/password and Google OAuth flows.

[→ View Source](https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit) • [→ Try it live](https://costasford.github.io/gpt-fusion/auth-ui-kit/enhanced-index.html)

### 🎯 Unity 3D Demo
Interactive 3D game prototype with movement, items, and basic gameplay mechanics.

[→ View Unity Scripts](https://github.com/costasford/gpt-fusion/tree/main/unity-prototype)

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

## 🤝 Contributing

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
