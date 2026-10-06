# Day 10 expected results

Use the unchanged Day 9 data: four cities and eight observations. These tables contain expected values, not complete SQL answers. Follow the column order and sorting specified in queries.sql.

Original observed_at values below are displayed at +07. Equivalent UTC displays represent the same instants. local_time is a timestamp without a timezone suffix. Decimal trailing zeros can differ without changing a numeric value. NULL may appear as a blank or a NULL marker in pgAdmin.

## Q1 — Local time and date

| city_name | observed_at | local_time | local_date |
|---|---|---|---|
| Da Nang | 2026-09-18 09:00:00+07 | 2026-09-18 09:00:00 | 2026-09-18 |
| Da Nang | 2026-09-18 12:00:00+07 | 2026-09-18 12:00:00 | 2026-09-18 |
| Hanoi | 2026-09-18 09:00:00+07 | 2026-09-18 09:00:00 | 2026-09-18 |
| Hanoi | 2026-09-18 12:00:00+07 | 2026-09-18 12:00:00 | 2026-09-18 |
| Hanoi | 2026-09-19 09:00:00+07 | 2026-09-19 09:00:00 | 2026-09-19 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 2026-09-18 09:00:00 | 2026-09-18 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 2026-09-18 12:00:00 | 2026-09-18 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 2026-09-19 09:00:00 | 2026-09-19 |

## Q2 — September 18 observations

| city_name | observed_at | temperature_c |
|---|---|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 |

## Q3 — Daily summaries

| local_date | observation_count | avg_temperature_c | min_temperature_c | max_temperature_c |
|---|---:|---:|---:|---:|
| 2026-09-18 | 6 | 31.33 | 29.0 | 34.0 |
| 2026-09-19 | 2 | 31.50 | 31.0 | 32.0 |

September 18 sum: 188.0; September 19 sum: 63.0. Counts sum to 8, temperatures sum to 251.0.

## Q4 — Temperature bands

| city_name | observed_at | temperature_c | temperature_band |
|---|---|---:|---|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | cool |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | warm |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | warm |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | warm |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | warm |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | hot |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | hot |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | warm |

Band totals: cool 1, warm 5, hot 2. These are exercise labels.

## Q5 — Conditional counts

| city_name | observation_count | hot_observation_count |
|---|---:|---:|
| Da Nang | 2 | 0 |
| Hanoi | 3 | 1 |
| Ho Chi Minh City | 3 | 3 |
| Hue | 0 | 0 |

This query's hot condition is >= 32, unlike Q4's hot label at >= 33. Total qualifying observations: 4.

## Q6 — Above the overall average

The actual mean is 251.0 / 8 = 31.375. Compare against the calculated mean, not a typed or rounded version.

| city_name | observed_at | temperature_c |
|---|---|---:|
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 |

## Q7 — Every maximum observation

| city_name | observed_at | temperature_c |
|---|---|---:|
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 |

The fixed dataset has one maximum row. Your equality-to-MAX query must also retain ties if another dataset contains them.

## Q8 — Cities without observations

| city_name |
|---|
| Hue |

## Q9 — Filter a city summary CTE

| city_name | observation_count | avg_temperature_c |
|---|---:|---:|
| Hanoi | 3 | 31.0 |
| Ho Chi Minh City | 3 | 33.0 |

Before the outer filter, the INNER JOIN summary has a third row for Da Nang with count 2 and average 29.5. Hue has no group.

## Q10 — Daily report for all cities

| city_name | report_date | observation_count | avg_temperature_c | max_temperature_c | report_status |
|---|---|---:|---:|---:|---|
| Da Nang | 2026-09-18 | 2 | 29.5 | 30.0 | normal |
| Hanoi | 2026-09-18 | 2 | 31.0 | 32.0 | normal |
| Ho Chi Minh City | 2026-09-18 | 2 | 33.5 | 34.0 | hot |
| Hue | 2026-09-18 | 0 | NULL | NULL | no data |

Report counts sum to 6, matching Q2. The date names the day being reported, even when a city has no measurements for that day. No data is a separate state from a known normal temperature.
