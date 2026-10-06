# Day 07 assignment

Read raw_weather.json. Implement build_clean_record(raw) and validate_record(record). Clean fields: city, requested_at from the raw envelope; observed_at/timezone/temperature/humidity from response; source=open-meteo. Return a list of validation errors: nonblank city, valid observed_at ISO datetime, nonblank timezone, temperature -50..60, humidity integer0..100. Preserve the original requested_at; do not invent a new request time. Write output/weather_clean.json only if all five checks pass. Log success and counts; exit nonzero on validation failure. Add four reflection answers to reflection.md.

## Deliverables

- Your implementation in `pipeline.py`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.
