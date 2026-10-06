-- Day 10: use the existing weather_day09 database in pgAdmin.
-- Read guide.md and lesson.md; run checks.sql before starting.
-- Write your own SQL under each TODO. End each complete statement with ;.
-- Save this file and run ONE query at a time, including its entire WITH block.
-- Write one English sentence after each Explanation comment.

-- Q1: Show local time and date for each observation.
-- INNER JOIN cities AS c to weather_observations AS o on city_id.
-- Return c.city_name, o.observed_at,
-- o.observed_at AT TIME ZONE c.timezone_name AS local_time,
-- and the date part of that local_time AS local_date.
-- Repeat the conversion expression before ::date; an alias is not a variable.
-- Sort by c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- TODO: write Q1 below.
SELECT 
    c.city_name,
    o.observed_at,
    (o.observed_at AT TIME ZONE c.timezone_name) AS local_time,
    (o.observed_at AT TIME ZONE c.timezone_name)::date AS local_date
FROM cities AS c 
INNER JOIN weather_observations AS o 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;

-- Q2: Select all observations on September 18 in Vietnam's timezone.
-- Return city_name, observed_at, temperature_c using an INNER JOIN.
-- Use observed_at >= TIMESTAMPTZ '2026-09-18 00:00:00+07:00'
-- AND observed_at < TIMESTAMPTZ '2026-09-19 00:00:00+07:00'.
-- Sort by c.city_name ASC, o.observed_at ASC. Expected: 6 rows.
-- TODO: write Q2 below.
SELECT
    c.city_name, o.observed_at, o.temperature_c
FROM cities AS c 
INNER JOIN weather_observations AS o 
ON c.city_id = o.city_id
WHERE o.observed_at >= TIMESTAMPTZ '2026-09-18 00:00:00+07:00'
AND o.observed_at < TIMESTAMPTZ '2026-09-19 00:00:00+07:00'
ORDER BY c.city_name ASC, o.observed_at ASC;

