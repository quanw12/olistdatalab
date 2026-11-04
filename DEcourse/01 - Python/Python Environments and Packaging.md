---
tags: [decourse, python, environment]
module: 01
---

# Python Environments and Packaging

> [!info] Learning goals
> After this note you can: explain what an interpreter, a virtual environment and a package are; create and use a venv on Windows and Linux; read a `pyproject.toml`; understand the difference between version ranges and locked versions; configure a run with environment variables; and diagnose "works on my machine" problems.

## 1. The moving parts

- **Interpreter:** the `python` executable. You can have several installed (3.11, 3.12, …). `python --version` and `python -c "import sys; print(sys.executable)"` tell you which one runs.
- **Package:** installable code (pandas, duckdb, dbt-core) published on PyPI and installed with `pip`.
- **site-packages:** the folder where an interpreter keeps installed packages.
- **Virtual environment (venv):** a private copy of site-packages tied to one interpreter. Each project gets its own, so project A's `pandas 1.5` does not break project B's `pandas 2.2`.

Without venvs, every project shares one global set of packages and upgrades in one project silently break another.

## 2. Creating and using a venv

PowerShell (Windows) — run from the repo root, with Python installed:

```powershell
python --version
python -m venv .venv-study
.\.venv-study\Scripts\python.exe -m pip install -e ".[dev,dbt]"
.\.venv-study\Scripts\python.exe -m pip check
.\.venv-study\Scripts\python.exe -m pytest
```

Bash (Linux/macOS/WSL):

```bash
python3 -m venv .venv-study
source .venv-study/bin/activate        # now 'python' means the venv interpreter
python -m pip install -e ".[dev,dbt]"
python -m pytest
```

- Calling the venv's executable directly (`.\.venv-study\Scripts\python.exe`) avoids installing into the wrong interpreter. Activation (`.\.venv-study\Scripts\Activate.ps1`) just puts it first on `PATH`.
- Always use `python -m pip`, not bare `pip`: it guarantees pip belongs to the interpreter you mean.
- `pip check` reports incompatible installed versions.
- The `py` launcher does not exist on every Windows machine; do not rely on it in instructions.
- Never commit the venv folder; add it to `.gitignore`.

The repo recommends Python 3.12; if you use another version, record it and test.

## 3. `pyproject.toml`: describing the project

```toml
[project]
name = "OlistDataLab"                 # distribution name (pip list); import name is olist_platform
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "duckdb>=1.0",
  "pandas>=2.2",
  "pyarrow>=15",
]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff"]
dbt = ["dbt-core>=1.8", "dbt-duckdb>=1.8"]

[project.scripts]
olist = "olist_platform.cli:main"     # creates an `olist` command
```

- `dependencies` are always installed; **extras** (`[dev]`, `[dbt]`) are opt-in: `pip install -e ".[dev,dbt]"`.
- `-e` (*editable*) installs your own `src/` package so code changes take effect without reinstalling.
- `[project.scripts]` turns a function into a command-line tool.

## 4. Ranges vs locks: reproducibility

`pandas>=2.2` is a **range**: today it installs 2.2.3, next year maybe 3.0 with breaking changes. Ranges say what *should* work; they do not prove what *did* work.

A **lock** or **constraints file** pins every package, including transitive dependencies, to the exact versions that passed your tests:

```text
# constraints.txt (excerpt)
duckdb==1.1.3
pandas==2.2.3
numpy==2.1.3
pyarrow==18.1.0
```

```powershell
python -m pip install -e ".[dev]" -c constraints.txt
```

Workflow: after a successful run in a **clean** environment, export the exact versions (`python -m pip freeze --exclude-editable > constraints.txt`), then prove reproducibility by installing from it in another fresh environment and running the tests. A `pip freeze` from a venv shared by several projects is a messy snapshot, not a good lock. Tools like `uv` and `pip-tools` automate locking.

## 5. Configuration through environment variables

