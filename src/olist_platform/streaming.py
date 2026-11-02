"""Replay Olist order lifecycles as Kafka events and consume them into a live table.

Producer: reads the staged orders and emits one event per lifecycle step
(purchased -> approved -> shipped -> delivered | canceled | unavailable), in event-time order.

Consumer: at-least-once delivery + an idempotent sink.
- Offsets are committed only after the events are written, so a crash re-delivers them.
- Re-delivered events are ignored because event_id is a primary key (deterministic id).
- Events that fail validation go to a dead-letter table instead of stopping the stream.
- live.order_status keeps the latest state per order by EVENT time, not arrival time, so an
  out-of-order event never moves an order backwards.

The pure functions (build_events, validate_event, apply_events) are tested without Kafka.
"""

from __future__ import annotations

import hashlib
import json
import logging
import time
from collections.abc import Iterable, Iterator
from datetime import datetime
from pathlib import Path

import duckdb

logger = logging.getLogger(__name__)

SCHEMA_VERSION = 1
EVENT_TYPES = {"purchased", "approved", "shipped", "delivered", "canceled", "unavailable"}
TERMINAL_STATUSES = {"canceled", "unavailable"}


def event_id(order_id: str, event_type: str) -> str:
    return hashlib.sha1(f"{order_id}:{event_type}".encode()).hexdigest()


def build_events(order: dict) -> list[dict]:
    """Turn one staged order row into its lifecycle events. Missing steps produce no event."""
    steps = [
        ("purchased", order.get("purchased_at_utc")),
        ("approved", order.get("approved_at_utc")),
        ("shipped", order.get("carrier_pickup_at_utc")),
        ("delivered", order.get("delivered_at_utc")),
    ]
    events = []
    for event_type, at in steps:
        if at is None:
            continue
        events.append(_event(order, event_type, at))
    if order.get("order_status") in TERMINAL_STATUSES:
        last = max(e["event_time"] for e in events) if events else None
        if last:
            events.append(_event(order, order["order_status"], datetime.fromisoformat(last)))
    return events


def _event(order: dict, event_type: str, at: datetime) -> dict:
    return {
        "event_id": event_id(order["order_id"], event_type),
        "schema_version": SCHEMA_VERSION,
        "order_id": order["order_id"],
        "customer_id": order.get("customer_id"),
        "event_type": event_type,
        "event_time": at.isoformat(),
    }


def validate_event(event: dict) -> str | None:
    """Return None if valid, else the reason it goes to the dead-letter table."""
    for key in ("event_id", "order_id", "event_type", "event_time"):
        if not event.get(key):
            return f"missing {key}"
    if event.get("schema_version") != SCHEMA_VERSION:
        return f"unsupported schema_version {event.get('schema_version')!r}"
    if event["event_type"] not in EVENT_TYPES:
        return f"unknown event_type {event['event_type']!r}"
    try:
        datetime.fromisoformat(event["event_time"])
    except (TypeError, ValueError):
        return "event_time is not ISO-8601"
    return None


