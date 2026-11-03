---
tags: [decourse, python, dataframe]
module: 04
---

# DataFrames: pandas and Polars

> [!info] Learning goals
> After this note you can: explain what a DataFrame is and how it differs from a list of dicts and from a SQL table; select, filter, derive, group and join with pandas; protect joins with `validate` and `indicator`; profile a raw dataset; reason about dtypes and missing values; and know when Polars or SQL is the better tool.

## 1. What a DataFrame is

A DataFrame is an in-memory table: named **columns**, each a typed array (a *Series*), aligned by a row **index**. Operations work on whole columns at once (*vectorised*), implemented in C, so `df["price"] * 2` is orders of magnitude faster than a Python loop over rows.

| Tool | Where the data lives | Best at |
|---|---|---|
| Python lists/dicts | Python objects | Small control logic, records one by one |
| pandas | Memory of one machine | Exploration, profiling, small/medium transforms, tests |
| Polars | Memory (or streaming) of one machine | Fast multi-core transforms, lazy query optimisation |
| SQL engine (DuckDB/Postgres/BigQuery) | Engine storage | Joins/aggregations, data larger than memory, shared tables |

You do not need to master all three APIs before building your first pipeline. In this course pandas + DuckDB SQL are core; Polars is optional.

## 2. pandas essentials

```python
# runnable
import pandas as pd

items = pd.DataFrame({
    "order_id": ["o1", "o1", "o2", "o3"],
    "seller_id": ["s1", "s2", "s1", "s1"],
    "price": [100.0, 50.0, 30.0, None],
})

assert items.shape == (4, 3)                                 # rows, columns
assert list(items.columns) == ["order_id", "seller_id", "price"]
assert items["price"].isna().sum() == 1                      # missing values

expensive = items[items["price"] > 40]                       # boolean filter (NaN > 40 is False)
assert list(expensive["order_id"]) == ["o1", "o1"]

items = items.assign(price_with_tax=items["price"] * 1.1)    # derive a column (returns new df)
by_seller = (items.groupby("seller_id", as_index=False)
                  .agg(items=("order_id", "count"), revenue=("price", "sum")))
assert by_seller.to_dict("records") == [
    {"seller_id": "s1", "items": 3, "revenue": 130.0},
    {"seller_id": "s2", "items": 1, "revenue": 50.0},
]
```

Things to notice:

- `count` counts rows with a non-missing `order_id`; `sum` **skips** missing prices (like SQL `SUM`). `NaN` does not make the total `NaN` unless you pass `min_count`.
- `df[mask]` filters with a boolean Series. Combine conditions with `&`, `|`, `~` and parentheses: `df[(df.a > 1) & (df.b == "x")]`.
- Use `.loc[row_selector, column_selector]` for label-based selection and assignment: `df.loc[df.price.isna(), "flag"] = "missing"`. Chained assignment like `df[df.a > 1]["b"] = 0` may modify a copy and do nothing.
- `assign`, `groupby().agg()` with named aggregations, and method chaining keep transformations readable.

## 3. dtypes and missing values

Each column has a dtype: `int64`, `float64`, `bool`, `datetime64[ns]`, `object` (generic Python objects, often strings), or the newer `string`, `Int64` (nullable integer), `boolean` dtypes.

Classic surprise: an integer column with one missing value becomes `float64`, because NumPy integers cannot hold `NaN`. Use nullable dtypes (`astype("Int64")`) when that matters.

```python
# runnable
import pandas as pd

s = pd.Series([1, None, 3])
assert str(s.dtype) == "float64"              # NaN forced float
assert str(s.astype("Int64").dtype) == "Int64"
assert s.astype("Int64").isna().sum() == 1    # shown as <NA>

raw = pd.DataFrame({"ts": ["2018-01-15 22:30:00", "bad", ""]})
parsed = pd.to_datetime(raw["ts"], errors="coerce", format="%Y-%m-%d %H:%M:%S")
assert parsed.isna().sum() == 2               # 'bad' and '' became NaT
```

