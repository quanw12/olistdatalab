# Point-in-time feature data and leakage

## Understand it

A feature must use information available at prediction time. Filtering by occurred_at alone can leak late arrivals or future corrections. Reconstruct source state available before cutoff, then select eligible events and aggregate. Training labels typically come from a later window and must remain separate. Correct data engineering helps ML without requiring a full model-training course.

## Syntax and trace

~~~python
from datetime import datetime
cutoff = datetime.fromisoformat("2026-09-02T00:00:00+00:00")
occurred = datetime.fromisoformat("2026-09-01T09:00:00+00:00")
available = datetime.fromisoformat("2026-09-02T10:00:00+00:00")
print(occurred < cutoff, available < cutoff)
~~~

The event occurred earlier but its revision was unavailable at cutoff. That future correction cannot be used.

## Engineering connection

Point-in-time datasets are an optional bridge from DE to ML.

Original practice contract; review [sources.md](../../sources.md) for context.

