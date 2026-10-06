> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in previous-work/.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 3 hints

Work through one TODO at a time. Type the code into `build_snapshot` rather than pasting the whole function.

## Step 1: get the current object

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

## Step 2: parse time text

~~~python
observed_at = datetime.fromisoformat(current["time"])
~~~

Use the source's observation time. Do not create a new time here.

## Step 3: extract numbers

~~~python
temperature_c = float(current["temperature_2m"])
humidity_pct = int(current["relative_humidity_2m"])
~~~

The sample values are already numbers. Explicit conversions also allow the function to handle numeric text.

## Step 4: apply the configuration rule

~~~python
if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
    raise ValueError("temperature_c is outside configured range")
~~~

Place this after numeric conversion and before `return`.

## Step 5: return the snapshot

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
