# Shared contract for Days 13–30

This is the assignment's interface specification, not a finished implementation.

## Environments and fixtures

- Days 13–17: local PostgreSQL, database weather_course.
- From Day 18: container PostgreSQL on host port 5433, database weather_course; bootstrap it separately.
- Day 29: a new weather_course_demo database for a clean rehearsal.
- Base: ../data/weather_batch.json has 8 observations across 3 observed cities; cities.csv also includes Hue.
- Next batch: ../data/weather_batch_next.json has an exact replay, a newer correction, and two new observations. Applying it after base gives 10 distinct observations.
- After Day 17, rerunning older base data must not overwrite the correction.
- Live source is open-meteo; fixture source is open-meteo-demo. Filter fixture checks by source if the database also contains live data.

Fixture dates are fixed; they are not today's weather. Use an explicit clock for tests.

## Normalized observation

| Field | JSON type | Rule |
|---|---|---|
| city | string | Nonblank configured city name |
| observed_at | ISO string with offset | Measurement instant |
| requested_at | ISO string with offset | Request instant |
| timezone_name | string | IANA zone; Asia/Ho_Chi_Minh here |
| temperature_c | number | Finite, -50 through 60 Celsius |
| humidity_pct | integer | 0 through 100; reject booleans and fractions |
| source | string | Nonblank provider label |

Keep missing values distinct from zero. Normalize instants to UTC in clean JSON. Business identity is **(city, observed_at, source)**, explicitly extending Day 12's single-provider grain.

## Raw envelope

Each element of raw_batch.json has this shape:
~~~json
{
  "city": "Hanoi",
  "requested_at": "2026-09-18T02:01:00+00:00",
  "source": "open-meteo-demo",
  "payload": {
    "timezone": "Asia/Ho_Chi_Minh",
    "current": {
      "time": "2026-09-18T09:00",
      "temperature_2m": 30.0,
      "relative_humidity_2m": 80
    }
  }
}
~~~
Attach payload.timezone to the API's naive local time before converting to UTC. Preserve the full raw payload.

## Database contract

Write your DDL in capstone/sql/staging.sql and capstone/sql/mart.sql.

**staging.weather_observations**: the seven normalized fields. city/source/timezone_name are TEXT; instants TIMESTAMPTZ; temperature NUMERIC(4,1); humidity SMALLINT. All NOT NULL. PK (city, observed_at, source). Add nonblank and range checks.

**mart.dim_city**: city_key INTEGER identity PK, city_name TEXT NOT NULL UNIQUE, timezone_name TEXT NOT NULL. Load all four configured cities, including Hue. Keep one current description per city.

**mart.dim_date**: calendar_date DATE PK; calendar_year INTEGER, calendar_month SMALLINT, iso_weekday SMALLINT. Attributes NOT NULL with sensible ranges.

**mart.fact_weather**: observation_key BIGINT identity PK; city_key FK; observation_date FK; observed_at and requested_at TIMESTAMPTZ; temperature_c NUMERIC(4,1); humidity_pct SMALLINT; source TEXT. All NOT NULL. UNIQUE (city_key, observed_at, source). Derive the date using the city's timezone.

Resolve generated city keys through unique city_name. Do not assume generated IDs match source positions.

Day 17 adds **ops.pipeline_state**: pipeline_name TEXT PK, watermark TIMESTAMPTZ NOT NULL. This exercise uses one fixture stream with an overlap; it does not guarantee discovery of arbitrarily late data.

## Package and interfaces

Create files when their lessons introduce them:
~~~text
capstone/
  weather_pipeline/
    __init__.py
    __main__.py
    load.py
    mart.py
    extract.py
    transform.py
    pipeline.py
    quality.py
  sql/staging.sql, sql/mart.sql
  tests/
  requirements.txt
  Dockerfile, compose.yaml, .dockerignore
  orchestration.py, serve.py
  evidence/
~~~

- normalize_record(envelope): one normalized dictionary or ValueError.
- transform_batch(envelopes): (accepted_rows, rejected_rows); each rejection has input index and reason.
- load_records(connection, rows): accepts an existing Psycopg connection; does not commit or close it.
- refresh_mart(connection, cities): resolves dimensions and upserts facts; caller owns the transaction.
- fetch_envelope(...): returns the raw envelope. Inject the HTTP client and sleeper for tests.
- run_pipeline(...): returns input_count, accepted_count, rejected_count, status, run_id; exceptions cannot become success.
- Importing modules must not call APIs or mutate the database.

## CLI progression

Implement these as the lessons specify; they do not work before you write the code:
~~~powershell
python -m weather_pipeline load --input ../data/weather_batch.json
python -m weather_pipeline run --mode fixture --input ../data/raw_batch.json --output-dir output
python -m weather_pipeline run --mode live --cities ../data/cities.csv --output-dir output
python -m weather_pipeline backfill --input ../data/raw_batch.json --start 2026-09-18 --end 2026-09-20 --output-dir output
python -m weather_pipeline quality --source open-meteo-demo --as-of 2026-09-19T03:00:00+00:00 --max-age-hours 2
~~~
Backfill uses local dates with inclusive start/exclusive end, replaying stored observations. The current-weather endpoint cannot supply arbitrary historical snapshots.

## Reliability policy

- Validate before batch writes. Invalid rows may be quarantined; input = accepted + rejected.
- A database failure rolls back the accepted batch.
- Newer requested_at may correct a key; older requests must not overwrite it.
- Day 17 commits checkpoint, staging, and mart together.
- Save raw data first; publish success manifest after database commit.
- Files and PostgreSQL do not share a transaction. If manifest writing fails after commit, replay idempotently.
- Retries are finite and target transient extraction errors. Validation errors are not blindly retried.
- Hue's missing measurements stay missing.

## Expected states

Base: 8 rows, temperature sum 251.0, observation average 31.375, maximum 34.0.
After next batch: 10 rows, sum 314.0, average 31.4, maximum 34.0.
Daily analytics exercises explicitly use the base CSV when they need a fixed independent dataset.
