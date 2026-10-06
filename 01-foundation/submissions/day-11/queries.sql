-- Day 11: use the unchanged weather_day09 database in pgAdmin.
-- Read guide.md and the matching lesson.md section before each exercise.
-- Write SQL under each TODO; end every complete statement with ;.
-- Run the entire WITH block and final SELECT together when using a CTE.
-- Keep an Explanation sentence in your own English after each query.

-- Q1: Keep each observation and show its city's full average.
-- INNER JOIN cities AS c to weather_observations AS o on city_id.
-- Return c.city_name, o.observed_at, o.temperature_c,
-- ROUND(AVG(o.temperature_c) OVER (PARTITION BY o.city_id), 1)
--   AS city_avg_temperature_c.
-- Do not use GROUP BY or ORDER BY inside this average's OVER clause.
-- Final sort: c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- TODO: write Q1 below.
SELECT 
    c.city_name, 
    o.observed_at,
    o.temperature_c,
    ROUND(AVG(o.temperature_c) OVER (PARTITION BY o.city_id), 1) AS city_avg_temperature_c
FROM weather_observations AS o
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;

-- Q2: Number observations chronologically within each city.
-- INNER JOIN to return city_name, observed_at, temperature_c,
-- and ROW_NUMBER() OVER (PARTITION BY o.city_id ORDER BY o.observed_at ASC)
--   AS observation_number.
-- Final sort: c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- TODO: write Q2 below.
SELECT
    c.city_name, 
    o.observed_at, 
    o.temperature_c,
    ROW_NUMBER() OVER(PARTITION BY o.city_id ORDER BY o.observed_at ASC) AS observation_number
FROM weather_observations AS o
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q3: Select the latest observation for each city that has data.
-- WITH numbered AS (...): INNER JOIN the two tables, selecting city_name,
-- observed_at, temperature_c, and ROW_NUMBER() with PARTITION BY o.city_id
-- ORDER BY o.observed_at DESC AS latest_number.
-- The outer SELECT returns city_name, observed_at, temperature_c only.
-- Filter WHERE latest_number = 1 in the OUTER query.
-- Final sort: city_name ASC. Expected: 3 rows; Hue is absent.
-- TODO: write Q3 below.
WITH numbered AS (
    SELECT
        c.city_name,
        o.observed_at,
        o.temperature_c,
        ROW_NUMBER() OVER(PARTITION BY o.city_id ORDER BY o.observed_at DESC) AS latest_number 
    FROM weather_observations AS o
    INNER JOIN cities AS c 
    ON c.city_id = o.city_id
)
SELECT
    city_name, observed_at, temperature_c
FROM numbered 
WHERE latest_number = 1
ORDER BY city_name ASC;
-- Q4: Compare ranking functions across ALL eight observations.
-- INNER JOIN to return city_name, observed_at, temperature_c,
-- RANK() OVER (ORDER BY o.temperature_c DESC) AS temperature_rank,
-- DENSE_RANK() OVER (ORDER BY o.temperature_c DESC) AS temperature_dense_rank.
-- Do not PARTITION BY city: this is a global ranking.
-- Inside these OVER clauses, order ONLY by temperature so equal values tie.
-- Final sort: o.temperature_c DESC, c.city_name ASC, o.observed_at ASC.
-- Expected: 8 rows; both 32-degree observations share rank 3.
-- TODO: write Q4 below.
SELECT
    c.city_name,
    o.observed_at,
    o.temperature_c,
    RANK() OVER(ORDER BY o.temperature_c DESC) AS temperature_rank,
    DENSE_RANK() OVER (ORDER BY o.temperature_c DESC) AS temperature_dense_rank
