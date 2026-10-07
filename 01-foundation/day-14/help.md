# Day 14 — Mini-project 2: a reusable loader and SQL mart

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

1. Create weather_pipeline and empty __init__.py. Implement __main__.py argument parsing; test --help.
2. Copy your reusable Day 13 functions into load.py. Remove script-level execution, then import functions from __main__.py.
3. Write sql/mart.sql from the contract; retain sql/staging.sql for fresh setups. DDL is a bootstrap step, not part of every batch.
4. Upsert all configured cities by city_name. Insert distinct local dates with year/month/ISO weekday. Then join staging to dimensions and upsert facts.
5. Use the same connection for staging and mart. A second connection cannot share the transaction or see uncommitted staging writes.
6. Query Hue with LEFT JOIN and COUNT(f.observation_key), preserving NULL average.
7. Raise an intentional temporary error inside refresh_mart to check rollback; remove it after proving atomicity. Do not report success if only staging completed.

</details>
