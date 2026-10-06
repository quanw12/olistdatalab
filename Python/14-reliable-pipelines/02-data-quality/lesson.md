# Data-quality checks and fixed-clock freshness

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/datetime.html).

## Concept and purpose

Code tests ask whether a function behaves according to its specification. Data-quality checks ask whether a particular dataset meets expectations: uniqueness, completeness, range, relationships and freshness.

Return measured counts rather than only a vague pass/fail flag. A report can explain which rule failed and how many records were affected. Decide separately whether a violation quarantines a row, fails a batch, or produces an alert.

Freshness uses event time and an explicit now. Define the boundary: this lab treats age greater than the threshold as stale; exactly at the threshold is still fresh. Future times are reported separately, because treating them as fresh hides clock or source errors.

A uniqueness count of n-len(unique_keys) measures duplicate occurrences after the first, not the number of key groups. State which meaning your metric uses. Stable definitions matter when comparing runs.

## Syntax example

~~~python
from datetime import datetime,timedelta,timezone
now=datetime(2026,10,2,tzinfo=timezone.utc)
observed=now-timedelta(hours=24)
print(now-observed>timedelta(hours=24))
print(observed>now)
~~~

## Trace

Both checks are False: exactly 24 hours is inside the threshold and the event is not in the future.

## DE connection

A pipeline can complete successfully while delivering stale or duplicated data.

Use [exercise.py](exercise.py) for the exact input/output contract.
