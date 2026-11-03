from copy import deepcopy

import pytest
from my_state import apply_events, daily_totals


def event(order="o1", version=1, day="2026-01-01", amount=100, deleted=False):
    return {"order_id": order, "version": version, "business_date": day,
            "amount_cents": amount, "deleted": deleted}


def test_replay_is_idempotent():
    events = [event(), event("o2", amount=50)]
    assert apply_events(events * 3) == apply_events(events)
    assert daily_totals(apply_events(events * 3)) == {"2026-01-01": 150}


def test_out_of_order_does_not_restore_older_version():
    state = apply_events([event(version=2, amount=120), event()])
    assert state["o1"]["version"] == 2
    assert daily_totals(state) == {"2026-01-01": 120}


def test_update_old_business_date_is_not_ignored():
    changes = [event(), event(version=2, amount=130)]
    assert daily_totals(apply_events(changes)) == {"2026-01-01": 130}


def test_move_date_removes_old_partition_total():
    changes = [event(), event(version=2, day="2026-02-01", amount=120)]
    assert daily_totals(apply_events(changes)) == {"2026-02-01": 120}


def test_tombstone_prevents_old_event_resurrection():
    state = apply_events([event(version=2, deleted=True), event()])
    assert state["o1"]["deleted"] is True
    assert daily_totals(state) == {}


def test_conflicting_version_fails_even_if_newer_event_exists():
    with pytest.raises(ValueError):
        apply_events([event(version=2), event(), event(amount=999)])


@pytest.mark.parametrize("change", [
    {"version": 0}, {"amount_cents": True}, {"business_date": "not-a-date"},
    {"deleted": "false"}, {"order_id": ""}, {"amount_cents": -1},
])
def test_invalid_event_rejected(change):
    row = event()
    row.update(change)
    with pytest.raises(ValueError):
        apply_events([row])


def test_does_not_mutate_callers_events():
    changes = [event(), event(version=2, day="2026-02-01")]
    original = deepcopy(changes)
    state = apply_events(changes)
    state["o1"]["amount_cents"] = 999
    assert changes == original
