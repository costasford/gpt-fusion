---
layout: default
title: Tutorial
---

# Tutorial

{% include nav.html %}

<div id="toc">
  <p class="toc-title">Quick links</p>
</div>

This guide walks through installing the project, loading the bundled
dataset and calling a few helper functions from ``gpt_fusion``. It expands
on the examples in the main README with step‑by‑step instructions.

## Setup

Ensure Python&nbsp;3.8 or newer is installed and clone the repository:

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

<script src="assets/js/external-links.js"></script>
<script src="assets/js/anchor-links.js"></script>
<script src="assets/js/toc.js"></script>
