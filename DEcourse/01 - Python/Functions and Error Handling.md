---
tags: [decourse, python, reliability]
module: 01
---

# Functions and Error Handling

> [!info] Learning goals
> After this note you can: design small functions with clear inputs and outputs that are easy to test; use positional, keyword-only and default parameters correctly; raise, catch and chain exceptions so failures are visible; manage resources with `with`; and decide which errors to retry, which to reject and which must stop the pipeline.

## 1. Why functions matter in pipelines

A pipeline that is one long script can only be tested by running all of it against real data. Split it into functions with **explicit inputs and outputs** and each piece can be tested with three rows of fake data in milliseconds. The goal is "pure" functions where possible: the result depends only on the arguments, and nothing outside is changed. Side effects (reading files, calling APIs, writing to a database, sleeping) are pushed to the edges and **passed in**, so tests can replace them.

```text
read (side effect) -> parse/validate/transform (pure, tested heavily) -> write (side effect)
```

## 2. Defining functions

```python
# runnable
def net_amount(price: float, freight: float = 0.0, *, discount: float = 0.0) -> float:
    """Return price + freight - discount.

    'discount' is keyword-only (everything after '*'), so callers must write
    discount=... and cannot swap arguments by accident.
    """
    return price + freight - discount

assert net_amount(100) == 100
assert net_amount(100, 10) == 110
assert net_amount(100, 10, discount=5) == 105
try:
    net_amount(100, 10, 5)          # third positional argument is not allowed
except TypeError:
    pass
else:
    raise AssertionError("expected TypeError")
```

- **Type hints** (`price: float`, `-> float`) document the contract and let tools like mypy and your editor catch mistakes. Python does **not** check them at runtime.
- **Docstrings** explain *why* and the contract (inputs, outputs, errors raised), not a line-by-line restatement.
- **Keyword-only parameters** (`*`) make boolean flags and easily-confused numbers readable: `load(path, overwrite=True)` beats `load(path, True)`.
- `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict. Use them for wrappers, not to avoid designing a signature.

### The mutable default trap

```python
# runnable
def bad_append(row, rows=[]):        # the [] is created ONCE, at definition time
    rows.append(row)
    return rows

assert bad_append(1) == [1]
assert bad_append(2) == [1, 2]       # surprise: state leaked between calls

def good_append(row, rows=None):
    rows = [] if rows is None else rows
    rows.append(row)
    return rows

assert good_append(1) == [1]
assert good_append(2) == [2]
```

## 3. Exceptions: how failure travels

When something goes wrong Python **raises** an exception. It travels up the call stack until some code catches it; if nothing does, the program stops with a traceback and a non-zero exit code. That non-zero exit code is how a scheduler like Airflow knows a task failed — which is why swallowing exceptions is so harmful.

```python
# runnable
def parse_count(text: str | None, *, allow_missing: bool = True) -> int | None:
    if text is None or not text.strip():
        if allow_missing:
            return None
        raise ValueError('count is required')
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError(f'invalid count: {text!r}') from error
    if value < 0:
        raise ValueError('count must be non-negative')
    return value

assert parse_count(' 12 ') == 12          # int() tolerates surrounding spaces
assert parse_count('') is None
try:
    parse_count('bad')
except ValueError as error:
    assert 'invalid count' in str(error)
    assert isinstance(error.__cause__, ValueError)   # original error preserved
else:
    raise AssertionError('expected rejection')
```

Key syntax:

| Syntax | Meaning |
|---|---|
| `try: … except SomeError as e: …` | Handle a specific error type |
| `else:` | Runs only if no exception happened |
| `finally:` | Always runs (cleanup) |
| `raise ValueError("msg")` | Signal a failure |
| `raise NewError(...) from e` | Wrap a low-level error, keeping the cause in the traceback |
| `raise` (bare, inside except) | Re-raise the current exception unchanged |

### Custom exceptions

Define your own exception classes for errors the caller should handle differently:

```python
# runnable
class ContractError(Exception):
    """Input data violates the agreed contract; do not publish."""

class RetryableError(Exception):
    """Temporary failure (timeout, 429, 503); safe to try again."""

def validate_columns(actual: list[str], expected: list[str]) -> None:
    missing = sorted(set(expected) - set(actual))
    if missing:
        raise ContractError(f"missing columns: {missing}")

try:
    validate_columns(["order_id"], ["order_id", "order_status"])
except ContractError as error:
    assert "order_status" in str(error)
