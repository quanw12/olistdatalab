# 04 · pandas, NumPy and Polars

> **DEcourse:** [Syntax và ví dụ tiếng Việt](../../DEcourse/01%20-%20Python/DataFrames%20pandas%20Polars.md) · [Lịch chuẩn và core/tự chọn](../README.md). Video dùng theo bài chẩn đoán, không bắt buộc xem hết.

**Lịch mới:** 7–8 · **Điều kiện:** 01, 03

## Goal
Load, clean, join and aggregate tabular data in Python with DataFrames; know when pandas, Polars
or SQL (DuckDB) is the better tool; read and write Parquet.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Pandas vs PySpark vs Polars: The DataFrame Explained Visually — Data with Baraa](https://www.youtube.com/watch?v=TYnXqVrVz8k) | First, for the big picture | 18 min |
| [Learn NumPy in 1 hour — Bro Code](https://www.youtube.com/watch?v=VXU4LSAQDSc) | Arrays, vectorisation | 1 h |
| [Corey Schafer — pandas Part 1](https://www.youtube.com/watch?v=ZyhVh-qRZPA), [Part 2](https://www.youtube.com/watch?v=zmdjNSmRXF4), [Part 4 Filtering](https://www.youtube.com/watch?v=Lw2rlcxScZY) | Then continue the playlist (grouping, cleaning, dates) | ~3 h total |
| [Polars Crash Course — NeuralNine](https://www.youtube.com/watch?v=OlsRyy-au0E) | Week 8 | 1 h |
| [Jupyter Notebook Complete Beginner Guide — Rob Mulla](https://www.youtube.com/watch?v=5pf0_bpNbkw) | Before your first notebook | 25 min |

## 2. Read
- [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [Merge, join](https://pandas.pydata.org/docs/user_guide/merging.html) · [Group by](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [NumPy: absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Polars user guide: getting started](https://docs.pola.rs/user-guide/getting-started/)
- [DuckDB + pandas/Polars from Python](https://duckdb.org/docs/stable/clients/python/overview)

## 3. Syntax sheet
```python
import pandas as pd
df = pd.read_csv("file.csv", dtype=str)                 # read everything as text first
df["price"] = pd.to_numeric(df["price"], errors="coerce")  # bad values -> NaN (count them!)
df["ts"] = pd.to_datetime(df["ts"], format="%Y-%m-%d %H:%M:%S")
df = df.drop_duplicates(subset=["id"])
summary = (df.groupby("seller_id", as_index=False)
             .agg(items=("id", "size"), revenue=("price", "sum")))
joined = left.merge(right, on="id", how="left", validate="one_to_one", indicator=True)
joined["_merge"].value_counts()                          # who had no match?
df.to_parquet("out.parquet", index=False)

import numpy as np
a = np.array([1.0, 2.0, np.nan]); np.nanmean(a)          # vectorised, NaN-aware

import polars as pl
out = (pl.scan_csv("file.csv")                           # lazy: nothing read yet
         .filter(pl.col("price") > 0)
         .group_by("seller_id")
         .agg(pl.len().alias("items"), pl.col("price").sum().alias("revenue"))
         .collect())                                     # runs the optimized plan

import duckdb
duckdb.sql("SELECT seller_id, sum(price) FROM df GROUP BY 1").df()   # SQL on a DataFrame
```

## 4. Practice
1. With pandas on any dataset: missing values per column, top categories, a pivot table.
2. NumPy: compute a moving average of 1M random numbers with a loop and vectorised; time both.

## 5. Apply to the project — notebook `notebooks/04-profile-olist.ipynb`
Use `olist sample --orders 20000` data (later: the real Kaggle files).
1. **Profile** each CSV: rows, nulls per column, distinct values of low-cardinality columns,
   min/max of dates and prices. Write 5 observations in a markdown cell.
2. **Grain check:** prove `order_id` is unique in orders and `(order_id, order_item_id)` in items.
   Hint: `duplicated(subset=...)`.
3. **Pre-aggregate then join:** items per order (count, sum price, sum freight) and payments per
   order, then merge both into orders with `validate="one_to_one"`. Check: row count = orders.
4. Same as 3 in **DuckDB SQL**; **Polars** is optional. Time all three (`%%timeit`) on 100k orders.
5. Write the result to Parquet; compare its file size with the CSV; read it back and check dtypes.

Then compare your step 3 with `dbt/models/intermediate/int_order_items_by_order.sql` and `fct_orders.sql`.

## 6. Self-check
- Why read as `dtype=str` first in a pipeline?
- What does `validate="one_to_one"` protect you from?
- Lazy vs eager execution — what does Polars gain from being lazy?
- Why is Parquet smaller and faster than CSV?

## Done when
- [ ] Notebook committed with profiling notes and the timing table
- [ ] **Gate 1** passed (see the roadmap)

## Yêu cầu cập nhật · hướng sản phẩm

Pandas + DuckDB SQL là core; Polars và benchmark ba engine là mở rộng. Có thể profile Olist thật ngay ở đây, giữ sample và real ở thư mục khác nhau. Báo 5 quan sát bằng query, phân biệt quan sát với giả thuyết nguyên nhân.
