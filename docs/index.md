---
layout: default
title: GPT Fusion Playground
image: /auth-ui-screenshot.png
---

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

# GPT Fusion Playground

**Practical demos of human-AI collaboration**

[![CI Status](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml/badge.svg)](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml)

## Project Health

- [CI workflow](https://github.com/costasford/gpt-fusion/actions/workflows/ci.yml)
- [Open issues](https://github.com/costasford/gpt-fusion/issues)

Welcome to **GPT Fusion**, a small playground for blending human creativity with AI tooling. Explore the projects below to see what we're experimenting with.

## Quickstart

New to the repo? See the [main README](https://github.com/costasford/gpt-fusion#readme) for setup details. In
short, clone the project, run `pytest` to verify the Python utilities and then
open the demos described below.

These small examples feed into one another. The Python helpers can power the
login form or provide data for the Unity prototype. Throughout the docs you'll
see how tests and tutorials tie the components together.

## Projects

More information about each demo lives on the [Projects page](projects.md).

### Python utilities

Reusable helpers for greetings, math, text processing and simple CSV analysis. The package also ships with a web scraper and optional Twitter and FastAPI extras. [Read the docs](README.md).

### Auth UI Kit

Tailwind CSS login form using Firebase. Replace the config in `app.js` with your
project credentials and serve the directory locally to try out email/password
and Google sign in flows. The UI also includes sign-up and password reset
dialogs for quick experimentation.
[View the demo](https://github.com/costasford/gpt-fusion/tree/main/auth-ui-kit).

![Auth UI screenshot](/auth-ui-screenshot.png)

### Unity prototype

A small 3D demo showcasing simple movement and item pickups. Copy the `Assets`
folder into a new Unity project (tested with Unity&nbsp;2021 or later) and run the
scene to explore. [Check the repo](https://github.com/costasford/gpt-fusion/tree/main/unity-prototype).


### Tutorial

Learn how to load sample data and compute averages. [Follow the tutorial](tutorial.md).

### Contribute

Want to get involved? Read the [contributing guide](contributing.md) to learn
how we format code, lint, and run tests. The detailed rules used by Codex are
listed on the [Guidelines](guidelines.md) page.

Enjoy fusing ideas with code!

<script src="assets/js/external-links.js"></script>
<script src="assets/js/anchor-links.js"></script>
<script src="assets/js/toc.js"></script>
