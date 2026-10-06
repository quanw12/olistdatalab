# Quality checks, reconciliation and fixed-clock freshness

## Understand it

Validate individual values and the shape of whole datasets. Uniqueness, referential integrity and accounting totals detect errors that parsing cannot. Freshness depends on which clock and timestamp you mean; using a fixed test clock makes the decision reproducible. A quality failure should identify evidence and stop affected publication, not silently discard revenue.

## Syntax and trace

~~~python
from datetime import datetime
now = datetime.fromisoformat("2026-09-03T12:00:00+00:00")
observed = datetime.fromisoformat("2026-09-03T10:00:00+00:00")
print((now - observed).total_seconds() / 3600)
~~~

The age is two hours. Define whether equality at your threshold passes and whether future timestamps are a defect.

## Engineering connection

A trusted mart has explainable counts, key relationships and amounts.

Original practice contract; review [sources.md](../../sources.md) for context.

