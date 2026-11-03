"""Lab 07 — reliable extraction of exchange rates.

Make `pytest labs/07-api -v` green. No network: every dependency is passed in.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path


class FxError(RuntimeError):
    def __init__(self, message: str, *, retryable: bool):
        super().__init__(message)
        self.retryable = retryable


def classify(status_code: int) -> bool:
    """True if a request that got this HTTP status is worth retrying.

    Retry: 408 (timeout), 425, 429 (rate limited), every 5xx. Everything else: no.
    """
    raise NotImplementedError


def fetch_with_retry(fetch: Callable[[], bytes], *, attempts: int = 3, base_delay: float = 1.0,
                     sleep: Callable[[float], None]) -> bytes:
    """Call fetch() until it succeeds.

    fetch raises FxError; retry only when error.retryable is True.
    Wait base_delay * 2**(n-1) seconds before retry n (1, 2, 4 ... for base_delay=1).
    After the last attempt, re-raise the last error. Never sleep after the final attempt.
    """
    raise NotImplementedError


def validate(rows: object, quotes: list[str]) -> list[dict]:
    """Check a parsed API response and return the clean rows.

    Raise FxError(retryable=False) when:
      - rows is not a list, or is empty
      - a row has no "date" or no "quote"
      - a row's quote is not in `quotes`
    Drop (do not raise for) rows whose "rate" is missing or not an int/float (bool is not a number).
    Return [{"date": ..., "quote": ..., "rate": float}, ...]
    """
    raise NotImplementedError


def save_raw(content: bytes, path: Path) -> None:
    """Write bytes atomically: create parent folders, write <path>.tmp, then rename onto path.

    Hint: Path.with_suffix, Path.write_bytes, Path.replace
    """
    raise NotImplementedError
