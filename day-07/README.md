# Weather Snapshot Pipeline

Week 1 mini-project in the Data Engineering learning plan.

## Problem

Turn a raw weather API response into a clean record with a clear contract. Write output only after all five quality checks pass.

## Data flow

~~~text
raw_weather.json -> build_clean_record -> validate_record -> weather_clean.json
~~~

## Run the project

From `C:\DE Courses\day-07`:

~~~powershell
python pipeline.py
~~~

Specify different input/output paths if needed:

~~~powershell
python pipeline.py --input raw_weather.json --output output/weather_clean.json
~~~

## Input

raw_weather.json simulates the API raw layer and preserves:

- The user-selected city label.
- Request time.
- Request parameters.
- Original API response.

## Output contract

| Field | Type | Meaning |
|---|---|---|
| `city` | String | City label supplied by the user |
| `requested_at` | ISO datetime string | Time the pipeline called the API |
| `observed_at` | ISO datetime string | Time the API observed weather |
| `timezone` | String | Observation timezone |
| `temperature_c` | Float | Temperature in Celsius |
| `humidity_pct` | Integer | Humidity percentage |
| `source` | String | Data source |

## Quality checks

The pipeline rejects records with empty city/timezone, invalid ISO observation time, temperature outside -50 to 60, or humidity outside 0 to 100.

## What I learned

1. The raw layer preserves the original data almost unchanged for debugging, auditing, or replay. The clean layer keeps needed fields and normalizes and validates them.
2. requested_at is when the pipeline calls the API; observed_at is when the API records the weather.
3. With humidity_pct = 130, the function adds an error.
4. Fixed input produces the same result each time, making debugging and checking easier than with a live API.
