# Day 6 hints

Complete `fetch_current_weather` one TODO at a time.

## TODO 1: parameters

~~~python
params = {
    "latitude": args.latitude,
    "longitude": args.longitude,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": args.timezone,
}
~~~

## TODO 2: environment timeout

~~~python
timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
~~~

Environment variables are text, so convert this value to float.

## TODO 3: GET, timeout, and status

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

## TODO 4: JSON and contract check

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
| `NameError: os is not defined` | Missing import os | Keep the scaffold's import |
| `TypeError: 'str' object is not callable` | Mistyped function call | Check `os.getenv(...)` and its parentheses |
| `requests.exceptions.Timeout` | Short timeout or slow network | Increase WEATHER_TIMEOUT_SECONDS |
| `HTTPError` | Invalid URL/parameters or API failure | Read the status in the traceback and inspect params |
| `JSONDecodeError` | Response is not valid JSON | Do not write output; send the full error |