def connect_sink(path: Path) -> duckdb.DuckDBPyConnection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(path))
    con.execute("CREATE SCHEMA IF NOT EXISTS live")
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS live.order_events (
            event_id VARCHAR PRIMARY KEY, order_id VARCHAR, event_type VARCHAR,
            event_time TIMESTAMP, received_at TIMESTAMP DEFAULT current_timestamp
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS live.order_status (
            order_id VARCHAR PRIMARY KEY, status VARCHAR, status_time TIMESTAMP
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS live.dead_letter (
            payload VARCHAR, reason VARCHAR, received_at TIMESTAMP DEFAULT current_timestamp
        )
        """
    )
    return con


def apply_events(con: duckdb.DuckDBPyConnection, raw_messages: Iterable[bytes]) -> dict[str, int]:
    """Write one batch in a single transaction. Safe to call again with the same messages."""
    stats = {"written": 0, "duplicates": 0, "dead_letter": 0}
    con.execute("BEGIN TRANSACTION")
    try:
        for raw in raw_messages:
            try:
                event = json.loads(raw)
                reason = validate_event(event) if isinstance(event, dict) else "not an object"
            except (json.JSONDecodeError, UnicodeDecodeError):
                reason = "not valid JSON"
            if reason:
                con.execute("INSERT INTO live.dead_letter (payload, reason) VALUES (?, ?)",
                            [raw.decode("utf-8", "replace"), reason])
                stats["dead_letter"] += 1
                continue
            inserted = con.execute(
                "INSERT INTO live.order_events (event_id, order_id, event_type, event_time) "
                "VALUES (?, ?, ?, ?) ON CONFLICT DO NOTHING RETURNING event_id",
                [event["event_id"], event["order_id"], event["event_type"],
                 event["event_time"]],
            ).fetchall()
            if not inserted:
                stats["duplicates"] += 1
                continue
            stats["written"] += 1
            con.execute(
                """
                INSERT INTO live.order_status VALUES (?, ?, ?)
                ON CONFLICT (order_id) DO UPDATE SET
                    status = excluded.status, status_time = excluded.status_time
                WHERE excluded.status_time >= order_status.status_time
                """,
                [event["order_id"], event["event_type"], event["event_time"]],
            )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    return stats


def read_orders_for_replay(warehouse: Path, limit: int | None) -> list[dict]:
    with duckdb.connect(str(warehouse), read_only=True) as con:
        sql = ("SELECT order_id, customer_id, order_status, purchased_at_utc, approved_at_utc, "
               "carrier_pickup_at_utc, delivered_at_utc FROM staging.stg_orders "
               "ORDER BY purchased_at_utc")
        if limit:
            sql += f" LIMIT {int(limit)}"
        cursor = con.execute(sql)
        columns = [d[0] for d in cursor.description]
        return [dict(zip(columns, row, strict=True)) for row in cursor.fetchall()]


def ordered_events(orders: list[dict]) -> Iterator[dict]:
    events = [e for order in orders for e in build_events(order)]
    yield from sorted(events, key=lambda e: e["event_time"])


def produce(bootstrap: str, topic: str, warehouse: Path, limit: int | None = 500,
            rate_per_sec: float = 200.0) -> int:
    from confluent_kafka import Producer  # optional dependency: pip install -e ".[stream]"

    producer = Producer({"bootstrap.servers": bootstrap, "enable.idempotence": True,
                         "acks": "all"})
    sent = 0
    for event in ordered_events(read_orders_for_replay(warehouse, limit)):
        # Key by order_id: all events of one order land in one partition, in order.
        producer.produce(topic, key=event["order_id"], value=json.dumps(event).encode())
        producer.poll(0)
        sent += 1
        if rate_per_sec:
            time.sleep(1 / rate_per_sec)
    producer.flush(10)
    logger.info("produced %d events to %s", sent, topic)
    return sent


def consume(bootstrap: str, topic: str, sink_path: Path, group_id: str = "olist-live",
            batch_size: int = 200, idle_timeout_s: float = 10.0) -> dict[str, int]:
    from confluent_kafka import Consumer

    consumer = Consumer({"bootstrap.servers": bootstrap, "group.id": group_id,
                         "auto.offset.reset": "earliest", "enable.auto.commit": False})
    consumer.subscribe([topic])
    con = connect_sink(sink_path)
    totals = {"written": 0, "duplicates": 0, "dead_letter": 0}
    idle_since = time.monotonic()
    try:
        while time.monotonic() - idle_since < idle_timeout_s:
            messages = consumer.consume(num_messages=batch_size, timeout=1.0)
            payloads = [m.value() for m in messages if m.error() is None]
            if not payloads:
                continue
            idle_since = time.monotonic()
            stats = apply_events(con, payloads)
            consumer.commit(asynchronous=False)  # only after the write succeeded
            for k, v in stats.items():
                totals[k] += v
            logger.info("batch %s", stats)
    finally:
        consumer.close()
        con.close()
    logger.info("consumer stopped after %.0fs idle: %s", idle_timeout_s, totals)
    return totals
