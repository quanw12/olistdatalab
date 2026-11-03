---
tags: [decourse, ml, features]
module: 15
---

# ML Features and Point-in-Time Correctness

> [!info] Learning goals
> After this note you can: describe the data engineer's role in ML; define the prediction moment, label and training grain; build features that were truly available at prediction time (point-in-time joins); recognise and prevent leakage; split data by time; evaluate against a baseline with suitable metrics; version datasets and experiments; and keep training and scoring features consistent.

## 1. What the data engineer owns in ML

Most ML failures are data failures: wrong rows, leaked information, features computed differently in training and production. The data engineer builds **training and scoring datasets** with the right grain, timing and versions. You do not need to master every model; you need to make sure the model sees only what it could have known.

## 2. Frame the problem

Before any feature, write:

- **Prediction moment:** when is the prediction made? e.g. "when the order is approved".
- **Label:** what is predicted? e.g. "delivered after the estimated date" (1/0).
- **Population:** which rows? e.g. orders that were eventually delivered (a conditional target — say so).
- **Grain:** one row per order at its approval time.
- **Use:** who acts on the score, and what does a false positive/negative cost?

## 3. Point-in-time joins

Every feature value must have been **known at the prediction moment**. For features that change over time, store versions with a `known_at` timestamp and join the latest version known **before** the prediction time.

```sql
-- runnable
-- expect: [["o1", 0.2]]
WITH predictions(order_id, at_time) AS (
    VALUES ('o1',TIMESTAMP '2026-01-02 10:00:00')
), feature_versions(order_id, known_at, risk) AS (
    VALUES ('o1',TIMESTAMP '2026-01-01 10:00:00',0.2),
           ('o1',TIMESTAMP '2026-01-03 10:00:00',0.9)
)
SELECT p.order_id, f.risk
FROM predictions p LEFT JOIN feature_versions f
  ON p.order_id=f.order_id AND f.known_at <= p.at_time
QUALIFY row_number() OVER (PARTITION BY p.order_id, p.at_time ORDER BY f.known_at DESC)=1;
-- Expected: o1,0.2; never a value that became known after the prediction time.
```

DuckDB also has an `ASOF JOIN` that does exactly this:

```sql
-- runnable
-- expect: [["s1", "2026-01-02", 4.1], ["s1", "2026-01-05", 3.2]]
WITH predictions(seller_id, at_date) AS (
    VALUES ('s1', DATE '2026-01-02'), ('s1', DATE '2026-01-05')
), seller_rating(seller_id, known_at, rating) AS (
    VALUES ('s1', DATE '2026-01-01', 4.1), ('s1', DATE '2026-01-04', 3.2), ('s1', DATE '2026-01-06', 1.0)
)
SELECT p.seller_id, CAST(p.at_date AS VARCHAR), r.rating
FROM predictions p ASOF JOIN seller_rating r
  ON p.seller_id = r.seller_id AND p.at_date >= r.known_at
ORDER BY p.at_date;
```

`known_at` is when the information could actually be used — not just the source's event time. A product attribute you see **today** may not be what it was when the order was approved; joining the current dimension leaks the future (the same issue as SCD2 in [[Data Modeling and SCD2]]).

## 4. Leakage

**Leakage** means the training data contains information not available at prediction time, producing great offline metrics and a useless model.

| Leak | Olist example |
|---|---|
| Target in disguise | `order_delivered_customer_date`, `delivery_days` |
| Post-outcome information | `review_score` (written after delivery) |
| Final status | `order_status = 'delivered'` |
| Aggregates over the future | seller's average delay computed over the whole dataset, including later orders |
| Random split across time | training on 2018 orders, testing on 2017 |
| Duplicate entities across splits | the same customer's similar orders in train and test |

Check each feature with "when was this known?", not just a deny-list of suspicious column names — a deny-list helps but does not prove the dataset is leakage-safe.

Rolling features must use only the past:

```sql
-- runnable
-- expect: [["o1", null], ["o2", 1.0], ["o3", 0.5]]
WITH orders(order_id, seller_id, approved_at, was_late) AS (
    VALUES ('o1', 's1', TIMESTAMP '2026-01-01', 1),
           ('o2', 's1', TIMESTAMP '2026-01-05', 0),
           ('o3', 's1', TIMESTAMP '2026-01-09', 1)
)
SELECT order_id,
       avg(was_late) OVER (PARTITION BY seller_id ORDER BY approved_at
                           ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS seller_past_late_rate
FROM orders ORDER BY order_id;
```

