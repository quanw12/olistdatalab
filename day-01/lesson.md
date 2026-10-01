# Day 1 tutorial: from raw CSV to clean data

## 1. What are you learning today?

A Data Engineer does more than read and save files. The job is to turn uncertain data into data that other people can trust and use.

Suppose a weather system needs Hanoi's average temperature. Wrong dates, text in a temperature field, humidity of 105%, and duplicate rows can make the average wrong or stop the program.

Today's small pipeline has four steps:

```text
raw CSV -> read each row -> validate/clean -> clean CSV + error report
```

This is a small version of a real pipeline. Later, the inputs and outputs will include APIs, databases, and warehouses, but the way of thinking stays the same.

## 2. Data contract: the rules for your data

Write the rules before coding. A **data contract** describes what a source should provide and what the pipeline accepts.

| Column | Type after cleaning | Rule |
|---|---|---|
| `city` | String | Must not be empty |
| `observed_at` | Date string `YYYY-MM-DD` | Must be a valid date |
| `temperature_c` | Float | From -50 to 60 |
| `humidity_pct` | Integer | From 0 to 100 |

The unique key is `(city, observed_at)`: one observation per city per day.

In real systems, rules may live in documentation, database constraints, or tests. Today they live in `clean_row`.

## 3. CSV does not know data types

CSV is text. When `csv.DictReader` reads:

```csv
Hanoi,2026-08-01,31.2,78
```

Python receives:

```python
{
    "city": "Hanoi",
    "observed_at": "2026-08-01",
    "temperature_c": "31.2",
    "humidity_pct": "78",
}
```

Both numbers are still strings. `"31.2" + "1"` produces `"31.21"`, not `32.2`.

Convert the types deliberately:

```python
temperature_c = float(raw_row["temperature_c"])
humidity_pct = int(raw_row["humidity_pct"])
```

A value such as `not_available` causes `ValueError`. Use that signal to reject the row and record the reason.

## 4. Give `clean_row` one clear job

The function receives one raw row and returns one of two results:

```python
clean_row(raw_row)
# Valid: (cleaned_dictionary, None)
# Invalid: (None, "reason")
```

A valid result:

```python
cleaned = {
    "city": "Hanoi",
    "observed_at": "2026-08-01",
    "temperature_c": 31.2,
    "humidity_pct": 78,
}
return cleaned, None
```

A rejected result:

```python
return None, "temperature_c is not a number"
```

Separating this work into a function lets you read, test, and change the rules for **one row** without also thinking about files, output, and reporting.

## 5. Check each field in order

Inside `clean_row`, return immediately when a check fails.

### 5.1 City

```python
city = raw_row["city"].strip()
if not city:
    return None, "city is empty"
```

`strip()` removes leading and trailing whitespace. A string containing only spaces becomes empty.

### 5.2 Date

```python
observed_at = raw_row["observed_at"].strip()
try:
    date.fromisoformat(observed_at)
except ValueError:
    return None, "observed_at is not YYYY-MM-DD"
```

`date.fromisoformat` parses an ISO date and checks that it exists. For example, `2026-02-30` is rejected.

### 5.3 Numbers

```python
try:
    temperature_c = float(raw_row["temperature_c"])
    humidity_pct = int(raw_row["humidity_pct"])
except ValueError:
    return None, "temperature_c or humidity_pct is not numeric"
```

Then check the ranges:

```python
if not -50 <= temperature_c <= 60:
    return None, "temperature_c is outside allowed range"

if not 0 <= humidity_pct <= 100:
    return None, "humidity_pct is outside allowed range"
```

Avoid `except Exception`: it can hide programming mistakes. Here, the expected conversion error is `ValueError`.

## 6. Four data structures used in the exercise

| Structure | Used for | Why |
|---|---|---|
| `dict` | One data row | Access values by column name, such as `row["city"]` |
| `list` | `accepted_rows` | Keep clean rows in order for output |
| `set` | `seen_keys` | Check whether a key has been seen |
| `Counter` | `rejection_reasons` | Count how often each rejection reason occurs |

Duplicate detection:

```python
key = (clean["city"], clean["observed_at"])
if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue

seen_keys.add(key)
accepted_rows.append(clean)
```

`continue` skips the rest of the current loop iteration and moves to the next CSV row.

## 7. Read and write files safely

