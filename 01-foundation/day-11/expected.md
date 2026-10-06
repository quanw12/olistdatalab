# Day 11 expected results

Use the unchanged weather_day09 data. These tables show expected values and ordering, not full query answers. Original observed_at values are shown at +07; an equivalent UTC display represents the same instant. NULL may display as a blank or a NULL marker. Extra trailing decimal zeros do not change a number.

## Q1 — City average beside each observation

| city_name | observed_at | temperature_c | city_avg_temperature_c |
|---|---|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 29.5 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 29.5 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 31.0 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 31.0 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 31.0 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 33.0 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 33.0 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 33.0 |

Eight observation rows remain; each city's full average repeats beside its observations.

## Q2 — Chronological observation numbers

| city_name | observed_at | temperature_c | observation_number |
|---|---|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 1 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 2 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 1 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 2 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 3 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 1 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 2 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 3 |

## Q3 — Latest observation for each observed city

| city_name | observed_at | temperature_c |
|---|---|---:|
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 |

Hue is absent because this query starts with observed cities through an INNER JOIN.

## Q4 — Global temperature ranks

| city_name | observed_at | temperature_c | temperature_rank | temperature_dense_rank |
|---|---|---:|---:|---:|
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 1 | 1 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 2 | 2 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 3 | 3 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 3 | 3 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 5 | 4 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 6 | 5 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 6 | 5 |
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 8 | 6 |

Equal temperatures have equal ranks. The final display sort resolves their row order without changing the ranking windows.

## Q5 — Previous temperature and change

| city_name | observed_at | temperature_c | previous_temperature_c | temperature_change_c |
|---|---|---:|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | NULL | NULL |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 29.0 | 1.0 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | NULL | NULL |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 30.0 | 2.0 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 32.0 | -1.0 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | NULL | NULL |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 33.0 | 1.0 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 34.0 | -2.0 |

There are three missing predecessors: one for each observed city's first row. A NULL change means no comparison is available.

## Q6 — Trailing average and frame size

| city_name | observed_at | temperature_c | rolling_avg_3_c | frame_row_count |
|---|---|---:|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 29.00 | 1 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 29.50 | 2 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 30.00 | 1 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 31.00 | 2 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 31.00 | 3 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 33.00 | 1 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 33.50 | 2 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 33.00 | 3 |

The first frames are partial, not padded with zero. The explicit three-observation frame is required even though this fixture contains no fourth observation within a city.

In lesson.md's four-row demo, the rolling means must be 10.00, 15.00, 20.00, 30.00, with frame counts 1, 2, 3, 3. The unbounded running means are 10.00, 15.00, 20.00, 25.00.

## Q7 — Maximum seen so far

| city_name | observed_at | temperature_c | running_max_temperature_c |
|---|---|---:|---:|
| Da Nang | 2026-09-18 09:00:00+07 | 29.0 | 29.0 |
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 30.0 |
| Hanoi | 2026-09-18 09:00:00+07 | 30.0 | 30.0 |
| Hanoi | 2026-09-18 12:00:00+07 | 32.0 | 32.0 |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 32.0 |
| Ho Chi Minh City | 2026-09-18 09:00:00+07 | 33.0 | 33.0 |
| Ho Chi Minh City | 2026-09-18 12:00:00+07 | 34.0 | 34.0 |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 34.0 |

The maximum never decreases within a city's chronological history.

## Q8 — Latest-weather trend report for all cities

| city_name | observed_at | temperature_c | previous_temperature_c | temperature_change_c | rolling_avg_3_c | trend_status |
|---|---|---:|---:|---:|---:|---|
| Da Nang | 2026-09-18 12:00:00+07 | 30.0 | 29.0 | 1.0 | 29.50 | warming |
| Hanoi | 2026-09-19 09:00:00+07 | 31.0 | 32.0 | -1.0 | 31.00 | cooling |
| Ho Chi Minh City | 2026-09-19 09:00:00+07 | 32.0 | 34.0 | -2.0 | 33.00 | cooling |
| Hue | NULL | NULL | NULL | NULL | NULL | no data |

Latest means latest available per city: the cities' timestamps do not have to match. The trend compares the latest two available measurements; it is not a forecast. The rolling average uses each city's history before the latest-row selection.
