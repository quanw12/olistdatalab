# Day 6 — CLI, environment variables, and HTTP APIs

## Today's goal

Fetch current weather from the public Open-Meteo API using Python.

~~~text
terminal arguments + WEATHER_TIMEOUT_SECONDS
              -> HTTP GET with timeout
              -> check HTTP status + JSON response
              -> output/weather_api_response.json
~~~

This exercise does not need an API key. `WEATHER_TIMEOUT_SECONDS` lets you practise configuration outside the code.

## Learning order

1. Read [lesson.md](lesson.md), sections 1–6.
2. Read `parse_args` and `main` in `fetch_weather.py`.
3. Complete the four TODOs in `fetch_current_weather`.
4. Use [help.md](help.md) when stuck.
5. Run with the default timeout from `C:\DE Courses\day-06`:

~~~powershell
python fetch_weather.py
~~~

6. Try another city:

~~~powershell
python fetch_weather.py --city "Da Nang" --latitude 16.0544 --longitude 108.2022
~~~

## Environment variable

Set a 15-second timeout in the **current PowerShell session**:

~~~powershell
$env:WEATHER_TIMEOUT_SECONDS = "15"
python fetch_weather.py
~~~

This assignment does not persist after closing the terminal. The session's configuration is not stored in Git.

## Expected results

~~~text
city: Ho Chi Minh City
current weather: {...}
wrote: output\weather_api_response.json
~~~

Temperature and observation time change with the live API data. Open `output/weather_api_response.json` and check for:

- `city` and `requested_at`.
- `request` containing coordinates, timezone, and requested current variables.
- `response.current`.

## Network and API failures

The script should report an error instead of writing an empty JSON file.

| Error | Meaning |
|---|---|
| `Timeout` | Request exceeded a configured waiting limit |
| `HTTPError` | Server returned an error status, such as 4xx or 5xx |
| `ConnectionError` | Cannot connect to the endpoint |
| `ValueError: response has no current weather` | JSON violates this exercise's contract |

Do not add retries today. Real pipelines need bounded retries with clear rules; we return to them in Day 15.

## Git checkpoint

When the script works, run from `C:\DE Courses`:

~~~powershell
git add README.md roadmap.md requirements.txt day-06
git commit -m "feat(day-06): fetch weather with CLI"
git push
~~~

## Send after finishing

1. Full terminal output from one successful run.
2. The output file's request and response.current sections.
3. Your `fetch_current_weather` function body.
4. Why use `params=...` instead of manually building a URL query string?
