> Refreshed workflow: write DDL in schema.sql, run it on weather_day09, then run the provided fixture.sql once. The fixture load is now separate from your table definitions. Follow guide.md for this order.

# Day 12 — Expected structure and results

Compare these after attempting the design and queries. The data is the fixed Day 9 fixture. Set the Query Tool display timezone to Asia/Ho_Chi_Minh.

## 1. Model structure

- Database: weather_day09.
- Schema: day12_mart.
- Tables: dim_city, dim_date, fact_weather.
- dim_city: one row per city; **4 rows**, including Hue.
- dim_date: one row per calendar date; **2 rows**.
- fact_weather: one observed instant for one city, from the fixture's single provider; **8 rows**.
- fact_weather.city_key references dim_city.city_key.
- fact_weather.observation_date references dim_date.calendar_date.
- Both fact foreign-key columns are NOT NULL.
- The fact has a generated observation_key primary key and UNIQUE (city_key, observed_at).
- Each dimension row can relate to zero or many facts; each fact must relate to exactly one city and one date.

Generated key numbers are not part of the expected report values. Verify their relationships rather than hard-coding IDs. The date dimension in this exercise contains only observed dates.

Your diagram and dictionary should agree with the actual SQL. Constraint names can differ; their columns and rules should match schema.sql's requirements.

## 2. Checks

| Check | Expected |
|---|---|
| B1 | weather_day09; 4 source cities; 8 observations; sum 251.0; one provider, open-meteo-demo |
| B2 | Da Nang 2; Hanoi 3; Ho Chi Minh City 3; Hue 0 |
| A1 | 4 dimension cities; 2 dimension dates; 8 facts |
| A2 | The two calendar rows below |
| A3 | Zero duplicate groups |
| A4 | missing_reference_count = 0 |
| A5 | mismatch_count = 0 |
| A6 | fact_count = 8 and joined_count = 8 |

| calendar_date | calendar_year | calendar_month | iso_weekday |
|---|---:|---:|---:|
| 2026-09-18 | 2026 | 9 | 5 |
| 2026-09-19 | 2026 | 9 | 6 |

## 3. Q1 — Individual observations

Exactly **8 rows**, sorted by city and observed_at. PostgreSQL may display the timestamp differently while representing the same instant; the table below uses +07.

| city_name | calendar_date | observed_at | temperature_c | humidity_pct |
|---|---|---|---:|---:|
| Da Nang | 2026-09-18 | 2026-09-18 09:00:00+07 | 29.0 | 85 |
| Da Nang | 2026-09-18 | 2026-09-18 12:00:00+07 | 30.0 | 80 |
| Hanoi | 2026-09-18 | 2026-09-18 09:00:00+07 | 30.0 | 80 |
| Hanoi | 2026-09-18 | 2026-09-18 12:00:00+07 | 32.0 | 70 |
| Hanoi | 2026-09-19 | 2026-09-19 09:00:00+07 | 31.0 | 75 |
| Ho Chi Minh City | 2026-09-18 | 2026-09-18 09:00:00+07 | 33.0 | 65 |
| Ho Chi Minh City | 2026-09-18 | 2026-09-18 12:00:00+07 | 34.0 | 60 |
| Ho Chi Minh City | 2026-09-19 | 2026-09-19 09:00:00+07 | 32.0 | 70 |

## 4. Q2 — Daily report

Exactly **5 rows**. The result's grain is one city on one observed local calendar date. The stored fact remains at observation grain.

| city_name | calendar_date | observation_count | avg_temperature_c | avg_humidity_pct |
|---|---|---:|---:|---:|
| Da Nang | 2026-09-18 | 2 | 29.50 | 82.50 |
| Hanoi | 2026-09-18 | 2 | 31.00 | 75.00 |
| Hanoi | 2026-09-19 | 1 | 31.00 | 75.00 |
| Ho Chi Minh City | 2026-09-18 | 2 | 33.50 | 62.50 |
| Ho Chi Minh City | 2026-09-19 | 1 | 32.00 | 70.00 |

Hue has no observations and therefore no city/date group in this inner-join report.

## 5. Q3 — All cities

Exactly **4 rows**, including Hue.

| city_name | observation_count | avg_temperature_c |
|---|---:|---:|
| Da Nang | 2 | 29.50 |
| Hanoi | 3 | 31.00 |
| Ho Chi Minh City | 3 | 33.00 |
| Hue | 0 | NULL |

These are averages over recorded observations. They are not time-weighted averages, and the data does not represent complete daily coverage.

## 6. Reasoning checks

Before submitting, confirm that your answers explain:

- Why two observations on one date can coexist in the fact.
- Why a generated row key alone does not prevent duplicate observations.
- Why source IDs and warehouse IDs can differ.
- Why a date dimension supports grouping without summarizing the stored measurements.
- Why temperature sums do not describe a useful combined temperature.
- Why missing data remains missing rather than becoming zero.

For unequal-size groups, weight each group's unrounded average by its observation count. Prefer calculating directly from the atomic observations when they are available. Rounding is for the final display.
