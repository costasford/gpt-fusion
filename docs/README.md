# Documentation

This project demonstrates small utilities for blending human and AI workflows.

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

If you just want to see everything working, follow these steps and then head
back to the [main README](https://github.com/costasford/gpt-fusion#readme) for more detail:

1. Clone this repository.
2. Run `pytest` from the project root to ensure the utilities work as expected.
3. Serve the login demo with `python -m http.server --directory auth-ui-kit` and
   open `http://localhost:8000` in your browser.
4. Open the `unity-prototype` folder in Unity to explore the 3D example.

## Further reading

See [tutorial.md](tutorial.md) for a walkthrough on loading the sample dataset
and computing averages.

<script src="assets/js/external-links.js"></script>

<script src="assets/js/anchor-links.js"></script>
