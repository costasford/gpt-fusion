## 🧠 Purpose

This document guides AI agents (e.g. Codex, ChatGPT, OpenAI Agents SDK) on how to interpret and contribute to `gpt-fusion`. It covers project structure, coding style, tests, CI, collaboration patterns, and recommended workflows.

---

## 1. Project Overview

* **Repo name**: `gpt-fusion`
* **Goal**: A playground for human–AI collaboration—reusable modules, simple CLI/API/demos, and multi-agent orchestration.

### Layout:

```
src/gpt_fusion/
  ├─ core.py       # greeting helper
  ├─ utils.py      # math, chat-history container
  ├─ analysis.py   # CSV utilities
tests/             # pytest suite
data/              # sample numbers.csv
docs/              # Jekyll-powered tutorials & demos
```

---

## 2. Agent Roles & Responsibilities

### Human vs AI

* **Core Library**: small, deterministic, standard-library–only (unless extras are installed)
* **backend & twitter extras**: require FastAPI and Tweepy—AI can scaffold endpoints or bot logic.
* **Sample apps** (`auth-ui-kit/`, `twitter_bot.py`, `top-viewer-games/`, `unity-prototype/`): AI may generate code but humans must insert keys/configs.

### Agent Objectives

* Analyze CSV via `analysis.py`
* Update greeting logic in `core.py`
* Extend math/chat tools in `utils.py`
* Scaffold or improve demo apps under human guidance

---

## 3. Coding Conventions

* Use **Python 3.10+**
* Adhere to **PEP8 formatting**
* Comments required where logic is non-obvious
* Use **pre-commit** for linting: `pre-commit run --all-files`
* Run **pytest** for any code change

---

## 4. Testing

* Always include unit tests for new code in `tests/`
* Tests use **pytest**
* Code coverage should improve or stay stable
* Agent must:

  1. Create focused test cases (assert input/output)
  2. Pass them with CI

---

## 5. CI & Hooks

* **pre-commit** auto-runs formatting/linting
* **GitHub Actions** runs on PRs:

  * Format checks
  * pytest suite
* Agent must fail fast and tell user when tests or format checks fail.

---

## 6. Multi-Agent Patterns

* Use **"agent-as-tool"** orchestration (OpenAI Agents SDK pattern) ([Agents.md Guide for OpenAI Codex][1], [OpenAI Cookbook][2], [vibecoding.com][3])

  * Example: one orchestrator calls core/math/CSV agents.
* Ensure **state** (chat history) is passed through `utils.ChatHistory`.
* Favor modular agents: e.g., a greeting enhancer, CSV summarizer, math calculator.

---

## 7. Tool Integration

* Register tools with clear JSON output patterns
* Provide examples and error handling
* Example:

  ```python
  def summarize_csv(path: str) -> dict:
      """Reads CSV and returns { 'rows': int, 'cols': int, 'summary': {...}}"""
  ```
* Tests ensure stability.

---

## 8. Human–AI Collaboration Workflow

Derived from SmythOS and DragonScale best practices:

* Assign repetitive or data-heavy tasks to AI (formatting, basic utils) ([SmythOS][4])
* Keep humans in loop for review, architecture, config, secrets
* Maintain transparency: AI-generated code should include docstrings/warnings
* Provide feedback loops: update prompts or behavior based on test failure or review ([Agents.md Guide for OpenAI Codex][1])

---

## 9. Orchestration Example

```python
from openai_agents_sdk import AgentManager
from gpt_fusion import core, utils, analysis

def main_agent(input):
    greeting = core.greet(input.user)
    math_result = utils.calculate(input.math_expr)
    csv_summary = analysis.summarize_csv("data/numbers.csv")
    return {
      "greeting": greeting,
      "math": math_result,
      "csv": csv_summary
    }
```

Agents should orchestrate using this transparent structure.

---

## 10. Contribution & PR Guidelines

* Keep PRs concise—single change per PR
* Include test updates with feature changes
* PR title must start with `feat:`, `fix:`, or `docs:`
* AI-generated code flagged with `# GENERATED` comment and reviewed before merge

---

## 11. Troubleshooting & FAQs

* **Tests failing?** Rerun pytest locally and fix errors.
* **Formatting issues?** Run `pre-commit run --all-files` and commit before PR.
* **Secrets missing?** Skip Twitter or backend demos if no credentials configured.
* **Agent is hallucinating?** Add guardrails: fallback to error or human review.

---

## 12. Agent Configuration

To tune Codex or OpenAI agents, reference:

* File structure & nested agents rules ([Agents.md Guide for OpenAI Codex][1], [vibecoding.com][3], [OpenAI][5])
* Codex configuration hierarchy: root-level → dir-level overrides
* Keep doc concise; add nested `AGENTS.md` in subfolders if specialized behavior needed

---

## Summary Table

| Area            | Agent Instructions                                       |
| --------------- | -------------------------------------------------------- |
| Structure       | Use folder comments to detect agents in `src/`, `tests/` |
| Style           | PEP8, docstrings, pre-commit enforced                    |
| Testing         | Use pytest, new tests for new features                   |
| Orchestration   | Agent-as-tool pattern, modular agents                    |
| Human oversight | Always flag AI-generated code, human reviews required    |
| CI              | Ensure code passes lint & tests in GitHub Actions        |
