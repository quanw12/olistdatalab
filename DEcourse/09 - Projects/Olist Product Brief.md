---
tags: [decourse, project, olist]
module: 17
---

# Olist Product Brief

> [!info] Purpose
> This brief turns the Olist dataset into a product with users, decisions and a definition of done. It is a simulated requirement for learning, not Olist's real requirement. Every module contributes to it; [[Module 17 - Capstone]] is the acceptance checklist.

## 1. The dataset

The [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) contains ~100k orders (2016–2018) from a Brazilian marketplace, in 9 CSV files: orders, order items, payments, reviews, customers, sellers, products, geolocation and a category name translation. Check the licence/terms before sharing derived data.

Key facts you will discover while profiling (verify each one yourself):

- `customer_id` is per order; `customer_unique_id` identifies the person.
- Items, payments and reviews are 1:n with orders — the fan-out trap ([[JOIN Grain and Fan-out]]).
- Timestamps carry no timezone; the project assumes São Paulo local time ([[Datetime Decimal and Timezones]]).
- Geolocation has many rows per zip prefix.
- Review text is Portuguese free text.

## 2. Users and decisions

- **Operations lead:** wants to investigate regions with late deliveries and problematic sellers.
- **Finance analyst:** needs daily payments that are not inflated by joins, in BRL and converted to USD/VND with documented FX dates.

## 3. Three questions to answer

1. What are payments per day/month, and how many orders have no payment?
2. How does the late-delivery rate per state change over time, with a valid denominator?
3. Which sellers have enough volume and a late rate worth investigating, with a drill-down to the orders?

## 4. Definition of done

- The grain and key of every source and fact are documented; no parents are lost through wrong LEFT JOIN conditions.
- Money reconciles between source and fact; payments that differ from items + freight are reported separately, with a cause stated only when there is evidence.
- Raw versions/hashes, the timezone assumption, the NULL policy and snapshot freshness are recorded.
- One dashboard with metric definitions and data status ([[BI Metrics and Data Products]]).
- The real batch has been run, with real counts in `docs/data-contract.md` (code repo); sample data is for tests.
- Replay and recovery are verified; reader permissions are tested after publishing.

## 5. Separate sample and real environments — PowerShell from the code repo

```powershell
# Sample: generate into its own path, never pointing at the real Olist data.
$env:OLIST_DATA_DIR = "data/sample"
$env:DUCKDB_PATH = "data/warehouse/sample.duckdb"
python -m olist_platform sample --orders 500
python -m olist_platform run --offline

# Real: first download the dataset (respecting its terms) into data/real/landing/olist.
$env:OLIST_DATA_DIR = "data/real"
$env:DUCKDB_PATH = "data/warehouse/real.duckdb"
python -m olist_platform run
```

Use the Python of the venv where the project is installed. `--offline` uses fake FX rates for tests; never report those numbers as real finance results. Data is never committed to the repo.

## 6. Integration milestones

Module 04 real profile → module 09 real batch → module 11 schedule/backfill → module 20 recovery → module 14 cloud → one branch extension → acceptance. Do not cram everything into the last two weeks.

## 7. Evidence to keep

Command, versions, input hash, counts and key checks, reconciliation queries, a dashboard screenshot, and an incident report with recovery time. A screenshot illustrates; queries and logs are the verifiable evidence.

## 8. Review questions

> [!question]- Why does this brief name users and decisions before tools?
> Because the metrics, grain, freshness and acceptable error all follow from what the user decides; tools are chosen afterwards.

> [!question]- What would make the payments chart wrong even though the SQL runs?
> Joining payments together with items (fan-out), mixing UTC and local dates, using `--offline` FX, or silently dropping orders without payments.

Related: [[BI Metrics and Data Products]], [[Failure Drills]], [[Progress and Evidence]], [[Module 17 - Capstone]].
