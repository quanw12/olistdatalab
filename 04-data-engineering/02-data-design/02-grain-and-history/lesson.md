# Grain, dimensions and historical meaning

## Understand it

Declare grain before columns. An order-line fact, a current order fact and a daily customer summary answer different questions. Summing a current-state table does not recover what analysts saw yesterday. Natural business keys identify source entities; surrogate dimension keys identify warehouse rows. Type 1 overwrites attributes; Type 2 stores validity intervals, preserving historical attributes.

## Syntax and trace

~~~sql
-- PostgreSQL: syntax illustration, not the assignment schema.
CREATE TABLE sample_customer_version (
    customer_sk BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id TEXT NOT NULL,
    segment TEXT NOT NULL,
    valid_from TIMESTAMPTZ NOT NULL,
    valid_to TIMESTAMPTZ,
    CHECK (valid_to IS NULL OR valid_to > valid_from)
);
-- Match event time using [valid_from, valid_to), not a date alone.
~~~

A segment change at 10:00 belongs to the new version at exactly 10:00. A CHECK constraint does not prevent overlapping rows for the same customer; you still need a strategy and a test.

## Engineering connection

Wrong grain and temporal joins cause incorrect metrics even when every query runs.

[Reference](https://www.postgresql.org/docs/18/ddl-constraints.html). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

