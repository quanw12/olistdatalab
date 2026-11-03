# 01 · Python from zero

> **DEcourse:** [Syntax và ví dụ tiếng Việt](../../DEcourse/01%20-%20Python/Python%20co%20ban%20va%20Collections.md) · [Lịch chuẩn và core/tự chọn](../README.md). Video dùng theo bài chẩn đoán, không bắt buộc xem hết.

**Lịch mới:** 1–3 · **Điều kiện:** none

## Goal
Write small, clean Python programs from a blank file: variables, control flow, functions,
collections, files, errors, dates, modules and a virtual environment. These are exactly the
pieces the platform's `ingest.py` and `fx.py` are made of.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Python Full Course for Beginners — Data with Baraa](https://www.youtube.com/watch?v=Rq5gJVxz55Q) | **The whole course**, in order. Main course of this module | 13 h |
| [Python Virtual Environments (Windows) — Corey Schafer](https://www.youtube.com/watch?v=APOPm01BVrk) | After Baraa's setup chapter | 17 min |
| [Comprehensions — Corey Schafer](https://www.youtube.com/watch?v=3dt4OGnU5sM) | After lists/dicts | 18 min |
| [OOP 1: Classes and Instances — Corey Schafer](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) and [OOP 4: Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE) | Week 3, enough OOP to read `dataclass` and exceptions | 35 min |
| [Logging Basics — Corey Schafer](https://www.youtube.com/watch?v=-ARI4Cz-awo) | Week 3 | 14 min |

Split Baraa's 13 h into ~1.5 h per session. Type every example; do not just watch.

## 2. Read (official docs)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) — chapters 3–9 as a written companion to the video
- [`csv`](https://docs.python.org/3/library/csv.html) · [`pathlib`](https://docs.python.org/3/library/pathlib.html) · [`datetime`](https://docs.python.org/3/library/datetime.html) · [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html) · [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) · [`hashlib`](https://docs.python.org/3/library/hashlib.html)
- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## 3. Syntax sheet
```python
# collections
ids = ["a", "b", "a"]
unique = set(ids)                         # {'a', 'b'}
counts = {}                               # dict counting by hand
for x in ids:
    counts[x] = counts.get(x, 0) + 1
from collections import Counter
Counter(ids).most_common(1)               # [('a', 2)]
squares = [n * n for n in range(5) if n % 2 == 0]   # comprehension with a filter

# functions with type hints and keyword-only args
def greet(name: str, *, loud: bool = False) -> str:
    text = f"hello {name}"
    return text.upper() if loud else text

# files: always `with`, always an encoding
from pathlib import Path
import csv
path = Path("data") / "file.csv"
with path.open(newline="", encoding="utf-8") as f:
    for line_no, row in enumerate(csv.DictReader(f), start=2):   # row is a dict
        print(line_no, row["some_column"])

# errors: raise your own message, keep the original cause
try:
    value = int("abc")
except ValueError as e:
    raise ValueError("price is not a number: 'abc'") from e

# dates and time zones
from datetime import datetime, timezone
from zoneinfo import ZoneInfo            # Windows: pip install tzdata
naive = datetime.strptime("2017-10-02 10:56:33", "%Y-%m-%d %H:%M:%S")
local = naive.replace(tzinfo=ZoneInfo("Asia/Ho_Chi_Minh"))
utc = local.astimezone(timezone.utc)
```

## 4. Practice (not the project yet)
1. FizzBuzz, then a function `word_count(text) -> dict` without `Counter`, then with it.
2. Read any CSV you have (school data, a Kaggle file); print row count and the 3 most common values of one column.
3. Write `safe_int(text) -> int | None` that returns `None` for blanks and raises a clear error for garbage.
4. Convert "2024-03-10 01:30:00" and "2024-03-10 03:30:00" from `America/New_York` to UTC. Compare elapsed time and wall-clock time across the spring DST transition. Investigate why local 02:30 did not exist.

## 5. Apply to the project — lab 01
Folder: [`labs/01-python`](../../labs/01-python). Open `olist_basics.py`: every function has a
docstring that says what to do and a hint, but no code. Make the tests pass:

```powershell
olist sample --orders 500          # gives you a real-looking CSV in data/landing/olist/
pytest labs/01-python -v           # red at first; your job is to make it green
```

Hints, in order of the tests:
- `normalize_status`: think about which string methods remove spaces and change case. What should happen for `None`?
- `parse_olist_time`: `strptime` → attach the São Paulo zone → convert to UTC. Empty text means "not happened yet", not an error.
- `find_duplicates`: a `set` of seen ids answers "seen before?" in one step. `ids.count(x)` inside a loop is correct but gets ~4× slower each time the data doubles — measure it with 100k ids.
- `read_orders`: `csv.DictReader`, `encoding="utf-8-sig"` (Excel adds an invisible BOM). Return the rows and the line number of each.
- `summarize_status`: one pass over the rows.

When everything is green, compare your `parse_olist_time` with the dbt macro `dbt/macros/olist_time.sql`:
same idea, different tool.

## 6. Self-check
- Difference between a list, a tuple, a set and a dict — when do you pick each?
- What does `with` guarantee?
- Why store timestamps in UTC but report by local date?
- What is a virtual environment and why does every project get its own?

## Done when
- [ ] Baraa's Python course finished, examples typed
- [ ] `pytest labs/01-python` green without looking at reference code
- [ ] Practice 1–4 done in your own folder
