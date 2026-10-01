# Day 5 hints

Complete `build_summary` one TODO at a time. No for loop is needed.

## TODO 1: merge

~~~python
enriched_df = weather_df.merge(
    city_df,
    on="city",
    how="left",
    validate="many_to_one",
)
~~~

## TODO 2: check for missing regions

~~~python
missing_region = enriched_df["region"].isna()

if missing_region.any():
    unknown_cities = enriched_df.loc[missing_region, "city"].unique()
    raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
~~~

## TODO 3: grouping and aggregation

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

## TODO 4: finish and return the report

~~~python
summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)
summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop=True)

if summary_df["observation_count"].sum() != len(enriched_df):
    raise ValueError("summary observation count does not match input rows")

return summary_df
~~~

## Troubleshooting

| Error or symptom | Common cause | Fix |
|---|---|---|
| `MergeError: not a many-to-one merge` | Duplicate city in lookup | Keep one lookup row per city |
| `KeyError: region` | Missing merge or wrong column | Complete TODO 1 and use region |
| `city lookup is missing...` | Weather city absent from lookup | Add its lookup entry; do not change the join to hide the error |
| Only one summary row | Wrong grouping columns | Group by both region and city |
| Wrong summary count | Wrong aggregation column or duplicated merged rows | Check many_to_one validation and the final count check |
