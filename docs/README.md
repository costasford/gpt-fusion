# Documentation

This project demonstrates small utilities for blending human and AI workflows.

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
```

