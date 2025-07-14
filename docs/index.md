---
layout: default
title: GPT Fusion Playground
image: /auth-ui-screenshot.png
---
<!--
Plan:
1. Show a short demo inside each project card for quick context.
2. Use preformatted blocks for CLI output and an iframe for the Unity preview.
3. Keep markup lightweight so existing CSS continues to work.
4. Link to pip install instructions.
-->

{% include nav.html %}

<div class="hero container">
  <h1>GPT Fusion Playground</h1>
  <p><strong>Practical demos of human-AI collaboration</strong></p>
  <p>
    <a href="https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml"><img src="https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg" alt="CI Status" loading="lazy"></a>
    <a href="https://codecov.io/gh/costasford/gpt-fusion"><img src="https://codecov.io/gh/costasford/gpt-fusion/branch/main/graph/badge.svg" alt="Coverage Status" loading="lazy"></a>
    <a href="https://pypi.org/project/gpt-fusion/"><img src="https://img.shields.io/pypi/dm/gpt-fusion.svg" alt="PyPI Downloads" loading="lazy"></a>
    <a href="https://github.com/costasford/gpt-fusion/blob/main/LICENSE"><img src="https://img.shields.io/github/license/costasford/gpt-fusion" alt="License" loading="lazy"></a>
  </p>
  <p>Use the search bar to jump directly to any topic in the docs.</p>
</div>

<section class="container">
  <h2>Quickstart</h2>
  <p>New to the repository? See the <a href="https://github.com/costasford/gpt-fusion#readme">main README</a> for setup details. You can also install the package with <code>pip install gpt-fusion</code> and run <code>pytest</code> to verify the utilities before exploring the demos.</p>
  <p>These concise examples build on one another. The Python helpers can power the login form or provide data for the Unity prototype. Throughout the documentation you will see how tests and tutorials connect the components.</p>
</section>

<section class="container">
  <h2>Projects</h2>
  <p>More information about each demo lives on the <a href="projects.md">Projects page</a>.</p>
  <div class="projects-grid">
    <div class="project-card">
      <h3>Python utilities</h3>
      <p>Reusable helpers for greetings, math, text processing and simple CSV analysis. The package also ships with a web scraper and optional Twitter and FastAPI extras. <a href="README.md">Read the docs</a>.</p>
      <pre><code>$ python examples/tutorial.py
Values: [1.0, 2.0, 3.0, 4.0, 5.0]
Average: 3.0
Median: 3.0</code></pre>
    </div>
    <div class="project-card">
      <h3>Auth UI Kit</h3>
      <p>Tailwind CSS login form using Firebase. Replace the config in <code>app.js</code> with your project credentials and serve the directory locally to try out email/password and Google sign in flows.</p>
      <p><a href="https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit">View the demo</a></p>
      <img src="/auth-ui-screenshot.png" alt="Auth UI screenshot" loading="lazy">
    </div>
    <div class="project-card">
      <h3>Unity prototype</h3>
      <p>A small 3D demo showcasing simple movement and item pickups. Copy the <code>Assets</code> folder into a new Unity project (tested with Unity&nbsp;2021 or later) and run the scene to explore. <a href="https://github.com/costasford/gpt-fusion/tree/main/unity-prototype">View the repository</a>.</p>
      <div class="preview">
        <iframe src="https://play.unity.com/mg/other/unity-webgl" width="100%" height="180" allowfullscreen loading="lazy" title="Unity preview"></iframe>
      </div>
    </div>
    <div class="project-card">
      <h3>Tutorial</h3>
      <p>Learn how to load sample data and compute averages. <a href="tutorial.md">Follow the tutorial</a>.</p>
      <pre><code>$ python examples/tutorial.py
Values: [1.0, 2.0, 3.0, 4.0, 5.0]
Average: 3.0
Median: 3.0</code></pre>
    </div>
    <div class="project-card">
      <h3>Contribute</h3>
      <p>Want to get involved? Read the <a href="contributing.md">contributing guide</a> to learn how we format code, lint, and run tests. For ongoing care of the project, consult the <a href="sustainability.md">Sustainability Guide</a>.</p>
      <pre><code>$ python scripts/run_checks.py
black..................Passed
flake8.................Passed
eslint.................Passed
37 passed in 0.69s</code></pre>
    </div>
  </div>
</section>

<script src="assets/js/bundle.js"></script>
