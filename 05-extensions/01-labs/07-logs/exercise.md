# LAB07 — Assignment

Implement classify_run(events). Each event contains exactly stage, attempt, status; allowed stages are extract/load/quality/publish, attempt is an exact positive int, status is succeeded or failed. Reject malformed events or conflicting statuses for any identical (stage, attempt) with ValueError; accept identical duplicate events.

Select highest attempt per stage. Return {"status": ..., "retry_count": ..., "failed_stages": [...], "missing_stages": [...]}. failed/missing lists are alphabetically sorted. Overall status is failed if a selected event failed; otherwise incomplete if any required stage is absent; otherwise succeeded. retry_count is sum(max_attempt - 1) for present stages. An empty input is incomplete with retry_count 0.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
