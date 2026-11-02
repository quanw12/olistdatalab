import json
from datetime import datetime

import pytest

from olist_platform.streaming import apply_events, build_events, connect_sink, validate_event

ORDER = {
    "order_id": "o1",
    "customer_id": "c1",
    "order_status": "delivered",
    "purchased_at_utc": datetime(2017, 10, 2, 13, 56),
    "approved_at_utc": datetime(2017, 10, 2, 14, 7),
    "carrier_pickup_at_utc": datetime(2017, 10, 4, 21, 55),
    "delivered_at_utc": None,
}


@pytest.fixture
def sink(tmp_path):
    con = connect_sink(tmp_path / "stream.duckdb")
    yield con
    con.close()


def as_messages(events):
    return [json.dumps(e).encode() for e in events]


def test_missing_steps_produce_no_event():
    types = [e["event_type"] for e in build_events(ORDER)]
    assert types == ["purchased", "approved", "shipped"]


def test_canceled_order_ends_with_canceled_event():
    order = {**ORDER, "order_status": "canceled", "carrier_pickup_at_utc": None}
    assert build_events(order)[-1]["event_type"] == "canceled"


def test_event_ids_are_deterministic():
    assert build_events(ORDER)[0]["event_id"] == build_events(ORDER)[0]["event_id"]


@pytest.mark.parametrize(("change", "reason"), [
    ({"event_type": "teleported"}, "unknown event_type"),
    ({"schema_version": 2}, "unsupported schema_version"),
    ({"event_time": "yesterday"}, "ISO-8601"),
    ({"order_id": ""}, "missing order_id"),
])
def test_invalid_events_are_explained(change, reason):
    event = {**build_events(ORDER)[0], **change}
    assert reason in validate_event(event)


def test_redelivered_batch_is_idempotent(sink):
    messages = as_messages(build_events(ORDER))
    first = apply_events(sink, messages)
    second = apply_events(sink, messages)  # consumer crashed before committing offsets
    assert first["written"] == 3
    assert second == {"written": 0, "duplicates": 3, "dead_letter": 0}
    assert sink.execute("SELECT count(*) FROM live.order_events").fetchone()[0] == 3


def test_out_of_order_event_does_not_move_status_backwards(sink):
    purchased, approved, shipped = build_events(ORDER)
    apply_events(sink, as_messages([shipped, purchased, approved]))
    status = sink.execute("SELECT status FROM live.order_status").fetchone()[0]
    assert status == "shipped"


def test_bad_messages_go_to_dead_letter(sink):
    stats = apply_events(sink, [b"not json", json.dumps({"event_id": "x"}).encode()])
    assert stats["dead_letter"] == 2
    assert sink.execute("SELECT count(*) FROM live.dead_letter").fetchone()[0] == 2
