---
tags: [decourse, metrics, product]
module: 10
---

# BI, Metrics and Data Products

> [!info] Learning goals
> After this note you can: describe what makes a dataset a data product; write a metric contract (user, decision, numerator, denominator, exclusions, timezone, freshness); aggregate ratios correctly; define revenue precisely; design a dashboard that shows coverage and freshness instead of hiding gaps; and provide a drill-down from every number to the rows behind it.

## 1. From tables to data products

A table becomes a **data product** when it has: a known user and the decision it supports, clear definitions, an owner, a freshness promise, quality checks, documentation and a way to tell when numbers are incomplete. A beautiful dashboard cannot fix a wrong grain or an ambiguous metric.

Questions to answer before building anything:

1. Who uses it, and what decision does it change?
2. Which metrics, defined how?
3. How fresh must it be, and what happens when it is late?
4. What is the acceptable error, and how will users know about gaps?

## 2. The metric contract

| Field | Example |
|---|---|
| User | Operations lead |
| Decision | Investigate regions with late deliveries |
| Metric | Late-delivery rate |
| Numerator | Delivered orders whose actual delivery date > estimated delivery date |
| Denominator | Delivered orders with both actual and estimated dates |
| Exclusions | Cancelled / not yet delivered; report missing timestamps separately |
| Time attribution | Purchase date in the source's assumed timezone (or delivery date — choose!) |
| Grain of reporting | Per state per month |
| Freshness | Based on the expected input snapshot/partition |
| Owner | You (in this course) |

Write this before writing SQL. Two analysts with different denominators will produce two "late-delivery rates" and lose the business's trust.

## 3. Ratios: aggregate numerator and denominator

```sql
-- runnable
-- expect: [[0.16666666666666666, 0.3]]
WITH groups(state, late, eligible) AS (VALUES ('SP',1,2), ('RJ',1,10))
SELECT sum(late)::DOUBLE / sum(eligible) AS correct_rate,
       avg(late::DOUBLE / eligible) AS wrong_unweighted_average
FROM groups;
-- Expected: 2/12 = 0.1666...; the average of rates is wrong = 0.3.
```

A state with 2 orders weighs as much as one with 10 in the "average of rates". Store **numerator and denominator** in marts and compute the ratio at query time for whatever grouping the user picks. The same applies to averages (store sum and count) and distinct counts (cannot be summed — recompute from detail).

## 4. Revenue is not one number

| Term | Olist source | Notes |
|---|---|---|
| Item value (GMV) | `order_items.price` | Product price before freight |
| Freight | `order_items.freight_value` | Shipping charged |
| Payment total | `order_payments.payment_value` | What the customer paid (may include instalment interest, vouchers) |
| Refunds / cancellations | status + business rules | Olist has no refund table — state the limitation |
| Recognition date | purchase vs approval vs delivery | Changes monthly figures |

Always say which one a chart shows. If payment total differs from items + freight, investigate before labelling the difference as "interest" or "fees" — you need evidence from the source.

## 5. Dashboard design that tells the truth

- Every chart states **unit, date range, definition, and last updated time**.
- Show **coverage**: "1,240 orders excluded: missing estimated date (2.1%)". Do not silently drop them.
- Use a **date spine** so days with zero orders appear as zero, not as missing ([[Aggregation and Window Functions]]).
- Mark **incomplete periods** (the current month, cohorts not yet observable).
- Choose chart types for the question: line for trends, bar for comparing categories, table for exact numbers. Start bar axes at zero.
- Provide a **drill-down**: a query or table listing the orders behind any number, so users can verify.

```sql
-- runnable
-- expect: [["SP", 2, 1, 1, 0.5]]
WITH orders(order_id, state, status, delivered, estimated) AS (
    VALUES ('o1', 'SP', 'delivered', DATE '2018-01-10', DATE '2018-01-08'),
           ('o2', 'SP', 'delivered', DATE '2018-01-05', DATE '2018-01-08'),
           ('o3', 'SP', 'delivered', NULL,              DATE '2018-01-08'),
           ('o4', 'SP', 'canceled',  NULL,              DATE '2018-01-09')
)
SELECT state,
       count(*) FILTER (WHERE status = 'delivered' AND delivered IS NOT NULL AND estimated IS NOT NULL) AS eligible,
       count(*) FILTER (WHERE status = 'delivered' AND delivered > estimated)                            AS late,
       count(*) FILTER (WHERE status = 'delivered' AND (delivered IS NULL OR estimated IS NULL))         AS missing_dates,
       late / NULLIF(eligible, 0) AS late_rate
FROM orders GROUP BY state;
```

The query reports the rate together with its denominator and the excluded rows — that is what makes the number trustworthy.

## 6. Semantic layers

A semantic layer (dbt Semantic Layer/MetricFlow, Cube, LookML) defines metrics once in code so every tool computes them the same way. Even without one, keep metric definitions in version-controlled SQL/YAML next to the marts, not inside individual dashboard widgets.

## 7. Applying it to Olist

Pick 3 questions from [[Olist Product Brief]]. For each chart: unit, date range, definition, update status, and a drill-down query to the orders behind the total. One Metabase or Power BI dashboard is enough for the core.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Averaging rates | Wrong weighted metric | Sum numerator and denominator |
| "Revenue" without definition | Conflicting numbers | Name the measure and recognition date |
| Silently excluding bad rows | False confidence | Show coverage and exclusions |
| Missing days not shown | Misleading trends | Date spine |
| Metric logic inside dashboards | Inconsistent definitions | Central, versioned definitions |
| No freshness indicator | Decisions on stale data | "Data as of" on every page |

## 9. Exercises

1. Write the metric contract for "average delivery time" and implement it with numerator/denominator columns.
2. The user switches from purchase date to delivery date. Which date dimension and metric definitions change, and which numbers move between months?
3. If 20% of orders lack an estimated date, design how the dashboard shows confidence/coverage instead of silently dropping them.
4. Build a drill-down query from "late rate SP Jan 2018" to the individual late orders.

## 10. Review questions

> [!question]- Why store numerator and denominator rather than a rate?
> Rates are non-additive; to aggregate to any grouping you need the underlying counts and divide afterwards.

> [!question]- What turns a table into a data product?
> A known user and decision, defined metrics, owner, freshness promise, quality checks, documentation and visibility of gaps.

> [!question]- Why show excluded rows on a dashboard?
> So users can judge how representative the metric is and spot data problems, instead of trusting a number built on hidden exclusions.

> [!question]- What must "revenue" specify?
> Which measure (item value, freight, payments, net of refunds), currency, and which date the revenue is recognised on.

Related: [[SELECT NULL and CASE]], [[Data Modeling and SCD2]], [[Observability and Recovery]], [[Module 10 - Docker Postgres and BI]]. Sources: [Kimball dimensional modelling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/), [dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl).
