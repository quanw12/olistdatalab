# 20 · Observability and recovery

> **Theory notes:** [[Observability and Recovery]] · [[Failure Drills]] · [[Incident Report]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]

**Week:** 22 · **Mandatory** · **Prerequisites:** 08, 11, 19

## Goal

Detect a job that is green while the data is wrong or late, work out the impact, recover and reconcile. Practise on a copy; never break your only copy of real data.

## Lab · `labs/20-operations` (create it in the code repo)

Learning SLO: yesterday's partition is available before 07:00 Asia/Ho_Chi_Minh. Use a simulated feed that produces new data; do not apply today's freshness rules to Olist purchase dates from 2016–2018.

1. Audit table: run_id, interval, input version, rows read/written/rejected, duration, status.
2. Freshness based on the expected partition / source arrival — not only on when the task finished.
3. Block the new batch but let the code exit 0: your check must detect the missing partition.
4. Simulate a sharp drop in row count; alert using a baseline, a minimum sample size and a way to record legitimate exceptions.
5. Fail after the DB commit but before the export: the retry must fix the missing file and any stale file still lying around.
6. Delete the warehouse in the drill environment; restore from raw, reconcile keys/counts/money; measure the time and any data that could be lost.
7. Incident report: impact, detection, timeline, cause, recovery, verification, prevention (use [[Incident Report]]).

## Verification SQL

```sql
-- Pattern: create two audit tables with these columns in your lab first.
SELECT expected_date FROM expected_partitions
EXCEPT
SELECT partition_date FROM published_partitions WHERE status = 'published';
-- Expect 0 rows; anything else must alert, even if the scheduler is green.
```

## Done when

- [ ] Alerts name the dataset, interval, impact and runbook.
- [ ] At least 4 failure drills have results and a measured recovery time.
- [ ] You never call the system production-ready just because it succeeded once.
