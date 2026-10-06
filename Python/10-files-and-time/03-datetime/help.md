# Help — Aware time, UTC, and deterministic clocks

## First hint

Validate awareness after parsing, then convert, then serialize.

## Detailed approach

Use datetime.fromisoformat(text), guard if dt.tzinfo is None or dt.utcoffset() is None, then dt.astimezone(timezone.utc).isoformat(timespec='microseconds'). Fixed precision gives sortable canonical text for this lab. Do not truncate fractional seconds or append Z to an unconverted local clock.

## Troubleshooting

An unchanged hour with a different offset means you relabeled the timezone rather than converted it. Acceptance of a date-only string means the awareness guard is missing.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.

## Conversion versus relabeling

~~~python
from datetime import datetime, timezone

local = datetime.fromisoformat("2026-10-01T08:30:00+07:00")
utc = local.astimezone(timezone.utc)
print(utc.isoformat(timespec="microseconds"))
~~~

Result: 2026-10-01T01:30:00.000000+00:00. astimezone preserves the instant while changing its displayed offset. Replacing tzinfo without conversion would give the same clock reading a different meaning. In this exercise, reject a naive datetime because the source did not supply an offset; do not silently assume your computer's timezone.

Check awareness with value.tzinfo and value.utcoffset(). Keep fixed microseconds so later canonical UTC strings have a consistent representation.
