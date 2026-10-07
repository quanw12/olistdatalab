# LAB04 — Learn

## Own the interval boundaries

A backfill rebuilds historical data for a requested interval. Use half-open windows [start, end): include the start, exclude the end. Adjacent windows then neither overlap nor leave gaps. A loop that only emits full chunks drops the last short interval.

## Syntax — Python

~~~python
from datetime import datetime, timedelta, timezone
instant = datetime.fromisoformat("2024-02-28T00:00:00+00:00")
utc = instant.astimezone(timezone.utc)
candidate_end = utc + timedelta(days=2)
~~~
An aware timestamp represents an instant; a date-shaped string without an offset is ambiguous. This lab requires UTC midnight boundaries so adding days has an explicit meaning. It does not model local-time DST days. timedelta handles leap days/month boundaries without hand-written calendar arithmetic.

Review DE09. The planner should be pure: it schedules windows but does not execute the backfill.

[Assignment](exercise.md) · [Hints](help.md)
