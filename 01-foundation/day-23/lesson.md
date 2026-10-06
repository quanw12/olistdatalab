# Day 23 — Data quality and deterministic freshness checks


## Code correctness and data quality differ

Passing unit tests does not prove today's input is complete or fresh. Data quality checks inspect the data being produced. Use several kinds:

| Check | Question |
|---|---|
| Schema/types | Are required fields present and correctly typed? |
| Validity | Are numeric/time/text values allowed? |
| Uniqueness | Is each observation identity stored once? |
| References | Does every fact map to a city/date? |
| Completeness | Does every configured city have observations? |
| Freshness | Is the newest observation recent enough for the chosen clock? |

Hue intentionally has no base observations. A missing temperature is NULL, not0°C. A completeness failure can be legitimate source behavior while still needing attention.

## Make the clock explicit

datetime.now() is useful in production but makes historical fixture assertions change over time. Accept --as-of as an aware ISO timestamp and --max-age-hours as a positive threshold. Live mode may default to current UTC. Tests must inject a fixed clock.

Compute age = as_of - newest observed_at per city. Missing observations are missing, future observations are invalid/future-dated, age greater than the threshold is stale, and equality at the threshold is still fresh under this policy.

~~~python
from datetime import datetime, timedelta

as_of = datetime.fromisoformat("2026-09-19T03:00:00+00:00")
newest = datetime.fromisoformat("2026-09-19T02:00:00+00:00")
assert as_of - newest <= timedelta(hours=2)
~~~

## SQL NULL behavior

On your own model, group from dim_city with a LEFT JOIN to facts filtered for the chosen source in the JOIN condition. MAX(observed_at) returns NULL for no matching data. Filtering source in the final WHERE would drop Hue.

A CASE expression should check missing first, future second, then stale/fresh. Keep failure reason and measured age, not just a Boolean.

## Reports and exit codes

Produce output/quality_report.json with the as-of time, source, thresholds, check names, counts/status/reasons and per-city freshness. Required check failures produce a nonzero CLI exit code; use2 for failed quality checks in this course. Failure reports are still useful outputs. Do not print 'passed' just because the file was written.

Use the base fixture in a dedicated test DB for exact expected freshness. After Day 17's next batch, Da Nang has a newer observation and is fresh; the expected failures change. Keep the dataset state and clock in your evidence.

Read: [PostgreSQL aggregates](https://www.postgresql.org/docs/18/functions-aggregate.html), [datetime](https://docs.python.org/3.13/library/datetime.html).
