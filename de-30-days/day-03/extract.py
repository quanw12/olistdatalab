# Day 03: JSON, configuration, and datetime
# Read lesson.md, then exercise.md. Detailed guidance: help.md.
# Read weather_response.json and settings.json. Implement build_snapshot(payload, settings).
# Parse current.time, convert temperature/humidity, validate configured temperature bounds, and
# return city, observed_at, timezone, temperature_c, humidity_pct, source. Serialize observed_at
# with isoformat(), not a datetime object. timezone comes from payload, source from settings.
# Write output/weather_snapshot.json and print one JSON event containing event=snapshot_written,
# logged_at (current UTC), and details with city and observed_at.
# Write your own implementation below. No solution is supplied here.
