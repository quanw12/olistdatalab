"""Check the actual local fixture warehouse after learner dbt builds."""
import argparse
from pathlib import Path

import duckdb

COURSE = Path(__file__).resolve().parents[1]


def verify(path, incremental=False):
    if not path.is_file():
        raise ValueError("warehouse missing; complete DE13 models/seed/build first")
    with duckdb.connect(str(path), read_only=True) as con:
        latest = con.execute("SELECT id, version, amount_cents, op FROM latest_changes ORDER BY id").fetchall()
        assert latest == [("A", 2, 1200, "upsert"), ("B", 2, 0, "delete"), ("C", 1, 800, "upsert")], "unexpected latest entity state"
        mart = con.execute("SELECT customer_id, order_count, total_cents FROM mart_customer ORDER BY customer_id").fetchall()
        assert mart == [("c1", 2, 2000)], "unexpected fixture mart"
        if incremental:
            actual = con.execute("SELECT * FROM current_incremental ORDER BY id").fetchall()
            expected = con.execute("SELECT * FROM latest_changes ORDER BY id").fetchall()
            assert actual == expected, "incremental and latest state differ"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=COURSE / "project/dbt/warehouse.duckdb")
    parser.add_argument("--incremental", action="store_true")
    args = parser.parse_args()
    try:
        verify(args.db.resolve(), args.incremental)
    except Exception as exc:
        print(f"FAIL: warehouse: {type(exc).__name__}: {exc}")
        return 1
    print("PASS: local fixture warehouse. Record dbt test/mutation and live loader evidence separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
