# 19 · Incremental loads, CDC and changing data

> **Theory notes:** [[Incremental CDC and Backfill]] · [[CTE Dedup and Incremental SQL]] · [[Data Modeling and SCD2]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]

**Week:** 21 · **Mandatory** · **Prerequisites:** 06, 09, 11

## Goal

Keep results correct when records arrive late, are corrected or are deleted. Tell apart snapshots, timestamp watermarks and log-based CDC. Understand why a 3-day lookback does not handle every historical change.

## Read with a purpose

- [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models): unique key and the incremental filter.
- [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html): snapshot, change events, deletes. Installing Debezium is an extension; you do not need it to understand CDC.

## Lab 19 · `labs/19-incremental` (code repo)

Implement `my_state.py` yourself; do not open the reference implementation before you have made one honest attempt. The tests are red on purpose and are not part of the default `pytest` run.

```powershell
python -m pytest labs/19-incremental -v
```

### The contract

Each event has `order_id`, `version` (positive integer), `business_date` (ISO date), `amount_cents` (non-negative integer) and `deleted` (bool). Versions increase **per order**, not across the whole feed. The same order/version with different content is a conflict: raise `ValueError`; never silently keep whichever copy arrived first.

- `apply_events` takes events that may be duplicated or out of order and returns the current state per `order_id`, keeping tombstones.
- `daily_totals` sums only current, non-deleted orders per day; a day that becomes empty must disappear from the result.
- Never mutate the caller's input.

After the pure functions pass, extend the lab yourself: persistence in DuckDB/Postgres, batched input with a checkpoint, and a `[start, end)` backfill. After every batch, compare with a full rebuild in both directions — especially for a changed date and for deleting every order in a partition. This is a mini lab about CDC semantics, not a log-based CDC connector.

**Evidence:** pytest output, small expected values computed by hand, an ADR on how you chose versions/checkpoints, and logs before/after a recovery.

## Exercise sequence

Create your own fixture `orders(order_id, order_date, amount, updated_at, is_deleted)`. Every change has an increasing version; store event time and processing time separately.

1. Load 5 orders; save the baseline count and money per day.
2. Correct an order whose `order_date` is 30 days old but whose `updated_at` is new. Prove that filtering on purchase date misses it.
3. Merge by key and version; recompute both the old day and the new day when `order_date` changes.
4. Add a tombstone/delete; decide whether the mart drops the order or keeps a flag, and adjust the aggregates.
5. Replay the same events: the result does not change. An older event arriving later must not move the state backwards.
6. Backfill `[start, end)` twice; compare with a full rebuild using `EXCEPT ALL` in both directions.
7. SCD2 seller with two addresses: no overlapping rows; join facts with `valid_from <= event_time AND event_time < valid_to`.

Hints: a watermark must handle equal timestamps; a hard delete never shows up in an `updated_at` query unless the source emits a tombstone. Commit the checkpoint **after** the output is durable.

## Mandatory checks

| Change | Expected |
|---|---|
| Update an order from 30 days ago | Exactly one current row; historical money is corrected |
| Delete | No longer counted, according to the chosen policy |
| Purchase date changed | Old and new day both match a full rebuild |
| Replay / out of order | No duplicates, never reverts to an older version |
| Two changes with the same timestamp | A deterministic tie-breaker decides |

## Done when

- [ ] Tests exist for all five situations, with hand-computed expected values.
- [ ] An ADR records the watermark/CDC choice, its limits and the delete policy.
- [ ] A backfill command takes an interval and an input version, and you have counts before/after.
