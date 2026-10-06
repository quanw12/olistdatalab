# Day 07: Mini-project 1: a reproducible weather snapshot
# Read lesson.md, then exercise.md. Detailed guidance: help.md.
# Read raw_weather.json. Implement build_clean_record(raw) and validate_record(record). Clean
# fields: city, requested_at from the raw envelope; observed_at/timezone/temperature/humidity
# from response; source=open-meteo. Return a list of validation errors: nonblank city, valid
# observed_at ISO datetime, nonblank timezone, temperature -50..60, humidity integer0..100.
# Preserve the original requested_at; do not invent a new request time. Write
# output/weather_clean.json only if all five checks pass. Log success and counts; exit nonzero
# on validation failure. Add four reflection answers to reflection.md.
# Write your own implementation below. No solution is supplied here.
