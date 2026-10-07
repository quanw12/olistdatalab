# Day 12 — Grain, dimensions and facts

Use native PostgreSQL and pgAdmin on **weather_day09**. Keep the public source tables intact.
Your DDL belongs in schema.sql; the supplied fixture.sql loads it only after the tables exist.
Read the column specifications in schema.sql as the task contract, not as a worked solution.

## Concepts you need

| Term | Meaning and decision |
|---|---|
| Database / PostgreSQL schema | A database holds data; a schema is a namespace inside it, such as public or day12_mart. |
| OLTP / OLAP | Operational writes/lookups versus analytical grouping/comparison. PostgreSQL can support both workloads. |
| Grain | Exactly what one fact row means. Decide it before choosing keys or aggregates. |
| Fact | An event or measurement at the declared grain. A detail observation and a daily summary have different grains. |
| Dimension | Descriptive attributes used to label or group facts, such as a city or calendar date. |
| Star model | Facts reference dimensions. CREATE SCHEMA alone does not create this modeling pattern. |
| Natural / surrogate key | A source identifier versus a model-owned identifier. Their values need not match. |
| Mart | An analytical model for a particular subject. This small fixture teaches design, not a performance benchmark. |

For this single-provider assignment, each fact represents one city at one observed instant.
The calendar date is an attribute of the observation; several observations can share it.
Which uniqueness rule preserves both readings? Decide that in model.md before writing DDL.
Adding another provider later would require revisiting the grain and key.

Keep Hue in the city dimension even when there are no observations. Missing measurements
are not zero-degree measurements. Describe the grain of a report separately from stored fact grain.

## Required SQL syntax

These shapes use a different subject. Adapt the syntax to your column specifications;
they are not complete weather table definitions.

~~~sql
BEGIN;
CREATE SCHEMA sample_inventory;
CREATE TABLE sample_inventory.locations (
    location_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_id INTEGER NOT NULL UNIQUE,
    label TEXT NOT NULL CHECK (length(btrim(label)) > 0)
);
COMMIT;
~~~

| Shape | Purpose |
|---|---|
| column TYPE NOT NULL | Require a value; CHECK alone can allow NULL. |
| PRIMARY KEY (a, b) | A unique, nonnull composite identity. |
| UNIQUE (a, b) | Reject a repeated combination; choose columns from the grain. |
| REFERENCES namespace.table(key) | Require the referenced dimension value. |
| CHECK (expression) | Enforce a row-level condition, such as a numeric range. |
| INSERT INTO target (a, b) SELECT x, y FROM source | Map selected values to target columns by position. |
| SELECT DISTINCT expression | Produce one occurrence of each selected value. |
| EXTRACT(YEAR / MONTH / ISODOW FROM a_date) | Read calendar attributes; ISO weekday is Monday 1 through Sunday 7. |

Run a complete build in a transaction. A failing statement leaves the transaction
aborted: inspect the error and roll back before retrying. Do not run CREATE TABLE twice
against an existing model or reload fixture.sql merely to fix a report query.
Never substitute a generated key for a source ID without looking up their mapping.

## Time and report syntax

TIMESTAMPTZ represents an instant; its display depends on the session time zone.
The separate timezone_name tells you which city's calendar to use:

~~~sql
SELECT
    (TIMESTAMPTZ '2026-10-01 23:30:00+00'
       AT TIME ZONE 'Asia/Tokyo')::date AS local_date,
    EXTRACT(ISODOW FROM DATE '2026-10-02') AS weekday;
~~~

Predict the local date before running it. Casting an instant straight to date uses
the session time zone, which can produce the wrong business date near midnight.
Use the city's time zone for this assignment.

For reports, know JOIN ... ON, LEFT JOIN, GROUP BY, ORDER BY, COUNT(column),
AVG, MIN, MAX and ROUND. An unmatched LEFT JOIN row has NULL fact columns;
COUNT(*) and COUNT(fact_key) therefore answer different questions.
Choose the report's starting table according to which entities must appear.

Temperature has no useful sum across these observations. An observation average
weights readings equally; it is not a time-weighted average. Averaging group averages
can give a different answer when their counts differ. State what your report measures.

## Before coding

Write model.md, then finish your own schema.sql. Follow the guide's
DDL → fixture → checks → report order. Required names/types/constraints are in the
assignment and shared contract. Keep result tables in expected.md closed until your first attempt.

References: [PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html),
[date/time functions](https://www.postgresql.org/docs/18/functions-datetime.html),
[Kimball grain](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/).
