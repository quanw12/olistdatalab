-- Day 8: complete the five TODOs before running this file.
-- Run once on the dedicated, empty weather_day08 database.

CREATE TABLE cities (
    city_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city_name TEXT NOT NULL,
    timezone_name TEXT NOT NULL
    -- TODO 1: add a named UNIQUE constraint for city_name.
    -- TODO 2: add named CHECK constraints rejecting blank city_name/timezone_name.
);

CREATE TABLE weather_observations (
    city_id INTEGER NOT NULL,
    observed_at TIMESTAMPTZ NOT NULL,
    requested_at TIMESTAMPTZ NOT NULL,
    temperature_c NUMERIC(4,1) NOT NULL,
    humidity_pct SMALLINT NOT NULL,
    source TEXT NOT NULL
    -- TODO 3: add a named FOREIGN KEY from city_id to cities.city_id.
    -- TODO 4: add a named composite PRIMARY KEY on (city_id, observed_at).
    -- TODO 5: add named CHECK constraints for temperature, humidity, nonblank source.
);
