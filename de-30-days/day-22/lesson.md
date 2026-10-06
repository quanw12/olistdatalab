# Day 22 — Meaningful automated tests with pytest


## Test a contract

A test supplies input and asserts observable behavior. It should catch a real regression, not merely repeat the implementation. A unit test isolates a function; an integration test verifies cooperating components such as PostgreSQL constraints and transactions. Mocking PostgreSQL cannot prove real rollback behavior.

pytest discovers test_*.py files and test_* functions. A failed assert reports the mismatch. Small syntax examples:

~~~python
import pytest

@pytest.mark.parametrize("text, expected", [("12", 12), ("-3", -3)])
def test_integer_conversion(text, expected):
    assert int(text) == expected

def test_bad_integer():
    with pytest.raises(ValueError):
        int("rain")
~~~

The example tests built-ins to teach syntax; your assignment must test your own code.

## Fixtures and temporary paths

A pytest fixture prepares reusable input. A fixture function marked @pytest.fixture is requested by naming it as a test argument. Return a fresh deep copy of nested raw input so one test cannot contaminate another.

tmp_path is a provided temporary directory unique to a test. Use it for manifests/output. It prevents tests from overwriting your real evidence.

~~~python
def test_small_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("ok", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "ok"
~~~

## Test external behavior offline

Inject a fake client/sleeper/clock from Day 15. Assert attempts, pauses and result/exception. Do not use live weather as a unit-test fixture. monkeypatch can replace an attribute when injection is not available; patch where the code looks up the name. Prefer explicit injection when it keeps the function simpler.

Unit tests should not import a module that immediately connects to DB/API. That import behavior is also worth checking.

## Integration tests

Mark PostgreSQL tests with @pytest.mark.integration. Register the marker in pytest.ini:

~~~ini
[pytest]
markers =
    integration: requires the dedicated PostgreSQL test database
~~~

Use weather_course_test, created explicitly in pgAdmin, with the same bootstrap DDL. Add an exact database-name guard before any setup/cleanup. Never truncate your learning DB during a test. Use real transactions, check rollback, and isolate test data between cases. Run integration tests separately with their own PGDATABASE.

Read: [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html), [monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html).
