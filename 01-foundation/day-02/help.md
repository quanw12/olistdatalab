> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic. Previous submissions are preserved in ../submissions/day-02/.

Function-body fragments containing return must be indented inside the named function; they are not standalone scripts.

# Day 2 hints

Open only the TODO you are stuck on. Type each line yourself and track what each variable contains.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>TODOs 1 and 2: empty collections</summary>

~~~python
temperatures = []
cities = set()
~~~

`[]` creates an empty list. `set()` creates an empty set; `{}` creates an empty dictionary.

</details>

<details>
<summary>Step 3: visit each row</summary>

~~~python
for row in rows:
    city = row["city"]
    temperature_c = row["temperature_c"]
~~~

`row` is a temporary variable. Each iteration assigns the next dictionary in `rows` to it.

</details>

<details>
<summary>Step 4: collect values</summary>

Place these **inside** the loop, at the same indentation as the two lookup lines:

~~~python
cities.add(city)
temperatures.append(temperature_c)
~~~

The set keeps each city name once. The list keeps every temperature because each is an observation used in the calculation.

</details>

<details>
<summary>Step 5: calculate statistics</summary>

Place this **after** the loop, at the function body's indentation level (four spaces):

~~~python
lowest_temperature = min(temperatures)
highest_temperature = max(temperatures)
average_temperature = sum(temperatures) / len(temperatures)
~~~

The list now contains five numbers. Their sum divided by their count gives the mean.

</details>

<details>
<summary>Step 6: return the report</summary>

~~~python
return {
    "row_count": len(rows),
    "cities": sorted(cities),
    "temperature_min_c": lowest_temperature,
    "temperature_max_c": highest_temperature,
    "temperature_avg_c": average_temperature,
}
~~~

`sorted(cities)` produces an ordered list so the output is consistent.

</details>

<details>
<summary>Troubleshooting</summary>

| Error or symptom | Common cause | Fix |
|---|---|---|
| `NameError: temperatures is not defined` | Missing list or wrong scope | Create it inside `summarize_weather`, before `for` |
| `KeyError: ...` | Misspelled key | Use `"city"` and `"temperature_c"` |
| `TypeError: 'NoneType' object is not subscriptable` | Function does not return a dictionary | Complete Step 6 and remove `pass` |
| `IndentationError` | Inconsistent block indentation | Use four spaces; do not mix tabs and spaces |
| Incorrect average | Append outside the loop, or missing division | Check TODOs 4 and 5 |

</details>

<details>
<summary>Trace by hand</summary>

First iteration:

~~~python
row = {"city": "Hanoi", "temperature_c": 31.2}
~~~

After collecting the values:

~~~python
cities        # {"Hanoi"}
temperatures  # [31.2]
~~~

The second iteration adds `"Da Nang"` and `30.1`. After five iterations, the list has five temperatures and the set has three city names.

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
<summary>Empty input and display formatting</summary>

Before min/max/division, handle an empty temperatures list. Return row_count0, cities[], and None for all three temperature statistics. A check such as if not temperatures detects an empty list. In print_summary, display "no data" for None; otherwise format one decimal place with an f-string format specifier such as f"{value:.1f}". Keep the calculated mean unrounded until display.

</details>
