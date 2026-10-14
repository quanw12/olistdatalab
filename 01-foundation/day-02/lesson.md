> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic.

# Day 2 lesson: understand Python through Day 1's pipeline

## 1. How does the Day 1 script run?

When you run:

~~~powershell
python clean.py
~~~

Python reads the file from top to bottom. Function definitions create functions, but their bodies do not run until called. At the bottom:

~~~python
if __name__ == "__main__":
    main()
~~~

When a file runs directly, its special variable `__name__` is `"__main__"`. The condition is true, so Python calls `main()`.

~~~text
main()
  -> create output folder and collections
  -> open weather.csv
  -> loop over raw_row
       -> call clean_row(raw_row)
       -> invalid: count reason, skip
       -> duplicate: count reason, skip
       -> valid: keep row
  -> write accepted rows to CSV
  -> print report
~~~

`main` coordinates the work; `clean_row` cleans **one** row.

## 2. Variables and values

A variable is a name referring to a value:

~~~python
city = "Hanoi"
temperature_c = 31.2
~~~

`=` assigns the value on the right to the name on the left. Equality comparison uses `==`:

~~~python
city == "Hanoi"  # True or False
~~~

| Type | Example | Purpose |
|---|---|---|
| `str` | `"Hanoi"` | Text |
| `int` | `78` | Whole numbers |
| `float` | `31.2` | Numbers with a fractional part |
| `bool` | `True`, `False` | True/false values |

Type conversions:

~~~python
int("78")        # 78
float("31.2")    # 31.2
str(78)          # "78"
~~~

If Python cannot convert `"not_available"` to a number, it raises `ValueError`.

## 3. Functions: a named piece of work

Define a function using `def`:

~~~python
def say_hello(name):
    message = f"Hello, {name}"
    return message
~~~

- `def` starts the definition.
- `say_hello` is the function name.
- `name` is a **parameter**, which receives input.
- The indented block is the function body.
- `return` sends a value back to the caller and ends this function call.

Call it:

~~~python
greeting = say_hello("Quan")
print(greeting)  # Hello, Quan
~~~

In `clean.py`:

~~~python
clean, rejection_reason = clean_row(raw_row)
~~~

The raw row is passed into the function. Its two returned values form a tuple, then Python **unpacks** it into two variables. This is equivalent to:

~~~python
result = clean_row(raw_row)
clean = result[0]
rejection_reason = result[1]
~~~

### Return versus print

~~~python
def double(number):
    return number * 2

answer = double(4)  # answer receives 8
print(answer)       # Displays 8 in the terminal
~~~

`return` gives data to other code for reuse. `print` displays a value for the person running the program.

## 4. Type hints in `clean.py`

This line is long because of type hints:

~~~python
def clean_row(raw_row: dict[str, str]) -> tuple[dict[str, object] | None, str | None]:
~~~

First read the basic definition:

~~~python
def clean_row(raw_row):
~~~

These are function-header fragments, not complete runnable programs. Add an indented body below the colon. The rest describes expected types:

| Part | Meaning |
|---|---|
| `raw_row: dict[str, str]` | Dictionary with string keys and values |
| `-> ...` | Describes the return type |
| `tuple[A, B]` | A pair containing A and B |
| `X | None` | Either X or None |
| `object` | Any Python object |

The function can still run without these hints. Day 2 leaves them out of `exercise.py` so you can focus on the logic; we will use them again later.

## 5. Dictionaries, lists, and sets

### Dictionary: a row with named fields

~~~python
row = {
    "city": "Hanoi",
    "temperature_c": 31.2,
}

city = row["city"]                 # "Hanoi"
row["temperature_c"] = 30.5        # Updates the value
~~~

`row["city"]` is not a function call. Square brackets look up a key. A missing key raises `KeyError`.

### List: values in order

~~~python
temperatures = []
temperatures.append(31.2)
temperatures.append(30.1)
~~~

`append` is a **method**: a function associated with the list. The list becomes `[31.2, 30.1]`. Lists preserve insertion order and allow duplicates.

### Set: each value appears once

