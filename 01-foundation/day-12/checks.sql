-- Day 12 ready-made, read-only checks. No TODOs here.
-- Run B1–B2 BEFORE building. Run A1–A6 AFTER schema.sql AND fixture.sql succeed.
-- Execute one complete statement at a time in pgAdmin on weather_day09.
-- Counts and values refer to the unchanged Day 9 fixture.

-- B1: Source overview.
-- Expected: weather_day09, 4, 8, 251.0, 1, open-meteo-demo.
SELECT
    current_database() AS database_name,
    (SELECT COUNT(*) FROM public.cities) AS source_city_count,
    COUNT(*) AS source_observation_count,
    SUM(temperature_c) AS source_temperature_sum,
    COUNT(DISTINCT source) AS source_provider_count,
    MIN(source) AS source_name
FROM public.weather_observations;

-- B2: Source counts, including cities without observations.
-- Expected: Da Nang 2; Hanoi 3; Ho Chi Minh City 3; Hue 0.
SELECT
    c.city_name,
    COUNT(o.observed_at) AS observation_count
FROM public.cities AS c
LEFT JOIN public.weather_observations AS o ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name;

-- A1: Model counts.
-- Expected: dim_city_count 4; dim_date_count 2; fact_count 8.
SELECT
    (SELECT COUNT(*) FROM day12_mart.dim_city) AS dim_city_count,
    (SELECT COUNT(*) FROM day12_mart.dim_date) AS dim_date_count,
    (SELECT COUNT(*) FROM day12_mart.fact_weather) AS fact_count;

-- A2: Calendar attributes.
-- Expected: 2026-09-18, 2026, 9, 5; 2026-09-19, 2026, 9, 6.
SELECT calendar_date, calendar_year, calendar_month, iso_weekday
FROM day12_mart.dim_date
ORDER BY calendar_date;

-- A3: Grain duplicates. Expected: zero rows.
SELECT city_key, observed_at, COUNT(*) AS duplicate_count
FROM day12_mart.fact_weather
GROUP BY city_key, observed_at
HAVING COUNT(*) > 1
ORDER BY city_key, observed_at;

-- A4: Missing dimension references. Expected: missing_reference_count = 0.
-- Foreign keys should also prevent these rows from being inserted.
SELECT COUNT(*) AS missing_reference_count
FROM day12_mart.fact_weather AS f
LEFT JOIN day12_mart.dim_city AS c ON c.city_key = f.city_key
LEFT JOIN day12_mart.dim_date AS d ON d.calendar_date = f.observation_date
WHERE c.city_key IS NULL OR d.calendar_date IS NULL;

-- A5: Wrong local dates or calendar attributes. Expected: mismatch_count = 0.
-- Foreign keys alone do not prove that a referenced date is the correct date.
SELECT COUNT(*) AS mismatch_count
FROM day12_mart.fact_weather AS f
INNER JOIN day12_mart.dim_city AS c ON c.city_key = f.city_key
INNER JOIN day12_mart.dim_date AS d ON d.calendar_date = f.observation_date
WHERE f.observation_date <> (f.observed_at AT TIME ZONE c.timezone_name)::date
   OR d.calendar_year <> EXTRACT(YEAR FROM d.calendar_date)
   OR d.calendar_month <> EXTRACT(MONTH FROM d.calendar_date)
   OR d.iso_weekday <> EXTRACT(ISODOW FROM d.calendar_date);

-- A6: Loss or multiplication when joining the star.
-- Expected: fact_count 8; joined_count 8.
-- Unique dimension keys give each fact exactly one matching city and date.
SELECT
    (SELECT COUNT(*) FROM day12_mart.fact_weather) AS fact_count,
    COUNT(*) AS joined_count
FROM day12_mart.fact_weather AS f
INNER JOIN day12_mart.dim_city AS c ON c.city_key = f.city_key
INNER JOIN day12_mart.dim_date AS d ON d.calendar_date = f.observation_date;
