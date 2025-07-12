# Tutorial

This short guide shows how to load a sample dataset and compute its average
value using ``gpt_fusion`` utilities.

```python
from pathlib import Path
from gpt_fusion import load_numbers_from_csv, average_from_csv, median_from_csv

csv_path = Path("../data/numbers.csv")
values = load_numbers_from_csv(csv_path)
print(f"Loaded values: {values}")
print(f"Average: {average_from_csv(csv_path)}")
print(f"Median: {median_from_csv(csv_path)}")
```

### Web scraping

Use the ``scrape`` helper to pull text from any page using a CSS selector:

```python
from gpt_fusion import scrape

titles = scrape("https://example.com", "h1")
print(titles)
```
