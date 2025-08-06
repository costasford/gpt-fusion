---
layout: default
title: Tutorial
---
<!-- Plan: mention PyPI install alongside editable install -->

# Tutorial

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

This guide walks through how to install the project, load the bundled
dataset and call a few helper functions from ``gpt_fusion``. It expands
on the examples in the main README with step‑by‑step instructions.

## Installation

The easiest way to get started is to install from PyPI:

```bash
pip install gpt-fusion
```

For development or to access the latest features, clone and install locally:

```bash
git clone https://github.com/costasford/gpt-fusion.git
cd gpt-fusion
pip install -e .
```

To explore the optional API server, web scraper and Twitter helpers install the extras:

```bash
pip install "gpt-fusion[backend,twitter,web]"
```

## Loading sample data

The ``data/`` folder contains a small ``numbers.csv`` file with a single
``value`` column:

```
value
1
2
3
4
5
```

We'll use this file in the examples below to compute averages and medians.

```python
from pathlib import Path
from gpt_fusion import load_numbers_from_csv, average_from_csv, median_from_csv

csv_path = Path("../data/numbers.csv")
values = load_numbers_from_csv(csv_path)
print(f"Loaded values: {values}")
print(f"Average: {average_from_csv(csv_path)}")
print(f"Median: {median_from_csv(csv_path)}")
```

Running this snippet prints the numbers from the file along with their
average and median. Any rows that can't be converted to ``float`` are
ignored, so you can safely extend ``numbers.csv`` with your own values.

### Custom datasets

The helpers accept any CSV that includes a ``value`` column. Missing or
malformed rows are skipped:

```python
custom = Path("my_values.csv")
custom.write_text("value\n10\nnot-a-number\n20\n", encoding="utf-8")
print(average_from_csv(custom))
```

### Web scraping

Use the ``scrape`` helper to pull text from any page using a CSS selector:

```python
from gpt_fusion import scrape

titles = scrape("https://example.com", "h1")
print(titles)
```

### Tracking conversation history

The ``ChatHistory`` container stores a list of messages. It can be handy
when experimenting interactively:

```python
from gpt_fusion import ChatHistory, greet

history = ChatHistory(messages=[])
history.add_message(greet("Fusion"))
history.add_message("How can I help?")
print(history.messages)
```

### Live API demo

Type a name and call the `/greet` endpoint without leaving the page:

<div id="playground">
  <input id="name-input" type="text" value="Fusion" aria-label="Name">
  <button id="greet-btn">Greet</button>
  <pre id="greet-output"></pre>
</div>

<script src="assets/js/bundle.js"></script>
