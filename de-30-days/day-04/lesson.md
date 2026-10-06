> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in previous-work/.

# Day 4 lesson: clean whole columns with pandas

## 1. Why pandas?

Day 1 used for loops, conditions, and a set to clean one CSV row at a time. That is useful for understanding pipeline logic.

Pandas works well with tables. Instead of processing one row, you can say "convert this whole column to numbers" or "keep rows that satisfy all conditions".

~~~text
CSV                 DataFrame
city,temperature    a table of rows and columns
Hanoi,31.2          filter and process whole columns
~~~

Pandas makes table operations shorter; you still need a data contract.

## 2. DataFrame and Series

~~~python
import pandas as pd

df = pd.read_csv("messy_weather.csv")
~~~

`df` is a **DataFrame**, the whole table. Select a column:

~~~python
temperature = df["temperature_c"]
~~~

`temperature` is a **Series**, a labelled sequence corresponding to that column.

Inspect unfamiliar data:

~~~python
print(df.head())
print(df.dtypes)
print(df.info())
~~~

- `head()` shows the first few rows.
- `dtypes` shows the current column types.
- `info()` reports non-null counts and types.

## 3. Missing values and NaN

CSV is text. An empty cell or an unparseable numeric value may become NaN in pandas, marking a missing numeric value.

~~~python
pd.isna(df["temperature_c"])
df["temperature_c"].isna()
df["temperature_c"].notna()
~~~

These produce a True/False Series.

| CSV value | After numeric conversion with errors="coerce" |
|---|---|
| `31.2` | `31.2` |
| `not_available` | NaN |
| Empty cell | NaN |

Your pipeline can then apply its own rejection rules instead of stopping at the first bad value.

## 4. Normalize columns

### Clean text

~~~python
df["city"] = df["city"].str.strip()
~~~

`.str` provides string methods for the Series. `.strip()` removes surrounding whitespace from each value.

### Convert numbers

~~~python
df["temperature_c"] = pd.to_numeric(
    df["temperature_c"],
    errors="coerce",
)
~~~

`float(...)` converts one value; `pd.to_numeric` converts the whole Series.

### Convert dates

~~~python
df["observed_at"] = pd.to_datetime(
    df["observed_at"],
    format="%Y-%m-%d",
    errors="coerce",
)
~~~

Valid dates become pandas datetime values. Missing or invalid dates become NaT, the missing datetime marker.

## 5. Boolean masks: conditions for a column

Ordinary Python checks a single value:

~~~python
if 0 <= humidity <= 100:
    ...
~~~

Pandas applies a condition to a Series:

~~~python
df["humidity_pct"].between(0, 100)
~~~

~~~text
0     True
1     True
2    False
...
~~~

Combine conditions with `&`. Use parentheses around the combined expression; comparison expressions need parentheses when combined with these operators.

~~~python
valid_rows = (
    df["city"].notna()
    & df["city"].ne("")
    & df["observed_at"].notna()
    & df["temperature_c"].between(-50, 60)
    & df["humidity_pct"].between(0, 100)
    & df["humidity_pct"].mod(1).eq(0)
)
~~~

The **mask** is True for accepted rows and False for rejected rows.

Count invalid rows:

~~~python
invalid_rows = int((~valid_rows).sum())
~~~

`~` reverses the mask. Summing Boolean values counts True values, because True contributes 1 and False contributes 0.

## 6. Filter, copy, and remove duplicates

~~~python
candidate_df = df.loc[valid_rows].copy()
~~~

`.loc[valid_rows]` selects rows marked True. `copy()` gives you a separate table to modify without changing the original.

Deduplicate by city and date:

~~~python
before_deduplicate = len(candidate_df)
clean_df = candidate_df.drop_duplicates(
    subset=["city", "observed_at"],
    keep="first",
).copy()
duplicate_rows = before_deduplicate - len(clean_df)
~~~

`subset` defines the duplicate key. `keep="first"` keeps the first valid occurrence, matching Day 1's rule.

## 7. Prepare output

Convert datetime values to clear date text:

~~~python
clean_df["observed_at"] = clean_df["observed_at"].dt.strftime("%Y-%m-%d")
~~~

Write CSV:

~~~python
clean_df.to_csv(output_path, index=False)
~~~

`index=False` prevents pandas from writing its row index as an extra CSV column.

## 8. Exercise flow

~~~text
main
  -> pd.read_csv: CSV to DataFrame
  -> clean_weather
       -> copy table
       -> normalize text, numbers, dates
       -> build valid_rows
       -> filter invalid rows
       -> remove duplicates
       -> return clean_df and two counts
  -> to_csv: write output
  -> print: show report
~~~

The function returns three values:

~~~python
clean_df, invalid_rows, duplicate_rows = clean_weather(raw_df)
~~~

This is tuple unpacking, like Day 1's `clean, rejection_reason = clean_row(raw_row)`.

## 9. References

- [pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [pandas: Missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas: read_csv API](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

Read what you need, then return to the exercise. Grouping and merging come in Day 5.
