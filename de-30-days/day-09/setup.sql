-- Day 9 ready-made practice data. No TODOs in this file.
-- Run the ENTIRE file ONCE on the EMPTY weather_day09 database.
-- This is fixed demo data, not a live API response.

BEGIN;

DO $day09$
BEGIN
    IF current_database() <> 'weather_day09' THEN
        RAISE EXCEPTION 'Open Query Tool on weather_day09 before running setup.sql';
    END IF;
END;
$day09$;

CREATE TABLE cities (
    city_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city_name TEXT NOT NULL,
    timezone_name TEXT NOT NULL,
    CONSTRAINT uq_cities_name UNIQUE (city_name),
    CONSTRAINT ck_cities_name CHECK (btrim(city_name) <> ''),
    CONSTRAINT ck_cities_timezone_name CHECK (btrim(timezone_name) <> '')
);

CREATE TABLE weather_observations (
    city_id INTEGER NOT NULL,
    observed_at TIMESTAMPTZ NOT NULL,
    requested_at TIMESTAMPTZ NOT NULL,
    temperature_c NUMERIC(4,1) NOT NULL,
    humidity_pct SMALLINT NOT NULL,
    source TEXT NOT NULL,
    CONSTRAINT fk_cities_id FOREIGN KEY (city_id) REFERENCES cities(city_id),
    CONSTRAINT pk_weather_observations PRIMARY KEY (city_id, observed_at),
    CONSTRAINT ck_temperature CHECK (temperature_c BETWEEN -50 AND 60),
    CONSTRAINT ck_humidity CHECK (humidity_pct BETWEEN 0 AND 100),
    CONSTRAINT ck_source CHECK (btrim(source) <> '')
);

-- In a fresh database, these receive IDs 1, 2, 3, and 4 in this order.
INSERT INTO cities (city_name, timezone_name)
VALUES
    ('Hanoi', 'Asia/Ho_Chi_Minh'),
    ('Da Nang', 'Asia/Ho_Chi_Minh'),
    ('Ho Chi Minh City', 'Asia/Ho_Chi_Minh'),
    ('Hue', 'Asia/Ho_Chi_Minh');

-- Hue (city_id 4) intentionally has no observations.
INSERT INTO weather_observations
    (city_id, observed_at, requested_at, temperature_c, humidity_pct, source)
VALUES
    (1, '2026-09-18T09:00:00+07:00', '2026-09-18T02:01:00+00:00', 30.0, 80, 'open-meteo-demo'),
    (1, '2026-09-18T12:00:00+07:00', '2026-09-18T05:01:00+00:00', 32.0, 70, 'open-meteo-demo'),
    (1, '2026-09-19T09:00:00+07:00', '2026-09-19T02:01:00+00:00', 31.0, 75, 'open-meteo-demo'),
    (2, '2026-09-18T09:00:00+07:00', '2026-09-18T02:01:00+00:00', 29.0, 85, 'open-meteo-demo'),
    (2, '2026-09-18T12:00:00+07:00', '2026-09-18T05:01:00+00:00', 30.0, 80, 'open-meteo-demo'),
    (3, '2026-09-18T09:00:00+07:00', '2026-09-18T02:01:00+00:00', 33.0, 65, 'open-meteo-demo'),
    (3, '2026-09-18T12:00:00+07:00', '2026-09-18T05:01:00+00:00', 34.0, 60, 'open-meteo-demo'),
    (3, '2026-09-19T09:00:00+07:00', '2026-09-19T02:01:00+00:00', 32.0, 70, 'open-meteo-demo');

COMMIT;

SELECT COUNT(*) AS city_count FROM cities;
SELECT COUNT(*) AS observation_count FROM weather_observations; 