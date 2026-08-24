---
layout: default
title: GPT Fusion - Human-AI Collaboration Toolkit
description: Practical demos of human-AI collaboration with Python utilities, web scraping, FastAPI backend, and more
---

<section class="py-16 sm:py-24 bg-gradient-to-b from-blue-50 to-white dark:from-gray-800 dark:to-gray-900 text-center">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h1 class="text-4xl sm:text-5xl font-extrabold tracking-tight mb-4">
      <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">GPT Fusion</span>
    </h1>
    <p class="text-lg text-gray-600 dark:text-gray-400 max-w-xl mx-auto mb-6">
      A Python toolkit for building AI-assisted applications: text processing, web scraping, a FastAPI backend, and the interactive demos below.
    </p>

    <div class="flex flex-wrap items-center justify-center gap-2 mb-8">
      <a href="https://github.com/costasford/gpt-fusion/actions"><img class="h-5" src="https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
      <a href="https://www.python.org/downloads/"><img class="h-5" src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python"></a>
      <a href="https://github.com/costasford/gpt-fusion/releases"><img class="h-5" src="https://img.shields.io/badge/version-0.4.4-brightgreen.svg" alt="Version"></a>
      <a href="https://github.com/costasford/gpt-fusion/blob/main/LICENSE"><img class="h-5" src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
      <a href="https://github.com/costasford/gpt-fusion/actions"><img class="h-5" src="https://img.shields.io/badge/tests-135%20passed-brightgreen.svg" alt="Tests"></a>
      <a href="https://github.com/costasford/gpt-fusion"><img class="h-5" src="https://img.shields.io/badge/coverage-92%25-brightgreen.svg" alt="Coverage"></a>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-3">
      <code class="bg-gray-900 text-green-400 px-5 py-2.5 rounded-lg font-mono text-sm">pip install gpt-fusion</code>
      <a href="#interactive-demos" class="bg-blue-600 text-white px-5 py-2.5 rounded-lg font-medium hover:bg-blue-700 transition">Try Interactive Demos</a>
      <a href="https://github.com/costasford/gpt-fusion" class="border border-gray-300 dark:border-gray-600 px-5 py-2.5 rounded-lg font-medium hover:bg-gray-50 dark:hover:bg-gray-800 transition">View on GitHub</a>
    </div>
  </div>
</section>

<section class="py-16">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-bold text-center mb-10">🚀 Quick Start</h2>

    <div class="grid md:grid-cols-2 gap-6 mb-6">
      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <h3 class="text-lg font-bold mb-1">📦 Quick Install</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Core text, math &amp; CSV utilities</p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto mb-4"><code>pip install gpt-fusion</code></pre>
        <ul class="text-sm space-y-1">
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> Text processing</li>
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> CSV data analysis</li>
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> Project generators</li>
        </ul>
      </div>

      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <h3 class="text-lg font-bold mb-1">🎯 Full Install</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Everything, including optional extras</p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto mb-4"><code>pip install "gpt-fusion[web,twitter,backend,build]"</code></pre>
        <ul class="text-sm space-y-1">
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> Web scraping (BeautifulSoup)</li>
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> FastAPI backend server</li>
          <li class="flex items-center"><span class="text-green-500 mr-2">✓</span> Twitter integration</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="interactive-demos" class="py-16 bg-gray-50 dark:bg-gray-800/50">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-bold text-center mb-2">✨ Features</h2>
    <p class="text-center text-gray-600 dark:text-gray-400 mb-10">Every feature this package ships, showcased once - the first three run live in your browser, no install required.</p>

    <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-6">
      <h3 class="text-xl font-bold mb-1">🔤 Text Processing</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Smart text utilities with instant results</p>

      <div class="grid md:grid-cols-2 gap-6">
        <div>
          <label for="text-input" class="block text-sm font-medium mb-2">Enter text to process:</label>
          <textarea id="text-input"
                    class="w-full p-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
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

    <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-6">
      <h3 class="text-xl font-bold mb-1">📊 CSV Data Analysis</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Powerful data processing with streaming support</p>

      <div class="grid md:grid-cols-2 gap-6">
        <div>
          <label for="csv-input" class="block text-sm font-medium mb-2">Enter CSV data (comma-separated values):</label>
          <textarea id="csv-input"
                    class="w-full p-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
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

    <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-6">
      <h3 class="text-xl font-bold mb-1">🛠️ Project Generator</h3>
      <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Generate production-ready projects instantly</p>

      <div class="grid md:grid-cols-3 gap-4">
        <button type="button" class="w-full text-left bg-transparent border border-gray-200 dark:border-gray-600 rounded-lg p-4 hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition cursor-pointer" onclick="showProjectCode('csv')">
          <div class="text-center">
            <div class="text-3xl mb-2">📊</div>
            <h4 class="font-semibold">CSV Analytics App</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2">FastAPI backend with data visualization</p>
          </div>
        </button>

        <button type="button" class="w-full text-left bg-transparent border border-gray-200 dark:border-gray-600 rounded-lg p-4 hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition cursor-pointer" onclick="showProjectCode('ui')">
          <div class="text-center">
            <div class="text-3xl mb-2">🎨</div>
            <h4 class="font-semibold">Tailwind UI Kit</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2">Modern responsive web interface</p>
          </div>
        </button>

        <button type="button" class="w-full text-left bg-transparent border border-gray-200 dark:border-gray-600 rounded-lg p-4 hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition cursor-pointer" onclick="showProjectCode('fullstack')">
          <div class="text-center">
            <div class="text-3xl mb-2">🚀</div>
            <h4 class="font-semibold">Full-Stack App</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2">Complete app with auth &amp; database</p>
          </div>
        </button>
      </div>

      <div class="mt-6">
        <label class="block text-sm font-medium mb-2">Generated Command:</label>
        <div id="project-output" class="bg-gray-900 text-white p-4 rounded-lg font-mono">
          Click a project type above to see the generation command! 🎯
        </div>
      </div>
    </div>

    <script src="{{ '/assets/js/demo.js' | relative_url }}"></script>

    <div class="grid md:grid-cols-3 gap-6 mb-6">
      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <div class="flex items-center mb-3">
          <div class="feature-icon w-10 h-10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
            <span class="text-white text-xl">🌐</span>
          </div>
          <h3 class="text-lg font-bold">Web Scraping</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Simple scraping utilities with BeautifulSoup, blocked from hitting private/internal addresses. Install: <code class="text-xs">pip install "gpt-fusion[web]"</code></p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto"><code>gpt_fusion.scrape("https://example.com", "p")
