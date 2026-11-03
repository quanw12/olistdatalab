# 05 · Data modelling

> **Theory notes:** [[Data Modeling and SCD2]] · [[JOIN Grain and Fan-out]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 9 · **Prerequisites:** 03, 04

## Goal
Design tables that answer questions correctly: grain, keys, facts vs dimensions, star schema,
slowly changing dimensions, and the medallion layers (bronze/silver/gold).

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [SQL Data Warehouse from Scratch — Data with Baraa](https://www.youtube.com/watch?v=9GVqKuTVANE) | **All of it.** Bronze/silver/gold, ETL, star schema: the same architecture as this repo, in SQL Server | 4 h 23 |
| [Data Modeling Tutorial: Star Schema (Kimball) — Kahan Data Solutions](https://www.youtube.com/watch?v=gRE3E7VUzRU) | All | 17 min |
| [Star vs Snowflake schema, fact vs dimension — codebasics](https://www.youtube.com/watch?v=hQvCOBv_-LE) | All | 7 min |
| [The Medallion Data Architecture (Pros & Cons) — Kahan Data Solutions](https://www.youtube.com/watch?v=8p77fOWp5F4) | All | 9 min |

Baraa's project repo: [DataWithBaraa/sql-data-warehouse-project](https://github.com/DataWithBaraa/sql-data-warehouse-project).
Do the project in DuckDB instead of SQL Server if you like; the point is the design.

## 2. Read
- [Kimball dimensional modelling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) — read: grain, fact table types, conformed dimensions, SCD types 1–2
- [Databricks: medallion architecture](https://www.databricks.com/glossary/medallion-architecture)
- This repo: `docs/data-contract.md` (code repo) (grain table)

## 3. Concept sheet
| Term | Meaning | Olist example |
|---|---|---|
| Grain | What one row means. Decide it **before** columns | one row per order item |
| Fact | Events with measures (numbers you sum) | order, order item, payment |
| Dimension | Context you filter/group by | customer, seller, product, date |
| Surrogate vs natural key | Generated id vs id from the source | `customer_unique_id` is natural |
| Fan-out | A join that repeats rows of the "one" side | orders × items × payments |
| SCD type 1 / 2 | Overwrite history / keep a row per version with valid_from/valid_to | customer moves state |
| Bronze / silver / gold | Raw as received / cleaned & typed / business-ready marts | `bronze.*` / `staging.*` / `marts.*` |

## 4. Practice
Model on paper (photo in your notes) a star schema for: a coffee shop, a school's grades, a ride-hailing app.
For each: state the grain of every fact table in one sentence.

## 5. Apply to the project
Before reading `dbt/models/marts/`, design the Olist warehouse yourself in `docs/my-model.md`:
1. List each source table with its grain and key (verify each key with a SQL `GROUP BY … HAVING count(*) > 1`).
2. Draw the star (Mermaid `erDiagram` renders on GitHub — [syntax](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)): which facts, which dimensions, which keys join them.
3. Decide: is `payment_total` a measure of the order fact or its own fact? Why?
4. Decide: what is a "customer" in `dim_customers`?
5. Decide how to store time: UTC timestamp, local date, or both? Why?
6. Which questions from module 03 become one-line queries on your model?

Then compare with the reference marts and `docs/decisions.md`. Write 3 differences and which design you prefer.

## 6. Self-check
- Explain grain to a non-technical person in two sentences.
- Why do two one-to-many joins to the same parent inflate sums?
- When would you choose SCD2 over overwriting?

## Done when
- [ ] Baraa's data warehouse project done (any engine)
- [ ] `docs/my-model.md` with diagram and decisions, compared with the reference

## Product-focused requirements

Besides the ERD, write a metric contract for payments and the late-delivery rate: numerator/denominator, NULL handling, timezone, recognition date and audience. Simulate two versions of a seller, check that SCD2 rows do not overlap and that the join picks the right version on boundary dates. Do not infer address history from a current snapshot.