Code should not hard-code paths, credentials or modes. Read them from the environment:

```python
# runnable
import os
from pathlib import Path

def settings(env=os.environ):
    return {
        "data_dir": Path(env.get("OLIST_DATA_DIR", "data/landing/olist")),
        "duckdb_path": Path(env.get("DUCKDB_PATH", "data/warehouse/olist.duckdb")),
        "offline": env.get("OLIST_OFFLINE", "0") == "1",
    }

cfg = settings({"OLIST_DATA_DIR": "data/sample", "OLIST_OFFLINE": "1"})
assert cfg["data_dir"] == Path("data/sample")
assert cfg["offline"] is True
assert cfg["duckdb_path"] == Path("data/warehouse/olist.duckdb")   # default
```

Separating sample and real runs in PowerShell:

```powershell
# Sample session: check this is NOT the real data folder before generating.
$env:OLIST_DATA_DIR = "data/sample"
$env:DUCKDB_PATH = "data/warehouse/sample.duckdb"
.\.venv-study\Scripts\python.exe -m olist_platform sample --orders 500
.\.venv-study\Scripts\python.exe -m olist_platform run --offline
```

- Environment variables stay set for the rest of that shell session — a common source of "why is it using the sample data?". Log the effective settings at the start of every run.
- `.env` files hold local values and must never be committed; `.env.example` holds only placeholders.
- Secrets (API keys, passwords) come from environment variables or a secret manager, never from code or Git (see [[Security and Governance]]).

## 6. How imports find code

`import olist_platform` searches the directories in `sys.path`: the script's folder, then site-packages. "ModuleNotFoundError" usually means: wrong interpreter (package installed elsewhere), package not installed in editable mode, or running from a folder where a local file shadows the package (a file named `pandas.py` in your folder breaks `import pandas`).

## 7. Diagnosing environment problems

> [!bug] When you hit an environment error
> Record the command, the interpreter path (`sys.executable`), versions, and the **first** traceback. A dbt error while parsing a library file is a different problem from a SQL error in a mart. Do not edit SQL at random while the parser has not even finished reading the packages.

Checklist:

1. `python -c "import sys; print(sys.executable, sys.version)"` — right interpreter?
2. `python -m pip show <package>` — installed here, which version?
3. `python -m pip check` — conflicts?
4. Fresh venv + constraints — does the problem disappear? Then it was your environment.

## 8. Applying it to Olist

Create a fresh venv, install core + dev, and see which tests are skipped without dbt. Then install the `dbt` extra and run the integration tests. Explain the difference between an installed third-party package and your own module in `src/`.

## 9. Exercises

1. Create two venvs with different pandas versions and print `pandas.__version__` from each.
2. Install the project without the `dbt` extra; which tests skip or fail, and why?
3. Generate a constraints file from a clean, passing environment; reinstall from it in a new venv and run the tests.
4. Make `settings()` reject an `OLIST_DATA_DIR` that equals the real data folder when the command is `sample`.

## 10. Review questions

> [!question]- Why use `python -m pip` instead of `pip`?
> It guarantees pip runs under the interpreter you are targeting, so packages are installed into the right environment.

> [!question]- What is the difference between `pandas>=2.2` and `pandas==2.2.3`?
> The first is a compatibility range that may resolve to different versions over time; the second pins the exact version that was tested, which makes the environment reproducible.

> [!question]- Why must every run log its effective configuration?
> Environment variables persist in a shell and defaults change; without the logged values you cannot tell whether a run used sample or real data, or which database it wrote to.

> [!question]- What does `pip install -e .` do?
> It installs your project in editable mode: Python imports your source folder directly, so edits take effect without reinstalling.

Related: [[Delivery and Reproducibility]], [[Testing Logging and CI]], [[Module 01 - Python]]. Sources: [venv](https://docs.python.org/3/library/venv.html), [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), [pip constraints files](https://pip.pypa.io/en/stable/user_guide/#constraints-files).
