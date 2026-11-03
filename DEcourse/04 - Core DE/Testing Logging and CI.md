---
tags: [decourse, testing, ci]
module: 08
---

# Testing, Logging and CI

> [!info] Learning goals
> After this note you can: explain the test pyramid for data pipelines (unit, integration, end-to-end, data tests); write pytest tests with fixtures, parametrisation and `tmp_path`; design hand-written expected values (test oracles); test failure paths, not just happy paths; write structured logs that support debugging without leaking secrets; and set up CI that runs the right tests and is honest about what it skips.

## 1. Why test data pipelines

A pipeline can run green and still publish wrong numbers. Tests catch wrong assumptions **before** metrics reach users. Two families matter:

- **Code tests** check your logic with controlled inputs (pytest).
- **Data tests** check real data at run time (uniqueness, not-null, reconciliation, freshness) — dbt tests and contract checks ([[Ingestion Contracts and Idempotency]]).

You need both: code tests prove the logic handles NULLs, duplicates and late data; data tests prove today's input respects the contract.

## 2. The test pyramid

| Level | Scope | Speed | Example |
|---|---|---|---|
| Unit | one function, fake inputs | ms | `parse_count('bad')` raises |
| Integration | real engine/service, small data | seconds | load 5 rows into DuckDB and query the mart |
| End-to-end | whole pipeline | minutes | sample data → ingest → dbt → export, then check counts |
| Data tests | production data, every run | varies | `fct_orders.order_id` unique; payments reconcile |

Many fast unit tests, fewer integration tests, a few end-to-end tests. Do not mock the whole engine and call it an integration test.

## 3. Writing good tests

### The oracle: expected values written by hand

```python
# runnable
def latest(events):
    state = {}
    for key, version, value in events:
        if key not in state or version > state[key][0]:
            state[key] = (version, value)
    return state

events = [('o1', 2, 120), ('o1', 1, 100)]
expected = {'o1': (2, 120)}  # oracle written by hand, not computed by calling the code again
assert latest(events) == expected
assert latest(events * 3) == expected                   # idempotent under replay
assert latest(list(reversed(events))) == expected       # order-independent
```

If the expected value is produced by the same code you are testing, the test proves nothing. Compute 3–5 expected rows by hand.

### Property-style checks

Beyond specific examples, assert properties that must always hold: replay does not change the result; shuffling input order does not change it; the sum of parts equals the total; row count of a fact equals its driving table.

### pytest essentials

```python
# Pattern for a test file (tests/test_parse.py); requires the dev extras.
import pytest
from olist_platform.parse import parse_required

@pytest.mark.parametrize('text', ['', None, '   '])
def test_required_value_rejected(text):
    with pytest.raises(ValueError, match='required'):
        parse_required(text)

def test_export_writes_parquet(tmp_path):
    out = tmp_path / "orders.parquet"          # isolated temporary folder per test
    export(rows=[{"order_id": "o1"}], path=out)
    assert out.exists()

@pytest.fixture
def duck():
    import duckdb
    with duckdb.connect() as connection:       # fresh in-memory database per test
        yield connection
```

- **Fixtures** provide setup/teardown (`tmp_path`, a fresh DuckDB connection, sample data).
- **Parametrize** runs one test for many inputs.
- **monkeypatch / fakes** replace network, clock and sleep.
- Name tests after behaviour: `test_snapshot_a_b_a_publishes_a`.
- Run a subset: `pytest -k ingest -v`; stop at first failure: `-x`.

### Test the failure paths

| Failure | Evidence that the pipeline handles it |
|---|---|
| Fan-out | Count/key test + payment reconciliation |
| Snapshot A/B/A | Final published output is A |
| Missing or stale output | Retry restores it from DB/raw |
| API failure on page 7 | No gaps or duplicates; checkpoint correct |
| Late update / delete | Incremental equals rebuild |
| Reader tries to write | Permission denied with the real role |

A suite with only "nice" inputs proves nothing about recovery.

## 4. Coverage is not correctness

