---
tags: [decourse, incremental, cdc]
module: 19
---

# Incremental Loads, CDC and Backfill

> [!info] Learning goals
> After this note you can: compare full snapshots, timestamp watermarks, snapshot diffs and log-based CDC; distinguish event time, update time and processing time; merge changes by key and version while keeping tombstones; handle late, out-of-order, deleted and moved records; design a correct backfill over `[start, end)`; and prove an incremental pipeline matches a full rebuild.

## 1. Three clocks

| Time | Example column | Answers |
|---|---|---|
| **Event / business time** | `order_purchase_timestamp`, `order_date` | When did it happen in the real world? |
| **Update time** | `updated_at`, change-log position | When did the source record last change? |
| **Processing time** | `loaded_at`, run id | When did *our* pipeline see it? |

An order purchased last month can be corrected today. A lookback of "3 days by purchase date" misses that correction; a watermark on `updated_at` catches it. Mixing these clocks is the root of most incremental bugs.

## 2. Strategies to capture change

| Strategy | Fits | Limits |
|---|---|---|
| **Full snapshot** (reload everything) | Small datasets; source exports complete files | Heavy I/O; you must know the snapshot is complete |
| **Snapshot diff** (compare today's full snapshot with yesterday's) | Sources without timestamps; detects hard deletes | Needs full snapshots; compute cost |
| **`updated_at` watermark** | Sources with reliable change timestamps | Misses hard deletes; equal timestamps; clock skew; long transactions committing "in the past" |
| **Log-based CDC** (Debezium reading the Postgres WAL / MySQL binlog) | Every insert/update/delete in commit order | Initial snapshot bootstrap, ordering, log retention, source permissions, operational complexity |
| **Backfill by interval** | Fixing history, logic changes | Needs versioned input and coordination with live runs |

### What a CDC event looks like

```json
{"op": "u", "before": {"order_id": "o1", "amount": 100}, "after": {"order_id": "o1", "amount": 120},
 "source": {"lsn": 2309, "ts_ms": 1760000000000}}
```

`op` is `c` (create), `u` (update), `d` (delete, `after` is null) or `r` (snapshot read). The log position (`lsn`) gives a reliable order per table.

## 3. Merging changes: key + version + tombstones

```python
# runnable
events = [
    {'id': 'o1', 'v': 2, 'amount': 120, 'deleted': False},
    {'id': 'o1', 'v': 1, 'amount': 100, 'deleted': False},
    {'id': 'o2', 'v': 1, 'amount': 50, 'deleted': False},
    {'id': 'o2', 'v': 2, 'amount': 50, 'deleted': True},
]
state = {}
for event in events * 3:                  # duplicated and out of order on purpose
    previous = state.get(event['id'])
    if previous is None or event['v'] > previous['v']:
        state[event['id']] = event
active = {key: row for key, row in state.items() if not row['deleted']}
assert list(active) == ['o1']
assert active['o1']['amount'] == 120
assert len(state) == 2  # keep the tombstone so an old event cannot resurrect o2
```

Properties this gives you:

- **Idempotent:** replaying the same events changes nothing.
- **Order-independent:** an older version arriving late cannot overwrite a newer one.
- **Delete-safe:** the tombstone stays in the state, so o2 version 1 replayed later is ignored.

This is a teaching fixture, not a durable consumer: real state lives in a database, the checkpoint advances after the commit, and two different payloads with the same version must raise a conflict rather than be silently resolved.

```python
# runnable
def apply(state, event):
    previous = state.get(event['id'])
    if previous and previous['v'] == event['v'] and previous != event:
        raise ValueError(f"conflict for {event['id']} v{event['v']}")
    if previous is None or event['v'] > previous['v']:
        state[event['id']] = event

state = {}
apply(state, {'id': 'o1', 'v': 1, 'amount': 100})
apply(state, {'id': 'o1', 'v': 1, 'amount': 100})          # exact replay: fine
try:
    apply(state, {'id': 'o1', 'v': 1, 'amount': 999})      # same version, different content
except ValueError as error:
    assert 'conflict' in str(error)
else:
    raise AssertionError('conflict not detected')
```

## 4. Aggregates must follow moved records

If an order's date changes from 1 January to 3 January, **both** daily totals change. An incremental model that only recomputes "days touched by new events" must include the **old** date of every changed record.

