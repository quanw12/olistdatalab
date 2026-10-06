> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in ../submissions/day-05/.

# Day 5 lesson: merge, groupby, and data checks

## 1. Two tables with different jobs

`weather_clean.csv` stores weather observations:

| city | observed_at | temperature_c | humidity_pct |
|---|---|---:|---:|
| Hanoi | 2026-09-14 | 31.2 | 78 |
| Da Nang | 2026-09-14 | 30.1 | 81 |

`city_lookup.csv` stores shared city information:

| city | region |
|---|---|
| Hanoi | North |
| Da Nang | Central |

You can look up region by city instead of repeating it in the weather source. Join the tables using their shared `city` key.

## 2. What does merge do?

~~~python
enriched_df = weather_df.merge(
    city_df,
    on="city",
    how="left",
    validate="many_to_one",
)
~~~

| Part | Meaning |
|---|---|
| `weather_df.merge(city_df, ...)` | Adds lookup data to weather rows |
| `on="city"` | Uses city as the matching key |
| `how="left"` | Keeps every weather row |
| `validate="many_to_one"` | Each weather row can match at most one lookup row |

The merged weather rows now include region.

### Why a left join?

When a weather city is absent from the lookup, a left join keeps that observation with a missing region. The pipeline can detect the problem.

An inner join drops unmatched rows. The report may look successful while losing data.

### Why validate the relationship?

Two lookup rows for Hanoi could duplicate every Hanoi weather row during the merge. `validate="many_to_one"` raises an error instead of silently producing an incorrect report.

## 3. Check immediately after merging

~~~python
missing_region = enriched_df["region"].isna()

if missing_region.any():
    unknown_cities = enriched_df.loc[missing_region, "city"].unique()
    raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
~~~

- `isna()` creates a Boolean mask.
- `any()` is true if at least one value is true.
- `.loc[mask, "city"]` selects cities with missing regions.
- `unique()` removes repeated city names from the error message.

This quality check prevents reporting on data without its required context.

## 4. Groupby: form groups

~~~python
enriched_df.groupby(["region", "city"], as_index=False)
~~~

Rows in each group share region and city. Add `agg` to calculate results:

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

This is **named aggregation**. Its general form is:

~~~python
output_column=("input_column", "operation")
~~~

For example, `("temperature_c", "mean")` calculates the group's mean temperature.

## 5. Round, sort, and check totals

Round means for readability:

~~~python
summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)
~~~

Sort for consistent output order:

~~~python
summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop=True)
~~~

`reset_index(drop=True)` creates a new 0, 1, ... index without keeping the old index as a column.

The report's observation total must equal the merged row count:

~~~python
if summary_df["observation_count"].sum() != len(enriched_df):
    raise ValueError("summary observation count does not match input rows")
~~~

This is one consistency check, not proof that the whole report is correct. Use it together with merge validation and the missing-region check.

## 6. Exercise flow

~~~text
main
  -> read weather_clean.csv and city_lookup.csv
  -> build_summary
       -> merge
       -> check missing regions
       -> groupby + agg
       -> round + sort
       -> check observation total
  -> write summary CSV
  -> print report
~~~

## 7. References

- [pandas merge API](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [pandas merge guide](https://pandas.pydata.org/docs/user_guide/merging.html)
- [pandas groupby guide](https://pandas.pydata.org/docs/user_guide/groupby.html)

Focus on left merge, validate, groupby, and agg. Other join types and pivot tables can wait.
