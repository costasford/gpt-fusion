# GPT Fusion – AGENTS.md

## 1 · Purpose

This file tells any AI coding agent (e.g. OpenAI Codex / GPT‑Fusion) **how to contribute to this repository** without breaking our conventions or CI.
Human teammates should skim it too—think of it as the *AI contributor handbook*.

---

## 2 · Project map

| Path               | What lives here                | Notes                            |
| ------------------ | ------------------------------ | -------------------------------- |
| `src/gpt_fusion/`  | Core Python package            | Pure‑Python 3.11+ utilities      |
| `auth-ui-kit/`     | Tailwind + Firebase login demo | Runs in any static web server    |
| `unity-prototype/` | Unity 2021 LTS sample scene    | Requires Unity‑Hub project setup |
| `docs/`            | Jekyll site for tutorials      | `bundle exec jekyll serve`       |
| `tests/`           | `pytest` suite                 | All code changes **must** pass   |
| `scripts/`         | Dev automation helpers         | See `scripts/run_checks.py`      |

---

## 3 · Language & style conventions

### 3.1 Python

* **Version:** 3.11 or newer
* **Formatter:** `black` (line length = 88)
* **Lint:** `flake8` (config in `.flake8`)
* **Typing:** `mypy` strict mode on new files
* **Docstrings:** NumPy style

### 3.2 JavaScript / TypeScript

* **Runtime:** Node 20 LTS
* **Style:** `eslint` with rules in `eslint.config.js`
* **Frameworks:** ESM, React functional comps only
* **Formatting:** `prettier` (default width 80)

### 3.3 C# (Unity)

* **Unity:** 2021.3 LTS or higher
* **API compatibility:** `.NET Standard 2.1`
* **Naming:** PascalCase for classes, camelCase for fields
* **Testing:** Unity Test Runner

---

## 4 · Build, test & CI

| Task        | Command                      |
| ----------- | ---------------------------- |
| Format code | `pre-commit run --all-files` |
| Unit tests  | `pytest`                     |
| Type check  | `mypy src`                   |
| JS tests    | `npm test --workspaces`      |
| Docs build  | `scripts/build_docs.sh`      |

CI is mirrored locally by `python scripts/run_checks.py`. Agents **must** call this script and ensure all checks pass before proposing a PR.

---

## 5 · Agent workflow

1. **Analyse context** – read this file plus any nearer `AGENTS.md`.
2. **Ask clarifying questions** if uncertainty > 0.1.
3. **Plan**: write a step‑by‑step strategy in comments at the top of each modified file.
4. **Implement**: follow style rules; keep commits small and atomic.
5. **Self‑test**: run `scripts/run_checks.py`.
6. **Prepare PR**: include the template from §6.

Failure to follow these steps will cause the CI to fail or the PR to be rejected.

---

## 6 · Pull‑request template

```
[Feat] <concise summary>

### Why
Explain the user story or issue.

### How
Bullet list of key changes.

### Tests
`pytest -q` output pasted here.

### Screenshots / GIFs
If UI changes apply.

### Checklist
- [ ] I ran `scripts/run_checks.py`
- [ ] I updated docs where needed
- [ ] I asked for review from @costasford
```

---

## 7 · Sub‑folder overrides

If a sub‑directory needs different rules, add an `AGENTS.md` there.
Example: `unity-prototype/AGENTS.md` can specify Unity‑only guidelines and will override the C# rules above **for that folder only**.

---

## 8 · License & contact

This repository is MIT‑licensed; keep any generated code MIT‑compatible.
Questions? Mention @costasford in your PR description.