`with` closes the file when the block finishes, even if an error occurs:

```python
with INPUT_PATH.open(newline="", encoding="utf-8") as source_file:
    reader = csv.DictReader(source_file)
    for raw_row in reader:
        print(raw_row)
```

`DictReader` uses the CSV header as dictionary keys. The `csv` module recommends `newline=""` when opening CSV files to handle newlines correctly across operating systems.

`DictWriter` needs the output column order:

```python
writer = csv.DictWriter(output_file, fieldnames=[
    "city", "observed_at", "temperature_c", "humidity_pct",
])
writer.writeheader()
writer.writerows(accepted_rows)
```

## 8. Pseudocode for the unfinished work

Read the pseudocode and turn it into Python yourself. Return to earlier sections if you get stuck.

### 8.1 TODOs 5–7: code inside the loop

Three variables are already prepared in `main`:

```python
accepted_rows = []             # Stores valid rows
rejection_reasons = Counter()  # Counts rejection reasons
seen_keys = set()              # Remembers keys already seen
```

Immediately after:

```python
clean, rejection_reason = clean_row(raw_row)
```

replace the three TODOs and `pass` with:

```python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue

key = (clean["city"], clean["observed_at"])

if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue

seen_keys.add(key)
accepted_rows.append(clean)
```

**Branch 1: invalid row.** `clean_row` returns `(None, "reason")`. The condition `clean is None` is true, so increment that reason's count and move to the next row:

```python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue
```

For a row containing `temperature_c = not_available`, the counter becomes:

```python
rejection_reasons["temperature_c or humidity_pct is not numeric"]
# 1
```

**Branch 2: valid but duplicate.** After branch 1, `clean` is a dictionary. Build a tuple of city and date, which can be stored in a set:

```python
key = (clean["city"], clean["observed_at"])
```

For Hanoi on 2026-08-01:

```python
("Hanoi", "2026-08-01")
```

If the key is already in `seen_keys`, count the duplicate and skip the row. Do not append it:

```python
if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue
```

**Branch 3: valid and new.** This is where you save the row. Remember its key, then append the clean dictionary:

```python
seen_keys.add(key)
accepted_rows.append(clean)
```

### 8.2 Syntax needed for TODOs 5–7

| Syntax | Meaning in this exercise |
|---|---|
| `if condition:` | Run the indented block only when the condition is true |
| `continue` | Stop processing this row and move to the next loop iteration |
| `key in seen_keys` | Check whether the set already contains the key |
| `counter[name] += 1` | Increment the count for a named reason |

Read the relevant sections, about 5–10 minutes each:

- [Python: `if`](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python: `continue` in loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Python: sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python: Counter](https://docs.python.org/3/library/collections.html#collections.Counter)

### 8.3 Check the column name before running

The column in `weather.csv` is named `temperature_c`. Use that exact key in TODO 2:

```python
temperature_c = float(raw_row["temperature_c"])
```

`raw_row["temperature"]` raises `KeyError` because that column does not exist.

```text
create the output folder
create a list for valid rows
create a Counter for rejection reasons
create a set for seen keys

for each CSV row:
    call clean_row
    if invalid:
        count the reason
        move to the next row

    build a key from city and observed_at
    if the key has been seen:
        count the duplicate
        move to the next row

    save the key in the set
    append the clean row to the list

write the valid rows to CSV
print the counts and reasons
```

## 9. Check your understanding

1. Why convert `"78"` to `78`?
2. Why should one invalid row not stop the whole cleaning pipeline?
3. Why use `(city, observed_at)` instead of only `city` for duplicates?
4. If you run the script twice, does the output double in size? Why?

Question 4 introduces **idempotency**: repeating the same input should still produce the correct result. We return to it in Day 17.

## 10. References for today's topics

Open only what you need:

- [Python Tutorial: control flow, functions, and data structures](https://docs.python.org/3/tutorial/)
- [Python csv: DictReader and DictWriter](https://docs.python.org/3/library/csv.html)
- [Python datetime: dates](https://docs.python.org/3/library/datetime.html)
- [Pro Git: basics](https://git-scm.com/book/en/v2)

## When should you look for an answer?

Try a TODO yourself for up to 45 minutes. If stuck, send your current code and the error. I will give a hint for that step so you can still practise solving it.
