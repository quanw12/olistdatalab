---
tags: [decourse, python, storage]
module: 01
---

# Files: CSV, JSON and Parquet

> [!info] Learning goals
> After this note you can: work with paths safely using `pathlib`; read and write CSV correctly (quoting, encodings, BOM, newlines); use JSON for nested and raw API data; explain why Parquet is the default analytical format; and write files atomically so readers never see half-written output.

## 1. Paths with `pathlib`

String concatenation for paths breaks across operating systems (`\` vs `/`) and with spaces. `pathlib.Path` handles it:

```python
# runnable
from pathlib import Path

root = Path("data") / "landing" / "olist"
csv_path = root / "olist_orders_dataset.csv"
assert csv_path.name == "olist_orders_dataset.csv"
assert csv_path.suffix == ".csv"
assert csv_path.stem == "olist_orders_dataset"
assert csv_path.parent == root
assert csv_path.with_suffix(".parquet").name == "olist_orders_dataset.parquet"
```

Useful methods: `.exists()`, `.mkdir(parents=True, exist_ok=True)`, `.glob("*.csv")`, `.read_text(encoding=...)`, `.write_text(...)`, `.open(...)`, `.replace(target)`. Always pass `encoding="utf-8"` explicitly: on Windows the default encoding may not be UTF-8.

## 2. Text encodings in one minute

Files store **bytes**; text is bytes decoded with an **encoding**. UTF-8 is the standard. Two practical issues:

- **BOM:** Excel often writes UTF-8 with a byte-order mark (`﻿`) at the start. Read with `encoding="utf-8-sig"` and the BOM disappears; otherwise your first column is called `﻿order_id` and lookups fail.
- **Wrong encoding:** decoding Latin-1 bytes as UTF-8 raises `UnicodeDecodeError` or produces garbage like `SÃ£o Paulo`. Olist contains Portuguese text (`São Paulo`), so this matters.

## 3. CSV: simple to write, hard to read correctly

CSV has no types and many dialects. Fields containing the delimiter, quotes or newlines are wrapped in quotes, and quotes inside are doubled (`""`). That is why `line.split(",")` is wrong:

```python
# runnable
import csv
import json
from io import StringIO

source = StringIO('order_id,note\no1,"fast delivery, well packed"\n')
rows = list(csv.DictReader(source))
assert len(rows) == 1
assert rows[0]['note'] == 'fast delivery, well packed'

naive = 'o1,"fast delivery, well packed"'.split(',')
assert len(naive) == 3            # wrong: the comma inside quotes split the field

payload = json.dumps(rows, ensure_ascii=False)
assert json.loads(payload) == rows
```

A field can even contain a newline, so "number of lines" is not "number of records":

```python
# runnable
import csv
from io import StringIO

text = 'id,comment\n1,"line one\nline two"\n2,ok\n'
assert text.count("\n") == 4                  # what `wc -l` would count
assert len(list(csv.DictReader(StringIO(text)))) == 2   # actual records
```

Rules for reading CSV files in Python:

```python
from pathlib import Path
import csv

with Path("orders.csv").open(newline="", encoding="utf-8-sig") as handle:
    for row in csv.DictReader(handle):   # each row is a dict of strings
        ...
```

- `newline=""` lets the csv module handle line endings inside quoted fields.
- Every value comes back as a **string** (or `""` for empty). Types are your job.
- At the bronze layer, reading everything as text is deliberate: you keep exactly what the source sent and cast later where errors can be reported per column.

Writing:

```python
# runnable
import csv
from io import StringIO

out = StringIO()
writer = csv.DictWriter(out, fieldnames=["order_id", "note"])
writer.writeheader()
writer.writerow({"order_id": "o1", "note": 'said "hi", left'})
assert out.getvalue().splitlines()[1] == 'o1,"said ""hi"", left"'
```

## 4. JSON: nested data and raw API responses

JSON maps directly to Python: object ↔ dict, array ↔ list, string, number, `true/false` ↔ `True/False`, `null` ↔ `None`.

```python
# runnable
import json

raw = '{"base": "BRL", "date": "2018-01-15", "rates": {"USD": 0.31, "VND": 7000}}'
doc = json.loads(raw)
assert doc["rates"]["USD"] == 0.31
assert json.loads(json.dumps(doc)) == doc         # round trip

lines = '{"id": 1}\n{"id": 2}\n'                  # JSON Lines: one object per line
records = [json.loads(line) for line in lines.splitlines()]
assert [r["id"] for r in records] == [1, 2]
```

Use JSON for **raw API payloads**: store exactly what the API returned before transforming it, so you can **replay** the transformation later without calling the API again (see [[API Retry Pagination and Replay]]). JSON Lines (`.jsonl`) is better for large logs because you can append and stream line by line.

Caveats: JSON numbers are parsed as `float` unless you pass `parse_float=Decimal`; JSON has no date type (use ISO-8601 strings); keys are always strings.

## 5. Parquet: the analytical default

Parquet is a **columnar**, **typed**, **compressed** file format.

| Property | CSV | Parquet |
|---|---|---|
| Layout | Row by row | Column by column (in row groups) |
| Types | None (all text) | Stored in the schema (int, decimal, timestamp, …) |
| Compression | Rare | Built in, very effective per column |
| Read 2 of 40 columns | Must parse every byte | Reads only those 2 columns |
| Filter pushdown | No | Row-group statistics (min/max) let engines skip data |
| Human readable | Yes | No |

Why columnar helps: analytical queries usually touch few columns over many rows (`SUM(price) GROUP BY seller_id`). Storing each column contiguously means the engine reads only the needed columns, and similar values compress well.

```python
# runnable
import pandas as pd
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / 'orders.parquet'
    expected = pd.DataFrame({'order_id': ['o1', 'o2'], 'amount': [10, 20]})
    expected.to_parquet(path, index=False)
    actual = pd.read_parquet(path)
    pd.testing.assert_frame_equal(expected, actual)
    # Read a single column: the other columns are never decoded.
    only_ids = pd.read_parquet(path, columns=['order_id'])
    assert list(only_ids.columns) == ['order_id']
```

DuckDB can query Parquet directly: `SELECT seller_id, sum(price) FROM 'data/lake/silver/order_items.parquet' GROUP BY 1`. Large datasets are often split into many files by a partition column (`order_date=2018-01-15/part-0.parquet`); see [[Performance and Storage]].

**When to choose which:** CSV for exchanging small data with humans or legacy systems; JSON for nested/raw API data and configs; Parquet for anything analysed repeatedly.

## 6. Atomic writes: never expose half a file

If a process crashes while writing `orders.parquet`, a reader may see a truncated file. The fix: write to a temporary file **on the same filesystem**, then rename it over the target. A rename on the same filesystem is atomic: readers see either the old file or the new one.

```python
# runnable
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    target = Path(directory) / 'raw.json'
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text('{"batch": 1}', encoding='utf-8')
    temporary.replace(target)          # atomic swap on the same filesystem
    assert target.read_text(encoding='utf-8') == '{"batch": 1}'
    assert not temporary.exists()
```

Limits: this does not create a transaction across the database **and** the filesystem; it does not guarantee durability through a power loss unless you also `fsync`; and it does not work across different filesystems or object stores (S3/GCS have their own semantics).

## 7. Applying it to Olist

- Raw CSVs land in `data/landing/olist/` exactly as downloaded; you hash them to detect new versions (see [[Ingestion Contracts and Idempotency]]).
- Raw FX API responses are stored as JSON before transformation, so you can replay.
- Gold tables are exported to Parquet for analysis and dashboards.
- A Parquet export can fail **after** the database commit, so a retry must repair the output even if the database is already loaded. A file existing does not mean it is the right version.

## 8. Common mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| `line.split(",")` | Wrong fields when quotes contain commas | `csv` module |
| Counting lines as records | Wrong counts with multi-line fields | Count parsed records |
| Default encoding on Windows | `UnicodeDecodeError`, mojibake | `encoding="utf-8"` / `"utf-8-sig"` |
| Writing directly to the final path | Readers see partial files | Temp file + `replace` |
| Parsing money from JSON as float | Rounding errors | `parse_float=Decimal` |
| Storing analytics data as CSV | Slow, untyped, large | Parquet |

## 9. Exercises

1. Build a CSV with a comma inside quotes, a newline inside quotes, a BOM and a blank line. Read it with `csv` and show how manual splitting goes wrong.
2. Write the same 100k-row DataFrame to CSV and Parquet; compare file sizes and the time to read one column.
3. Delete the Parquet output of a copy of the pipeline and run the loader again: does it rebuild the file even though the database already has the data?

## 10. Review questions

> [!question]- When would you choose JSON instead of Parquet?
> For nested or semi-structured data, raw API payloads you want to replay exactly, configuration and small messages. Parquet is for typed tabular data that will be queried.

> [!question]- Why does write-to-temp-then-rename not make the whole pipeline atomic?
> It protects one file only. The database commit and the file write are separate operations; a crash between them leaves them inconsistent, so retries must be able to repair either side.

> [!question]- Why read bronze CSVs as text?
> To keep exactly what the source sent. Casting happens in staging where each failure can be reported with the raw value, instead of a loader guessing types and silently converting.

> [!question]- What does columnar storage buy you?
> Reading only the needed columns, much better compression, and min/max statistics that let engines skip whole row groups.

Related: [[Ingestion Contracts and Idempotency]], [[Performance and Storage]], [[DataFrames pandas and Polars]]. Sources: [csv module](https://docs.python.org/3/library/csv.html), [pathlib](https://docs.python.org/3/library/pathlib.html), [pandas IO tools](https://pandas.pydata.org/docs/user_guide/io.html), [Apache Parquet docs](https://parquet.apache.org/docs/).
