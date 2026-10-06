# Day 23 — Data quality and deterministic freshness checks


Write read-only SQL checks first. A duplicate query groups by the actual identity and filters COUNT(*)>1. An orphan check LEFT JOINs each dimension and counts missing keys. Compare the fact date to observed_at converted using its city's timezone.

For freshness, start from all configured cities. Put f.source=%s in the JOIN's ON condition. Select MAX(f.observed_at), then evaluate missing/future/stale/fresh with the injected clock. Do not compare naive and aware timestamps.

Build a report dictionary first, then write JSON with ISO strings. At the CLI boundary use SystemExit(2) if required checks fail; keep file-writing success separate from data-quality success.

Create/reset only the dedicated test database intentionally; do not clear your real weather_course history to force expected numbers. Check base-only counts before comparing the table below.
