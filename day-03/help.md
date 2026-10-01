# Day 3 hints

Work through one TODO at a time. Type the code into `build_snapshot` rather than pasting the whole function.

## TODO 1: get the current object

~~~python
current = payload["current"]
~~~

Now `current` contains:

~~~python
{
    "time": "2026-09-13T09:00",
    "temperature_2m": 30.4,
    "relative_humidity_2m": 76,
}
~~~

## TODO 2: parse time text

~~~python
observed_at = datetime.fromisoformat(current["time"])
~~~

Use the source's observation time. Do not create a new time here.

## TODO 3: extract numbers

~~~python
temperature_c = float(current["temperature_2m"])
humidity_pct = int(current["relative_humidity_2m"])
~~~

The sample values are already numbers. Explicit conversions also allow the function to handle numeric text.

## TODO 4: apply the configuration rule

~~~python
if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
    raise ValueError("temperature_c is outside configured range")
~~~

Place this after numeric conversion and before `return`.

## TODO 5: return the snapshot

~~~python
return {
    "city": settings["city"],
    "observed_at": observed_at.isoformat(),
    "timezone": payload["timezone"],
    "temperature_c": temperature_c,
    "humidity_pct": humidity_pct,
    "source": settings["source"],
}
~~~

`isoformat()` converts datetime back to an ISO string for JSON. `json.dump` does not serialize datetime objects by default.

## Trace the values

| Variable | Value after processing |
|---|---|
| `current` | Dictionary under the `"current"` key |
| `observed_at` | Datetime for 2026-09-13 09:00 |
| `temperature_c` | `30.4` |
| `humidity_pct` | `76` |
| Returned snapshot | Dictionary with six output keys |

For `KeyError`, temporarily print `payload` or `current` and compare the actual keys in the JSON file. Do not guess key names.
