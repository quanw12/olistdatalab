# 08 · Testing, logging and CI

**Level:** Intermediate · **Weeks:** 13–14 · **Prerequisite:** 01–07

## Goal
Prove your pipeline works with tests that would catch real bugs, make failures visible in logs
and exit codes, and run all of it automatically on every push.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Pytest Tutorial — freeCodeCamp](https://www.youtube.com/watch?v=cHYq1MRoyI0) | All | 1 h 29 |
| [Logging Advanced — Corey Schafer](https://www.youtube.com/watch?v=jxmzY9soFXg) | All | 20 min |
| [GitHub Actions Tutorial — TechWorld with Nana](https://www.youtube.com/watch?v=R8_veQiYBjI) | All (concepts) | 33 min |
| [Complete GitHub Actions Course — DevOps Directive](https://www.youtube.com/watch?v=Xwpi0ITkL3U) | Chapters on workflows, jobs, caching, artifacts | ~1.5 h |

## 2. Read
- [pytest: fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) · [monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) · [tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [GitHub Actions: workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Ruff](https://docs.astral.sh/ruff/) · [pre-commit](https://pre-commit.com/)

## 3. Syntax sheet
```python
import pytest

@pytest.fixture
def sample_csv(tmp_path):                       # a fresh temp folder per test
    path = tmp_path / "orders.csv"
    path.write_text("order_id\no1\n", encoding="utf-8")
    return path

@pytest.mark.parametrize(("raw", "expected"), [(" A ", "a"), ("b", "b")])
def test_normalize(raw, expected):
    assert normalize(raw) == expected

def test_rejects_blank():
    with pytest.raises(ValueError, match="empty"):
        normalize("  ")

def test_no_network(monkeypatch):
    monkeypatch.setattr(module.requests, "get", fake_get)   # replace for this test only

# logging: one logger per module, configured once at the entry point
import logging
logger = logging.getLogger(__name__)
logger.info("loaded %d rows from %s", n, path)             # lazy formatting
logger.exception("ingest failed")                          # inside except: adds traceback

# exit code a scheduler can see
import sys
sys.exit(1)
```
```yaml
# .github/workflows/ci.yml (skeleton)
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12", cache: pip }
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest
```

## 4. Practice
For each of your lab functions, write **one more test that you think will fail**. If it passes,
your code was right; if it fails, you found a bug. Keep both.

## 5. Apply to the project
1. Read `tests/test_ingest.py`: each test is a failure scenario from `docs/runbook.md`. Map them.
2. Add your labs to CI as a separate job: `pytest labs/01-python labs/06-ingest labs/07-api`.
3. Add [pre-commit](https://pre-commit.com/) with ruff; check a badly formatted file is blocked.
4. Add a CI step that uploads `logs/` when a job fails (`actions/upload-artifact`, `if: failure()`).
5. Add a test that the `olist` CLI exits with code 1 when the landing folder is empty.
   Hint: `subprocess.run([...], capture_output=True)` and check `returncode`.
6. Coverage: `pip install pytest-cov`, `pytest --cov=olist_platform`. Find one important
   uncovered branch and test it.

## 6. Self-check
- What makes a test useful rather than decorative?
- Why must a failed job exit with a non-zero code?
- Unit test vs end-to-end test: one example of each in this repo.

## Done when
- [ ] Labs in CI, pre-commit, failure artifact, CLI exit-code test merged
- [ ] **Gate 2:** labs 06 + 07 green in CI — add Phases 1–2 to your CV and start applying