```sql
-- runnable
-- expect: [["2026-01-01", 0], ["2026-01-03", 120]]
WITH previous_state(order_id, day, amount) AS (
    VALUES ('o1', DATE '2026-01-01', 100), ('o2', DATE '2026-01-02', 50)
), changes(order_id, day, amount) AS (
    VALUES ('o1', DATE '2026-01-03', 120)          -- o1 moved to 3 Jan and was corrected
), new_state AS (
    SELECT * FROM previous_state WHERE order_id NOT IN (SELECT order_id FROM changes)
    UNION ALL SELECT * FROM changes
), affected_days AS (
    SELECT day FROM previous_state WHERE order_id IN (SELECT order_id FROM changes)
    UNION SELECT day FROM changes
)
SELECT d.day, coalesce(sum(s.amount), 0) AS total
FROM affected_days d LEFT JOIN new_state s ON s.day = d.day
GROUP BY d.day
ORDER BY d.day;
```

Only the affected days are recomputed: 1 January (o1 left it) and 3 January (o1 arrived); 2 January is untouched. 1 January is now empty, so its old row (100) must be **deleted** from the output, not left in place — "replace every affected partition, removing the ones that became empty" handles this naturally.

## 5. Backfill done right

A backfill recomputes a historical range, e.g. after fixing a bug.

**Recipe:** pinned input version + interval `[start, end)` + code/config version → output that can be verified.

- **Deterministic:** running the same interval twice produces the same result.
- **Partition-replacing:** each partition in the interval is overwritten (delete + insert in a transaction or atomic swap), so empty partitions are cleared too.
- **Isolated from live runs:** a backfill must not overwrite today's fresh data with an old input version. Lock the interval, or run backfills on intervals the live job no longer touches.
- **Bounded:** split long ranges into chunks; record progress so a failed backfill resumes.
- **Verified:** compare with a full rebuild for the interval (two-way `EXCEPT ALL`, see [[CTE Dedup and Incremental SQL]]) and compare counts/money before and after.

Airflow passes `data_interval_start` / `data_interval_end` to each run so tasks work on exactly one interval ([[Airflow Intervals and Backfill]]).

## 6. Choosing a strategy

- Data small enough to rebuild in time and budget? **Full refresh** — simplest and most trustworthy.
- Source has reliable `updated_at` and tombstones? **Watermark + upsert + lookback.**
- Need hard deletes but only have full exports? **Snapshot diff.**
- Need every change in order with low latency? **Log-based CDC.**

Whatever you choose, write an ADR describing the clock used, how deletes are detected, the conflict rule and the verification ([[Architecture Decision Record]]).

## 7. Applying it to Olist

The Olist CSVs are snapshots, so `--full-refresh` is the correct and simple baseline. Incremental models are only worth it with a measured benefit and a policy for historical corrections. Module 19 and lab `labs/19-incremental` require: an update after 30 days, a delete, a changed date, an old event arriving late and a timestamp tie — always compared with a full rebuild key by key, not just totals.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Lookback on business date | Corrections to old records missed | Watermark on change time / CDC |
| Ignoring hard deletes | Deleted orders still counted | Tombstones, CDC or snapshot diff |
| Dropping tombstones from state | Deleted keys resurrected by replays | Keep tombstones (with retention policy) |
| Recomputing only new dates | Old date of moved records stays stale | Include old and new partitions |
| Checkpoint before commit | Lost changes after a crash | Commit output, then checkpoint |
| Backfill with live input | History overwritten with today's data | Pinned input version per interval |

## 9. Exercises

1. Extend the Python merge so a conflict (same version, different content) raises, and add a test.
2. Implement `daily_totals(state)` that excludes deleted orders and drops empty days; test a date move and deleting every order of a day.
3. Write a backfill function `backfill(start, end, input_version)` that replaces partitions and is safe to run twice.
4. How does a hard delete disappear from an `updated_at` query, and what are three ways to detect it?

> [!example]- Answer for 4
> A hard-deleted row no longer exists, so no row with a new `updated_at` is returned. Detect deletes with source tombstones/soft-delete flags, log-based CDC delete events, or a periodic full snapshot diff of keys.

## 10. Review questions

> [!question]- When can advancing a checkpoint too early lose data?
> If the checkpoint is saved before the output is durably committed, a crash in between makes the restart skip records that were never written.

> [!question]- How do you keep a backfill from overwriting live data with an older version?
> Pin the input version per interval, restrict backfills to intervals the live job no longer writes, or lock intervals; verify after the run.

> [!question]- Why must tombstones be kept in the state?
> So late or replayed older events for a deleted key are recognised as older and ignored, instead of recreating the record.

> [!question]- Which partitions must be recomputed when an order's date changes?
> Both the old date's partition and the new date's partition.

Related: [[CTE Dedup and Incremental SQL]], [[Airflow Intervals and Backfill]], [[Kafka Offsets Replay and Ordering]], [[Module 19 - Incremental and CDC]]. Sources: [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models).
