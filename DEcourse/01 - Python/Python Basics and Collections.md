---
tags: [decourse, python, foundations]
module: 01
---

# Python Basics and Collections

> [!info] Learning goals
> After this note you can: explain how Python names, values and types work; pick the right collection (list, tuple, set, dict) for a job and know its cost; write loops and comprehensions that clean messy records; and avoid the classic traps (mutable aliasing, silent overwrites, `None` vs. empty).

## 1. Why Python in data engineering

A pipeline has two kinds of work. **Set-based transformations** — filter, join, aggregate millions of rows — belong in an engine (SQL, DuckDB, Spark), because the engine optimises and parallelises them. **Control and glue** — read files, call APIs, validate records, decide what to do on failure, orchestrate steps — belong in a general-purpose language. Python is the default glue language of data engineering because it reads like pseudocode, has libraries for every file format and service, and is what Airflow, dbt, Spark (PySpark) and most SDKs expose.

Rule of thumb: if you are writing a Python loop that does what `GROUP BY` does, stop and ask whether SQL should do it.

## 2. Names, values and types

In Python a variable is a **name bound to an object**. The object has a type; the name does not.

```python
# runnable
count = 3          # name 'count' -> int object 3
count = "three"    # the same name now points to a str object
assert type(count) is str

a = [1, 2]
b = a              # b is another name for the SAME list object
b.append(3)
assert a == [1, 2, 3]       # a "changed" because a and b are one object
assert a is b               # identity: same object
c = list(a)                 # a shallow copy is a new object
assert c == a and c is not a
```

- `==` compares **values**; `is` compares **identity** (same object). Use `is` only for `None`, `True`, `False`.
- **Mutable** objects (list, dict, set) can change in place. **Immutable** objects (int, float, str, tuple, frozenset) cannot; "changing" them creates a new object.
- Aliasing (two names, one mutable object) is the source of many bugs: a function that "only reads" a list but appends to it changes the caller's data.

### Core scalar types

| Type | Example | Notes for data work |
|---|---|---|
| `int` | `42` | Arbitrary precision — no overflow |
| `float` | `0.1` | Binary floating point: `0.1 + 0.2 != 0.3`. Never use for money (see [[Datetime Decimal and Timezones]]) |
| `bool` | `True` | A subclass of int: `True + True == 2` |
| `str` | `"o1"` | Immutable Unicode text; `.strip()`, `.lower()`, `.split()` return new strings |
| `None` | `None` | "No value". Not `0`, not `""`, not `False` — but all four are *falsy* |

**Truthiness:** `if x:` is false for `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`. That is convenient and dangerous: `if amount:` treats a legitimate `0` the same as a missing value. When missingness matters, write `if amount is None:`.

## 3. Collections and when to use each

| Type | Ordered | Mutable | Duplicates | Lookup `x in c` | Use for |
|---|---|---|---|---|---|
| `list` | yes | yes | yes | O(n) scan | sequences, rows in arrival order |
| `tuple` | yes | no | yes | O(n) | fixed records, dict keys made of several fields |
| `set` | no | yes | no | O(1) average | membership tests, distinct values, set algebra |
| `dict` | insertion order | yes | keys unique | O(1) average by key | key → value lookups, grouping, records |

**Big-O in one paragraph:** O(1) means the cost does not grow with size; O(n) means it grows linearly. `x in my_list` scans every element, so doing it inside a loop over n items costs O(n²): fine for 1,000 items, painful for 1,000,000. Convert the list to a set first and the same loop becomes O(n).

### Lists

```python
# runnable
rows = ["o1", "o2", "o3"]
rows.append("o4")              # add at the end, O(1)
first, *rest = rows            # unpacking
assert first == "o1" and rest == ["o2", "o3", "o4"]
assert rows[-1] == "o4"        # negative index from the end
assert rows[1:3] == ["o2", "o3"]   # slice: start inclusive, end exclusive
assert sorted(["b", "a", "c"]) == ["a", "b", "c"]  # sorted() returns a new list
```

### Tuples

A tuple is an immutable sequence. Because it is immutable (and hashable when its items are), it can be a **dict key or set member** — perfect for composite keys like `(order_id, item_id)`. A one-element tuple needs a trailing comma: `(x,)`; `(x)` is just `x` in parentheses.

### Sets

```python
# runnable
yesterday = {"o1", "o2", "o3"}
today = {"o2", "o3", "o4"}
assert today - yesterday == {"o4"}            # new keys
assert yesterday - today == {"o1"}            # disappeared keys (possible deletes!)
assert today & yesterday == {"o2", "o3"}      # in both
assert today | yesterday == {"o1", "o2", "o3", "o4"}
```

That snippet is a real data-engineering technique: diffing the key sets of two snapshots finds inserts and hard deletes (see [[Incremental CDC and Backfill]]). Never use set iteration order as business order — it is arbitrary.

### Dicts

```python
# runnable
order = {"order_id": "o1", "status": "delivered"}
assert order.get("amount") is None             # .get avoids KeyError
assert order.get("amount", 0) == 0             # explicit default
order["status"] = "canceled"                   # assignment OVERWRITES silently
assert order["status"] == "canceled"

# grouping: key -> list of values
from collections import defaultdict
items = [("o1", 10), ("o2", 5), ("o1", 7)]
by_order = defaultdict(list)
for order_id, price in items:
    by_order[order_id].append(price)
assert dict(by_order) == {"o1": [10, 7], "o2": [5]}
```

Building a dict from records with `{r["id"]: r for r in rows}` keeps **only the last** record per id. If ids are duplicated, data disappears without an error. Check uniqueness first.

