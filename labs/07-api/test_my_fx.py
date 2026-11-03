import pytest
from my_fx import FxError, classify, fetch_with_retry, save_raw, validate


@pytest.mark.parametrize(("code", "retry"), [
    (408, True), (425, True), (429, True), (500, True), (503, True), (599, True),
    (400, False), (401, False), (404, False), (422, False), (200, False),
])
def test_classify(code, retry):
    assert classify(code) is retry


def make_fetch(outcomes):
    calls = []

    def fetch():
        calls.append(1)
        item = outcomes.pop(0)
        if isinstance(item, Exception):
            raise item
        return item
    return fetch, calls


def test_retries_then_succeeds_with_backoff():
    fetch, calls = make_fetch([FxError("503", retryable=True),
                               FxError("timeout", retryable=True), b"ok"])
    delays = []
    assert fetch_with_retry(fetch, sleep=delays.append) == b"ok"
    assert len(calls) == 3
    assert delays == [1.0, 2.0]


def test_does_not_retry_permanent_errors():
    fetch, calls = make_fetch([FxError("422", retryable=False)])
    delays = []
    with pytest.raises(FxError):
        fetch_with_retry(fetch, sleep=delays.append)
    assert len(calls) == 1 and delays == []


def test_gives_up_after_max_attempts_without_final_sleep():
    fetch, calls = make_fetch([FxError("503", retryable=True)] * 4)
    delays = []
    with pytest.raises(FxError):
        fetch_with_retry(fetch, attempts=4, base_delay=0.5, sleep=delays.append)
    assert len(calls) == 4
    assert delays == [0.5, 1.0, 2.0]


@pytest.mark.parametrize("rows", [
    {}, [], [{"quote": "USD", "rate": 1.0}],
    [{"date": "2017-01-02", "quote": "EUR", "rate": 1.0}],
])
def test_validate_rejects_broken_response(rows):
    with pytest.raises(FxError) as err:
        validate(rows, ["USD", "VND"])
    assert err.value.retryable is False


def test_validate_drops_rows_without_numeric_rate():
    rows = [
        {"date": "2017-01-02", "quote": "USD", "rate": 0.31},
        {"date": "2017-01-02", "quote": "VND", "rate": "n/a"},
        {"date": "2017-01-03", "quote": "VND"},
        {"date": "2017-01-03", "quote": "USD", "rate": True},
        {"date": "2017-01-03", "quote": "VND", "rate": 7000},
    ]
    assert validate(rows, ["USD", "VND"]) == [
        {"date": "2017-01-02", "quote": "USD", "rate": 0.31},
        {"date": "2017-01-03", "quote": "VND", "rate": 7000.0},
    ]


def test_save_raw_is_atomic(tmp_path):
    target = tmp_path / "raw" / "fx.json"
    save_raw(b'[{"a": 1}]', target)
    assert target.read_bytes() == b'[{"a": 1}]'
    assert [p.name for p in target.parent.iterdir()] == ["fx.json"]
