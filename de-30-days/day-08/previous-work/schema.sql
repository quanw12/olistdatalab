-- Day 8: complete the five TODOs before running this file.
-- Run once on the dedicated, empty weather_day08 database.

CREATE TABLE cities (
    city_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city_name TEXT NOT NULL,
    timezone_name TEXT NOT NULL,
    -- TODO 1: add a named UNIQUE constraint for city_name.
    CONSTRAINT uq_cities_name UNIQUE(city_name),
    -- TODO 2: add named CHECK constraints rejecting blank city_name/timezone_name.
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
    -- TODO 3: add a named FOREIGN KEY from city_id to cities.city_id.
    CONSTRAINT fk_cities_id FOREIGN KEY (city_id) REFERENCES cities(city_id),
    -- TODO 4: add a named composite PRIMARY KEY on (city_id, observed_at).
    CONSTRAINT pk_weather_observations PRIMARY KEY (city_id, observed_at),
    -- TODO 5: add named CHECK constraints for temperature, humidity, nonblank source.
    CONSTRAINT ck_temperature CHECK (temperature_c >= -50 AND temperature_c <= 60),
    CONSTRAINT ck_humidity CHECK (humidity_pct >= 0 AND humidity_pct <= 100),
    CONSTRAINT ck_source CHECK (btrim(source) <> '')
);  
