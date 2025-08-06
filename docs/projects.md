---
layout: default
title: Projects
---

<!--
Plan:
1. Provide inline demo snippets for the Python utilities and tutorial sections.
2. Keep the existing iframes for other projects.
-->

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

# Projects

This repository hosts several small demos that showcase different aspects of human‑AI collaboration. This page summarises each component and links to further details. The optional API server exposes these entries at the `/projects` route so you can fetch them programmatically. To simplify the experience for newcomers attending events such as Codemotion, the sections below embed live previews or short recordings wherever possible.

## Python utilities

The `gpt_fusion` package bundles greeting helpers, math functions, text utilities and a small CSV reader. It also exposes a web scraper, a Twitter bot and an optional FastAPI backend. See the [tutorial](tutorial.html) for an overview.

```bash
$ python examples/tutorial.py
Values: [1.0, 2.0, 3.0, 4.0, 5.0]
Average: 3.0
Median: 3.0
```

## Auth UI Kit

A Tailwind‑styled login form powered by Firebase. Update `auth-ui-kit/app.js` with your project credentials and serve the folder locally to experiment with email/password and Google sign in flows.

<div class="preview">
  <iframe src="https://codesandbox.io/embed/github/costasford/gpt-fusion/tree/main/auth-ui-kit?fontsize=14&hidenavigation=1"
          style="width:100%; height:500px; border:0; border-radius:4px; overflow:hidden;"
          title="Auth UI live preview"
          allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
          sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts">
  </iframe>
</div>

## Unity prototype

A basic 3D scene demonstrating player movement, item pickups and simple enemy AI. Copy the `Assets` directory from `unity-prototype/` into a new Unity project (Unity 2021 or later). The build can be exported for WebGL and placed under `docs/unity-demo`.

<div class="preview">
  <iframe src="unity-demo/" width="640" height="360" allowfullscreen loading="lazy" title="Unity WebGL demo"></iframe>
</div>

## Top Viewer Games

Live view of the most popular Twitch channels and games. Configure your Twitch
client credentials and run `viewer.py` from the `top-viewer-games` folder to see
current statistics.

```text
Top Games:
Fortnite - 33214
Just Chatting - 22190

Top Streams:
Streamer123 playing Fortnite with 20000 viewers
StreamerABC playing Just Chatting with 15000 viewers
```
## API Playground

Host the FastAPI demo on Render or Heroku and open `/api/redoc` to experiment with the endpoints. See [api-playground.md](api-playground.md) for setup steps.


## Tutorial

Walk through loading the sample dataset and computing averages in [tutorial.md](tutorial.md).

```bash
$ python examples/tutorial.py
Values: [1.0, 2.0, 3.0, 4.0, 5.0]
Average: 3.0
Median: 3.0
```

For development instructions see the [Guidelines](guidelines.md).

<script src="assets/js/bundle.js"></script>
