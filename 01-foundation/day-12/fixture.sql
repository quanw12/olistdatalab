-- PROVIDED fixture loader. Run ONCE after completing schema.sql.
BEGIN;
DO $fixture$
BEGIN
    IF current_database() <> 'weather_day09' THEN
        RAISE EXCEPTION 'Use weather_day09';
    END IF;
    IF (SELECT COUNT(*) FROM public.cities) <> 4 OR
       (SELECT COUNT(*) FROM public.weather_observations) <> 8 OR
       (SELECT SUM(temperature_c) FROM public.weather_observations) IS DISTINCT FROM 251.0 THEN
        RAISE EXCEPTION 'Expected unchanged Day09 fixture: 4 cities, 8 observations, sum 251';
    END IF;
    IF EXISTS (SELECT 1 FROM public.weather_observations WHERE source <> 'open-meteo-demo') THEN
        RAISE EXCEPTION 'Expected the single-provider demo fixture';
    END IF;
    IF EXISTS (SELECT 1 FROM day12_mart.dim_city) OR
       EXISTS (SELECT 1 FROM day12_mart.dim_date) OR
       EXISTS (SELECT 1 FROM day12_mart.fact_weather) THEN
        RAISE EXCEPTION 'Target already contains data; run checks.sql instead';
    END IF;
END;
$fixture$;
INSERT INTO day12_mart.dim_city
    (source_city_id, city_name, timezone_name)
SELECT city_id, city_name, timezone_name
FROM public.cities
ORDER BY city_name;

-- This small date dimension contains only the dates observed in the fixture.
-- A larger warehouse can populate a complete calendar separately.
WITH local_dates AS (
    SELECT DISTINCT
        (o.observed_at AT TIME ZONE c.timezone_name)::date AS calendar_date
    FROM public.weather_observations AS o
    INNER JOIN public.cities AS c ON c.city_id = o.city_id
)
INSERT INTO day12_mart.dim_date
    (calendar_date, calendar_year, calendar_month, iso_weekday)
SELECT
    calendar_date,
    EXTRACT(YEAR FROM calendar_date)::integer,
    EXTRACT(MONTH FROM calendar_date)::smallint,
    EXTRACT(ISODOW FROM calendar_date)::smallint
FROM local_dates
ORDER BY calendar_date;

-- Resolve the warehouse city key through source_city_id.
-- city_key and source_city_id can have different numeric values.
-- Keep both original instants and derive the local observation date.
INSERT INTO day12_mart.fact_weather
    (city_key, observation_date, observed_at, requested_at,
     temperature_c, humidity_pct, source)
SELECT
    c.city_key,
    (o.observed_at AT TIME ZONE c.timezone_name)::date,
    o.observed_at,
    o.requested_at,
    o.temperature_c,
    o.humidity_pct,
    o.source
FROM public.weather_observations AS o
INNER JOIN day12_mart.dim_city AS c ON c.source_city_id = o.city_id
ORDER BY c.city_name, o.observed_at;


COMMIT;
