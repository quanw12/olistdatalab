> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in ../submissions/day-06/.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 6 hints

Complete `fetch_current_weather` one TODO at a time.

## Step 1: parameters

~~~python
params = {
    "latitude": args.latitude,
    "longitude": args.longitude,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": args.timezone,
}
~~~

## Step 2: environment timeout

~~~python
timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
~~~

Environment variables are text, so convert this value to float.

## Step 3: GET, timeout, and status

~~~python
try:
    response = requests.get(
        API_URL,
        params=params,
        timeout=timeout_seconds,
    )
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    raise RuntimeError(f"weather request failed: {error}") from error
~~~

## Step 4: JSON and contract check

~~~python
payload = response.json()

if "current" not in payload:
    raise ValueError("response has no current weather")

return payload, params
~~~

The function returns two values, which main unpacks:

~~~python
payload, params = fetch_current_weather(args)
~~~

## Troubleshooting

| Error | Common cause | What to do |
|---|---|---|
| `NameError: os is not defined` | Missing import os | Add import os at the top of your file |
| `TypeError: 'str' object is not callable` | Mistyped function call | Check `os.getenv(...)` and its parentheses |
| `requests.exceptions.Timeout` | Short timeout or slow network | Increase WEATHER_TIMEOUT_SECONDS |
| `HTTPError` | Invalid URL/parameters or API failure | Read the status in the traceback and inspect params |
| `JSONDecodeError` | Response is not valid JSON | Do not write output; send the full error |

## Building the driver when starting from a blank file

Define helper functions first; call them from main. A function definition does not execute its body. This small unrelated example shows the syntax:

~~~python
from pathlib import Path

def save_message(text):
    folder = Path("output")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "message.txt").write_text(text, encoding="utf-8")

def main():
    save_message("Practice complete")

if __name__ == "__main__":
    main()
~~~

Read input inside main, pass data to your transformation, validate the result, then write output. Test one helper with a tiny input before connecting all steps. Use print(repr(value)) to inspect an unexpected value; remove temporary prints after debugging. Return data from helpers and print only at the CLI boundary.

For CSV use csv.DictReader/csv.DictWriter (or pandas read_csv/to_csv on Days4–5). For JSON use json.load/json.dump with an opened UTF-8 file. CSV writer files need newline="". JSON datetime values must become ISO strings before serialization. Catch the expected exception around the risky conversion; do not hide every error behind except Exception: pass.
