import json
from datetime import date

import pytest
import requests

from olist_platform import fx


class FakeResponse:
    def __init__(self, status_code, body=b"[]"):
        self.status_code = status_code
        self.content = body


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(kwargs)
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


GOOD = json.dumps([{"date": "2017-01-02", "base": "BRL", "quote": "USD", "rate": 0.31}]).encode()


def test_request_has_timeout_and_params():
    session = FakeSession([FakeResponse(200, GOOD)])
    fx.fetch(date(2017, 1, 1), date(2017, 1, 3), session=session)
    assert session.calls[0]["timeout"] == (3.05, 30)
    assert session.calls[0]["params"]["quotes"] == "USD,VND"


def test_retries_5xx_and_timeouts_with_backoff():
    session = FakeSession([FakeResponse(503), requests.Timeout(), FakeResponse(200, GOOD)])
    delays = []
    body = fx.fetch_with_retry(date(2017, 1, 1), date(2017, 1, 3), session=session,
                               sleep=delays.append)
    assert body == GOOD
    assert delays == [1.0, 2.0]


def test_does_not_retry_client_errors():
    session = FakeSession([FakeResponse(422)])
    with pytest.raises(fx.FxError) as err:
        fx.fetch_with_retry(date(2017, 1, 1), date(2017, 1, 3), session=session,
                            sleep=lambda s: None)
    assert err.value.retryable is False
    assert len(session.calls) == 1


@pytest.mark.parametrize(("payload", "message"), [
    ({}, "non-empty list"),
    ([], "non-empty list"),
    ([{"quote": "USD", "rate": 1}], "without date"),
    ([{"date": "2017-01-02", "quote": "EUR", "rate": 1}], "unexpected currency"),
])
def test_broken_responses_are_rejected(payload, message):
    with pytest.raises(fx.FxError, match=message):
        fx.parse(json.dumps(payload).encode())


def test_non_numeric_rate_is_skipped():
    rows = fx.parse(json.dumps([
        {"date": "2017-01-02", "quote": "USD", "rate": 0.3},
        {"date": "2017-01-02", "quote": "VND", "rate": "n/a"},
    ]).encode())
    assert rows == [{"date": "2017-01-02", "quote": "USD", "rate": 0.3}]


def test_offline_rates_have_a_vnd_gap():
    rows = fx.parse(fx.offline_rates(date(2017, 1, 1), date(2017, 6, 30)))
    usd = {r["date"] for r in rows if r["quote"] == "USD"}
    vnd = {r["date"] for r in rows if r["quote"] == "VND"}
    assert usd - vnd, "at least one day must miss VND to exercise the as-of join"