-- Q3: Summarize observations by local calendar date.
-- Read weather_observations; use the explicit Asia/Ho_Chi_Minh timezone.
-- Return local_date, COUNT(*) AS observation_count,
-- ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
-- MIN(temperature_c) AS min_temperature_c,
-- MAX(temperature_c) AS max_temperature_c.
-- GROUP BY the same local-date expression; sort by local_date ASC.
-- Expected: 2 rows. Do not group by city_id or the full timestamp.
-- TODO: write Q3 below.
SELECT 
    (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date AS local_date,
    COUNT(*) AS observation_count,
    ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
    MIN(temperature_c) AS min_temperature_c,
    MAX(temperature_c) AS max_temperature_c
FROM weather_observations 
GROUP BY (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date
ORDER BY (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date ASC;


-- Q4: Label each observation using CASE.
-- INNER JOIN to return city_name, observed_at, temperature_c, temperature_band.
-- temperature_band rules: below 30 -> 'cool'; 30 up to but excluding 33 -> 'warm';
-- 33 or above -> 'hot'. Use CASE WHEN ... THEN ... ELSE ... END.
-- Sort by c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- These are exercise labels, not official weather categories.
-- TODO: write Q4 below.
SELECT 
    c.city_name, 
    o.observed_at, 
    o.temperature_c, 
    CASE 
        WHEN o.temperature_c < 30 THEN 'cool'
        WHEN o.temperature_c < 33 THEN 'warm'
        ELSE 'hot'
    END AS temperature_band
FROM weather_observations AS o 
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q5: Count hot observations per city, retaining Hue.
-- Start from cities AS c and LEFT JOIN weather_observations AS o on city_id.
-- Return city_name, COUNT(o.observed_at) AS observation_count,
-- SUM(CASE WHEN o.temperature_c >= 32 THEN 1 ELSE 0 END) AS hot_observation_count.
-- GROUP BY c.city_id, c.city_name; sort by c.city_name ASC.
-- Expected: 4 rows. Hue has both counts = 0.
-- The >= 32 threshold here differs deliberately from Q4's >= 33 label.
-- TODO: write Q5 below.
SELECT 
	c.city_name,
	COUNT(o.observed_at) AS observation_count,
	SUM(CASE WHEN o.temperature_c >= 32 THEN 1 ELSE 0 END) AS hot_observation_count
FROM cities AS c
LEFT JOIN weather_observations AS o
ON c.city_id = o.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name ASC;

-- Q6: Find observations above the overall average temperature.
-- INNER JOIN to return city_name, observed_at, temperature_c.
-- Use a scalar subquery: SELECT AVG(temperature_c) FROM weather_observations.
-- Compare o.temperature_c > (the subquery), with no ROUND in the comparison.
-- Do not type the average as a number or average separately for each city.
-- Sort by temperature_c DESC, c.city_name ASC, o.observed_at ASC.
-- Expected: 4 rows.
-- TODO: write Q6 below.
SELECT 
    c.city_name, 
    o.observed_at, 
    o.temperature_c
FROM weather_observations AS o 
INNER JOIN cities AS c 
ON c.city_id = o.city_id
WHERE o.temperature_c > (
    SELECT AVG(temperature_c) FROM weather_observations)
ORDER BY temperature_c DESC, c.city_name ASC, o.observed_at ASC;
-- Q7: Find EVERY observation equal to the overall maximum temperature.
-- INNER JOIN to return city_name, observed_at, temperature_c.
-- Use equality with a scalar subquery containing MAX(temperature_c).
-- Do not use LIMIT 1: tied maxima must all be retained.
-- Sort by c.city_name ASC, o.observed_at ASC. Expected: 1 row in this dataset.
-- TODO: write Q7 below.
SELECT 
    c.city_name, 
    o.observed_at, 
    o.temperature_c
FROM weather_observations AS o 
INNER JOIN cities AS c 
ON c.city_id = o.city_id
WHERE o.temperature_c = (
    SELECT MAX(temperature_c) FROM weather_observations)
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q8: Find cities that have no weather observations.
-- Read cities AS c; return c.city_name only.
-- Use NOT EXISTS with a subquery on weather_observations AS o,
-- correlated using WHERE o.city_id = c.city_id.
-- Sort by c.city_name ASC. Expected: 1 row.
-- TODO: write Q8 below.
SELECT c.city_name
FROM cities AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM weather_observations AS o
    WHERE o.city_id = c.city_id
)
ORDER BY c.city_name ASC;

-- Q9: Create a city summary CTE, then filter it.
-- WITH city_summary AS (...): use an INNER JOIN and GROUP BY c.city_id, c.city_name.
-- The CTE returns city_name, COUNT(*) AS observation_count,
-- and AVG(o.temperature_c) AS avg_temperature_c. Keep its average unrounded.
-- The final SELECT reads city_summary, returns city_name, observation_count,
-- and ROUND(avg_temperature_c, 1) AS avg_temperature_c.
-- Filter the CTE rows with WHERE avg_temperature_c >= 31.
-- Sort by city_name ASC. Expected: 2 rows.
-- TODO: write Q9 below.
WITH city_summary AS(
    SELECT 
        c.city_name,
        COUNT(*) AS observation_count,
        AVG(o.temperature_c) AS avg_temperature_c
    FROM weather_observations o
    INNER JOIN cities c ON c.city_id = o.city_id
    GROUP BY c.city_id, c.citY_name
)
SELECT
    city_name,
    observation_count,
    ROUND(avg_temperature_c, 1) AS avg_temperature_c
FROM city_summary 
WHERE avg_temperature_c >= 31
ORDER BY city_name ASC;
-- Q10: Build a daily weather report for ALL four cities.
-- Step 1: WITH daily_summary AS (...).
-- Read weather_observations; apply Q2's September 18 timestamp bounds.
-- and return city_id, COUNT(*) AS observation_count,
-- AVG(temperature_c) AS avg_temperature_c, MAX(temperature_c) AS max_temperature_c.
-- Step 2: SELECT from cities AS c LEFT JOIN daily_summary AS d on city_id.
-- Return these columns in this order:
--   c.city_name,
--   DATE '2026-09-18' AS report_date,
--   COALESCE(d.observation_count, 0) AS observation_count,
--   ROUND(d.avg_temperature_c, 1) AS avg_temperature_c,
--   d.max_temperature_c,
--   a CASE expression AS report_status.
-- report_status rules, in this order:
--   d.observation_count IS NULL -> 'no data';
--   d.max_temperature_c >= 33 -> 'hot';
--   otherwise -> 'normal'.
-- Keep missing temperature values as NULL. Sort by c.city_name ASC.
-- Expected: 4 rows. Hue has 0, NULL, NULL, and 'no data'.
-- Do not add a final WHERE condition that removes Hue.
-- TODO: write Q10 below.
WITH daily_summary AS(
	SELECT 
		city_id, 
		COUNT(*) AS observation_count,
		AVG(temperature_c) AS avg_temperature_c, 
		MAX(temperature_c) AS max_temperature_c
	FROM weather_observations
	WHERE observed_at >= TIMESTAMPTZ '2026-09-18 00:00:00+07:00'
	AND observed_at < TIMESTAMPTZ '2026-09-19 00:00:00+07:00'
	GROUP BY city_id
)
SELECT 
	c.city_name,
	DATE '2026-09-18' AS report_date,
	COALESCE(d.observation_count, 0) AS observation_count,
	ROUND(d.avg_temperature_c, 1) AS avg_temperature_c,
    d.max_temperature_c,
	CASE 
		WHEN d.observation_count IS NULL THEN 'no data'
		WHEN d.max_temperature_c >= 33 THEN 'hot'
		ELSE 'normal'
	END AS report_status
FROM cities c
LEFT JOIN daily_summary d on c.city_id = d.city_id
ORDER BY c.city_name ASC;
-- Reflection 1: Why convert observed_at to a named timezone before taking ::date?
-- Your answer: because timezone is fixed in "UTC", we must convert observed_at to how to correct with our timezone(UTC+7)

-- Reflection 2: Why use < the next day's midnight rather than BETWEEN both midnights?
-- Your answer: because we don't calculate precisely at the moment it crosses midnight, since the new day has already begun.

-- Reflection 3: Does city_summary become a permanent table after Q9? Explain.
-- Your answer: No, CTE means Common Table Expression. WITH gives an intermediate query result a name within one statement

-- Reflection 4: In Q10, why replace a missing observation count with 0 but keep a missing average as NULL?
-- Your answer: Regarding the quantity, reporting it as 0 when there is none makes it cleaner for the reader; however, since the average temperature is a data point, it should be explicitly labeled as NULL—otherwise, people might assume the average temperature is actually 0.
