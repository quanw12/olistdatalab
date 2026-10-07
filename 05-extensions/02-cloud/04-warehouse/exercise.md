# CL04 — Assignment

Implement local_query.sql as one SQLite SELECT over history(event_id, sku, observed_at, version, units, op). Return those six columns, exactly one latest version per event_id, including deletes, sorted by event_id. The checker supplies valid conflict-free rows and changed versions. Do not filter delete before ranking.

Write cloud_merge.sql as a GoogleSQL MERGE from your checked latest-stage table into current, keeping event_id grain and retained tombstones. Update only for a greater version; same-version equality/conflicts must be checked upstream. Write a load plan with deterministic job IDs, validated staging, result inspection and recovery. This SQL is a student deliverable, not executed by the offline checker.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
