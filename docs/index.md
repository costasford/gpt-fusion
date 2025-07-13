---
layout: default
title: GPT Fusion Playground
image: /auth-ui-screenshot.png
---

{% include nav.html %}

<div class="scroller">
  <section>
    <h1>GPT Fusion Playground</h1>
    <p><strong>Practical demos of human-AI collaboration</strong></p>
    <p><a href="https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml"><img src="https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg" alt="CI Status"></a></p>
  </section>

  <section>
    <h2>Quickstart</h2>
    <p>New to the repo? See the <a href="https://github.com/costasford/gpt-fusion#readme">main README</a> for setup details. In short, clone the project, run <code>pytest</code> to verify the Python utilities and then open the demos described below.</p>
    <p>These small examples feed into one another. The Python helpers can power the login form or provide data for the Unity prototype. Throughout the docs you'll see how tests and tutorials tie the components together.</p>
  </section>

  <section>
    <h2>Projects</h2>
    <p>More information about each demo lives on the <a href="projects.md">Projects page</a>.</p>
    <h3>Python utilities</h3>
    <p>Reusable helpers for greetings, math, text processing and simple CSV analysis. The package also ships with a web scraper and optional Twitter and FastAPI extras. <a href="README.md">Read the docs</a>.</p>
    <h3>Auth UI Kit</h3>
    <p>Tailwind CSS login form using Firebase. Replace the config in <code>app.js</code> with your project credentials and serve the directory locally to try out email/password and Google sign in flows. The UI also includes sign-up and password reset dialogs for quick experimentation. <a href="https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit">View the demo</a>.</p>
    <p><img src="/auth-ui-screenshot.png" alt="Auth UI screenshot"></p>
    <h3>Unity prototype</h3>
    <p>A small 3D demo showcasing simple movement and item pickups. Copy the <code>Assets</code> folder into a new Unity project (tested with Unity&nbsp;2021 or later) and run the scene to explore. <a href="https://github.com/costasford/gpt-fusion/tree/main/unity-prototype">Check the repo</a>.</p>
    <h3>Tutorial</h3>
    <p>Learn how to load sample data and compute averages. <a href="tutorial.md">Follow the tutorial</a>.</p>
    <h3>Contribute</h3>
    <p>Want to get involved? Read the <a href="contributing.md">contributing guide</a> to learn how we format code, lint, and run tests. The detailed rules used by Codex are listed on the <a href="guidelines.md">Guidelines page</a>.</p>
    <p>Enjoy fusing ideas with code!</p>
  </section>
</div>

<script src="assets/js/external-links.js"></script>
<script src="assets/js/anchor-links.js"></script>
