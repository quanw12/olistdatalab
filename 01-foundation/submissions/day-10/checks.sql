-- Day 10: read-only checks. No TODOs and no table changes.
-- Highlight and execute ONE statement at a time in pgAdmin.
-- Use the existing weather_day09 database; do not create weather_day10.

-- Expected: weather_day09. Stop if this names another database.
SELECT current_database() AS database_name;

-- Run in each new Query Tool tab for consistent timestamp display.
SET TIME ZONE 'Asia/Ho_Chi_Minh';

-- Expected: city_count = 4, observation_count = 8, temperature_sum_c = 251.0.
SELECT
    (SELECT COUNT(*) FROM cities) AS city_count,
    (SELECT COUNT(*) FROM weather_observations) AS observation_count,
    (SELECT SUM(temperature_c) FROM weather_observations) AS temperature_sum_c;

-- Expected: 2026-09-18 -> 6; 2026-09-19 -> 2.
SELECT
    (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date AS local_date,
    COUNT(*) AS observation_count
FROM weather_observations
GROUP BY (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date
ORDER BY local_date;

-- Expected: Da Nang -> 2; Hanoi -> 3; Ho Chi Minh City -> 3; Hue -> 0.
SELECT
    c.city_name,
    COUNT(o.observed_at) AS observation_count
FROM cities AS c
LEFT JOIN weather_observations AS o
    ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name;
