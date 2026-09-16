# Gợi ý Ngày 4

Hoàn thành `clean_weather` theo từng TODO. Các đoạn dưới là cú pháp cần dùng, không cần viết vòng lặp `for`.

## TODO 1: copy và chuẩn hóa

~~~python
df = raw_df.copy()
df["city"] = df["city"].str.strip()
~~~

`copy()` giữ nguyên `raw_df` để có thể so input với output.

## TODO 2: đổi kiểu dữ liệu

~~~python
df["observed_at"] = pd.to_datetime(
    df["observed_at"],
    format="%Y-%m-%d",
    errors="coerce",
)
df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors="coerce")
df["humidity_pct"] = pd.to_numeric(df["humidity_pct"], errors="coerce")
~~~

## TODO 3: lọc invalid

~~~python
valid_rows = (
    df["city"].notna()
    & df["observed_at"].notna()
    & df["temperature_c"].between(-50, 60)
    & df["humidity_pct"].between(0, 100)
)
invalid_rows = int((~valid_rows).sum())
candidate_df = df.loc[valid_rows].copy()
~~~

## TODO 4: bỏ trùng, định dạng ngày và return

~~~python
before_deduplicate = len(candidate_df)
clean_df = candidate_df.drop_duplicates(
    subset=["city", "observed_at"],
    keep="first",
).copy()
duplicate_rows = before_deduplicate - len(clean_df)

clean_df["observed_at"] = clean_df["observed_at"].dt.strftime("%Y-%m-%d")

return clean_df, invalid_rows, duplicate_rows
~~~

## Nếu có lỗi

| Lỗi | Thường do | Cách sửa |
|---|---|---|
| `AttributeError: Can only use .str accessor...` | Cột city không phải text hoặc gọi `.str` sai chỗ | Dùng `df["city"].str.strip()` |
| `TypeError: bad operand type for unary ~` | `valid_rows` không phải Series True/False | Kiểm tra từng điều kiện trong mask |
| `KeyError` | Sai tên cột | Chỉ dùng `city`, `observed_at`, `temperature_c`, `humidity_pct` |
| Có thêm cột 0,1,2 trong CSV output | Quên `index=False` | Giữ `clean_df.to_csv(..., index=False)` |
| Accepted không phải 4 | Bỏ quên `drop_duplicates` hoặc dùng mask thiếu một điều kiện | So lại TODO 3 và TODO 4 |
