-- Day 9: write ten SELECT queries on weather_day09.
-- Read guide.md and lesson.md first. setup.sql must already be loaded.
-- Save this file. Execute ONE completed query at a time in pgAdmin.
-- Each TODO is a comment: put real SQL beneath it, ending with a semicolon.
-- Replace each Explanation comment with one English sentence of your own.

-- Q1: SELECT columns and sort.
-- Return city_id, city_name, timezone_name from cities.
-- Sort by city_name ascending. Expected: 4 rows.
-- TODO: write Q1 below.
SELECT 
    city_id,
    city_name,
    timezone_name 
FROM cities
ORDER BY city_name ASC;
-- Q2: Read observations.
-- Return city_id, observed_at, temperature_c, humidity_pct.
-- Sort by city_id ascending, then observed_at ascending. Expected: 8 rows.
-- TODO: write Q2 below.
SELECT 
    city_id, 
    observed_at, 
    temperature_c, 
    humidity_pct
FROM weather_observations
ORDER BY city_id ASC, observed_at ASC;
-- Q3: Filter with two conditions.
-- Return city_id, observed_at, temperature_c, humidity_pct.
-- Keep temperature_c >= 32 AND humidity_pct <= 70.
-- Sort by temperature_c descending, city_id ascending, observed_at ascending.
-- Expected: 4 rows.
-- TODO: write Q3 below.
SELECT 
    city_id, observed_at, temperature_c, humidity_pct
FROM weather_observations
WHERE temperature_c >= 32 AND humidity_pct <= 70
ORDER BY temperature_c DESC, city_id ASC, observed_at ASC;
-- Q4: DISTINCT.
-- Return distinct city_id values from weather_observations, ascending.
-- Expected: 3 rows. Do not read cities for this query.
-- TODO: write Q4 below.
SELECT DISTINCT city_id
FROM weather_observations
ORDER BY city_id ASC;
-- Q5: Hottest two observations.
-- Return city_id, observed_at, temperature_c.
-- Sort by temperature_c descending, city_id ascending, observed_at ascending.
-- Use LIMIT to return exactly 2 rows.
-- TODO: write Q5 below.
SELECT city_id, observed_at, temperature_c
FROM weather_observations
ORDER BY temperature_c DESC, city_id ASC, observed_at ASC
LIMIT 2;
-- Q6: INNER JOIN.
-- Join cities AS c to weather_observations AS o on matching city_id.
-- Return c.city_name, o.observed_at, o.temperature_c, o.humidity_pct.
-- Sort by c.city_name ascending, then o.observed_at ascending.
-- Expected: 8 rows.
-- TODO: write Q6 below.
SELECT
    c.city_name, o.observed_at, o.temperature_c, o.humidity_pct
FROM cities AS c
INNER JOIN weather_observations AS o
ON o.city_id = c.city_id 
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q7: One summary for all observations.
-- Read weather_observations without GROUP BY.
-- Return COUNT(*) AS observation_count,
-- MIN(temperature_c) AS min_temperature_c,
-- MAX(temperature_c) AS max_temperature_c,
-- and AVG(temperature_c) rounded to 2 decimal places AS avg_temperature_c.
-- Expected: 1 row. Use ROUND(AVG(temperature_c), 2).
-- TODO: write Q7 below.
SELECT 
    COUNT(*) AS observation_count,
    MIN(temperature_c) AS min_temperature_c,
    MAX(temperature_c) AS max_temperature_c,
    ROUND(AVG(temperature_c), 2) AS avg_temperature_c
FROM weather_observations;
-- Q8: One summary per city WITH observations.
-- Use INNER JOIN; group by c.city_id, c.city_name.
-- Return city_name, observation_count, avg_temperature_c,
-- min_temperature_c, max_temperature_c. Average rounded to 1 decimal place.
-- Sort by city_name ascending. Expected: 3 rows.
-- TODO: write Q8 below.
SELECT 
    c.city_name, 
    COUNT(o.observed_at) AS observation_count, 
    ROUND(AVG(o.temperature_c), 1) AS avg_temperature_c,
    MIN(o.temperature_c) AS min_temperature_c,
    MAX(o.temperature_c) AS max_temperature_c
FROM cities c
INNER JOIN weather_observations AS o 
ON c.city_id = o.city_id 
GROUP BY c.city_id, c.city_name
ORDER BY city_name ASC;
-- Q9: Filter groups.
-- Use INNER JOIN and group by c.city_id, c.city_name.
-- Return city_name and COUNT(*) AS observation_count.
-- Keep only groups with at least 3 observations; use HAVING.
-- Sort by city_name ascending. Expected: 2 rows.
-- TODO: write Q9 below.
SELECT 
    c.city_name,
    COUNT(o.*) AS observation_count
FROM cities AS c
INNER JOIN weather_observations AS o 
ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
HAVING COUNT(o.*) >= 3
ORDER BY city_name ASC;
-- Q10: Include cities WITHOUT observations.
-- Start from cities AS c; LEFT JOIN weather_observations AS o.
-- Group by c.city_id, c.city_name and sort by c.city_name ascending.
-- Return city_name, COUNT(o.observed_at) AS observation_count,
-- and ROUND(AVG(o.temperature_c), 1) AS avg_temperature_c.
-- Keep NULL averages as NULL. Expected: 4 rows; Hue count = 0.
-- TODO: write Q10 below.
SELECT 
    city_name, 
    COUNT(o.observed_at) AS observation_count,
    ROUND(AVG(o.temperature_c), 1) AS avg_temperature_c
FROM cities AS c 
LEFT JOIN weather_observations AS o 
ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name ASC;


-- Reflection 1: Why does INNER JOIN omit Hue but LEFT JOIN includes it?
-- Your answer: the reason is that a LEFT JOIN include all data form the left table  and look for results in the right table that satisfy the condition(if no match is found, the corresponding fields will have a NULL value)
-- whereas an INNER JOIN includes only matching data and excludes results that do not meet the condition

-- Reflection 2: Why is COUNT(*) wrong for Hue's observation count after LEFT JOIN?
-- Your answer: LEFT JOIN produces one row for Hue with NULL observation fields 
-- COUNT(*)              → 1  (counts the joined row)
-- COUNT(o.observed_at)   → 0  (counts only non-NULL timestamps)

-- Reflection 3: Why use HAVING instead of WHERE for a group count?
-- Your answer: because HAVING using to filter group after grouping, whereas WHERE using to filter data before grouping

-- Reflection 4: Is a NULL average the same as zero degrees? Explain.
-- Your answer: Hue’s average is NULL because there are no temperatures to average. 0°C would mean an actual measured value. AVG ignores NULL inputs, but returns NULL when no non-NULL values exist.
