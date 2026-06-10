# cartera-inversion

## Stack

- **Python 3.13** (`.python-version`) managed via **uv** — do not use pip/pipenv/poetry.
- No dependencies yet. `pyproject.toml` is the single source of truth.

## Commands

```bash
uv run main.py          # run the app
uv add <package>        # add a dependency
uv sync                 # sync .venv with lockfile
python main.py          # also works if .venv is active
```

## Project state

- **No commits yet** — main branch is empty history.
- **No tests, no lint/formatter/typecheck config** — not yet wired.
- **Single entrypoint**: `main.py` exports `main()`.

## Conventions

- `uv.lock` is committed — keep it in sync after any dependency change.
- `.venv/` is gitignored; recreate with `uv sync`.
