# Day 4 hints

Complete `clean_weather` one TODO at a time. These examples use column operations; no for loop is needed.

## TODO 1: copy and normalize text

~~~python
df = raw_df.copy()
df["city"] = df["city"].str.strip()
~~~

`copy()` preserves `raw_df` so you can compare input and output.

## TODO 2: convert types

~~~python
df["observed_at"] = pd.to_datetime(
    df["observed_at"],
    format="%Y-%m-%d",
    errors="coerce",
)
df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors="coerce")
df["humidity_pct"] = pd.to_numeric(df["humidity_pct"], errors="coerce")
~~~

## TODO 3: filter invalid rows

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

## TODO 4: remove duplicates, format dates, and return

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

## Troubleshooting

| Error or symptom | Common cause | Fix |
|---|---|---|
| `AttributeError: Can only use .str accessor...` | Non-text column or misplaced .str | Check `df["city"].str.strip()` and its input type |
| `TypeError: bad operand type for unary ~` | Mask is not a Boolean Series | Inspect each mask condition |
| `KeyError` | Wrong column name | Use city, observed_at, temperature_c, humidity_pct |
| Extra index column in output | Missing index=False | Use `clean_df.to_csv(..., index=False)` |
| Accepted count is not 4 | Missing deduplication or mask condition | Check TODOs 3 and 4 |
