# 06 · Ingestion and data quality

> **DEcourse:** [Syntax và ví dụ tiếng Việt](../../DEcourse/04%20-%20Core%20DE/Ingestion%20Contract%20va%20Idempotency.md) · [Lịch chuẩn và core/tự chọn](../README.md). Video dùng theo bài chẩn đoán, không bắt buộc xem hết.

**Lịch mới:** 10–11 · **Điều kiện:** 01–05

## Goal
Build a loader that is **idempotent** (running twice = once), **checks a contract** before
publishing, keeps the last good data when a file is broken, and leaves an audit trail.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [What is a Data Contract? — IBM Technology](https://www.youtube.com/watch?v=-n3OD-ml_k0) | All | 3 min |
| [What Are Data Contracts? (in production) — The Data and AI Guy](https://www.youtube.com/watch?v=6svVYbAcfHc) | All | 12 min |
| [Idempotency — what it is and how to implement it — Alex Hyett](https://www.youtube.com/watch?v=XAccGbtl3Z8) | All | 8 min |
| [The Importance of Idempotency in Data Pipelines — PracticalGCP](https://www.youtube.com/watch?v=pKZ5n-y3ug4) | All | 4 min |
| [Docker for Data Engineering: Postgres, Compose — DataTalksClub (Zoomcamp)](https://www.youtube.com/watch?v=lP8xXebHmuE) | Ingestion part (loading CSV in chunks) | 2 h |

## 2. Read
- [DuckDB: reading CSV files](https://duckdb.org/docs/stable/data/csv/overview) · [Parquet export](https://duckdb.org/docs/stable/data/parquet/overview) · [Transactions](https://duckdb.org/docs/stable/sql/statements/transactions)
- [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) · [Python `dataclasses`](https://docs.python.org/3/library/dataclasses.html)
- Optional: how tools package these ideas — [Great Expectations](https://docs.greatexpectations.io/docs/core/introduction/), [Soda](https://docs.soda.io/)

## 3. Syntax sheet
```python
import duckdb, hashlib, yaml
con = duckdb.connect("lab.duckdb")

# load a CSV with every column as text, plus lineage columns
con.execute("""
    CREATE OR REPLACE TABLE stage_orders AS
    SELECT *, ? AS _source_file, current_timestamp AS _loaded_at
    FROM read_csv(?, header = true, all_varchar = true)
""", ["orders.csv", "data/orders.csv"])

# one check = one query that COUNTS failing rows
dupes = con.execute("""
    SELECT coalesce(sum(n - 1), 0) FROM
      (SELECT count(*) AS n FROM stage_orders GROUP BY order_id HAVING n > 1)
""").fetchone()[0]

# atomic publish: either the new table or the old one, never half
con.execute("BEGIN TRANSACTION")
con.execute("DROP TABLE IF EXISTS orders")
con.execute("ALTER TABLE stage_orders RENAME TO orders")
con.execute("COMMIT")

# file fingerprint for idempotency
digest = hashlib.sha256(open("data/orders.csv", "rb").read()).hexdigest()

contract = yaml.safe_load(open("contract.yml", encoding="utf-8"))
```

## 4. Practice
Load the same CSV twice with plain `INSERT INTO … SELECT` and count rows. Now design three ways
to make the second load a no-op (hash check, delete+insert by key, `INSERT … ON CONFLICT`).

## 5. Apply to the project — lab 06
Folder: [`labs/06-ingest`](../../labs/06-ingest). You write `my_ingest.py`; the tests describe the
behaviour. Run `pytest labs/06-ingest -v`.

Build it in this order (one test group at a time):
1. **Contract file** `contract.yml` for orders only: columns, primary key, not-null columns,
   accepted statuses, timestamp columns. Hint: start from the table in `docs/data-contract.md`.
2. `check_header(path, contract)` — missing column → raise; extra column → return its name.
3. `load_candidate(con, path)` — all text + `_source_file`, `_file_sha256`, `_loaded_at`.
4. `run_checks(con, table, contract)` → list of `(check_name, severity, failed_rows)`.
   Hint: write the SQL for one check by hand first, then generate it with an f-string per column.
   Severity: broken key/format = `error`; "delivered without date" = `warn`.
5. `ingest(con, path, contract)` — skip only if hash matches the current published table; else load → check →
   publish atomically → write manifest. On any `error` check: raise and keep the old table.

When green, compare with `src/olist_platform/ingest.py` and `quality.py`. Note in your PR
what you did differently.

## 6. Self-check
- What happens in your loader if the file arrives twice? Half-written? With a new column?
- Why keep bronze as text?
- Which checks should stop the pipeline and which only warn? Give one example each from Olist.

## Done when
- [ ] Contract-checks videos watched, lab 06 green
- [ ] Your design compared with the reference, differences in the PR description

## Yêu cầu cập nhật · hướng sản phẩm

Bắt buộc thêm regression A→B→A: skip chỉ khi input trùng phiên bản đang publish, không phải mọi hash từng nạp. Xóa Parquet và thử output cũ sau DB commit: retry phải khôi phục. Bản tham chiếu re-export local Parquet cả khi bỏ qua DB load; ghi trade-off I/O, giới hạn một writer và publish từng bảng.
