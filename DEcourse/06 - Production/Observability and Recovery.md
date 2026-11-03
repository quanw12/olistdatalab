---
tags: [decourse, operations, reliability]
module: 20
---

# Observability and Recovery

> [!info] Learning goals
> After this note you can: explain why "the job is green" is not the same as "the data is right"; monitor the five data signals (freshness, volume, schema, quality, reconciliation); define SLIs and SLOs for datasets; design alerts people act on; run a recovery from raw with verification; use RPO/RTO correctly; and write an incident report that prevents repeats.

## 1. Job health vs data health

A scheduler tracks **jobs**: did the code exit 0? Users care about **data**: is it correct, complete and on time? These diverge all the time:

- the job ran but the source file was yesterday's (stale data, green job);
- the job processed 2% of the usual rows because the export was partial;
- a renamed column made a measure NULL everywhere, with no error;
- the dashboard shows numbers from two different publishes.

Observability means being able to answer "is the data trustworthy right now, and if not, why?" from signals you collect deliberately.

## 2. The five data signals

| Signal | Question | Example check |
|---|---|---|
| Freshness | Has the expected input/output for the period arrived? | Yesterday's partition is missing at 07:00 |
| Volume | Are there enough rows? | Row count dropped 90% without explanation |
| Schema | Does the contract still hold? | Column renamed or type changed |
| Quality | Is the content valid? | Duplicate keys, stale FX rate, negative prices |
| Reconciliation | Do the layers agree? | Source payments ≠ fact payments |

### Freshness on expected partitions, not task end time

```python
# runnable
from datetime import date, timedelta

today = date(2026, 11, 3)  # fixed clock so the test is reproducible
expected = {today - timedelta(days=1)}
published = {date(2026, 11, 1)}
missing = expected - published
assert missing == {date(2026, 11, 2)}
job_exit_code = 0
assert job_exit_code == 0 and missing  # a green job must still alert on missing data
```

The same check in SQL, driven by the audit table ([[Ingestion Contracts and Idempotency]]):

```sql
-- runnable
-- expect: [["2026-11-02"]]
WITH expected_partitions AS (
    SELECT CAST(d AS DATE) AS expected_date
    FROM generate_series(DATE '2026-10-31', DATE '2026-11-02', INTERVAL 1 DAY) t(d)
), published_partitions(partition_date, status) AS (
    VALUES (DATE '2026-10-31', 'published'), (DATE '2026-11-01', 'published'),
           (DATE '2026-11-02', 'blocked')
)
SELECT CAST(expected_date AS VARCHAR) FROM expected_partitions
EXCEPT
SELECT CAST(partition_date AS VARCHAR) FROM published_partitions WHERE status = 'published';
```

Olist is static history: there are no new purchase dates every day. Measure snapshot arrival, or use a simulated feed for freshness drills. A wrong freshness definition produces meaningless alerts.

### Volume with a baseline

```python
# runnable
from statistics import median

def volume_alert(history: list[int], today: int, *, min_history=7, max_drop=0.5) -> str | None:
    if len(history) < min_history:
        return None                               # not enough baseline yet
    baseline = median(history[-min_history:])     # median resists one-off spikes
    if today < baseline * (1 - max_drop):
        return f"rows {today} < {int(baseline * (1 - max_drop))} (baseline {baseline})"
    return None

normal = [1000, 980, 1020, 1010, 990, 1005, 995]
assert volume_alert(normal, 990) is None
assert volume_alert(normal, 300).startswith("rows 300")
assert volume_alert(normal[:3], 10) is None
```

Record legitimate exceptions (holidays, known outages) so the alert does not fire every year on the same day.

## 3. SLIs, SLOs and alerts

- **SLI** (indicator): a measurable signal — "hours between partition end and its publish".
- **SLO** (objective): the target — "yesterday's partition published before 07:00 Asia/Ho_Chi_Minh on 99% of days".
- **Error budget:** the allowed misses (1% ≈ 3–4 days a year).

Good alerts are **actionable**: they name the dataset, interval, impact, likely cause and the runbook link. If an alert fires and nobody needs to do anything, tune or remove it — noisy alerts train people to ignore the real ones. Separate *page now* (users affected) from *ticket* (fix this week).

## 4. Recovery that you verify

1. **Scope:** which dataset, interval and users are affected?
2. **Contain:** keep the last good version or mark the data stale; stop downstream consumers from using wrong numbers.
3. **Fix the cause** and choose the input/code/config versions to rebuild with.
4. **Replay/backfill exactly the affected range**; do not advance checkpoints early ([[Incremental CDC and Backfill]]).
5. **Reconcile** keys, counts and money against the source and the consumers; save the evidence.
6. **Learn:** write an [[Incident Report]], add a test, improve the alert.

Recovery is only possible if you kept **raw inputs** with versions. A warehouse you cannot rebuild from raw is a single point of failure.

### RPO and RTO

- **RPO (recovery point objective):** how much data, measured in time, you can afford to lose — "at most the last 24 hours".
- **RTO (recovery time objective):** how long recovery may take — "back within 4 hours".

In the labs, record the **measured** detection time and recovery time; do not claim enterprise SLAs.

## 5. Metrics, logs, traces and lineage

- **Logs:** structured events per run (run_id, interval, counts, errors) — see [[Testing Logging and CI]].
- **Metrics:** numbers over time (duration, rows, lag) that can be graphed and alerted on.
- **Audit table:** one row per run and dataset — the backbone for freshness and lineage questions.
- **Lineage:** which downstream datasets and dashboards depend on a broken input (dbt docs, OpenLineage). It tells you the blast radius, but it does not replace quality tests.

## 6. Applying it to Olist

Module 20: an audit table, freshness on expected partitions, a volume drop alert, failure after DB commit but before export, restoring the warehouse from raw on a copy, and an incident report — with measured recovery times. [[Failure Drills]] lists the drills.

## 7. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Monitoring only task status | Stale/partial data unnoticed | Data signals on expected partitions |
| Freshness on task end time | Green while data is old | Freshness on data/partition arrival |
| Static thresholds without baseline | Noise or blindness | Median baseline, minimum sample, exceptions |
| Alerts without context or runbook | Slow response | Dataset, interval, impact, runbook link |
| No raw retention | Cannot recover | Keep versioned raw inputs |
| Declaring "recovered" without reconciliation | Hidden errors remain | Reconcile counts, keys, money |

## 8. Exercises

1. Pick three drills from [[Failure Drills]] (failure after commit, API error, missing partition); measure detection and recovery time.
2. Build an audit table and a freshness query that alerts on missing partitions for the last 7 days.
3. Tune the volume alert to avoid firing on a known holiday.
4. Which of your alerts really need a human to act? Remove or downgrade the rest.

## 9. Review questions

> [!question]- Does an SLO check the data or the scheduler?
> The data (or the user-facing outcome) — e.g. "partition available by 07:00" — not just whether the job ran.

> [!question]- Why is freshness measured on partitions rather than task completion?
> A task can finish on time while processing old or missing input; only the presence of the expected data proves freshness.

> [!question]- What is the difference between RPO and RTO?
> RPO is how much data (in time) may be lost; RTO is how long restoring service may take.

> [!question]- What makes an alert actionable?
> It identifies what is wrong, the impact, the scope and what to do next (runbook), and it fires only when someone needs to act.

Related: [[Ingestion Contracts and Idempotency]], [[Airflow Intervals and Backfill]], [[Failure Drills]], [[Module 20 - Observability and Recovery]]. Sources: [Google SRE — service level objectives](https://sre.google/sre-book/service-level-objectives/), [OpenLineage](https://openlineage.io/docs/).
