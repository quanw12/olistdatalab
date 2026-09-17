# Gợi ý Ngày 5

Làm `build_summary` theo từng TODO. Không cần viết vòng lặp `for`.

## TODO 1: merge

~~~python
enriched_df = weather_df.merge(
    city_df,
    on="city",
    how="left",
    validate="many_to_one",
)
~~~

## TODO 2: kiểm tra region thiếu

~~~python
missing_region = enriched_df["region"].isna()

if missing_region.any():
    unknown_cities = enriched_df.loc[missing_region, "city"].unique()
    raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
~~~

## TODO 3: groupby và aggregation

~~~python
summary_df = (
    enriched_df.groupby(["region", "city"], as_index=False)
    .agg(
        observation_count=("observed_at", "count"),
        avg_temperature_c=("temperature_c", "mean"),
        min_temperature_c=("temperature_c", "min"),
        max_temperature_c=("temperature_c", "max"),
        avg_humidity_pct=("humidity_pct", "mean"),
    )
)
~~~

## TODO 4: hoàn thiện report và return

~~~python
summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)
summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop=True)

if summary_df["observation_count"].sum() != len(enriched_df):
    raise ValueError("summary observation count does not match input rows")

return summary_df
~~~

## Nếu lỗi

| Lỗi | Thường do | Cách sửa |
|---|---|---|
| `MergeError: not a many-to-one merge` | city_lookup có city lặp | Kiểm tra bảng lookup, mỗi city chỉ một lần |
| `KeyError: region` | Merge chưa thành công hoặc sai tên cột | Hoàn thành TODO 1, dùng đúng `region` |
| `city lookup is missing...` | Có city weather không nằm trong lookup | Thêm city vào lookup, không đổi `how="left"` để che lỗi |
| Summary chỉ có 1 dòng | Quên `["region", "city"]` trong groupby | Group theo cả hai cột |
| Summary count sai | Aggregation dùng sai cột hoặc merge nhân bản hàng | So lại `validate="many_to_one"` và dòng kiểm tra cuối |