Coverage measures which lines ran, not whether the assertions were meaningful. 100% coverage with weak asserts misses every failure mode you did not imagine. Good practice: write a test that **fails** on the first naive implementation (e.g., the A→B→A test against "skip if seen"), keep it, and record the before/after.

## 5. Logging

Logs are how you debug a run you did not watch. Log events with context, in a structured format:

```python
# runnable
import json
import logging
from io import StringIO

stream = StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(message)s"))
log = logging.getLogger("olist.example")
log.handlers[:] = [handler]
log.setLevel(logging.INFO)
log.propagate = False

def log_event(event, **fields):
    log.info(json.dumps({"event": event, **fields}, sort_keys=True))

log_event("load_finished", run_id="r1", table="orders", source_sha256="ab12",
          rows_read=99441, rows_published=99441, duration_s=3.2)
record = json.loads(stream.getvalue())
assert record["event"] == "load_finished" and record["rows_published"] == 99441
```

Always include: **run_id**, source version, interval, row counts (read / written / rejected), duration, status and error class. Use levels deliberately: DEBUG (details), INFO (milestones), WARNING (degraded but continuing), ERROR (step failed). Never log tokens, passwords or personal data; redact them. JSON logs can be searched and aggregated by log tools ([[Observability and Recovery]]).

## 6. Continuous integration

CI runs checks automatically on every push/PR (GitHub Actions in this repo). A typical job:

```yaml
# .github/workflows/ci.yml (excerpt)
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: python -m pip install -e ".[dev]" -c constraints.txt
      - run: ruff check .
      - run: pytest -q
      - run: pytest labs/01-python labs/06-ingest -q   # add each lab once you finish it
```

Principles:

- Install dependencies exactly (pinned constraints) so CI matches your machine.
- Lint, unit tests, then integration tests that can run in CI (DuckDB yes; cloud usually no).
- If something is skipped (no broker, no cloud credentials), **say so** in the job output and README. A green job proves only what the job ran.
- Keep CI fast (minutes) so people actually wait for it.

The repo's default `testpaths=[tests]` covers reference code only; unsolved labs do not run by default. When you finish a lab, add it to CI. Never mark a lab permanently skipped to make CI green.

## 7. Applying it to Olist

Module 08: your labs run in CI, with tests for bad data (A/B/A, missing output, API page failure) and small hand-computed expected values. G2 requires CI to run **your** labs, not only the reference tests.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Expected values computed by the code under test | Tests always pass | Hand-written oracles |
| Only happy-path inputs | Recovery untested | Failure matrix |
| Real network/sleep in unit tests | Slow, flaky tests | Inject fakes |
| `print` debugging in production | No context, no search | Structured logging with run_id |
| Secrets in logs | Leaks | Redaction; never log credentials |
| Silent skips in CI | False confidence | Report skipped scope explicitly |

## 9. Exercises

1. Write a test that makes the "skip if hash seen" implementation fail; fix the code and keep the test.
2. Parametrise a test over `''`, `None`, `'  '`, `'abc'`, `'-1'` for a parser.
3. Add structured logging to your ingest lab with run_id and counts; write a test that checks the log record.
4. Add your finished labs to the CI workflow and make sure a failing lab fails the build.

## 10. Review questions

> [!question]- What failure modes can high coverage still miss?
> Any scenario you never asserted: wrong expected values, untested inputs (NULLs, duplicates, late data), concurrency, environment differences, and properties like idempotency.

> [!question]- What is a test that merely copies the implementation?
> One whose expected value is computed with the same logic (or by calling the function), so it cannot detect a wrong requirement.

> [!question]- What should every pipeline log line contain?
> Run id, step, source version/interval, counts, duration, status and error class — and no secrets or personal data.

> [!question]- What does a green CI job prove?
> Only that the checks it actually ran passed, in that environment. Skipped integrations remain unverified.

Related: [[Observability and Recovery]], [[Git Branches PRs and Review]], [[Functions and Error Handling]], [[Module 08 - Testing and CI]]. Sources: [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [Python logging HOWTO](https://docs.python.org/3/howto/logging.html), [GitHub Actions for Python](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python).
