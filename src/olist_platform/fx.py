"""Daily BRL exchange rates from the Frankfurter API -> bronze.fx_rates.

The date range comes from the data (first and last order, padded by one day each side, because a
UTC timestamp can fall on the previous Sao Paulo day). The raw response is kept byte for byte in
landing/, so a run can be replayed without calling the API again.

Retries: timeouts, connection errors, 408/425/429 and 5xx are retried with exponential backoff.
Other 4xx are not: asking again gives the same answer.
"""

from __future__ import annotations

import json
import logging
import math
import time
from datetime import date, timedelta
from pathlib import Path

import duckdb
import requests

logger = logging.getLogger(__name__)

URL = "https://api.frankfurter.dev/v2/rates"
BASE = "BRL"
QUOTES = ("USD", "VND")
RETRYABLE_STATUS = {408, 425, 429}


class FxError(RuntimeError):
    def __init__(self, message: str, *, retryable: bool):
        super().__init__(message)
        self.retryable = retryable


def fetch(start: date, end: date, quotes=QUOTES, session=requests) -> bytes:
    params = {"base": BASE, "quotes": ",".join(quotes), "from": start.isoformat(),
              "to": end.isoformat()}
    try:
        response = session.get(URL, params=params, timeout=(3.05, 30))
    except (requests.Timeout, requests.ConnectionError) as e:
        raise FxError(f"network failure: {e}", retryable=True) from e
    if response.status_code >= 400:
        code = response.status_code
        raise FxError(f"HTTP {code} for {start}..{end}",
                      retryable=code in RETRYABLE_STATUS or code >= 500)
    return response.content


def fetch_with_retry(start: date, end: date, *, attempts: int = 3, base_delay: float = 1.0,
                     sleep=time.sleep, **kwargs) -> bytes:
    for attempt in range(1, attempts + 1):
        try:
            return fetch(start, end, **kwargs)
        except FxError as e:
            if not e.retryable or attempt == attempts:
                raise
            delay = base_delay * 2 ** (attempt - 1)
            logger.warning("attempt %d/%d failed (%s), retrying in %.1fs",
                           attempt, attempts, e, delay)
            sleep(delay)
    raise AssertionError("unreachable")


def parse(payload: bytes, quotes=QUOTES) -> list[dict]:
    """Validate the whole response before anything is written. Rows without a number are dropped."""
    rows = json.loads(payload)
    if not isinstance(rows, list) or not rows:
        raise FxError("response is not a non-empty list", retryable=False)
    clean = []
    for row in rows:
        if not row.get("date") or not row.get("quote"):
            raise FxError(f"row without date or quote: {row}", retryable=False)
        if row["quote"] not in quotes:
            raise FxError(f"unexpected currency {row['quote']!r}", retryable=False)
        rate = row.get("rate")
        if not isinstance(rate, int | float) or isinstance(rate, bool):
            logger.warning("skipped row without a numeric rate: %s", row)
            continue
        clean.append({"date": row["date"], "quote": row["quote"], "rate": float(rate)})
    return clean


def offline_rates(start: date, end: date, quotes=QUOTES) -> bytes:
    """Deterministic fake rates for CI and the sample data, in the API's response format.

    One VND day is left out on purpose so the as-of join with a 3-day tolerance is exercised.
    """
    rows, day, n = [], start, 0
    while day <= end:
        wave = math.sin(n / 45)
        if "USD" in quotes:
            rows.append({"date": day.isoformat(), "base": BASE, "quote": "USD",
                         "rate": round(0.30 + 0.02 * wave, 5)})
        if "VND" in quotes and n % 97 != 50:
            rows.append({"date": day.isoformat(), "base": BASE, "quote": "VND",
                         "rate": round(6900 + 300 * wave, 2)})
        day, n = day + timedelta(days=1), n + 1
    return json.dumps(rows).encode()


def order_date_range(con: duckdb.DuckDBPyConnection) -> tuple[date, date]:
    first, last = con.execute(
        "SELECT min(try_strptime(order_purchase_timestamp, '%Y-%m-%d %H:%M:%S'))::DATE, "
        "max(try_strptime(order_purchase_timestamp, '%Y-%m-%d %H:%M:%S'))::DATE "
        "FROM bronze.orders"
    ).fetchone()
    if first is None:
        raise FxError("bronze.orders is empty; run ingest first", retryable=False)
    return first - timedelta(days=1), last + timedelta(days=1)


def load_fx(con: duckdb.DuckDBPyConnection, landing_dir: Path, run_id: str,
            offline: bool = False) -> int:
    start, end = order_date_range(con)
    logger.info("fx range %s..%s (%s)", start, end, "offline" if offline else URL)
    payload = offline_rates(start, end) if offline else fetch_with_retry(start, end)
    rows = parse(payload)

    raw_path = landing_dir.parent / "fx" / f"fx_{BASE}_{start}_{end}.json"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = raw_path.with_suffix(".json.tmp")
    tmp.write_bytes(payload)
    tmp.replace(raw_path)

    con.execute("BEGIN TRANSACTION")
    con.execute(
        "CREATE OR REPLACE TABLE bronze.fx_rates "
        "(rate_date DATE, base VARCHAR, quote VARCHAR, rate DOUBLE, _run_id VARCHAR)"
    )
    con.executemany(
        "INSERT INTO bronze.fx_rates VALUES (?, ?, ?, ?, ?)",
        [[r["date"], BASE, r["quote"], r["rate"], run_id] for r in rows],
    )
    con.execute("COMMIT")
    logger.info("fx: %d rates loaded", len(rows))
    return len(rows)
