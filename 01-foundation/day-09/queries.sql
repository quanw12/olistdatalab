-- Day 9: write ten SELECT queries on weather_day09.
-- Read guide.md and lesson.md first. setup.sql must already be loaded.
-- Save this file. Execute ONE completed query at a time in pgAdmin.
-- Each TODO is a comment: put real SQL beneath it, ending with a semicolon.
-- Replace each Explanation comment with one English sentence of your own.

-- Q1: SELECT columns and sort.
-- Return city_id, city_name, timezone_name from cities.
-- Sort by city_name ascending. Expected: 4 rows.
-- TODO: write Q1 below.


-- Q2: Read observations.
-- Return city_id, observed_at, temperature_c, humidity_pct.
-- Sort by city_id ascending, then observed_at ascending. Expected: 8 rows.
-- TODO: write Q2 below.


-- Q3: Filter with two conditions.
-- Return city_id, observed_at, temperature_c, humidity_pct.
-- Keep temperature_c >= 32 AND humidity_pct <= 70.
-- Sort by temperature_c descending, city_id ascending, observed_at ascending.
-- Expected: 4 rows.
-- TODO: write Q3 below.


-- Q4: DISTINCT.
-- Return distinct city_id values from weather_observations, ascending.
-- Expected: 3 rows. Do not read cities for this query.
-- TODO: write Q4 below.


-- Q5: Hottest two observations.
-- Return city_id, observed_at, temperature_c.
-- Sort by temperature_c descending, city_id ascending, observed_at ascending.
-- Use LIMIT to return exactly 2 rows.
-- TODO: write Q5 below.


-- Q6: INNER JOIN.
-- Join cities AS c to weather_observations AS o on matching city_id.
-- Return c.city_name, o.observed_at, o.temperature_c, o.humidity_pct.
-- Sort by c.city_name ascending, then o.observed_at ascending.
-- Expected: 8 rows.
-- TODO: write Q6 below.


-- Q7: One summary for all observations.
-- Read weather_observations without GROUP BY.
-- Return COUNT(*) AS observation_count,
-- MIN(temperature_c) AS min_temperature_c,
-- MAX(temperature_c) AS max_temperature_c,
-- and AVG(temperature_c) rounded to 2 decimal places AS avg_temperature_c.
-- Expected: 1 row. Use ROUND(AVG(temperature_c), 2).
-- TODO: write Q7 below.


-- Q8: One summary per city WITH observations.
-- Use INNER JOIN; group by c.city_id, c.city_name.
-- Return city_name, observation_count, avg_temperature_c,
-- min_temperature_c, max_temperature_c. Average rounded to 1 decimal place.
-- Sort by city_name ascending. Expected: 3 rows.
-- TODO: write Q8 below.


-- Q9: Filter groups.
-- Use INNER JOIN and group by c.city_id, c.city_name.
-- Return city_name and COUNT(*) AS observation_count.
-- Keep only groups with at least 3 observations; use HAVING.
-- Sort by city_name ascending. Expected: 2 rows.
-- TODO: write Q9 below.


-- Q10: Include cities WITHOUT observations.
-- Start from cities AS c; LEFT JOIN weather_observations AS o.
-- Group by c.city_id, c.city_name and sort by c.city_name ascending.
-- Return city_name, COUNT(o.observed_at) AS observation_count,
-- and ROUND(AVG(o.temperature_c), 1) AS avg_temperature_c.
-- Keep NULL averages as NULL. Expected: 4 rows; Hue count = 0.
-- TODO: write Q10 below.




-- Reflection 1: Why does INNER JOIN omit Hue but LEFT JOIN includes it?
-- Your answer:

-- Reflection 2: Why is COUNT(*) wrong for Hue's observation count after LEFT JOIN?
-- Your answer:

-- Reflection 3: Why use HAVING instead of WHERE for a group count?
-- Your answer:

-- Reflection 4: Is a NULL average the same as zero degrees? Explain.
-- Your answer:
