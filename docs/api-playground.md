---
layout: default
title: API Playground
---
<!--
Plan:
1. Provide instructions to deploy the FastAPI backend on Render or Heroku.
2. Mention running `uvicorn gpt_fusion.backend:app` locally as well.
3. Highlight the ReDoc docs available at /redoc for interactive testing.
-->

{% include nav.html %}

# API Playground

The project ships with a minimal FastAPI server defined in `gpt_fusion.backend`. You can run it locally or deploy it to a free hosting service for a live demo.

## Local preview

Install the optional backend extras and start the server:

```bash
pip install "gpt-fusion[backend]"
uvicorn gpt_fusion.backend:app
```

Open <http://localhost:8000/redoc> to explore the auto-generated ReDoc docs and call the endpoints.

## Deploying to Render

1. Create a new **Web Service** from your GitHub repo.
2. Set the build command to `pip install "gpt-fusion[backend]"`.
3. Use `uvicorn gpt_fusion.backend:app --host 0.0.0.0 --port $PORT` as the start command.
4. After the service spins up, visit `<service-url>/redoc` to try the API in your browser.

## Deploying to Heroku

1. Create a Python app and add a `Procfile` containing:
   ```
   web: uvicorn gpt_fusion.backend:app --host 0.0.0.0 --port $PORT
   ```
2. Install the backend extras with `pip install "gpt-fusion[backend]"` during the build step.
3. Once deployed, navigate to `<heroku-app-url>/redoc` for the interactive documentation.

<script src="assets/js/bundle.js"></script>
