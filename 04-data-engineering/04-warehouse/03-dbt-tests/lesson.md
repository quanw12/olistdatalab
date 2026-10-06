# dbt data tests and transformation evidence

## Understand it

A data test returns violations; zero rows passes that rule. Generic tests cover common column checks, singular SQL tests express business rules. Uniqueness tests detect problems rather than enforcing primary keys. Missing valid rows can pass uniqueness and null tests, so reconcile count and money too.

## Syntax and trace

~~~yaml
version: 2
models:
  - name: latest_changes
    columns:
      - name: id
        data_tests: [unique, not_null]
~~~
~~~sql
-- Singular test: failures only; no trailing semicolon.
select * from {{ ref('latest_changes') }} where amount_cents < 0
~~~

Negative-value and key tests are independent. A missing positive row needs a reconciliation check.

## Engineering connection

Make transformation assumptions executable and reviewable.

[Reference](https://docs.getdbt.com/docs/build/data-tests). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

