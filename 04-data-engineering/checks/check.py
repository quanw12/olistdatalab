"""Provided offline checks. Learner implementations remain prompt-only."""
import argparse
import copy
import importlib.util
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

COURSE = Path(__file__).resolve().parents[1]
TARGETS = {
    "DE03": "01-workflow/03-debugging/exercise.py",
    "DE04": "02-data-design/01-contracts/exercise.py",
    "DE08": "03-pipelines/01-corrections-and-deletes/exercise.py",
    "DE09": "03-pipelines/02-windows-and-cursors/exercise.py",
    "DE10": "03-pipelines/03-quality-and-reconciliation/exercise.py",
    "DE12": "04-warehouse/01-layers-and-duckdb/query.sql",
    "DE16": "05-orchestration/01-dependencies/exercise.py",
    "DE22": "06-platforms/04-security-and-ai/exercise.py",
    "DE24": "07-internship/02-ml-feature-data/exercise.py",
}


def fixture():
    return json.loads((COURSE / "data/all_changes.json").read_text(encoding="utf-8"))


def load(path):
    spec = importlib.util.spec_from_file_location("learner_engineering", path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = obj
    spec.loader.exec_module(obj)
    return obj


def error(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def function(obj, name):
    fn = getattr(obj, name, None)
    assert callable(fn), f"implement {name} first; the starter contains prompts only"
    return fn


def verify(lesson, path):
    rows = fixture()
    if lesson == "DE03":
        obj = load(path)
        fn = function(obj, "build_report")
        cases = [
            ([], {}),
            ([{"customer_id": " c1 ", "amount_cents": 10},
              {"customer_id": "c1", "amount_cents": 20},
              {"customer_id": "c2", "amount_cents": 5}], {"c1": 30, "c2": 5}),
            ([{"customer_id": "z", "amount_cents": 7},
              {"customer_id": "x", "amount_cents": 0},
              {"customer_id": " z ", "amount_cents": 2},
              {"customer_id": "z", "amount_cents": 11}], {"z": 20, "x": 0}),
            ([{"customer_id": "other", "amount_cents": 1000000},
              {"customer_id": "other", "amount_cents": 1}], {"other": 1000001}),
        ]
        for data, expected in cases:
            original = copy.deepcopy(data)
            result = fn(data)
            assert type(result) is dict and result == expected, "customer aggregate mismatch"
            assert all(type(value) is int for value in result.values()), "integer totals required"
            assert data == original, "input rows changed"
            assert fn(list(reversed(data))) == expected, "row order changed the totals"
        return
    if lesson == "DE12":
        import duckdb
        sql = path.read_text(encoding="utf-8")
        executable = "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--")).strip()
        assert executable, "implement the SQL SELECT first"
        with duckdb.connect() as con:
            con.execute("CREATE TABLE raw_changes (id VARCHAR, customer_id VARCHAR, occurred_at TIMESTAMPTZ, updated_at TIMESTAMPTZ, version INTEGER, amount_cents BIGINT, op VARCHAR)")
            assert len(con.extract_statements(sql)) == 1, "one SELECT statement required"
            for data in [rows, rows + [{**rows[2], "version": 3, "amount_cents": 1700}], rows[:2]]:
                con.execute("DELETE FROM raw_changes")
                con.executemany("INSERT INTO raw_changes VALUES (?, ?, ?, ?, ?, ?, ?)", [tuple(row.values()) for row in data])
                result = con.execute(sql)
                assert [c[0] for c in result.description] == list(rows[0]), "seven output columns in contract order"
                actual = {}
                for values in result.fetchall():
                    row = dict(zip(rows[0], values))
                    for field in ["occurred_at", "updated_at"]:
                        row[field] = row[field].astimezone(timezone.utc).isoformat()
                    assert row["id"] not in actual, "duplicate latest ID"
                    actual[row["id"]] = row
                expected = {}
                for row in data:
                    if row["id"] not in expected or row["version"] > expected[row["id"]]["version"]:
                        expected[row["id"]] = row
                assert actual == expected, "latest-state query mismatch"
        return
    obj = load(path)
    if lesson == "DE04":
        fn = function(obj, "validate_change")
        for row in rows:
            original = copy.deepcopy(row)
            result = fn(row)
            assert result == {"record": row, "errors": []}, "valid canonical record"
            assert original == row and result["record"] is not row, "do not mutate/share record"
        row = {**rows[0], "id": "  A ", "extra": "ignore", "occurred_at": "2026-09-01T16:00:00+07:00"}
        assert fn(row)["record"] == rows[0], "trim IDs, normalize UTC, ignore extras"
        for field, invalid in [("id", ""), ("customer_id", None), ("occurred_at", "2026-09-01T09:00:00"), ("updated_at", "bad"), ("version", True), ("amount_cents", -1), ("op", "remove")]:
            result = fn({**rows[0], field: invalid})
            assert result == {"record": None, "errors": [field]}, f"invalid {field}"
        invalid = {**rows[0], "id": "", "version": 0, "op": "bad"}
        assert fn(invalid)["errors"] == ["id", "version", "op"], "ordered multiple errors"
        assert fn({**rows[0], "amount_cents": 1000000})["errors"] == []
        assert fn({**rows[0], "amount_cents": 1000001})["errors"] == ["amount_cents"]
        assert fn({}) == {"record": None, "errors": list(rows[0])}
    elif lesson == "DE08":
        fn = function(obj, "choose_latest")
        state = {}
        original = copy.deepcopy(rows)
        for row in rows + rows[:2]:
            winner = fn(state.get(row["id"]), row)
            assert winner is not row, "return a separate dict"
            state[row["id"]] = winner
        assert rows == original, "source changed"
        assert state == {"A": rows[2], "B": rows[3], "C": rows[4]}
        current = copy.deepcopy(rows[2])
        assert fn(current, rows[0]) == current and current == rows[2]
        error(fn, rows[2], {**rows[2], "amount_cents": 1300})
        error(fn, rows[0], rows[1])
        assert fn(rows[3], rows[1]) == rows[3], "stale upsert resurrected delete"
    elif lesson == "DE09":
        window = function(obj, "select_window")
        page = function(obj, "page_after")
        original = copy.deepcopy(rows)
        first = window(rows, "2026-09-01T00:00:00+00:00", "2026-09-02T00:00:00+00:00")
        assert first == rows[:2], "half-open update-time window"
        tied = rows[2:]
        gathered, cursor = [], None
        for _ in range(4):
            batch = page(tied, cursor, 1)
            if not batch:
                break
            gathered.extend(batch)
            cursor = (batch[-1]["updated_at"], batch[-1]["id"])
        assert gathered == tied, "tied paging skipped or repeated rows"
        assert page(rows, ("2026-09-02T17:00:00+07:00", "A"), 10) == rows[3:]
        assert window(rows, "2026-09-02T10:00:00+00:00", "2026-09-02T10:00:01+00:00") == rows[2:]
        error(window, rows, "2026-09-01T00:00:00", "2026-09-02T00:00:00+00:00")
        error(window, rows, rows[0]["updated_at"], rows[0]["updated_at"])
        for value in [0, -1, True]:
            error(page, rows, None, value)
        assert rows == original
    elif lesson == "DE10":
        fn = function(obj, "quality_report")
        now = "2026-09-03T10:00:00+00:00"
        records = [rows[2], rows[2], rows[2], {**rows[4], "amount_cents": -1, "updated_at": "2026-09-03T11:00:00+00:00"}]
        original = copy.deepcopy(records)
        expected = {"duplicate_ids": 2, "negative_amounts": 1, "stale_rows": 0, "future_rows": 1}
        assert fn(records, now, 24) == expected, "counts and strict threshold"
        assert fn(records, now, 23)["stale_rows"] == 3
        assert fn([], now, 24) == dict.fromkeys(expected, 0)
        for threshold in [-1, True, float("inf"), float("nan")]:
            error(fn, records, now, threshold)
        error(fn, records, "2026-09-03T10:00:00", 24)
        assert records == original
    elif lesson == "DE16":
        fn = function(obj, "topo_order")
        graph = {"b": ["a"], "a": [], "c": []}
        assert fn(graph) == ["a", "b", "c"]
        assert graph == {"b": ["a"], "a": [], "c": []}
        assert fn({}) == []
        assert fn({"publish": ["load"], "load": ["validate"], "validate": ["extract"], "extract": []}) == ["extract", "validate", "load", "publish"]
        error(fn, {"a": ["missing"]})
        error(fn, {"a": ["b"], "b": ["a"]})
    elif lesson == "DE22":
        fn = function(obj, "validate_enrichment")
        payload = {"id": "A", "label": "priority"}
        result = fn(payload, {"A"})
        assert result == payload and result is not payload
        for value in [None, [], {}, {**payload, "id": " A "}, {**payload, "id": 1}, {**payload, "id": "Z"}, {**payload, "label": "urgent"}, {**payload, "label": []}, {**payload, "label": {}}, {**payload, "label": None}, {**payload, "sql": "SELECT 1"}]:
            error(fn, value, {"A"})
        assert payload == {"id": "A", "label": "priority"}
    elif lesson == "DE24":
        fn = function(obj, "build_features")
        original = copy.deepcopy(rows)
        assert fn(rows, "2026-09-02T00:00:00+00:00") == {"c1": {"order_count": 1, "total_cents": 1000}, "c2": {"order_count": 1, "total_cents": 1500}}
        assert fn(rows, "2026-09-03T00:00:00+00:00") == {"c1": {"order_count": 2, "total_cents": 2000}}
        assert fn(rows, "2026-09-02T10:00:00+00:00") == fn(rows[:2], "2026-09-02T10:00:00+00:00")
        assert fn([], "2026-09-03T00:00:00+00:00") == {}
        error(fn, rows, "2026-09-03T00:00:00")
        assert rows == original


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("lesson", choices=TARGETS)
    parser.add_argument("--file", type=Path, help="optional alternate implementation for your own regression lab")
    args = parser.parse_args()
    path = args.file or COURSE / TARGETS[args.lesson]
    try:
        verify(args.lesson, path.resolve())
    except Exception as exc:
        print(f"FAIL: {args.lesson}: {type(exc).__name__}: {exc}")
        return 1
    print(f"PASS: {args.lesson} fixture contract. Add changed-input evidence; explain the behavior.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

