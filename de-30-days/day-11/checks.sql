-- Day 11: ready-made checks, no TODOs and no table changes.
-- Use the existing weather_day09 database in pgAdmin.
-- Highlight and execute ONE complete statement at a time.

-- Expected: weather_day09. Stop if another database is shown.
SELECT current_database() AS database_name;

-- Run in each new Query Tool tab for consistent timestamp display.
SET TIME ZONE 'Asia/Ho_Chi_Minh';

-- Expected: 4 cities, 8 observations, temperature sum 251.0.
SELECT
    (SELECT COUNT(*) FROM cities) AS city_count,
    (SELECT COUNT(*) FROM weather_observations) AS observation_count,
    (SELECT SUM(temperature_c) FROM weather_observations) AS temperature_sum_c;

-- Expected city_name / count / first_observed_at / last_observed_at:
-- Da Nang / 2 / 2026-09-18 09:00+07 / 2026-09-18 12:00+07
-- Hanoi / 3 / 2026-09-18 09:00+07 / 2026-09-19 09:00+07
-- Ho Chi Minh City / 3 / 2026-09-18 09:00+07 / 2026-09-19 09:00+07
-- Hue / 0 / NULL / NULL
SELECT
    c.city_name,
    COUNT(o.observed_at) AS observation_count,
    MIN(o.observed_at) AS first_observed_at,
    MAX(o.observed_at) AS last_observed_at
FROM cities AS c
LEFT JOIN weather_observations AS o
    ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name;

-- Expected: eight observations in stable city-name/time order.
SELECT c.city_name, o.observed_at, o.temperature_c, o.humidity_pct
FROM cities AS c
INNER JOIN weather_observations AS o
    ON o.city_id = c.city_id
ORDER BY c.city_name, o.observed_at;
