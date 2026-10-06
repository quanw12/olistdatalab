> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in previous-work/.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 4 hints

Complete `clean_weather` one TODO at a time. These examples use column operations; no for loop is needed.

## Step 1: copy and normalize text

~~~python
df = raw_df.copy()
df["city"] = df["city"].str.strip()
~~~

`copy()` preserves `raw_df` so you can compare input and output.

## Step 2: convert types

~~~python
df["observed_at"] = pd.to_datetime(
    df["observed_at"],
    format="%Y-%m-%d",
    errors="coerce",
)
df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors="coerce")
df["humidity_pct"] = pd.to_numeric(df["humidity_pct"], errors="coerce")
~~~

## Step 3: filter invalid rows

~~~python
valid_rows = (
    df["city"].notna()
    & df["city"].ne("")
    & df["observed_at"].notna()
    & df["temperature_c"].between(-50, 60)
    & df["humidity_pct"].between(0, 100)
    & df["humidity_pct"].mod(1).eq(0)
)
invalid_rows = int((~valid_rows).sum())
candidate_df = df.loc[valid_rows].copy()
~~~

## Step 4: remove duplicates, format dates, and return

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

## Building the driver when starting from a blank file

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

A whitespace-only city becomes an empty string after strip; ne("") rejects it. mod(1).eq(0) requires whole-number humidity, so72.5 cannot be silently accepted. The bounded temperature mask rejects infinity and missing values.
