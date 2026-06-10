# cartera-inversion

## Stack

- **Python 3.13** (`.python-version`) managed via **uv** — do not use pip/pipenv/poetry.
- Dependencies in `pyproject.toml`: **yfinance**, **pandas**, **matplotlib**, **ipykernel**
- Single entrypoint: `main.py` exports `main()`.

## Commands

```bash
uv run main.py          # run the app (genera precios_mensuales.csv)
uv add <package>        # add a dependency
uv remove <package>     # remove a dependency
uv sync                 # sync .venv with lockfile
```

## Project state

- **Committed and pushed** to `origin/main` (GitHub).
- **No tests, no lint/formatter/typecheck config** — not yet wired.
- `main.py` descarga precios mensuales de ETFs vía `yfinance` y los guarda en CSV.

## Conventions

- `uv.lock` is committed — keep it in sync after any dependency change.
- `.venv/` and `.idea/` are gitignored; recreate venv with `uv sync`.
