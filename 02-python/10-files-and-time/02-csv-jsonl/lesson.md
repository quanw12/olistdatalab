# CSV, JSON, JSON Lines, and schema boundaries

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/csv.html).

## Concept and purpose

CSV separates fields, but quoted fields may contain commas and line breaks. Use csv.DictReader rather than splitting each line on commas. Open CSV with newline="" so the csv module handles newline translation.

DictReader maps headers to string values. It does not infer integers or dates. Check the expected field names before processing data. Missing fields, duplicate headers and extra columns can otherwise produce surprising records.

JSON encodes one structured value. JSON Lines stores one complete JSON value per line and is convenient for incremental writing and rejected records. Use json.loads for parsing and json.dumps for encoding; a Python dictionary's str representation is not JSON.

Schema validation and value validation are separate. This lesson checks shape and preserves raw strings. Later lessons interpret money/time and reject individual values.

## Syntax example

~~~python
import csv
import io
import json

text = 'city,amount\n"Hue, Central",10.00\n'
row = next(csv.DictReader(io.StringIO(text)))
print(row["city"])
print(json.dumps(row, ensure_ascii=False))
~~~

## Trace the example

The quoted comma stays inside the city field. The amount remains the string '10.00'.

## Apply it to DE

Preserving raw input allows you to explain a rejection instead of losing the original value during conversion.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.


## API quick reference

| Syntax | Purpose |
|---|---|
| `reader.fieldnames` | The parsed header list; compare it with the declared schema, including duplicates. |
| `row[None] / row[name] is None` | DictReader can place extra cells under None or use None for missing cells. |
| `json.loads(line) / json.dumps(record)` | Parse one JSON value / encode it. A JSONL record occupies one line. |
