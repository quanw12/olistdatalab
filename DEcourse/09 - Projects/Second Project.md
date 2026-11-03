---
tags: [decourse, project, independent]
module: 22
---

# Second Project: Transferring What You Learned

> [!info] Why a second project
> Rebuilding Olist with the reference code nearby proves you can follow. A new domain with ambiguous requirements and no solution proves you can **transfer** the ideas — which is what a job demands. The assignment is in [[Module 22 - Independent Project]]; this note helps you approach it.

## 1. A brief with no solution

"The delivery team needs a daily report: late deliveries per warehouse, delivery cost, refunds, and whether the data is complete enough to trust. One order can have several delivery attempts; the source can correct records up to 30 days later."

Create a new domain and data; do not copy Olist and rename the tables. Use an orders CSV + JSON delivery events, an explicit timezone, and versioned inputs you can replay offline. You clarify the metrics and choose the minimum stack.

## 2. Suggested data shape (not a model answer)

```json
{
  "event_id": "delivery-2-v3",
  "order_id": "order-42",
  "attempt_id": "attempt-2",
  "warehouse_id": "wh-1",
  "event_time": "2026-11-02T08:00:00Z",
  "updated_at": "2026-11-03T04:00:00Z",
  "version": 3,
  "status": "delivered"
}
```

You decide whether the fact is the order, the attempt or the event — no single grain is right for every question. Write down the business key, the delete policy and current state vs history.

## 3. Process

1. **Clarify:** list 8 questions with provisional assumptions (late compared to what, which date a refund counts on, cancelled orders in the denominator, timezone, multiple attempts, latency, permissions, budget). Get answers or record assumptions.
2. **Design:** one-page brief, ERD with grain sentences, metric contracts ([[BI Metrics and Data Products]], [[Data Modeling and SCD2]]).
3. **Decide:** an ADR for each significant choice — what you chose *not* to use and why ([[Architecture Decision Record]]).
4. **Build v1:** batch pipeline, report, contract, tests, freshness.
5. **Round two (v2):** late refunds, a warehouse that changes address, a new source schema. Record compatibility decisions, the backfill, and proof that history is not wrong.
6. **Hand over:** someone else clones and runs it from the README.

## 4. Acceptance

- [ ] Small expected values computed by hand; incremental matches rebuild.
- [ ] Replay, out-of-order events, deletes and moved partitions leave state correct.
- [ ] One data alert and one recovery drill.
- [ ] Reader/writer roles, configuration without secrets, clean clone.
- [ ] Someone else reviews and rebuilds it; you can explain it in 5 minutes.

Rubric (module 22): correctness 30, operations 25, product 20, handover 15, explanation 10. Aim for ≥ 75 with no critical issue: lost data, multiplied money, leaked secret or missing recovery.

## 5. Review questions

> [!question]- Which Olist patterns do not transfer directly to this domain?
> For example: one row per order no longer covers multiple delivery attempts; refunds create negative or corrective money events; corrections after 30 days require change-time tracking rather than snapshot loads.

> [!question]- Which ambiguous requirements must you ask about before coding?
> The definition of "late", refund recognition date, denominator rules, timezone, latency expectations, who may see what, and budget.

Related: [[Data Modeling and SCD2]], [[Architecture Decision Record]], [[Interviews and Portfolio]], [[Module 22 - Independent Project]].
