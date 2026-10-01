# Day 3 — JSON, datetime, configuration, and logs

## Today's goal

Read a JSON file that simulates a weather API response. Extract the fields you need, check temperature against a configuration file, and produce:

1. `output/weather_snapshot.json` — a normalized record.
2. A JSON log in the terminal — confirming that the pipeline wrote the output.

~~~text
weather_response.json + settings.json
             -> read and normalize
             -> weather_snapshot.json + JSON log
~~~

In Day 15, a live API will replace `weather_response.json`. The parsing, validation, and output logic will stay similar.

## Learning order

1. Read [lesson.md](lesson.md), sections 1–6.
2. Open `weather_response.json` and `settings.json`. Inspect their structure first.
3. Read the existing functions in `extract.py`: `load_json`, `write_json`, `log_event`, and `main`.
4. Complete the five TODOs in `build_snapshot`, one at a time.
5. When stuck, read the matching [hint](help.md).
6. Run from PowerShell in `C:\DE Courses\day-03`:

~~~powershell
python extract.py
~~~

## Expected results

The terminal shows one JSON line with `event`, `logged_at`, and `details`. `logged_at` changes each time you run it.

~~~text
{"event": "snapshot_written", "logged_at": "...", "details": {"city": "Ho Chi Minh City", "observed_at": "2026-09-13T09:00:00"}}
~~~

Open `output/weather_snapshot.json`. It should contain:

~~~json
{
  "city": "Ho Chi Minh City",
  "observed_at": "2026-09-13T09:00:00",
  "timezone": "Asia/Ho_Chi_Minh",
  "temperature_c": 30.4,
  "humidity_pct": 76,
  "source": "open-meteo-demo"
}
~~~

## Completion checklist

- [ ] Distinguish a JSON object, array, and JSON text string.
- [ ] Access `payload["current"]["temperature_2m"]`.
- [ ] Explain why you parse time text into datetime, then write ISO text again.
- [ ] Explain how `settings.json` changes rules without changing code.
- [ ] Produce the expected output record and log structure.

## Git checkpoint

After completing Days 2 and 3, run from `C:\DE Courses`:

~~~powershell
git add day-02 day-03 README.md roadmap.md
git commit -m "feat(day-03): add JSON weather snapshot exercise"
git push
~~~

## Send after finishing

1. The full log line from `python extract.py`.
2. Contents of `output/weather_snapshot.json`.
3. Your `build_snapshot` function body.
4. One sentence: why is `settings.json` useful compared with hard-coding temperature limits?
