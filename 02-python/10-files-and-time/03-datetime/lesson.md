# Aware time, UTC, and deterministic clocks

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/datetime.html).

## Concept and purpose

datetime.fromisoformat parses supported ISO text; a successful parse may still be naive, with no timezone. A naive local wall time cannot identify one instant without an explicit timezone policy.

Check dt.tzinfo and dt.utcoffset(). Convert an aware value with astimezone(timezone.utc). replace(tzinfo=...) attaches an interpretation without converting clock values, so it is not interchangeable with astimezone.

Use event time for when the source says an event occurred or changed, and request time for when your pipeline asked. Do not overwrite one with the other. Keep the original zone name separately if later reporting needs local calendar dates.

For fixed-clock quality checks, pass now into the function. Calling datetime.now inside every test makes boundary cases change over time. Real local zones use zoneinfo.ZoneInfo; on Windows, install tzdata if the system lacks IANA data. The exercises here use explicit offsets and do not require that package.

## Syntax example

~~~python
from datetime import datetime, timezone
local = datetime.fromisoformat("2026-10-01T08:00:00+07:00")
utc = local.astimezone(timezone.utc)
print(utc.isoformat(timespec="seconds"))
print(local == utc)
~~~

## Trace the example

08:00 at +07:00 is 01:00 at UTC. The two aware values compare equal because they identify the same instant.

## Apply it to DE

Consistent UTC versions prevent older updates from appearing newer merely because their offset strings differ.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.


## API quick reference

| Syntax | Purpose |
|---|---|
| `datetime.fromisoformat(text)` | Parse ISO text; separately require an offset. |
| `value.tzinfo / value.utcoffset()` | Inspect awareness; reject a missing offset when the contract requires an instant. |
| `value.astimezone(timezone.utc)` | Preserve the instant while changing its representation. |
| `value.isoformat(timespec='microseconds')` | Choose the precision required by the output contract. |