`errors="coerce"` turns unparseable values into missing — handy, but it can hide data problems. Count the coerced values and compare with how many were blank to begin with; report the difference as parse failures.

## 4. Joins (merge) with safety checks

`merge` is SQL `JOIN`. Its biggest danger is the same as in SQL: **fan-out**, when a key repeats on the side you thought was unique (see [[JOIN Grain and Fan-out]]). pandas gives you two guards:

```python
# runnable
import pandas as pd

orders = pd.DataFrame({'order_id': ['o1', 'o2', 'o3']})
payments = pd.DataFrame({'order_id': ['o1', 'o1', 'o2'], 'amount': [60, 40, 30]})
paid = payments.groupby('order_id', as_index=False).agg(total=('amount', 'sum'))
out = orders.merge(paid, on='order_id', how='left', validate='one_to_one', indicator=True)
assert len(out) == 3
assert out.loc[out.order_id == 'o1', 'total'].iloc[0] == 100
assert out.loc[out.order_id == 'o3', 'total'].isna().all()
assert (out['_merge'] == 'left_only').sum() == 1

try:
    orders.merge(payments, on='order_id', validate='one_to_one')   # payments repeat o1
except pd.errors.MergeError:
    pass
else:
    raise AssertionError('validate should have caught the duplicate key')
```

- `validate="one_to_one" | "one_to_many" | "many_to_one"` raises if the key cardinality is not what you claimed. It protects cardinality, not whether you chose the right business key.
- `indicator=True` adds `_merge` with `left_only`, `right_only`, `both` — perfect for finding orphans (an **anti-join**: `out[out._merge == "left_only"]`).
- o3 has no payment: the total is **missing**, not 0. Do not `fillna(0)` unless the business rule says "no payment row means zero paid".

`how` options: `inner` (only matches), `left` (keep all left rows), `right`, `outer` (all rows from both).

## 5. Profiling a raw dataset

Profiling is the first thing you do with new data. For each table, answer:

```python
# runnable
import pandas as pd

df = pd.DataFrame({
    "order_id": ["o1", "o2", "o2", "o4"],
    "status": ["delivered", "shipped", "shipped", None],
    "purchase_ts": pd.to_datetime(["2018-01-01", "2018-01-03", "2018-01-03", "2018-02-10"]),
})
profile = {
    "rows": len(df),
    "null_by_column": df.isna().sum().to_dict(),
    "distinct_order_ids": df["order_id"].nunique(),
    "duplicate_order_ids": int(df["order_id"].duplicated().sum()),
    "date_range": (df["purchase_ts"].min().date().isoformat(), df["purchase_ts"].max().date().isoformat()),
    "status_counts": df["status"].value_counts(dropna=False).to_dict(),
}
assert profile["rows"] == 4 and profile["distinct_order_ids"] == 3
assert profile["duplicate_order_ids"] == 1
assert profile["null_by_column"]["status"] == 1
assert profile["date_range"] == ("2018-01-01", "2018-02-10")
```

Write each finding as an **observation backed by a query** ("1 of 4 order rows duplicates an id"). Keep hypotheses about causes ("the export ran twice?") separate until you can prove them; correlation in a profile is not a business cause.

## 6. Reshaping and time series in brief

| Need | pandas |
|---|---|
| Wide → long | `df.melt(id_vars=["order_id"], var_name="metric", value_name="value")` |
| Long → wide | `df.pivot_table(index="month", columns="state", values="revenue", aggfunc="sum")` |
| Sort | `df.sort_values(["seller_id", "month"])` |
| Running total per group | `df.groupby("seller_id")["revenue"].cumsum()` |
| Previous value per group | `df.groupby("seller_id")["revenue"].shift(1)` |
| Resample by month | `df.set_index("ts").resample("MS")["price"].sum()` |

