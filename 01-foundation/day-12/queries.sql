-- Day 12 reports: read the LOADED day12_mart tables on weather_day09.
-- Write complete SQL under each TODO and end each statement with ;.
-- Do not reload schema.sql to run a report.
-- Save your own English sentence after each -- Explanation:.
-- Put design answers and reflections in model.md.

-- Q1: Show individual observations with their dimension labels.
-- Start with day12_mart.fact_weather AS f.
-- INNER JOIN day12_mart.dim_city AS c on city_key.
-- INNER JOIN day12_mart.dim_date AS d on f.observation_date = d.calendar_date.
-- Return, in order:
-- c.city_name, d.calendar_date, f.observed_at, f.temperature_c, f.humidity_pct.
-- Final sort: c.city_name ASC, f.observed_at ASC.
-- Expected: 8 rows. There is no GROUP BY: keep the fact's observation grain.
-- TODO:


-- Q2: Build a daily weather report from the same star.
-- INNER JOIN the same three tables using their actual keys.
-- Return, in order:
-- c.city_name, d.calendar_date,
-- COUNT(*) AS observation_count,
-- ROUND(AVG(f.temperature_c), 2) AS avg_temperature_c,
-- ROUND(AVG(f.humidity_pct), 2) AS avg_humidity_pct.
-- GROUP BY c.city_key, c.city_name, d.calendar_date.
-- Final sort: c.city_name ASC, d.calendar_date ASC.
-- Expected: 5 rows; Hue has no observed city/date group.
-- State the RESULT grain in your explanation.
-- TODO:


-- Q3: Summarize every city, including Hue.
-- Start with day12_mart.dim_city AS c.
-- LEFT JOIN day12_mart.fact_weather AS f on city_key.
-- Return, in order:
-- c.city_name,
-- COUNT(f.observation_key) AS observation_count,
-- ROUND(AVG(f.temperature_c), 2) AS avg_temperature_c.
-- GROUP BY c.city_key, c.city_name.
-- Final sort: c.city_name ASC.
-- Expected: 4 rows. Hue's count is 0 and average is NULL.
-- Explain why COUNT(*) would give the wrong observation count for Hue.
-- TODO:

-- Explanation:
