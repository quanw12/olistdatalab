# Help — Data-quality checks and fixed-clock freshness

## First hint

Use a fixed passed-in clock and independent counters.

## Detailed approach

Parse updated_at, use timedelta(hours=max_age_hours), and compare aware datetimes. Future rows do not have positive stale ages, but explicitly count them. For amount validity use type(value) is int and value >= 0. Compute duplicate occurrences with total minus distinct IDs.

## Troubleshooting

Failures that depend on today's date indicate an internal clock call. A boundary record marked stale means you used >= instead of >.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
