> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in previous-work/.

# Day 3 lesson: JSON, datetime, configuration, and logs

## 1. What is JSON?

JSON is a text format commonly used to exchange data between systems. APIs often return JSON; Python usually converts it to dictionaries and lists.

In `weather_response.json`:

~~~json
{
  "timezone": "Asia/Ho_Chi_Minh",
  "current": {
    "time": "2026-09-13T09:00",
    "temperature_2m": 30.4
  }
}
~~~

The outer JSON **object** corresponds to a Python dictionary:

~~~python
payload = {
    "timezone": "Asia/Ho_Chi_Minh",
    "current": {
        "time": "2026-09-13T09:00",
        "temperature_2m": 30.4,
    },
}
~~~

Access the nested object one level at a time:

~~~python
current = payload["current"]
temperature = current["temperature_2m"]

# Or use one line:

temperature = payload["current"]["temperature_2m"]
~~~

Using `current` is easier to read when learning. A wrong key raises `KeyError`, signalling that the structure differs from what the pipeline expects.

A JSON array corresponds to a Python list:

~~~json
{"cities": ["Hanoi", "Da Nang"]}
~~~

~~~python
data["cities"]  # ["Hanoi", "Da Nang"]
~~~

## 2. Read and write JSON

Python's `json` module is built in; no library installation is needed.

Read from a file:

~~~python
with path.open(encoding="utf-8") as source_file:
    data = json.load(source_file)
~~~

- `path.open` opens the file.
- `with` closes it after the block.
- `json.load` converts JSON in a file into Python objects.

Write a dictionary:

~~~python
with path.open("w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=2)
~~~

- `"w"` creates or overwrites the file.
- `indent=2` makes it readable.
- `ensure_ascii=False` preserves characters such as Vietnamese letters instead of escaping them.

| Functions | Work with |
|---|---|
| `json.load` / `json.dump` | Open files |
| `json.loads` / `json.dumps` | Text strings |

Today `dump` writes output to a file. `dumps` creates JSON text for printing a log in the terminal.

## 3. Datetime: time text and a parsed time

The JSON time begins as a string:

~~~python
time_text = "2026-09-13T09:00"
~~~

Parse it so Python can validate, compare, or calculate with it:

~~~python
observed_at = datetime.fromisoformat(time_text)
~~~

Invalid ISO text raises `ValueError`. After parsing, create normalized output text:

~~~python
observed_at.isoformat()  # "2026-09-13T09:00:00"
~~~

The sample also provides `timezone`: `2026-09-13T09:00` alone does not identify a timezone. Real systems commonly use UTC timestamps or make the timezone explicit.

| Field | Meaning |
|---|---|
| `observed_at` | Time the source observed the weather |
| `logged_at` | Time the pipeline wrote its log |

Current UTC time:

~~~python
datetime.now(timezone.utc).isoformat()
~~~

## 4. Configuration: separate rules from code

`settings.json` contains the city, source, and temperature limits. A shortened example:

~~~json
{
  "city": "Ho Chi Minh City",
  "temperature_min_c": -50,
  "temperature_max_c": 60
}
~~~

Read the limits from configuration rather than hard-coding them:

~~~python
if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
    raise ValueError("temperature_c is outside configured range")
~~~

A new rule or source can use different settings while keeping the validation code. This makes the pipeline easier to reuse.

`raise ValueError(...)` deliberately raises an error with a clear reason when the data violates the contract. Day 1 used `return None`; both approaches prevent invalid data from entering output, but they control execution differently.

## 5. Structured logs: readable by programs too

A free-form log might say:

~~~text
Wrote weather data for Ho Chi Minh City at 09:00
~~~

A person can read this, but it is harder for code to filter by city or event. A structured log uses named fields:

~~~json
{
  "event": "snapshot_written",
  "logged_at": "2026-09-13T02:05:00+00:00",
  "details": {
    "city": "Ho Chi Minh City",
    "observed_at": "2026-09-13T09:00:00"
  }
}
~~~

A logging system can search for `event = "snapshot_written"` or count events per city.

`log_event` builds a dictionary and prints:

~~~python
print(json.dumps(record, ensure_ascii=False))
~~~

One JSON record per terminal line is a common logging approach for scripts and pipelines. Keep passwords, API keys, and private information out of logs.

## 6. Read extract.py as a pipeline

~~~text
main
  -> load settings.json
  -> load weather_response.json
  -> build_snapshot: extract, convert, validate, normalize
  -> write_json: save output
  -> log_event: print JSON log
~~~

| Function | Input | Return value / effect |
|---|---|---|
| `load_json(path)` | Path | Dictionary from a JSON file |
| `write_json(path, data)` | Path and dictionary | Writes a JSON file |
| `log_event(event, details)` | Event name and details | Prints a log record |

Complete only `build_snapshot(payload, settings)`:

~~~text
Input: source payload and configuration settings.
Output: normalized dictionary, or ValueError for out-of-range temperature.
~~~

## 7. Work through the TODOs

1. Get `current` from `payload`.
2. Parse `current["time"]` into datetime.
3. Convert temperature and humidity to float and int.
4. Compare temperature with the two configured bounds.
5. Return a dictionary using the required keys.

After Step 3, temporarily inspect:

~~~python
print(current)
print(observed_at, temperature_c, humidity_pct)
~~~

Remove these debug prints before finishing.

## 8. Common errors

| Error | Common cause | What to check |
|---|---|---|
| `FileNotFoundError` | Wrong working folder | Run from `C:\DE Courses\de-30-days\day-03` |
| `JSONDecodeError` | Missing JSON comma or bracket | Inspect the JSON file |
| `KeyError` | Wrong key, such as temperature instead of temperature_2m | Compare with `weather_response.json` |
| `ValueError: Invalid isoformat string` | Invalid time text | Inspect the value passed to `datetime.fromisoformat` |
| `TypeError: 'NoneType' ...` | Missing dictionary return | Complete Step 5 |

## 9. Focused references

- [Python json](https://docs.python.org/3/library/json.html)
- [Python datetime](https://docs.python.org/3/library/datetime.html)
- [Python exceptions](https://docs.python.org/3/tutorial/errors.html)

Read only the parts needed for the exercise. The goal is to run a small pipeline yourself, not memorize the whole library.
