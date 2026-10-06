> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in previous-work/.

# Day 6 lesson: call an HTTP API from a CLI script

## 1. CLI: input from the terminal

CLI means **command-line interface**. Pass coordinates when running the script instead of editing code:

~~~powershell
python fetch_weather.py --city "Da Nang" --latitude 16.0544 --longitude 108.2022
~~~

`--city`, `--latitude`, and `--longitude` are command-line options. Python's argparse reads them:

~~~python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--city", default="Ho Chi Minh City")
parser.add_argument("--latitude", type=float, default=10.8231)
parser.add_argument("--longitude", type=float, default=106.6297)
parser.add_argument("--timezone", default="Asia/Ho_Chi_Minh")
args = parser.parse_args()
~~~

- `type=float` converts the input text to a number.
- `default` supplies a value when the option is absent.
- `args.latitude` accesses the parsed value.

See all options:

~~~powershell
python fetch_weather.py --help
~~~

## 2. Environment variables: configuration outside code

An environment variable is a key/value setting available to a process. Read one in Python:

~~~python
import os

timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
~~~

`os.getenv` reads the variable, falling back to `"10"` if absent. `float` converts the text for use as a timeout.

Timeout is runtime configuration, separate from cleaning logic. You can change it for an environment without editing Python.

API keys are also often read this way, such as `os.getenv("WEATHER_API_KEY")`. This exercise's public endpoint does not require a key. Keep real secrets out of source code, output JSON, and Git.

## 3. HTTP GET and query parameters

An HTTP request includes:

~~~text
method + URL + query parameters + headers + body (depending on request)
~~~

This exercise uses GET to retrieve data.

~~~python
import requests
API_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": args.latitude,
    "longitude": args.longitude,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": args.timezone,
}

response = requests.get(API_URL, params=params, timeout=timeout_seconds)
~~~

Requests encodes params into the URL query string. Manual concatenation is harder to read and makes encoding and parameter changes easier to get wrong.

## 4. Timeout and HTTP status

Without a timeout, a request may wait a long time during network problems. Pass it explicitly:

~~~python
response = requests.get(API_URL, params=params, timeout=timeout_seconds)
~~~

Requests does not automatically raise an exception for a 404 or 500 response. Check it:

~~~python
response.raise_for_status()
~~~

Wrap request and status checking:

~~~python
try:
    response = requests.get(API_URL, params=params, timeout=timeout_seconds)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    raise RuntimeError(f"weather request failed: {error}") from error
~~~

`RequestException` covers common Requests errors, including connection, timeout, and HTTP errors. `from error` preserves the original cause in the traceback.

## 5. JSON response and data contract

After a successful request:

~~~python
payload = response.json()
~~~

This parses response JSON into Python objects. It is similar to Day 3's json.load, but the source is a network response.

The exercise expects:

~~~python
payload["current"]
~~~

Check before using it:

~~~python
if "current" not in payload:
    raise ValueError("response has no current weather")
~~~

APIs can change their responses or return JSON error objects. Contract checks help detect unexpected data early.

## 6. Save raw response and metadata

Save more than the API payload:

~~~python
{
    "city": args.city,
    "requested_at": "...",
    "request": params,
    "response": payload,
}
~~~

- `city` is a label supplied by you; the API receives coordinates and does not confirm this city name.
- `requested_at` records when the pipeline called the API.
- `request` preserves the parameters for reproduction.
- `response` preserves raw data for a later transformation.

This introduces a **raw layer**: source data and metadata kept before cleaning.

## 7. Execution flow

~~~text
parse_args
  -> read CLI options
fetch_current_weather
  -> read timeout environment variable
  -> GET API with parameters and timeout
  -> check status
  -> parse JSON
  -> check current
main
  -> build raw record with metadata and response
  -> write JSON
  -> print summary
~~~

## 8. References

- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Python argparse](https://docs.python.org/3/library/argparse.html)
- [Open-Meteo API](https://open-meteo.com/en/docs)

Focus on GET, params, timeout, raise_for_status, and response.json today.
