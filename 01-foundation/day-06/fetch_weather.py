# Day 06: CLI, environment variables, and HTTP APIs
# Read lesson.md, then exercise.md. Detailed guidance: help.md.
# Build an argparse CLI with --city, --latitude, --longitude (defaults Ho Chi Minh City,
# 10.8231, 106.6297). Read positive WEATHER_TIMEOUT_SECONDS (default 10). Use requests.get with
# params for latitude, longitude, timezone=Asia/Ho_Chi_Minh and
# current=temperature_2m,relative_humidity_2m. Check status, parse JSON and require a current
# object. Capture requested_at in UTC before the request. Write output/weather_api_response.json
# containing city, requested_at, request (parameters), response (full body). Report failures; do
# not write a success file for a failed request. No retries yet.
# Write your own implementation below. No solution is supplied here.
