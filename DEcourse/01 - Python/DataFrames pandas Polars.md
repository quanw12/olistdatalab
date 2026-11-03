---
tags: [decourse, python, dataframe]
module: 04
---

# DataFrames: pandas và Polars

## Khi dùng

pandas để profile và xử lý dữ liệu vừa RAM; SQL cho join/aggregate trong engine; Polars là lựa chọn thêm khi cần lazy execution và expression API. Không cần thuộc ba API trước khi làm pipeline đầu tiên.

## Ví dụ pandas chạy độc lập

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
```

Kết quả: o1=100, o2=30, o3=thiếu payment, không tự thay bằng 0. `validate` bảo vệ cardinality nhưng không bảo đảm business key chọn đúng.

## Pattern Polars — cài riêng nếu chọn học

```python
# Pattern cần polars; không thuộc dependency core.
import polars as pl
result = (
    pl.scan_parquet('data/lake/gold/fct_orders.parquet')
    .filter(pl.col('order_status') == 'delivered')
    .group_by('customer_state')
    .agg(pl.col('payment_total').sum().alias('payments'))
    .collect()
)
```

Lazy plan có thể đẩy filter/projection xuống nguồn, không bảo đảm luôn nhanh hơn mọi workload. So sánh cùng dữ liệu, semantics và môi trường; kiểm tra NULL, kiểu tiền và thứ tự trước benchmark.

## Ứng dụng

Module 04: profile raw thật (rows/null/distinct/date range), kiểm tra keys trước join. Ghi 5 quan sát có query chứng minh, không suy nguyên nhân nghiệp vụ chỉ từ correlation.

## Tự luyện

Thêm payment có order_id không tồn tại; dùng anti-join/indicator phát hiện orphan. Thêm duplicate vào orders và xem merge validation. Đối chứng cùng aggregate trong DuckDB SQL.

Ôn: vì sao đọc toàn bộ CSV thành string hữu ích ở bronze nhưng không phải lựa chọn tối ưu cho mọi phân tích?

Liên quan: [[JOIN Grain va Fanout]], [[Performance va Storage]]. Nguồn: [pandas merge](https://pandas.pydata.org/docs/user_guide/merging.html), [Polars lazy](https://docs.pola.rs/user-guide/lazy/).
