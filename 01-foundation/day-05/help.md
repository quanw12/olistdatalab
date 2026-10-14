> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 5 hints

Complete `build_summary` one TODO at a time. No for loop is needed.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Step 1: merge</summary>

~~~python
enriched_df = weather_df.merge(
    city_df,
    on="city",
    how="left",
    validate="many_to_one",
)
~~~

</details>

<details>
<summary>Step 2: check for missing regions</summary>

~~~python
missing_region = enriched_df["region"].isna()

if missing_region.any():
    unknown_cities = enriched_df.loc[missing_region, "city"].unique()
    raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
~~~

</details>

<details>
<summary>Step 3: grouping and aggregation</summary>

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

</details>

<details>
<summary>Step 4: finish and return the report</summary>

~~~python
summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)
summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop=True)

if summary_df["observation_count"].sum() != len(enriched_df):
    raise ValueError("summary observation count does not match input rows")

return summary_df
~~~

</details>

<details>
<summary>Troubleshooting</summary>

| Error or symptom | Common cause | Fix |
|---|---|---|
| `MergeError: not a many-to-one merge` | Duplicate city in lookup | Keep one lookup row per city |
| `KeyError: region` | Missing merge or wrong column | Complete Step 1 and use region |
| `city lookup is missing...` | Weather city absent from lookup | Add its lookup entry; do not change the join to hide the error |
| Only one summary row | Wrong grouping columns | Group by both region and city |
| Wrong summary count | Wrong aggregation column or duplicated merged rows | Check many_to_one validation and the final count check |

</details>

<details>
<summary>Building the driver when starting from a blank file</summary>

Define helper functions first; call them from main. A function definition does not execute its body. This small unrelated example shows the syntax:

~~~python
from pathlib import Path

def save_message(text):
    folder = Path("output")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "message.txt").write_text(text, encoding="utf-8")

def main():
    save_message("Practice complete")

if __name__ == "__main__":
    main()
~~~

Read input inside main, pass data to your transformation, validate the result, then write output. Test one helper with a tiny input before connecting all steps. Use print(repr(value)) to inspect an unexpected value; remove temporary prints after debugging. Return data from helpers and print only at the CLI boundary.

For CSV use csv.DictReader/csv.DictWriter (or pandas read_csv/to_csv on Days4–5). For JSON use json.load/json.dump with an opened UTF-8 file. CSV writer files need newline="". JSON datetime values must become ISO strings before serialization. Catch the expected exception around the risky conversion; do not hide every error behind except Exception: pass.

</details>
