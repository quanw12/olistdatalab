# Day 16 — ETL, file layers, and a complete batch pipeline


## Layers explain where a failure happened

Extract obtains source data, transform changes structure/meaning, load writes a destination. ETL transforms before loading the target. ELT loads data first and transforms inside the database. This project combines Python normalization into staging with SQL transformation into a mart.

Raw data preserves provider content and request metadata. Clean data satisfies a contract. Rejected data retains failed input and reasons. A manifest describes one run's files, counts and status. Cleaning is more than deleting unused fields.

## Timezone syntax

~~~python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

local = datetime.fromisoformat("2026-09-18T09:00")
aware = local.replace(tzinfo=ZoneInfo("Asia/Ho_Chi_Minh"))
print(aware.astimezone(timezone.utc).isoformat())
# 2026-09-18T02:00:00+00:00

~~~

replace attaches a zone to a known local wall time; astimezone converts an aware instant. Attaching UTC to a local+07 time changes its meaning by seven hours. Other regions need explicit DST ambiguity policies; our fixture avoids that complication. Windows may need the tzdata package.

## Pure transformation

normalize_record(envelope) returns a new dictionary or raises ValueError with a field-specific reason. Do not mutate raw input. transform_batch returns accepted rows and rejected items with zero-based input index, reason and original input. Check required text, configured city/zone, offset-aware request time, valid observation time, finite temperature and integral humidity. Reject bool and fractional humidity before int conversion.

The accounting invariant is input_count = accepted_count + rejected_count.

## File formats

JSON supports nested data but not native datetime objects. CSV is portable but loses type information. Parquet stores typed columns and supports reading selected columns. The format does not enforce your business rules.

~~~python
from pathlib import Path
import json

path = Path("output") / "example.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps({"count": 3}, indent=2), encoding="utf-8")
~~~

Optional: write clean data as Parquet with pandas and pyarrow, read back and compare values/types. Convert timestamps explicitly; string columns do not become timestamps because the extension changes.

## File and database commits differ

Save raw input first, transform, then load staging and mart in one transaction. Publish a success manifest after commit. If writing the manifest fails after DB commit, the database is already changed. Record the failure and recover by idempotent replay. Use distinct run directories and replace a temporary manifest on the same filesystem to avoid a half-written published file.

Read: [zoneinfo](https://docs.python.org/3.13/library/zoneinfo.html), [pathlib](https://docs.python.org/3.13/library/pathlib.html), [Parquet](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html).
