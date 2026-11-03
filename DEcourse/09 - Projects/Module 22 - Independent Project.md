# 22 · Independent project: delivery fleet operations

> **Theory notes:** [[Second Project]] · [[Architecture Decision Record]] · [[Failure Drills]] · **Route:** [[Roadmap]]

**Weeks:** 29–31 · **Mandatory** · **Prerequisites:** G4. You may finish one elective branch in parallel.

## Brief

"Every morning I need to know late deliveries per warehouse, delivery cost and refunded orders so I can allocate staff. Old orders may be updated a month later. I want to know when the report does not yet have enough data."

There is no reference solution. Generate a new delivery source yourself or use public data you are allowed to use; renaming Olist tables does not make a new project.

## Before you code

Write 8 questions with a provisional assumption for each: late compared to which promise, which date a refund counts on, whether cancelled orders are in the denominator, timezone, one order with several delivery attempts, acceptable latency, permissions, budget. Settle a one-page brief.

## Minimum scope

- An orders CSV and a JSON/API event feed; fixtures with pinned versions so you can replay offline.
- Python + SQL + one warehouse, one orchestrator, one report/dashboard. Kafka/Spark are not required.
- Contract, grain, metric definitions, incremental update/delete, 30-day late updates, freshness, CI.
- Reader/writer roles and one restore-from-raw drill.

## Round two

After v1 the stakeholder says: "One order can have several deliveries; a warehouse moved address; refunds must correct past numbers." Keep the commits before/after and justify every change to grain/SCD2/metrics with a reason and a test.

## Rubric

| Area | Points | Criteria |
|---|---:|---|
| Correctness | 30 | Keys, NULLs, money, update/delete, compared with a full rebuild |
| Operations | 25 | Intervals, retries, alerts, measured recovery |
| Product | 20 | Meets the brief, clear metrics, reports missing data |
| Handover | 15 | Clean clone, permissions, README, ADR |
| Explanation | 10 | Demo of decisions and limits |

Aim for ≥ 75/100 with no critical defect: multiplied money, lost data, a leaked secret or missing recovery evidence. This is a learning standard, not a hiring prediction.

## Done when

- [ ] Brief, diagram, hand-computed expected values, CI, evidence.
- [ ] Another person reproduces it from the README; record their questions and fix the instructions.
- [ ] 5-minute demo: need → result → failure → recovery → decision.
