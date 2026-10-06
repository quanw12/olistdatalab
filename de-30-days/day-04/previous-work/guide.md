# Day 4 — Clean CSV data with pandas

## Today's goal

Day 1 cleaned CSV row by row. Today you do similar work with pandas, operating on whole columns.

~~~text
messy_weather.csv -> DataFrame -> normalize types + filter invalid rows
                 -> remove duplicates -> output/clean_weather.csv + report
~~~

Pandas is available in the current Python environment. Check it with:

~~~powershell
python -c "import pandas as pd; print(pd.__version__)"
~~~

## Learning order

1. Read [the pandas lesson](lesson.md), sections 1–7.
2. Open `messy_weather.csv`. Predict which six rows will not appear in the output.
3. Read `main` in `clean_pandas.py` to understand the input, output, and report.
4. Complete the four TODOs in `clean_weather` in order.
5. If stuck, read the matching [hint](help.md), then type the code yourself.
6. Run from `C:\DE Courses\day-04`:

~~~powershell
python clean_pandas.py
~~~

## Expected results

~~~text
input rows: 10
invalid rows: 5
duplicate rows: 1
accepted rows: 4
~~~

`output/clean_weather.csv` should contain four data rows:

~~~csv
city,observed_at,temperature_c,humidity_pct
Hanoi,2026-09-14,31.2,78
Da Nang,2026-09-14,30.1,81
Hanoi,2026-09-15,34.1,72
Da Nang,2026-09-15,29.5,78
~~~

This dataset's humidity column has no missing values and is written as integers. A numeric column with missing values may display values like `78.0` in pandas; the display alone does not make the data incorrect. We will control types more carefully when using databases.

## What you should understand

- A DataFrame is a table in Python.
- A Series is one column of a DataFrame.
- `pd.to_numeric(..., errors="coerce")` converts unparseable values to NaN so you can detect and reject them.
- A Boolean mask contains True/False values used to select rows.
- `drop_duplicates` handles duplicates without creating your own set.

## Git checkpoint

When the output is correct, run from `C:\DE Courses`:

~~~powershell
git add requirements.txt roadmap.md day-04
git commit -m "feat(day-04): clean weather data with pandas"
git push
~~~

## Send after finishing

1. Full report from `python clean_pandas.py`.
2. Contents of `output/clean_weather.csv`.
3. Your `clean_weather` function body.
4. Why is `errors="coerce"` useful compared with stopping at `not_available`?
