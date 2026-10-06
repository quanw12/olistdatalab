# Day 14 — Mini-project 2: a reusable loader and SQL mart


## Packages and imports

A module is a Python file. A package groups modules; use an empty __init__.py to mark this clearly. Running python -m weather_pipeline executes weather_pipeline/__main__.py from its parent directory.

Create the initial package in capstone: __init__.py, __main__.py, load.py and mart.py, plus sql/staging.sql and sql/mart.sql. Reuse your Day 13 solution. Daily folders hold study records; capstone holds the application.

An import brings a definition into another module:

~~~python
from weather_pipeline.load import load_records
~~~

This works after you create that package. Keep database connections and file reads inside functions, not at module import time.

## CLI subcommands

~~~python
import argparse

parser = argparse.ArgumentParser()
commands = parser.add_subparsers(dest="command", required=True)
load_command = commands.add_parser("load")
load_command.add_argument("--input", required=True)
args = parser.parse_args()
~~~

Subcommands allow load now and run/backfill/quality later. args.input is a string; Path(args.input) is a path object. Document capstone as the working directory, and test --help before adding database logic.

## Staging and mart

Staging contains normalized provider observations. A mart uses dimensions and facts to support reports. Both are schemas inside one database today.

Use [the contract](../capstone/contract.md) for columns. Load every configured city, including Hue. Resolve the generated city_key by city_name, not CSV row number. This project's city-name key is a simplification; a larger system needs stable source location identifiers and a renaming policy.

Load distinct local dates into dim_date. Load facts after dimensions. Keep UNIQUE(city_key, observed_at, source): an identity-generated observation_key alone cannot prevent duplicate observations.

## INSERT SELECT

On an unrelated model:

~~~sql
INSERT INTO example_fact (product_key, amount)
SELECT d.product_key, s.amount
FROM example_stage AS s
JOIN example_dimension AS d ON d.product_code = s.product_code;
~~~

Your refresh_mart uses this shape, with ON CONFLICT for reruns. Convert observed_at to each city's named zone before deriving observation_date. Validate unknown cities before an INNER JOIN so missing mappings cannot silently drop facts.

The caller opens one transaction, calls load_records then refresh_mart, and commits both. Full refresh from the tiny staging table is acceptable now; preserve keys and use upserts rather than destructive reloads.

Read: [Python modules](https://docs.python.org/3.13/tutorial/modules.html), [argparse](https://docs.python.org/3.13/library/argparse.html), [PostgreSQL INSERT](https://www.postgresql.org/docs/18/sql-insert.html).
