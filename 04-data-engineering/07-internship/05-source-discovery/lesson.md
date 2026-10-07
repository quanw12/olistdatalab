# Source discovery, profiling and a useful catalog

A sample shows what happened in that sample. It cannot prove an ID is always unique
or a feed complete. Inspect shape, raw types, blanks, repeated identities, time
formats and ranges before coding a loader. Separate observations, hypotheses and
confirmed owner decisions.

**Profiling** measures a sample without silently cleaning it. A **catalog** records
meaning, ownership and access. **Lineage** connects source fields/transformations to
outputs. Small Markdown tables are sufficient; no new catalog platform is needed.

## Required syntax

| Python syntax | Purpose |
|---|---|
| `csv.DictReader(stream), reader.fieldnames` | Read quoted CSV and its header; open with newline="" and encoding="utf-8". |
| `value.strip(), value.isascii(), value.isdecimal()` | Inspect blanks and ASCII digit text without guessing the source schema. |
| `set(), tuple(values), len(collection)` | Count distinct values or represent a composite candidate key. |
| `datetime.fromisoformat(text), value.utcoffset()` | Parse ISO time and inspect awareness. |
| `except ValueError:` | Count expected parse failures; preserve file/permission failures. |
| `argparse.ArgumentParser(), add_argument(...), parse_args()` | Define --input and --output options. |
| `json.dumps(report, indent=2)` | Encode JSON; a printed Python dictionary is not JSON. |

~~~python
from datetime import datetime

instant = datetime.fromisoformat("2026-10-01T09:00:00+09:00")
print(instant.utcoffset() is not None)
print(" 007 ".strip().isascii())
~~~

Both outputs are True. Neither confirms business meaning; an ID may preserve
leading zeros deliberately.

Candidate-key duplication depends on grain. Repeated item IDs might be history;
repeated item/site/version combinations might be replays or conflicts. Count first,
then ask. Different offset text can represent one instant. State whether you count
raw values or normalized meanings.

A contact email is unnecessary for a stock report. Record sensitivity/access/
retention and omit it from the consumer output. This synthetic fixture's retention
is a lab policy, not legal guidance.

The assignment leaves grouping, validation structure and reporting logic to you.
Your handoff must explain defects and unresolved guarantees, not just say checks passed.

[CSV reference](https://docs.python.org/3.13/library/csv.html) ·
[Datetime reference](https://docs.python.org/3.13/library/datetime.html)
