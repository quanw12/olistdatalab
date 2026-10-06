# Day 08 assignment

On the empty weather_day08 database, create cities and weather_observations. cities: city_id INTEGER identity PRIMARY KEY, city_name TEXT NOT NULL UNIQUE, timezone_name TEXT NOT NULL; reject blank names/timezones. observations: city_id INTEGER NOT NULL FK to cities, observed_at/requested_at TIMESTAMPTZ NOT NULL, temperature_c NUMERIC(4,1) NOT NULL in[-50,60], humidity_pct SMALLINT NOT NULL in[0,100], source TEXT NOT NULL/nonblank. Composite PK(city_id, observed_at). Write the COMPLETE CREATE TABLE statements, not just constraints. Then run supplied seed.sql once and verify.sql.

## Deliverables

- Your implementation in `schema.sql`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.