These map directly to SQL window functions ([[Aggregation and Window Functions]]).

## 7. Polars — optional, install separately

Polars is a newer DataFrame library written in Rust. It is multi-threaded and has a **lazy** API: you describe the query, Polars optimises the whole plan (pushing filters and column selection down to the file reader), then executes.

```python
# Pattern: requires `pip install polars`; not part of the core dependencies.
import polars as pl
result = (
    pl.scan_parquet('data/lake/gold/fct_orders.parquet')   # lazy: nothing read yet
    .filter(pl.col('order_status') == 'delivered')
    .group_by('customer_state')
    .agg(pl.col('payment_total').sum().alias('payments'))
    .collect()                                              # optimise + execute
)
```

Differences from pandas: no index; expressions (`pl.col(...)`) instead of indexing; strict types; missing values are always `null`. A lazy plan can push filters/projections down to the source, but it is not guaranteed to be faster for every workload. Benchmark on the same data, semantics and environment, and check NULL handling, money types and ordering before comparing speed.

## 8. pandas or SQL?

Push joins and aggregations over large data into DuckDB SQL (DuckDB can even query a pandas DataFrame by name: `duckdb.sql("SELECT … FROM df")`). Use pandas for profiling, small transforms, test fixtures and plotting. Whichever you use, cross-check one aggregate in the other — two independent implementations agreeing is strong evidence.

## 9. Applying it to Olist

Module 04: profile the real raw tables (rows, nulls, distinct keys, date ranges), check keys before every join, and export typed Parquet. Record five observations, each with the query that proves it.

## 10. Common mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| `merge` without `validate` | Silent fan-out multiplies money | `validate=` + row-count assertions |
| `fillna(0)` on joined amounts | Missing becomes "zero paid" | Keep NaN unless the rule says otherwise |
| Chained assignment | Change lost on a copy | `.loc[mask, col] = value` |
| `errors="coerce"` without counting | Bad data silently becomes NaT/NaN | Count coerced vs originally blank |
| Loading huge CSVs fully into pandas | Out of memory | DuckDB/Polars lazy, or read only needed columns |
| Comparing engines without matching semantics | Misleading benchmark | Same data, NULL rules and types first |

## 11. Exercises

1. Add a payment whose `order_id` does not exist in orders; detect the orphan with `indicator=True`.
2. Add a duplicate to `orders` and watch `validate` fail. What would have happened to the payment total without it?
3. Compute revenue per seller in pandas and in DuckDB SQL on the same data; assert they are equal.
4. Profile `olist_order_items_dataset.csv`: which columns form a unique key?

> [!example]- Hint for 4
> Try `df.duplicated(subset=["order_id", "order_item_id"]).sum()`. `order_item_id` is a sequence number *within* an order, so it is unique only together with `order_id`.

## 12. Review questions

> [!question]- Why is reading the whole CSV as strings useful at bronze, but not ideal for every analysis?
> At bronze it preserves exactly what the source sent and avoids silent type guesses. For analysis you want proper types (numbers, dates, decimals) so aggregations, comparisons and storage are correct and efficient — that is what staging/silver provides.

> [!question]- What does `validate="one_to_one"` guarantee, and what not?
> It guarantees each key appears at most once on both sides. It does not guarantee you joined on the right business key or that no rows are missing.

> [!question]- Why did an integer column turn into float?
> A missing value (NaN) cannot be stored in a NumPy integer array. Use the nullable `Int64` dtype if you need integers with missing values.

> [!question]- What makes Polars' lazy API potentially faster?
> It sees the whole query before executing, so it can push filters and column selection into the file scan, reorder operations and run in parallel.

Related: [[JOIN Grain and Fan-out]], [[Performance and Storage]], [[Module 04 - DataFrames]]. Sources: [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html), [pandas merging](https://pandas.pydata.org/docs/user_guide/merging.html), [Polars lazy API](https://docs.pola.rs/user-guide/lazy/).
