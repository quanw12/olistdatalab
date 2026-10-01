# Day 5 — Join data and build a city report

## Today's goal

Day 4 produced clean weather data. Today, add region information from a lookup table and summarize by city.

~~~text
weather_clean.csv + city_lookup.csv
             -> merge on city
             -> detect cities without a region
             -> groupby region + city
             -> output/city_weather_summary.csv
~~~

In a real pipeline, `weather_clean.csv` would come from Day 4. Today's folder includes a copy so this exercise can run independently.

## Learning order

1. Read [the merge and groupby lesson](lesson.md), sections 1–6.
2. Open `weather_clean.csv` and `city_lookup.csv`. Identify the shared key.
3. Read `summary.py`, especially `main`, to understand input and output.
4. Complete the four TODOs in `build_summary`.
5. Use the matching [hint](help.md) when stuck.
6. Run from `C:\DE Courses\day-05`:

~~~powershell
python summary.py
~~~

## Expected results

~~~text
weather rows: 4
city lookup rows: 3
summary rows: 2
~~~

`output/city_weather_summary.csv`:

~~~csv
region,city,observation_count,avg_temperature_c,min_temperature_c,max_temperature_c,avg_humidity_pct
Central,Da Nang,2,29.8,29.5,30.1,79.5
North,Hanoi,2,32.6,31.2,34.1,75.0
~~~

## Report data contract

Each output row represents **one city in one region**. This is the summary table's **grain**.

| Column | Meaning |
|---|---|
| `region`, `city` | Group being summarized |
| `observation_count` | Number of weather observations in the group |
| `avg_temperature_c` | Mean temperature |
| `min_temperature_c`, `max_temperature_c` | Lowest/highest temperature |
| `avg_humidity_pct` | Mean humidity |

Two required quality checks:

1. No missing `region` after merging.
2. The sum of `observation_count` equals the number of merged weather rows.

## Git checkpoint

When the output is correct, run from `C:\DE Courses`:

~~~powershell
git add README.md roadmap.md day-05
git commit -m "feat(day-05): summarize weather by city"
git push
~~~

## Send after finishing

1. Full output from `python summary.py`.
2. Contents of `output/city_weather_summary.csv`.
3. Your `build_summary` function body.
4. Why is `how="left"` better than `how="inner"` when detecting cities missing from the lookup?