`1 PRECEDING` excludes the current order's own label. Even this is slightly optimistic: a past order's lateness is only **known** once it was delivered, which may be after the current approval. The strict version filters past orders by `delivered_at <= current approved_at`.

## 5. Splitting and evaluating

- **Time-based split:** train on earlier periods, validate and test on later ones, with a gap if labels take time to mature. Random splits leak future patterns.
- **Baseline first:** majority class, or a simple rule ("late if the seller is in a remote state"). Log the label prevalence; a model must beat the baseline on the same test set.
- **Metrics:** with imbalanced labels, accuracy misleads. Report ROC-AUC **and** PR-AUC/average precision, plus precision and recall at a threshold chosen from business costs.
- **Population bias:** a delivered-only cohort fits a conditional target; do not generalise its results to cancelled or undelivered orders.

```python
# runnable
labels = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
always_on_time = [0] * len(labels)
accuracy = sum(p == y for p, y in zip(always_on_time, labels)) / len(labels)
recall = sum(p == y == 1 for p, y in zip(always_on_time, labels)) / sum(labels)
assert accuracy == 0.8 and recall == 0.0       # 80% "accurate" and useless for finding late orders
```

## 6. Versioning and reproducibility

Store together for every experiment: dataset version (query + input snapshot + cut-off dates), feature code version, model parameters, metrics and the model artefact. MLflow (used in this repo) tracks runs, parameters, metrics and artefacts.

## 7. Training/serving consistency

Scoring open orders must compute features **exactly** as training did: same definitions, same point-in-time logic, same handling of missing values. Share the feature SQL (or a feature store) between training and scoring; test that a historical order scored through the serving path gets the same features as in the training set.

**Drift:** input distributions change (data drift) or the relation between features and label changes (concept drift). Monitor feature distributions and, once labels arrive, model quality.

## 8. Applying it (ML branch)

Do not use `delivery_days`, `review_score` or the final status as features at approval time. Write `known_at` for every feature. Scoring open orders needs its own query with the same semantics as training. The core of the branch is availability, point-in-time joins, versions and a baseline; full batch scoring and three model experiments are required only if scoring is your main extension.

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Features known after the prediction moment | Inflated offline metrics | Point-in-time joins, `known_at` |
| Random split on time-dependent data | Optimistic evaluation | Time split with gap |
| Accuracy on imbalanced labels | Misleading success | PR-AUC, precision/recall at threshold |
| No baseline | Cannot tell if the model helps | Majority/rule baseline |
| Different feature code in serving | Silent quality drop | Shared feature definitions + consistency test |
| Unversioned datasets | Irreproducible results | Version data, code, params, metrics together |

## 10. Exercises

1. Add a feature known only after delivery and watch the metric jump; explain why it is useless at prediction time.
2. Build seller rolling features with a strict "known before approval" filter.
3. Compare a baseline and a model on the same time-based test set; report PR-AUC and recall at a chosen threshold.
4. How does data drift differ from a drop in model quality?

## 11. Review questions

> [!question]- What does `known_at` represent?
> The moment a value became available for use in a prediction — which can be later than when the underlying event happened.

> [!question]- Why does a time split not remove all leakage?
> Features can still include future information (current dimensions, aggregates over the whole history, post-outcome fields) even when rows are split by time.

> [!question]- Why report PR-AUC on imbalanced labels?
> It focuses on performance for the rare positive class; accuracy and even ROC-AUC can look good while the model finds few positives.

> [!question]- What is data drift vs model quality drop?
> Data drift is a change in input distributions; quality drop is worse prediction performance measured against labels. Drift may or may not hurt quality.

Related: [[Data Modeling and SCD2]], [[LLM Caching Evaluation and Guardrails]], [[Module 15 - ML]]. Sources: [scikit-learn common pitfalls (leakage)](https://scikit-learn.org/stable/common_pitfalls.html), [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html), [DuckDB ASOF join](https://duckdb.org/docs/stable/guides/sql_features/asof_join.html).