~~~python
cities = set()
cities.add("Hanoi")
cities.add("Hanoi")
cities.add("Da Nang")
~~~

The set contains only `"Hanoi"` and `"Da Nang"`. It helps detect duplicate keys in Day 1 and find distinct cities in Day 2.

~~~python
"Hanoi" in cities  # True
~~~

## 6. Loops and conditions

### For loops

~~~python
for row in rows:
    print(row["city"])
~~~

With five dictionaries in `rows`, the indented block runs five times. Each time, `row` refers to the next dictionary.

### If, not, and continue

The following fragment belongs inside the row loop; continue cannot appear outside a loop.

~~~python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue
~~~

- `is None` checks for the special value None.
- `+= 1` adds one to the current count.
- `continue` skips the rest of this iteration and moves to the next row.

For an invalid row, the code below does not run. Therefore, rows that reach the later code have a clean dictionary rather than None.

Range-check fragment inside clean_row (return must be inside a function):

~~~python
if not 0 <= humidity_pct <= 100:
    return None, "humidity_pct is outside allowed range"
~~~

`0 <= humidity_pct <= 100` checks whether humidity is within the range. `not` reverses the result, so the condition is true outside the range.

## 7. Handle expected errors with try and except

This fragment also belongs inside clean_row; it returns a result to the caller.

~~~python
try:
    temperature_c = float(raw_row["temperature_c"])
except ValueError:
    return None, "temperature_c is not numeric"
~~~

Python attempts the `try` block. If conversion raises `ValueError`, it runs the matching `except` block instead of stopping the whole program.

Catch errors you expect and know how to handle. `except Exception` is too broad here and may hide programming mistakes.

## 8. Other modules and methods in `clean.py`

`import` brings tools from Python's libraries into the file:

| Syntax | Purpose |
|---|---|
| `import csv` | Read/write CSV |
| `from collections import Counter` | Count occurrences |
| `from datetime import date` | Parse ISO dates |
| `from pathlib import Path` | Work with file and folder paths |

| Call | What it does |
|---|---|
| `raw_row["city"].strip()` | Gets city and removes surrounding whitespace |
| `OUTPUT_DIR.mkdir(exist_ok=True)` | Creates output; allows an existing folder |
| `INPUT_PATH.open(...)` | Opens a file |
| `with ... as source_file:` | Closes it after the block, including on errors |
| `csv.DictReader(source_file)` | Reads rows as dictionaries |
| `Counter()` | Creates an empty counter |
| `rejection_reasons[reason] += 1` | Increments this reason's count |
| `seen_keys.add(key)` | Adds a key to the set |
| `accepted_rows.append(clean)` | Appends a row to the list |
| `date.fromisoformat(text)` | Parses an ISO date into a date object |
| `len(values)` | Counts items |
| `sum(values)` | Adds numbers |
| `min(values)`, `max(values)` | Finds smallest/largest values |
| `round(number, 1)` | Rounds to one decimal place |
| `sorted(values)` | Creates a sorted list |

An **f-string** starts with `f` and inserts values inside `{}`:

~~~python
count = 5
print(f"accepted: {count}")
~~~

`pass` means "do nothing". It often holds a place for unfinished code. The remaining `pass` at the end of your Day 1 loop does not break it, but is unnecessary after adding real code.

## 9. Complete `exercise.py`

The function's contract:

~~~text
Input: a list of already-clean dictionaries.
Output: a dictionary with the row count, cities,
        minimum, maximum, and average temperature.
~~~

1. Create an empty `temperatures` list and `cities` set.
2. Loop over each row.
3. Look up city and temperature by dictionary key.
4. Add city to the set and temperature to the list.
5. Calculate minimum, maximum, and mean.
6. Return one dictionary.

Do it in small steps. After writing the loop, temporarily inspect:

~~~python
print(temperatures)
print(cities)
~~~

Remove debug prints before submitting.

## 10. Focused references

- [Python: defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python: lists, dictionaries, and sets](https://docs.python.org/3/tutorial/datastructures.html)
- [Python: errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

Read each section for 10–15 minutes, type a small example, then return to the exercise. Running code helps you remember syntax.