FROM weather_observations AS o
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY o.temperature_c DESC, c.city_name ASC, o.observed_at ASC;
-- Q5: Compare each temperature with the previous observation for its city.
-- WITH previous_readings AS (...): INNER JOIN to select city_name, observed_at,
-- temperature_c, and LAG(o.temperature_c) OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at ASC
-- ) AS previous_temperature_c.
-- Outer SELECT returns city_name, observed_at, temperature_c,
-- previous_temperature_c, and temperature_c - previous_temperature_c
--   AS temperature_change_c.
-- Do not replace the first previous value or its change with zero.
-- Final sort: city_name ASC, observed_at ASC. Expected: 8 rows.
-- TODO: write Q5 below.
WITH previous_readings AS (
    SELECT 
    c.city_name,
    o.observed_at,
    o.temperature_c,
    LAG(o.temperature_c) OVER (PARTITION BY o.city_id ORDER BY o.observed_at ASC) AS previous_temperature_c
    FROM weather_observations AS o 
    INNER JOIN cities AS c 
    ON c.city_id = o.city_id
)
SELECT 
    city_name, 
    observed_at, 
    temperature_c,
    previous_temperature_c,
    temperature_c - previous_temperature_c AS temperature_change_c
FROM previous_readings
ORDER BY city_name ASC;
-- Q6: Calculate a trailing average of up to THREE observations per city.
-- INNER JOIN to return city_name, observed_at, temperature_c,
-- ROUND(AVG(o.temperature_c) OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at ASC
--   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
-- ), 2) AS rolling_avg_3_c,
-- and COUNT(*) OVER (the same partition/order/ROWS frame) AS frame_row_count.
-- Type the complete OVER specification for both AVG and COUNT.
-- The first frame has 1 row; the second has 2; later frames have at most 3.
-- This is an observation-count window, not a three-hour or three-day window.
-- Final sort: c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- TODO: write Q6 below.
SELECT
    c.city_name,
    o.observed_at,
    o.temperature_c,
    ROUND(AVG(o.temperature_c) OVER(PARTITION BY o.city_id ORDER BY o.observed_at ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),2) AS rolling_avg_3_c,
    COUNT(*) OVER(PARTITION BY o.city_id ORDER BY o.observed_at ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS frame_row_count
FROM weather_observations AS o 
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q7: Calculate the maximum temperature seen so far within each city.
-- INNER JOIN to return city_name, observed_at, temperature_c,
-- MAX(o.temperature_c) OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at ASC
--   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- ) AS running_max_temperature_c.
-- The frame starts at the city's first observation and ends at the current one.
-- Final sort: c.city_name ASC, o.observed_at ASC. Expected: 8 rows.
-- TODO: write Q7 below.
SELECT 
    c.city_name,
    o.observed_at,
    o.temperature_c,
    MAX(o.temperature_c) OVER (PARTITION BY o.city_id ORDER BY o.observed_at ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_max_temperature_c
FROM weather_observations AS o 
INNER JOIN cities AS c 
ON c.city_id = o.city_id
ORDER BY c.city_name ASC, o.observed_at ASC;
-- Q8: Build a latest-weather trend report for ALL four cities.
-- Step 1: WITH observation_features AS (...).
-- Read weather_observations AS o; return city_id, observed_at, temperature_c,
-- LAG(o.temperature_c) OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at ASC
-- ) AS previous_temperature_c,
-- AVG(o.temperature_c) OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at ASC
--   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
-- ) AS rolling_avg_3_c,
-- ROW_NUMBER() OVER (
--   PARTITION BY o.city_id ORDER BY o.observed_at DESC
-- ) AS latest_number.
-- Compute these features on ALL observations, before selecting the latest row.
-- Step 2: SELECT from cities AS c LEFT JOIN observation_features AS f.
-- Match ON c.city_id = f.city_id AND f.latest_number = 1.
-- Return columns in this exact order:
--   c.city_name,
--   f.observed_at,
--   f.temperature_c,
--   f.previous_temperature_c,
--   f.temperature_c - f.previous_temperature_c AS temperature_change_c,
--   ROUND(f.rolling_avg_3_c, 2) AS rolling_avg_3_c,
--   a CASE expression AS trend_status.
-- CASE rules, in this order:
--   f.observed_at IS NULL -> 'no data';
--   f.previous_temperature_c IS NULL -> 'first observation';
--   f.temperature_c > f.previous_temperature_c -> 'warming';
--   f.temperature_c < f.previous_temperature_c -> 'cooling';
--   otherwise -> 'stable'.
-- Keep unavailable measurements as NULL. Do not add a final WHERE on f.
-- Final sort: c.city_name ASC. Expected: 4 rows, including Hue.
-- TODO: write Q8 below.
WITH observation_features AS(
	SELECT 
		city_id, 
		observed_at,
		temperature_c,
		LAG(o.temperature_c) OVER (PARTITION BY city_id ORDER BY observed_at ASC) AS previous_temperature_c,
		AVG(o.temperature_c) OVER (PARTITION BY city_id ORDER BY observed_at ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_3_c,
		ROW_NUMBER() OVER (PARTITION BY city_id ORDER BY o.observed_at DESC) AS latest_number
	FROM weather_observations o
)
SELECT 
	c.city_name,
	of.observed_at,
	of.temperature_c,
	of.previous_temperature_c,
	of.temperature_c - of.previous_temperature_c AS temperature_change_c,
	ROUND(of.rolling_avg_3_c, 2) AS rolling_avg_3_c,
	CASE 
		WHEN of.observed_at IS NULL THEN 'no data'
		WHEN of.previous_temperature_c IS NULL THEN 'first observation'
		WHEN of.temperature_c > of.previous_temperature_c THEN 'warming'
		WHEN of.temperature_c < of.previous_temperature_c THEN 'cooling'
		ELSE 'stable'
	END AS trend_status
FROM cities c 
LEFT JOIN observation_features of 
ON of.city_id = c.city_id
AND of.latest_number = 1
ORDER BY c.city_name ASC;

-- Reflection 1: Why does Q1 retain eight observations, while GROUP BY city_id
-- with AVG(temperature_c) would return only three groups?
-- Your answer: PARTITION BY separates calculations by city while keeping every observation visible.

-- Reflection 2: For values 35, 35, 32, 31 sorted descending, what are the
-- RANK and DENSE_RANK sequences? Why do the ranking OVER clauses omit a unique ID?
-- Your answer: 
-- RANK assigns rankings; if there is a tie, it skips the corresponding next rank, resulting in a sequence like 1, 1, 3, 4.
-- DENSE_RANK works differently; it treats tied positions as a single rank and proceeds to the very next rank without skipping any.
-- I don't no 

-- Reflection 3: Why are the first previous_temperature_c and temperature_change_c
-- NULL for each city? Why would replacing the previous value with zero be misleading?
-- Your answer: This occurs because it is the first position for each `city_id`; since the window function calculates from "2 preceding" to the current row, there are no preceding rows, resulting in a `NULL` value. Using zero is not recommended, as it could mislead viewers into thinking the actual figure is zero.

-- Reflection 4: Does ROWS BETWEEN 2 PRECEDING AND CURRENT ROW mean three days?
-- Explain the frame, including what happens when only one observation is available.
-- Your answer: That implies the two previous rows plus the current row; so, within the frame, it covers a three-day span. As the days progress, the window shifts along with them. However, if there is only a single observation, that specific one is used, as it still falls within the window.
-- ROWS BETWEEN 2 PRECEDING AND CURRENT ROW means up to three observations, regardless of elapsed time.

-- Reflection 5: Why must Q8 calculate LAG and the rolling average before keeping
-- only the latest observation? Why is latest_number = 1 in ON rather than final WHERE?
-- Your answer: Use LAG to calculate `temperature_change_c` and determine the average temperature for a `city_id` partitioned over the last three days; specify `latest_number = 1` in the `ON` clause rather than a final `WHERE` clause, as filtering during the join is more cost-effective than filtering after the join is complete.
--Calculate history features first because filtering to the latest observation first removes the preceding observations: LAG becomes NULL, and the rolling average contains only the latest temperature. Keep latest_number = 1 in ON to preserve cities without observations. A final WHERE with that condition removes Hue.