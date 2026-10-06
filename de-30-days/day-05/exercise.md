# Day 05 assignment

Read weather_clean.csv and city_lookup.csv. Implement build_summary(weather, lookup). Validate that lookup city names are unique, then LEFT JOIN on city. Detect missing regions and raise a clear error before grouping. Group by region/city, returning observation_count, avg/min/max_temperature_c and avg_humidity_pct. Round displayed averages to one decimal, sort by region then city, and write output/city_weather_summary.csv without an index. Assert sum of counts equals input weather rows.

## Deliverables

- Your implementation in `summary.py`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.
