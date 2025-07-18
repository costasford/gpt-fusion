---
layout: default
title: Overview
---
<!-- Plan: document site search with Algolia DocSearch. -->

# Documentation

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

This project demonstrates a collection of utilities that blend human and AI workflows.

## Project overview

The repository contains a few loosely coupled pieces that can be mixed and
matched:

- **Python utilities** (`gpt_fusion` package) – greeting helpers, math functions
  and a tiny CSV reader used throughout the docs and tests.
- **Auth UI Kit** – a Tailwind‑styled login form built with Firebase. It can be
  wired up to the Python utilities for quick experiments.
- **Unity prototype** – a starter Unity project showcasing basic player control
  scripts. Useful for exploring AI behaviour in a 3D environment.
- **Documentation** – these markdown files, rendered using Jekyll.

See [projects.md](projects.md) for a concise overview of each sample.

Each component is small on its own, but together they highlight different ways
to fuse code written by humans and AI tools.

## Usage examples

### Greeting helper

```python
from gpt_fusion import greet

print(greet("World"))
```

### Math utilities

```python
from gpt_fusion import add_numbers, multiply_numbers

add_numbers(2, 3)       # -> 5
multiply_numbers(4, 2)  # -> 8
```

### Chat history

```python
from gpt_fusion import ChatHistory

history = ChatHistory(messages=[])
history.add_message("Hello")
history.add_message("How are you?")
print(history.last_message())  # -> "How are you?"
history.clear()
print(history.messages)  # -> []
```

## Quickstart

To quickly validate the project, follow these steps and then return to the [main README](https://github.com/costasford/gpt-fusion#readme) for more detail:

1. Clone this repository.
2. Run `pytest` from the project root to ensure the utilities work as expected.
3. Serve the login demo with `python -m http.server --directory auth-ui-kit` and
   open `http://localhost:8000` in your browser. Use email/password, Google sign
   in, or the sign‑up and reset links to test authentication.
4. Open the `unity-prototype` folder in Unity to explore the 3D example.

## Auth UI Kit details

The authentication demo relies on Firebase. Replace the placeholders in
`auth-ui-kit/app.js` with your Firebase project configuration. Start a local
server with `python -m http.server --directory auth-ui-kit` and open the page in
your browser to test email/password and Google sign in flows. The UI includes
sign-up and password reset dialogs so you can experiment without writing any
backend code.

## Unity prototype details

The Unity sample is entirely optional but demonstrates how the Python helpers can
feed data into a game. Create a new Unity project and copy the `Assets` folder
from `unity-prototype`. The included scripts handle basic movement, camera
control, item pickups and pausing the game. Play the scene to explore how these
pieces interact.

### Project API

Run `uvicorn gpt_fusion.backend:app` to start the example FastAPI server. It exposes a `/projects` route that returns the demo list in JSON form.

### Serving the docs locally

The documentation is built with [Jekyll](https://jekyllrb.com/). After
installing the Jekyll gem and dependencies with `bundle install`, run
`jekyll serve` from this folder and open <http://localhost:4000> in your
browser.

### Deploying to GitHub Pages

GitHub Pages serves these files from a global CDN so delivery is fast worldwide.
The docs site is automatically published to the gh-pages branch after each merge to main.
Every pull request also gets its own preview link using `actions/deploy-pages`,
so reviewers can check the rendered HTML before merging.
Assets are compressed during the build using the `jekyll-minifier` plugin to
trim CSS, JavaScript, and HTML for faster load times.
If you need custom caching behaviour, create a `_headers` file in this
`docs/` directory and specify `Cache-Control` rules as required.

## Further reading

See [tutorial.md](tutorial.md) for a walkthrough on loading the sample dataset
and computing averages.

## Analytics

This documentation site uses [Plausible Analytics](https://plausible.io/) to collect
anonymous visit metrics and track uptime. The small snippet in
`_includes/head-custom.html` loads the script with `defer` so page performance
remains unaffected.

## Site search

The documentation is indexed by [Algolia DocSearch](https://docsearch.algolia.com/),
which automatically crawls the Markdown files and provides instant search across
all pages. Replace the placeholder credentials in `_config.yml` with your own
to enable indexing on a fork.

## Contributing

Interested in helping out? Check the [contributing guide](contributing.md) for
instructions on formatting, linting, and running tests before submitting a
pull request.

For ongoing maintenance tips, see the [Sustainability Guide](sustainability.md).

<script src="assets/js/bundle.js"></script>
