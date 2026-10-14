> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 7 hints

Complete `build_clean_record` before `validate_record`.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>build_clean_record</summary>

~~~python
response = raw["response"]
current = response["current"]
raw_humidity = current["relative_humidity_2m"]
if isinstance(raw_humidity, bool):
    raise ValueError("humidity cannot be Boolean")
humidity_value = float(raw_humidity)
if not humidity_value.is_integer() or not 0 <= humidity_value <= 100:
    raise ValueError("humidity must be a whole number in 0..100")
humidity_pct = int(humidity_value)

return {
    "city": raw["city"].strip(),
    "requested_at": raw["requested_at"],
    "observed_at": current["time"],
    "timezone": response["timezone"],
    "temperature_c": float(current["temperature_2m"]),
    "humidity_pct": humidity_pct,
    "source": "open-meteo",
}
~~~

</details>

<details>
<summary>validate_record</summary>

~~~python
errors = []

if not record["city"]:
    errors.append("city is empty")

try:
    datetime.fromisoformat(record["observed_at"])
except ValueError:
    errors.append("observed_at is not ISO datetime")

if not record["timezone"]:
    errors.append("timezone is empty")

if not -50 <= record["temperature_c"] <= 60:
    errors.append("temperature_c is outside allowed range")

if type(record["humidity_pct"]) is not int or not 0 <= record["humidity_pct"] <= 100:
    errors.append("humidity_pct is outside allowed range")

return errors
~~~

</details>

<details>
<summary>Debug deliberately</summary>

Before return in build_clean_record, temporarily add:

~~~python
print(response)
print(current)
~~~

Before `if errors` in main:

~~~python
print(clean_record)
print(errors)
~~~

Once you understand the values, remove debug prints so only the final report remains.

</details>

<details>
<summary>Building the driver when starting from a blank file</summary>

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

</details>

<details>
<summary>Preserve invalid values until you can reject them</summary>

Before converting raw humidity to int, reject bool and check that the numeric value is finite, has no fractional part, and lies in0..100. Otherwise int(72.5) becomes72 and hides an invalid reading from validate_record. Keep this check in build_clean_record or a shared helper called before conversion. Report conversion failure without publishing output.

</details>
