# Day 7 — Mini-project 1: Weather snapshot pipeline

## Week 1 goal

You have practised Python, CSV/JSON, pandas, Git, and HTTP APIs. Combine these ideas into a small pipeline you can run from the beginning:

~~~text
raw_weather.json
  -> read raw response + request metadata
  -> normalize a weather record
  -> run five quality checks
  -> output/weather_clean.json
~~~

The saved input simulates Day 6's output. No network is needed, making the exercise reproducible for testing and review.

## Learning order

1. Read the [project README](README.md) as a portfolio reviewer would.
2. Read [lesson.md](lesson.md), especially the contract and checks.
3. Open `raw_weather.json` and locate the temperature:

~~~python
raw["response"]["current"]["temperature_2m"]
~~~

4. Complete `build_clean_record` and `validate_record` in `pipeline.py`.
5. Open [help.md](help.md) only when needed.
6. Run from `C:\DE Courses\day-07`:

~~~powershell
python pipeline.py
~~~

## Expected results

~~~text
checks passed: 5
wrote: output\weather_clean.json
~~~

`output/weather_clean.json`:

~~~json
{
  "city": "Ho Chi Minh City",
  "requested_at": "2026-09-18T04:31:14+00:00",
  "observed_at": "2026-09-18T11:30",
  "timezone": "Asia/Ho_Chi_Minh",
  "temperature_c": 30.7,
  "humidity_pct": 72,
  "source": "open-meteo"
}
~~~

## Five quality checks

1. City is not empty.
2. observed_at is a valid ISO datetime.
3. Timezone is not empty.
4. Temperature is between -50 and 60.
5. Humidity is between 0 and 100.

If a check fails, the pipeline must not write output. This is a foundation of data quality.

## Reflect before committing

Answer in your own words:

1. How do the raw and clean layers differ?
2. Why keep requested_at and observed_at as separate fields?
3. What happens if the API supplies humidity_pct = 130?
4. Why is fixed input easier to test than a live API?

Add short answers to **What I learned** in [README.md](README.md).

## Git checkpoint

When the pipeline works and the reflection is complete, run from `C:\DE Courses`:

~~~powershell
git add README.md roadmap.md day-07
git commit -m "feat(day-07): add weather snapshot pipeline"
git push
~~~

## Send after finishing

1. Terminal output.
2. Contents of output/weather_clean.json.
3. The two completed functions.
4. Your four reflection answers.
