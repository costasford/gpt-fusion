# 🚀 GPT Fusion

**The Python toolkit that makes AI integration effortless**

GPT Fusion is a comprehensive Python library designed to streamline AI-assisted application development. It ships a real LLM client for OpenAI-compatible chat completions (OpenAI, Groq, a local Ollama server, anything speaking the same API), plus the text processing, web scraping, and interactive demo tooling it's had all along.

## 🎯 Why Choose GPT Fusion?

- **🤖 Real LLM Client**: OpenAI-compatible chat completions, works with OpenAI, Groq, local Ollama, or anything else on that API shape
- **⚡ Zero Setup Friction**: Install and start coding in seconds
- **🛡️ Production Ready**: Built-in security, performance optimizations, and error handling
- **🔌 Modular Design**: Use only what you need with optional dependencies
- **📚 Rich Examples**: Complete demo projects including Unity 3D games and auth systems
- **🧪 Battle Tested**: 80+ tests with 89%+ coverage and CI/CD pipeline

[![CI](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.3.0-brightgreen.svg)](https://github.com/costasford/gpt-fusion/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/costasford/gpt-fusion/blob/main/LICENSE)
[![Tests](https://img.shields.io/badge/tests-80%2B%20passed-brightgreen.svg)](https://github.com/costasford/gpt-fusion/actions)
[![Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen.svg)](https://github.com/costasford/gpt-fusion)

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

# 🚀 Generate small, real starter projects in seconds
print(gpt_fusion.create_csv_app('my-analytics-dashboard', with_api=True))
print(gpt_fusion.create_tailwind_ui('my-modern-webapp', dark_mode=True))
```

**Output:**
```
Words: 9
Reversed: dog lazy the over jumps fox brown quick The
Is palindrome: True
Average: 1247.83
Found 30 headlines
my-analytics-dashboard
my-modern-webapp
```

### 🤖 LLM Integration

```bash
pip install "gpt-fusion[llm]"
export OPENAI_API_KEY=sk-...
```

```python
from gpt_fusion import ask, LLMClient

# One-liner for a single question
reply = ask("Explain recursion in one sentence.")

# Or reuse a client across a multi-turn conversation
client = LLMClient(model="gpt-4o-mini")
reply = client.chat([
    {"role": "system", "content": "Answer in a single sentence."},
    {"role": "user", "content": "What's a closure?"},
])
client.close()
```

Points `base_url` anywhere that speaks the OpenAI chat completions API without changing your code. Verified working against [Groq](https://console.groq.com/)'s free tier:

```python
client = LLMClient(
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.1-8b-instant",
    api_key=os.environ["GROQ_API_KEY"],
)
```

The same pattern works for a local Ollama server (`base_url="http://localhost:11434/v1"`) or any other OpenAI-compatible endpoint.

### 🎛️ Optional Feature Sets

Choose the components you need:

```bash
# 🤖 LLM chat completions client
pip install "gpt-fusion[llm]"

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

### 🤖 LLM Client
Chat completions for OpenAI-compatible APIs - real requests, real error handling, no vendor lock-in.
```python
# Install: pip install "gpt-fusion[llm]"
from gpt_fusion import ask, LLMClient

ask("Summarize the plot of Hamlet in two sentences.")

client = LLMClient()  # reads OPENAI_API_KEY from the environment
client.chat("Hello!", temperature=0.2)
```
Raises `ConfigurationError` if no API key is available, and `APIError` if the request fails or the response comes back in an unexpected shape - both importable from `gpt_fusion`.

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
**Small, real starter kits** - not empty stubs, each command below actually
runs and produces working code:

```bash
# 📊 CSV demo script, plus a FastAPI wrapper over the same data
gpt-fusion create_csv_app my-analytics --with-api
# -> my-analytics/{app.py, numbers.csv, api.py}

# 🎨 Tailwind + Firebase auth UI (--dark-mode for the glass-effect variant)
gpt-fusion create_tailwind_ui my-webapp --dark-mode
# -> my-webapp/{index.html, app.js}

# 🚀 Both combined: a frontend/ + backend/ FastAPI app
gpt-fusion create_fullstack_app my-saas --auth --database
# -> my-saas/frontend/{index.html, app.js}
# -> my-saas/backend/{app.py, numbers.csv}
```

`--auth` adds a minimal HMAC-signed-token login flow (`POST /login` with
`demo`/`demo123`, then a bearer token on every other route) and
`--database` swaps reading the CSV live for a small SQLite-backed store -
both demo-grade and clearly commented as such in the generated code, not
production-hardened. Neither flag adds a new dependency beyond what
`gpt-fusion[backend]` already needs.

(`python -m gpt_fusion <command> ...` works the same way as `gpt-fusion
<command> ...` if you'd rather not rely on the installed console script.)

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
| GET | `/` | Welcome message | `{"message": "gpt-fusion backend"}` |
| GET | `/greet/{name}` | Personalized greeting | `/greet/Alice` → `{"message": "Hello, Alice! Welcome to gpt-fusion."}` |
| GET | `/profile/{uid}` | Basic user profile | `{"uid": "42", "display_name": "User 42"}` |
| GET | `/projects` | Available demo projects | List with GitHub links |
| GET | `/health` | Liveness/version check | `{"status": "healthy", "version": "0.3.0"}` |

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
# Run the full test suite (80+ tests)
pytest

# Check coverage (currently 89%+)
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
├── llm.py          # LLM chat completions client (optional)
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
