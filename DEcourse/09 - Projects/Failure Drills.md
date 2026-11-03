---
tags: [decourse, project, recovery]
module: 20
---

# Failure Drills

> [!warning] Practice environment
> Use a copy of raw data and the warehouse in a drill folder with its own environment variables. Never break your only copy of real data. Snapshot before acting; never automate deleting a shared database.

## 1. Why drill

Systems fail in ways nobody designed for: a column is renamed, an export is half-written, the network drops on page 7, an old order is corrected, a job is green while data is missing. A drill causes a failure **on purpose**, under controlled conditions, and proves that the pipeline detects it, protects consumers and recovers — with a measured time. Reading the code and believing it would work is not evidence.

## 2. Acceptance matrix

| Drill | Expected | Proof |
|---|---|---|
| Rename/drop a required column | Contract fails, last good version kept | Exception + query on the old version |
| Duplicate key | Not published | Key/count query |
| Snapshot A→B→A | Final state is A | Hash of the published version |
| Parquet missing or stale after commit | Retry repairs the output | Read Parquet, compare with DB |
| API fails on page 7/10 | No half-batch dataset | Page manifest + counts |
| API returns 404 | No endless retries | Request count |
| Update an order from 30 days ago | Old day's money corrected | Compare with full rebuild by key |
| Changed date / delete a whole day | Old partition keeps no stale numbers | Two-way `EXCEPT ALL` |
| Job exits 0 but a batch is missing | Freshness alert | Expected vs published partitions |
| Lose the drill warehouse | Rebuild from raw | Recovery time + reconciliation |
| Reader after republish | Can read marts, cannot write or read raw | Test with the reader login |
| Consumer crash after write (Kafka) | Redelivery causes no duplicate/loss | Produced vs sink event_ids |
| Review changed / model changed (LLM) | Old labels not reused | Cache versions + eval |

Kafka and LLM drills are mandatory only if you chose that branch; all core drills need evidence. Never write "passed" based on reading code.

Theory for each drill: [[Ingestion Contracts and Idempotency]], [[API Retry Pagination and Replay]], [[Incremental CDC and Backfill]], [[Observability and Recovery]], [[Security and Governance]], [[Kafka Offsets Replay and Ordering]], [[LLM Caching Evaluation and Guardrails]].

## 3. How to run a drill

1. **State the hypothesis:** "If the orders file loses `order_status`, the load is blocked and the dashboard keeps yesterday's data."
2. **Prepare:** separate env vars, copy of data, record versions.
3. **Trigger** the failure (edit the file, kill the process, block the network, delete the output).
4. **Observe:** did a check/alert fire? How long until detection?
5. **Recover** following the runbook; time it.
6. **Verify** with queries (keys, counts, money, permissions).
7. **Record** the result and fix gaps (new test, better alert, runbook update).

## 4. Result template

```text
Drill: ...
Input snapshot / code / config: ...
Trigger: ...
Expected: ...
Actual, with query proof: ...
Time to detect / time to recover: ...
Cause and limits: ...
Test/commit preventing a repeat: ...
```

## 5. Ask yourself

- Was the failure detected before a user noticed?
- Was old data kept and marked stale, or silently replaced?
- Could the retry make things worse (duplicates, API lockout)?
- After the fix, can consumers still read the schema with their old permissions?

Related: [[Incident Report]], [[Observability and Recovery]], [[Ingestion Contracts and Idempotency]], [[Module 20 - Observability and Recovery]].
