# Day 03 assignment

Read weather_response.json and settings.json. Implement build_snapshot(payload, settings). Parse current.time, convert temperature/humidity, validate configured temperature bounds, and return city, observed_at, timezone, temperature_c, humidity_pct, source. Serialize observed_at with isoformat(), not a datetime object. timezone comes from payload, source from settings. Write output/weather_snapshot.json and print one JSON event containing event=snapshot_written, logged_at (current UTC), and details with city and observed_at.

## Deliverables

- Your implementation in `extract.py`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.
