# Day 04 assignment

Read messy_weather.csv into a DataFrame. Implement clean_weather(df): normalize city whitespace; coerce numeric/date columns; reject missing/invalid values and humidity outside 0..100 or fractional. Temperature must be finite and in -50..60. Filter invalid rows BEFORE removing duplicates by city/date, keeping the first valid row. Return clean data and report counts. Write output/clean_weather.csv with no index and YYYY-MM-DD dates. Print input, invalid, duplicate, and accepted counts.

## Deliverables

- Your implementation in `clean_pandas.py`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.
