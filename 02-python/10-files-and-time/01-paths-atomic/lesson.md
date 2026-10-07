# Paths, context managers, and safe file replacement

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/pathlib.html).

## Concept and purpose

A Path represents a filesystem path. Path("data") / "orders.csv" combines components without manually concatenating separators. Relative paths resolve from the current working directory. For a script-owned fixture, anchor to Path(__file__).resolve().parent.

with manages a context's entry and exit, including exceptional exit. In with path.open("w", encoding="utf-8") as stream, path.open opens the file and leaving the block closes it. Parent directories can be created with mkdir(parents=True, exist_ok=True).

Writing directly to the final file can leave a truncated result if serialization fails midway. Serialize first, write a temporary sibling, close it, then replace the final path. Using the same directory keeps replacement on the same filesystem. tempfile.NamedTemporaryFile(delete=False, dir=parent) supplies a unique temporary name; close it before replacement on Windows.

This gives readers a complete old or new file at the replacement boundary. It is not a transaction across several files or a guarantee against every hardware/power failure.

## Syntax example

~~~python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "note.txt"
    path.write_text("Hello, Hue", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
~~~

## Trace the example

The text round-trips through an explicitly encoded file. TemporaryDirectory cleans its own lab directory on exit.

## Apply it to DE

A manifest should not appear complete while containing a half-written JSON document.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.


## API quick reference

| Syntax | Purpose |
|---|---|
| `NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, dir=parent)` | Unique sibling temporary file; close it before replacement on Windows. |
| `Path(temp_name).replace(destination)` | Replace one destination path, after serialization/writing succeeds. |
| `Path(temp_name).unlink(missing_ok=True)` | Remove your own leftover temporary file after an error. |