```

Now the orchestration layer can say: retry on `RetryableError`, stop and alert on `ContractError`.

## 4. Classifying errors: retry, reject or stop

| Kind | Examples | What to do |
|---|---|---|
| **Transient** | Timeout, connection reset, HTTP 429/503 | Retry with backoff and a limit (see [[API Retry Pagination and Replay]]) |
| **Bad record** | One row has an unparseable date | Quarantine the row with the reason, continue if the contract allows a reject rate |
| **Contract violation** | Missing column, duplicate primary key, schema drift | Stop, keep the last good output, alert |
| **Bug** | `KeyError` from your own code | Fail loudly; fix the code |

Retrying a contract violation just fails three times slower. Quarantining a bug hides it.

## 5. Resource management with `with`

Files, database connections and locks must be released even when an error occurs. A **context manager** guarantees cleanup:

```python
# runnable
from io import StringIO

with StringIO('order_id\no1\n') as stream:
    lines = stream.readlines()
assert stream.closed          # closed automatically at the end of the block
assert len(lines) == 2

from contextlib import contextmanager

events = []

@contextmanager
def step(name):
    events.append(f"start {name}")
    try:
        yield
        events.append(f"ok {name}")
    except Exception:
        events.append(f"failed {name}")
        raise                      # never swallow: re-raise after recording

try:
    with step("load"):
        raise RuntimeError("disk full")
except RuntimeError:
    pass
assert events == ["start load", "failed load"]
```

## 6. Dependency injection: testing retries without the network

Pass side effects as parameters so tests can substitute fakes:

```python
# runnable
def fetch_with_retry(fetch, *, attempts: int = 3, sleep=lambda seconds: None):
    for attempt in range(1, attempts + 1):
        try:
            return fetch()
        except TimeoutError:
            if attempt == attempts:
                raise
            sleep(2 ** attempt)        # exponential backoff: 2, 4, ...

calls, sleeps = [], []
def flaky():
    calls.append(1)
    if len(calls) < 3:
        raise TimeoutError
    return {"rate": 5.1}

assert fetch_with_retry(flaky, sleep=sleeps.append) == {"rate": 5.1}
assert len(calls) == 3 and sleeps == [2, 4]
```

The test runs instantly, makes no network calls, and proves both the number of calls and the backoff schedule.

## 7. Logging instead of printing

```python
import logging
log = logging.getLogger("olist.ingest")

def load(path):
    log.info("loading %s", path)            # lazy formatting, structured fields
    try:
        ...
    except Exception:
        log.exception("load failed for %s", path)   # logs the traceback
        raise                                        # and still fails
```

`log.exception` + `raise` gives you both a readable log and a failed task. See [[Testing Logging and CI]] for structured logs.

## 8. Applying it to Olist

The extractor in the code repo receives `fetch` and `sleep` from outside so retry logic is tested without the network or real waiting. The loader raises `ContractError`; the CLI logs the exception and exits with a non-zero code so the scheduler marks the run as failed.

## 9. Common mistakes

> [!bug] Traps
> - `except Exception: pass` makes the scheduler green while data is wrong. Catch specific exceptions, and re-raise anything you cannot handle.
> - A default argument `rows=[]` is shared between calls; use `None` and create a new list inside.
> - Catching an exception and returning `None` pushes the failure downstream where it is harder to diagnose.
> - Retrying non-transient errors (400, contract violations) wastes time and can hammer an API.
> - Losing the original error: always use `raise … from error` when wrapping.

## 10. Exercises

1. Add tests for `parse_count('-1')` and `parse_count('', allow_missing=False)`.
2. Write `parse_price(text) -> Decimal` that rejects negatives and more than 2 decimal places with a clear message.
3. Extend `fetch_with_retry` so it only retries `TimeoutError` and `RetryableError`, never `ValueError`. Prove it with a test that counts calls.
4. Write a context manager `timed(name, sink)` that appends `(name, seconds)` to `sink` even when the block raises.

> [!example]- Hint for 3
> Use `except (TimeoutError, RetryableError):` and let everything else propagate. The test for `ValueError` should assert exactly one call.

## 11. Review questions

> [!question]- Why must a failed pipeline step exit with a non-zero code?
> The scheduler decides success or failure from the exit code (or the raised exception). Swallowing errors produces a green run with wrong or missing data.

> [!question]- Which errors are worth retrying?
> Transient ones: timeouts, connection resets, 429 and 5xx responses. Bad input and contract violations will fail again and must be fixed or quarantined instead.

> [!question]- What does `raise … from error` add?
> It records the original exception as `__cause__`, so the traceback shows both the high-level message and the low-level root cause.

> [!question]- Why pass `sleep` and `fetch` as parameters?
> So tests can replace them with fakes, making retry tests fast, deterministic and network-free.

Related: [[API Retry Pagination and Replay]], [[Testing Logging and CI]], [[Python Basics and Collections]]. Sources: [Python tutorial — errors and exceptions](https://docs.python.org/3/tutorial/errors.html), [contextlib](https://docs.python.org/3/library/contextlib.html), [logging HOWTO](https://docs.python.org/3/howto/logging.html).
