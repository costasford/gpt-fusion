# 🚀 GPT Fusion

**The Python toolkit that makes AI integration effortless**

GPT Fusion is a comprehensive Python library designed to streamline AI-assisted application development. Whether you're building web scrapers, data analysis tools, or interactive demos, GPT Fusion provides the essential utilities and patterns to get you up and running quickly.

## 🎯 Why Choose GPT Fusion?

- **⚡ Zero Setup Friction**: Install and start coding in seconds
- **🛡️ Production Ready**: Built-in security, performance optimizations, and error handling
- **🔌 Modular Design**: Use only what you need with optional dependencies
- **📚 Rich Examples**: Complete demo projects including Unity 3D games and auth systems
- **🧪 Battle Tested**: 63+ tests with 95% coverage and CI/CD pipeline

[![CI](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/costasford/gpt-fusion/branch/main/graph/badge.svg)](https://codecov.io/gh/costasford/gpt-fusion)
[![PyPI Downloads](https://img.shields.io/pypi/dm/gpt-fusion.svg)](https://pypi.org/project/gpt-fusion/)
[![License](https://img.shields.io/github/license/costasford/gpt-fusion)](https://github.com/costasford/gpt-fusion/blob/main/LICENSE)

📦 **[Install from PyPI](https://pypi.org/project/gpt-fusion/)** • 🌐 **[Live Documentation](https://costasford.github.io/gpt-fusion/)** • 🎮 **[Try Live Demo](https://costasford.github.io/gpt-fusion/demo.html)**

## 🚀 Quick Start

### 📦 Installation

**Quick Install:**
```bash
pip install gpt-fusion
```

**Full Installation (all features):**
```bash
pip install "gpt-fusion[all]"
```

**Python Version Support:**
- ✅ Python 3.10+
- ✅ Python 3.11 (Recommended)
- ✅ Python 3.12

### ⚡ Quick Start Example

```python
import gpt_fusion

# 🔤 Smart text processing
text = "The quick brown fox jumps over the lazy dog"
print(f"Words: {gpt_fusion.word_count(text)}")
print(f"Reversed: {gpt_fusion.reverse_words(text)}")
print(f"Is palindrome: {gpt_fusion.is_palindrome('racecar')}")

# 📊 Powerful data analysis
data = gpt_fusion.load_numbers_from_csv('data/sales.csv')
print(f"Average: {gpt_fusion.average_from_csv('data/sales.csv', use_streaming=True)}")

# 🌐 Easy web scraping (with built-in security)
headlines = gpt_fusion.scrape("https://news.ycombinator.com", "a.storylink")
print(f"Found {len(headlines)} headlines")

# 🚀 Generate complete projects in seconds
gpt_fusion.create_csv_app('my-analytics-dashboard')
gpt_fusion.create_tailwind_ui('my-modern-webapp')
```

**Output:**
```
Words: 9
Reversed: dog lazy the over jumps fox brown quick The
Is palindrome: True
Average: 1247.83
Found 30 headlines
✅ Created my-analytics-dashboard/ with FastAPI backend
✅ Created my-modern-webapp/ with Tailwind CSS
```

### 🎛️ Optional Feature Sets

Choose the components you need:

```bash
# 🌐 Web scraping & HTTP clients
pip install "gpt-fusion[web]"

# 🚀 FastAPI backend with auto-docs
pip install "gpt-fusion[backend]"

# 🐦 Social media integration
pip install "gpt-fusion[twitter]"

# 🛠️ Asset optimization & building
pip install "gpt-fusion[build]"

# 🧪 Development tools
pip install "gpt-fusion[dev]"

# 🎯 Everything included
pip install "gpt-fusion[all]"
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
from gpt_fusion import TwitterBot

bot = TwitterBot(api_key, api_secret)
bot.tweet("Hello from GPT Fusion!")
```

## 🎮 Interactive Demos

### 🔐 Enhanced Auth UI Kit
**Modern, secure authentication system** with comprehensive security features:
- 🛡️ Rate limiting & input sanitization
- 🎨 Beautiful glass-effect UI with dark mode
- ♿ WCAG 2.1 AA accessibility compliance
- 🔍 Real-time password strength validation
- 📱 Fully responsive design

**Try it:** [Enhanced Demo](https://github.com/costasford/gpt-fusion/blob/main/auth-ui-kit/enhanced-index.html) | [Basic Version](https://github.com/costasford/gpt-fusion/blob/main/auth-ui-kit/index.html) | [Test Suite](https://github.com/costasford/gpt-fusion/blob/main/auth-ui-kit/tests.html)

### 🎯 Unity 3D Game Engine Integration
**Complete game architecture** demonstrating modern Unity patterns:
- ⚡ Event-driven systems (no Update() polling)
- 🏊 Object pooling for performance
- 🎛️ Scriptable Object configuration
- 🖥️ Modern UI with smooth animations
- 🏗️ Interface-based architecture

**Explore:** [Modern Scripts](https://github.com/costasford/gpt-fusion/tree/main/unity-prototype/Assets/Scripts) | [Setup Guide](https://github.com/costasford/gpt-fusion/blob/main/unity-prototype/README.md)

### 📊 Data Analysis Playground
**High-performance CSV processing** with streaming support for large datasets:
- ⚡ Memory-efficient streaming for large files
- 📈 Statistical analysis (mean, median, percentiles)
- 🔒 Built-in security (path traversal protection)
- 📋 Sample datasets included

```bash
$ python examples/tutorial.py
🔍 Loading data/numbers.csv...
📊 Values: [1.0, 2.0, 3.0, 4.0, 5.0]
📈 Average: 3.0 | Median: 3.0
⚡ Processing 1M rows in 2.3s (streaming mode)
✅ Analysis complete!
```

**Try:** [Tutorial Script](https://github.com/costasford/gpt-fusion/blob/main/examples/tutorial.py) | [Sample Data](https://github.com/costasford/gpt-fusion/tree/main/data)

### 🛠️ Project Generator
**Instant project scaffolding** with production-ready templates:

```bash
# 📊 Data analysis dashboard with FastAPI
gpt_fusion create_csv_app my-analytics --with-api

# 🎨 Modern web UI with Tailwind CSS
gpt_fusion create_tailwind_ui my-webapp --dark-mode

# 🚀 Full-stack app with auth
gpt_fusion create_fullstack_app my-saas --auth --database
```

**Generated projects include:**
- 📝 Complete documentation
- 🧪 Pre-configured testing
- 🚀 Deployment scripts
- 🔧 Development tooling

## 🚀 API & Deployment

### 💻 Local Development

**Start the development server:**
```bash
pip install "gpt-fusion[backend]"
uvicorn gpt_fusion.backend:app --reload --port 8000
```

**Interactive Features:**
- 📝 **Swagger UI**: `http://localhost:8000/docs`
- 🔧 **ReDoc**: `http://localhost:8000/redoc`
- 📊 **Health Check**: `http://localhost:8000/health`

### 🌐 API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | Welcome message | `{"message": "GPT Fusion API v0.2.0"}` |
| GET | `/greet/{name}` | Personalized greeting | `/greet/Alice` → `"Hello, Alice!"` |
| GET | `/projects` | Available demo projects | List with GitHub links |
| GET | `/health` | System health status | `{"status": "healthy", "version": "0.2.0"}` |

### 🌐 Cloud Deployment

**🚀 Deploy to Render (Recommended)**
```bash
# render.yaml is included in the repo
git push origin main  # Auto-deploys via GitHub integration
```

**🟣 Deploy to Heroku**
```bash
# Procfile is included
heroku create my-gpt-fusion-app
git push heroku main
```

**🐳 Deploy with Docker**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install "gpt-fusion[backend]"
EXPOSE 8000
CMD ["uvicorn", "gpt_fusion.backend:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🛠️ Troubleshooting

### Common Issues

**❌ Installation fails on Python 3.9**
```bash
# GPT Fusion requires Python 3.10+
pyenv install 3.11.0
pyenv local 3.11.0
pip install gpt-fusion
```

**❌ Import errors with optional dependencies**
```bash
# Install specific feature sets
pip install "gpt-fusion[web]"  # for scraping
pip install "gpt-fusion[backend]"  # for FastAPI
```

**❌ CSV files not loading**
```python
# Ensure CSV has 'value' column header
import gpt_fusion
data = gpt_fusion.load_numbers_from_csv('data.csv', use_streaming=True)
```

**🔍 Still having issues?**
- 📞 [GitHub Issues](https://github.com/costasford/gpt-fusion/issues)
- 📚 [Documentation](https://costasford.github.io/gpt-fusion/)

## 🤝 Contributing

### 🛠️ Development Setup
```bash
git clone https://github.com/costasford/gpt-fusion.git
cd gpt-fusion
pip install "gpt-fusion[dev]"  # Installs dev dependencies
pip install -e .  # Editable install
pre-commit install  # Git hooks for quality
```

### 🧪 Testing & Quality
```bash
# Run the full test suite (63 tests)
pytest

# Check coverage (currently 95%+)
pytest --cov=src/gpt_fusion --cov-report=html

# Code formatting and linting
black .
flake8 .

# Run all quality checks
python scripts/run_checks.py
```

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
📖 [GitHub Repository](https://github.com/costasford/gpt-fusion) • 📦 [PyPI Package](https://pypi.org/project/gpt-fusion/) • 🐛 [Report Issues](https://github.com/costasford/gpt-fusion/issues) • 📄 [MIT License](https://github.com/costasford/gpt-fusion/blob/main/LICENSE)

---

*GPT Fusion - Practical demos of human-AI collaboration. Built with ❤️ and Python.*