# ['This domain is for use in documentation
#   examples without needing permission. Avoid
#   use in operations.', 'Learn more']</code></pre>
      </div>

      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <div class="flex items-center mb-3">
          <div class="feature-icon w-10 h-10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
            <span class="text-white text-xl">🚀</span>
          </div>
          <h3 class="text-lg font-bold">FastAPI Backend</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Ready-to-deploy API server with auto-generated docs. Install: <code class="text-xs">pip install "gpt-fusion[backend]"</code></p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto"><code>GET /greet/Alice

{"message": "Hello, Alice! Welcome
  to gpt-fusion."}</code></pre>
      </div>

      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <div class="flex items-center mb-3">
          <div class="feature-icon w-10 h-10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
            <span class="text-white text-xl">🐦</span>
          </div>
          <h3 class="text-lg font-bold">Twitter Integration</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">Twitter bot utilities with OAuth support, reading credentials straight from the environment. Install: <code class="text-xs">pip install "gpt-fusion[twitter]"</code></p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-sm overflow-x-auto"><code>bot.post_tweet("x" * 300)
# ValueError: Tweet exceeds 280 characters</code></pre>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-6">
      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 text-center">
        <div class="text-4xl mb-2">🔐</div>
        <h3 class="font-bold text-lg mb-1">Auth UI Kit</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Tailwind CSS login form with Firebase auth: email/password and Google OAuth flows.</p>
        <div class="space-y-1 text-sm text-left mb-4">
          <div class="flex items-center"><span class="text-green-500 mr-2">✓</span> Accessible modal focus management</div>
          <div class="flex items-center"><span class="text-green-500 mr-2">✓</span> Field-level validation &amp; error messages</div>
          <div class="flex items-center"><span class="text-green-500 mr-2">✓</span> Hardened CSP, no inline scripts</div>
        </div>
        <div class="flex gap-2">
          <a href="https://costasford.github.io/gpt-fusion/auth-ui-kit/enhanced-index.html" class="flex-1 bg-blue-600 text-white text-center py-2 rounded-lg hover:bg-blue-700 transition">Try it Live</a>
          <a href="https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit" class="flex-1 bg-gray-600 text-white text-center py-2 rounded-lg hover:bg-gray-700 transition">Source</a>
        </div>
      </div>

      <div class="demo-card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 text-left">
        <div class="text-center">
          <div class="text-4xl mb-2">🎯</div>
          <h3 class="font-bold text-lg mb-1">Unity 3D Demo</h3>
        </div>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">C# gameplay systems (movement, items, achievements). Script-only reference - no packaged scenes to play yet, so here's the real object-pooling code instead of a screenshot:</p>
        <pre class="bg-gray-900 text-gray-100 p-3 rounded-lg text-xs overflow-x-auto mb-4"><code>Queue&lt;GameObject&gt; queue = _poolDictionary[tag];
if (queue.Count == 0)
{
    // Every object for this tag is still active/in-flight.
    // Fail loudly instead of corrupting an active object.
    Debug.LogWarning($"Pool '{tag}' exhausted - all objects in use.");
    return null;
}

GameObject objectToSpawn = queue.Dequeue();
objectToSpawn.SetActive(true);
objectToSpawn.transform.position = position;</code></pre>
        <a href="https://github.com/costasford/gpt-fusion/tree/main/unity-prototype" class="block bg-purple-600 text-white text-center py-2 rounded-lg hover:bg-purple-700 transition">View All Scripts</a>
      </div>
    </div>
  </div>
</section>

<section class="py-16">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

<div class="prose dark:prose-invert max-w-none" markdown="1">

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

</div>

  </div>
</section>

<section class="py-16 bg-gray-50 dark:bg-gray-800/50">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

<div class="prose dark:prose-invert max-w-none" markdown="1">

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

</div>

  </div>
</section>