## 4. Control flow and comprehensions

```python
# runnable
amounts = [120, None, 0, 45]
known = [a for a in amounts if a is not None]          # filter
labels = ["missing" if a is None else "zero" if a == 0 else "paid" for a in amounts]
assert known == [120, 0, 45]
assert labels == ["paid", "missing", "zero", "paid"]

squares = {n: n * n for n in range(4)}                 # dict comprehension
assert squares[3] == 9
assert {s.lower() for s in ["A", "a", "B"]} == {"a", "b"}   # set comprehension

total = 0
for index, value in enumerate(known, start=1):         # enumerate gives a counter
    total += value
assert total == 165 and index == 3

for left, right in zip(["a", "b"], [1, 2], strict=True):  # strict: lengths must match
    pass
```

Comprehensions are for building a collection from another. If the body needs several statements, error handling or logging, write a normal loop — readability wins.

## 5. Worked example: cleaning raw statuses and finding duplicates

Raw data is messy: inconsistent case, stray spaces, missing values, duplicate keys. Normalise in a staging step and **keep the raw value** so you can trace every decision.

```python
# runnable
from collections import Counter

statuses = ['Delivered', ' delivered ', None, 'canceled']
normalized = [s.strip().lower() if s is not None else None for s in statuses]
counts = Counter(normalized)
assert counts['delivered'] == 2
assert counts[None] == 1

ids = ['o1', 'o2', 'o1', 'o3', 'o2']
seen, duplicates = set(), set()
for order_id in ids:
    if order_id in seen:
        duplicates.add(order_id)
    seen.add(order_id)
assert duplicates == {'o1', 'o2'}

# Counter can also report how many times each id appears
repeat_counts = {k: v for k, v in Counter(ids).items() if v > 1}
assert repeat_counts == {'o1': 2, 'o2': 2}
```

Result: two delivered, one missing status; two ids appear more than once. Set membership is O(1) on average, so the whole pass is O(n).

> [!warning] Do not "fix" data by hiding the problem
> `set(ids)` loses how many times each id repeated. A dict built from duplicate keys silently drops records. Before deduplicating, find out **why** there are duplicates: a true duplicate delivery, two versions of the same record, or two different entities sharing an id? Each needs a different rule (see [[CTE Dedup and Incremental SQL]]).

## 6. Strings you will use every day

```python
# runnable
raw = "  SP | São Paulo  "
state, city = [part.strip() for part in raw.split("|")]
assert (state, city) == ("SP", "São Paulo")
assert "o1".startswith("o") and "file.csv".endswith(".csv")
assert f"{3.14159:.2f}" == "3.14"            # f-string formatting
assert ",".join(["a", "b"]) == "a,b"
assert "  ".strip() == ""                    # blank becomes empty, not None
```

Decide explicitly whether an empty string after `strip()` means "missing" (then convert to `None`) or is a valid value. Write that policy down in the data contract.

## 7. Applying it to Olist

In module 01 you implement `labs/01-python/olist_basics.py` in the code repo: normalise order statuses, find duplicate ids, parse timestamps. The Olist tables are joined by keys (`order_id`, `customer_id`, `seller_id`, `product_id`); knowing which collection gives fast key lookups is exactly what you need to check keys before a join (see [[JOIN Grain and Fan-out]]).

## 8. Common mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| `if amount:` to test missing | `0` is treated as missing | `if amount is None:` |
| `x in big_list` inside a loop | O(n²) | Build a set once |
| `b = a` then mutating `b` | Changes `a` too | Copy: `list(a)`, `dict(a)`, `copy.deepcopy` for nested |
| Dict from rows with duplicate ids | Silent data loss | Check `len(ids) == len(set(ids))` first |
| Relying on set order | Arbitrary, can change | `sorted(s)` when order matters |
| `(x)` as a one-item tuple | It is just `x` | `(x,)` |

## 9. Exercises

1. Count statuses without `Counter` using a plain dict, then check your result against `Counter`.
2. Add an empty string `""` to the status list. Should it become `None`? Write the policy and implement it.
3. Time `ids.count(x)` inside a loop for 10k and 20k elements, then the set-based version. What growth do you see?
4. Given two snapshots of `(order_id, status)` pairs, report inserted, deleted and changed ids.

> [!example]- Solution sketch for 4
> ```python
> old = {"o1": "created", "o2": "shipped"}
> new = {"o2": "delivered", "o3": "created"}
> inserted = new.keys() - old.keys()          # {'o3'}
> deleted = old.keys() - new.keys()           # {'o1'}
> changed = {k for k in old.keys() & new.keys() if old[k] != new[k]}  # {'o2'}
> ```
> Dict key views support set operations directly.

## 10. Review questions

> [!question]- When should you choose a set over a list?
> When you need fast membership tests or distinct values and do not care about order or duplicates. A set lookup is O(1) on average; a list lookup scans every element.

> [!question]- What information can deduplicating by id destroy?
> How many copies existed, which version was latest, and whether two different entities shared an id. Dedup is a business rule, not a cleanup step.

> [!question]- Why is `if amount:` dangerous for payments?
> Because `0` is falsy: a legitimate zero payment is treated like a missing one. Test `is None` when missingness matters.

> [!question]- What does `b = a` do for a list?
> It creates a second name for the same object. Mutating through `b` changes what `a` shows. Copy explicitly if you need independence.

Related: [[Functions and Error Handling]], [[JOIN Grain and Fan-out]], [[Module 01 - Python]]. Sources: [Python tutorial — data structures](https://docs.python.org/3/tutorial/datastructures.html), [Python time complexity](https://wiki.python.org/moin/TimeComplexity).
