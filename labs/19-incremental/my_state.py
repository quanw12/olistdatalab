"""Lab 19: implement current state and daily aggregates from versioned changes.

Tests start red by design. Monetary amounts use integer cents in this fixture.
"""

from collections.abc import Iterable, Mapping
from typing import Any


def apply_events(events: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Return latest state per order, including tombstones; do not mutate input.

    Validate required fields/types, positive version, ISO business_date and
    non-negative integer amount_cents (bool is not an integer amount).
    Identical events can repeat; conflicting contents at the same order/version
    raise ValueError even if a newer version also exists in the batch.
    Hint: separate validation/conflict detection from choosing current versions.
    """
    raise NotImplementedError


def daily_totals(state: Mapping[str, dict[str, Any]]) -> dict[str, int]:
    """Sum non-deleted current amounts by business_date; omit emptied dates.

    Hint: the current-state snapshot is the truth, not historical event amounts.
    Extension: maintain this incrementally and prove equality after every batch.
    """
    raise NotImplementedError
