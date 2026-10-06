> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in ../submissions/day-07/.

# Day 7 review: raw JSON to a clean record

## 1. Raw and clean layers

Day 6 saved the raw API response:

~~~json
{
  "city": "Ho Chi Minh City",
  "requested_at": "...",
  "request": {"latitude": 10.8231},
  "response": {
    "timezone": "Asia/Ho_Chi_Minh",
    "current": {"temperature_2m": 30.7}
  }
}
~~~

The raw layer keeps data as close to the source as possible. It helps debug API behavior, change transformations, and replay the pipeline.

The clean layer keeps normalized fields for downstream use:

~~~json
{
  "city": "Ho Chi Minh City",
  "observed_at": "2026-09-18T11:30",
  "temperature_c": 30.7,
  "humidity_pct": 72
}
~~~

It is smaller and easier to query, but does not replace the raw layer.

## 2. Two different times

| Field | Source | Meaning |
|---|---|---|
| `requested_at` | Pipeline machine | Time the request was sent |
| `observed_at` | response.current.time | Time the source observed the weather |

Do not replace observed_at with requested_at. The API may return an older observation or use a different timezone.

## 3. Build a clean record

Navigate the nested dictionary:

~~~python
response = raw["response"]
current = response["current"]

temperature_c = float(current["temperature_2m"])
humidity_pct = int(current["relative_humidity_2m"])
~~~

Return a new dictionary rather than modifying raw. Preserve the raw input for debugging or replay.

## 4. Data contract and validation

The contract states the conditions the clean record must satisfy. `validate_record` returns a list of errors; it does not write a file:

~~~python
errors = validate_record(clean_record)

if errors:
    raise ValueError("; ".join(errors))
~~~

Collecting errors lets you see multiple problems in one run instead of finding only the first one.

### Check datetime

~~~python
try:
    datetime.fromisoformat(record["observed_at"])
except ValueError:
    errors.append("observed_at is not ISO datetime")
~~~

### Check a range

~~~python
if not -50 <= record["temperature_c"] <= 60:
    errors.append("temperature_c is outside allowed range")
~~~

`not` reverses the condition: "if temperature is not within -50 to 60".

## 5. Fail before writing

In main:

~~~python
errors = validate_record(clean_record)
if errors:
    raise ValueError("; ".join(errors))

write_json(args.output, clean_record)
~~~

Validate first, then write. Writing before validation would put untrusted data in the output layer.

## 6. CLI and reproducibility

Input/output options make the pipeline flexible without code changes:

~~~powershell
python pipeline.py --input raw_weather.json --output output/weather_clean.json
~~~

Fixed raw input in the repository gives the same output for the same command. A live API's results can change with weather and time.

## 7. References

- [Python json](https://docs.python.org/3/library/json.html)
- [Python datetime](https://docs.python.org/3/library/datetime.html)
- [Pro Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
