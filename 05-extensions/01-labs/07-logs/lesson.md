# LAB07 — Learn

## Logs describe attempts, not just outcomes

An extract attempt fails, then retry 2 succeeds. Searching for any ERROR would label a recovered pipeline failed. Determine each stage's latest terminal attempt, then calculate the run result. This lab assumes one terminal event per attempt and a single run; events from other runs must be separated before this function.

## Syntax — Python

~~~python
latest = {}
for event in events:
    stage = event["stage"]
    previous = latest.get(stage)
    # Compare attempt numbers before selecting the authoritative event.
~~~
Dictionary lookup allows input events to arrive out of order. A repeated identical terminal event is harmless; conflicting terminal statuses for the same stage/attempt indicate inconsistent evidence and must fail validation.

Review structured logs from the foundation and DE11. retry_count here is inferred from maximum attempt numbers, assuming attempts start at 1 without gaps; it is not a count of every log line.

[Assignment](exercise.md) · [Hints](help.md)
