# LAB04 — Assignment

Implement plan_windows(start, end, chunk_days). start/end are ISO strings with offsets; convert to UTC and require both UTC instants to be exactly midnight. Reject naive/malformed timestamps, start >= end, and chunk_days unless it is an exact positive int.

Return a list of (start_iso, end_iso) tuples in order, using UTC isoformat strings ending +00:00. Cover the whole interval exactly once; shorten the final window. No mutation or system-clock dependence.

Reproduce the faulty loop in buggy.py and write tests spanning a leap day and year end.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
