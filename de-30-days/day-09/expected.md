# Day 9 expected results

Compare your results after writing each query. These are values and ordering, not complete SQL answers. Use the fixed data in setup.sql and the sort order specified in queries.sql. Decimal display such as 31.0 versus 31.00 does not change the numeric value.

Timestamps below use Asia/Ho_Chi_Minh, offset +07. Equivalent UTC timestamps represent the same instants. NULL may appear as a blank or a NULL marker in pgAdmin.

## Q1 — Four cities, ordered by name

| city_id | city_name | timezone_name |
|---:|---|---|
| 2 | Da Nang | Asia/Ho_Chi_Minh |
| 1 | Hanoi | Asia/Ho_Chi_Minh |
| 3 | Ho Chi Minh City | Asia/Ho_Chi_Minh |
| 4 | Hue | Asia/Ho_Chi_Minh |

## Q2 — Eight observations, ordered by city ID and time

| city_id | observed_at | temperature_c | humidity_pct |
|---:|---|---:|---:|
| 1 | 2026-09-18 09:00:00+07 | 30.0 | 80 |
| 1 | 2026-09-18 12:00:00+07 | 32.0 | 70 |
| 1 | 2026-09-19 09:00:00+07 | 31.0 | 75 |
| 2 | 2026-09-18 09:00:00+07 | 29.0 | 85 |
| 2 | 2026-09-18 12:00:00+07 | 30.0 | 80 |
| 3 | 2026-09-18 09:00:00+07 | 33.0 | 65 |
| 3 | 2026-09-18 12:00:00+07 | 34.0 | 60 |
| 3 | 2026-09-19 09:00:00+07 | 32.0 | 70 |

## Q3 — Four hot, lower-humidity observations

| city_id | observed_at | temperature_c | humidity_pct |
|---:|---|---:|---:|
| 3 | 2026-09-18 12:00:00+07 | 34.0 | 60 |
| 3 | 2026-09-18 09:00:00+07 | 33.0 | 65 |
| 1 | 2026-09-18 12:00:00+07 | 32.0 | 70 |
| 3 | 2026-09-19 09:00:00+07 | 32.0 | 70 |

## Q4 — Three distinct observed city IDs

| city_id |
|---:|
| 1 |
| 2 |
| 3 |

## Q5 — Two hottest observations

| city_id | observed_at | temperature_c |
|---:|---|---:|
| 3 | 2026-09-18 12:00:00+07 | 34.0 |
| 3 | 2026-09-18 09:00:00+07 | 33.0 |

## Q6 — Eight observations with names

| city_name | observed_at | temperature_c | humidity_pct |
|---|---|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 85 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 80 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 80 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 70 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 75 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 65 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 60 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 70 |

## Q7 — One overall summary

| observation_count | min_temperature_c | max_temperature_c | avg_temperature_c |
|---:|---:|---:|---:|
| 8 | 29.0 | 34.0 | 31.38 |

Temperature sum is 251.0; 251.0 / 8 = 31.375, rounded to 31.38.

## Q8 — Three observed-city summaries

| city_name | observation_count | avg_temperature_c | min_temperature_c | max_temperature_c |
|---|---:|---:|---:|---:|
| Da Nang | 2 | 29.5 | 29.0 | 30.0 |
| Hanoi | 3 | 31.0 | 30.0 | 32.0 |
| Ho Chi Minh City | 3 | 33.0 | 32.0 | 34.0 |

The counts sum to 8. Hue is absent because the INNER JOIN has no match for it.

## Q9 — Two cities with at least three observations

| city_name | observation_count |
|---|---:|
| Hanoi | 3 |
| Ho Chi Minh City | 3 |

## Q10 — All four city summaries

| city_name | observation_count | avg_temperature_c |
|---|---:|---:|
| Da Nang | 2 | 29.5 |
| Hanoi | 3 | 31.0 |
| Ho Chi Minh City | 3 | 33.0 |
| Hue | 0 | NULL |

Hue's average is missing, not zero. All reported observation counts still sum to 8.
