"""Supplied behavioral checks; not a source-profiler implementation."""
import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

FIELDS = ["item_id", "site_id", "observed_at", "units", "version", "contact_email"]
HERE = Path(__file__).resolve().parent


def run_checks(candidate_path):
    candidate_path = Path(candidate_path).resolve()
    spec = importlib.util.spec_from_file_location("_de27_candidate", candidate_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    profile = module.profile_source
    checks = 0

    def require(condition, label):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    def invalid(path):
        try:
            profile(path)
        except ValueError:
            return
        raise AssertionError("Malformed file schema must raise ValueError")

    def make_csv(path, rows, fields=FIELDS):
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(fields)
            writer.writerows(rows)

    source = HERE / "fixtures/source.csv"
    original = source.read_bytes()
    sample = profile(source)
    require(sample["row_count"] == 9, "Do not drop defective or duplicate rows")
    require(sample["parse_failures"] == {"observed_at": 2, "units": 3, "version": 1},
            "Count parse failures independently")
    require(sample["candidate_keys"] == [
        {"columns": ["item_id"], "duplicate_excess": 2},
        {"columns": ["item_id", "site_id", "version"], "duplicate_excess": 1},
    ], "Candidate keys have different duplicate counts")
    blanks = [0, 1, 0, 1, 1, 2]
    distinct = [7, 3, 7, 7, 2, 3]
    require(sample["column_stats"] == {
        field: {"blank_count": blank, "distinct_nonblank_count": unique}
        for field, blank, unique in zip(FIELDS, blanks, distinct)
    }, "Measure stripped raw cells")
    require(source.read_bytes() == original, "The supplied source must remain unchanged")

    with tempfile.TemporaryDirectory(prefix="de27 checks ") as folder:
        scratch = Path(folder)
        empty = scratch / "empty.csv"
        make_csv(empty, [])
        report = profile(str(empty))
        require(report["row_count"] == 0, "Header-only file is valid")
        require(report["column_stats"] == {
            field: {"blank_count": 0, "distinct_nonblank_count": 0} for field in FIELDS
        }, "Empty input retains every column")
        require(report["parse_failures"] == {"observed_at": 0, "units": 0, "version": 0},
                "Empty input has no parse failures")
        require(all(entry["duplicate_excess"] == 0 for entry in report["candidate_keys"]),
                "Empty input has no duplicate rows")

        changed = scratch / "changed.csv"
        make_csv(changed, [
            ["X", "T", "2026-10-01T01:00:00Z", "7", "1", "one@example.test"],
            ["X", "T", "2026-10-01T01:00:00Z", "8", "1", "two@example.test"],
        ])
        report = profile(changed)
        require(report["row_count"] == 2, "A profile must not select a latest row")
        require([e["duplicate_excess"] for e in report["candidate_keys"]] == [1, 1],
                "Conflicting key content still counts as repeated candidate identity")
        require(report["column_stats"]["units"]["distinct_nonblank_count"] == 2,
                "Retain conflicting raw values")
        require(report["parse_failures"] == {"observed_at": 0, "units": 0, "version": 0},
                "Changed valid input must not reuse sample failures")

        triple = scratch / "triple.csv"
        make_csv(triple, [
            ["X", "T", "2026-10-01T01:00:00Z", "7", "1", ""],
            ["X", "T", "2026-10-01T01:00:00Z", "8", "1", ""],
            ["X", "T", "2026-10-01T01:00:00Z", "9", "1", ""],
        ])
        report = profile(triple)
        require([e["duplicate_excess"] for e in report["candidate_keys"]] == [2, 2],
                "Three occurrences have two excess rows, not one duplicate group")

        whitespace = scratch / "spaces.csv"
        make_csv(whitespace, [[" ", "  ", "", "\t", " ", "  "]])
        report = profile(whitespace)
        require(all(v == {"blank_count": 1, "distinct_nonblank_count": 0}
                    for v in report["column_stats"].values()), "Whitespace is blank")
        require(report["parse_failures"] == {"observed_at": 1, "units": 1, "version": 1},
                "One row can fail three parsers")

        unusual = scratch / "unusual.csv"
        make_csv(unusual, [
            ["Q", "T", "2026-10-01T08:00:00+07:00", "１２", "0", ""],
            ["R", "T", "2026-10-01T01:00:00Z", " 0 ", " 2 ", ""],
        ])
        report = profile(unusual)
        require(report["parse_failures"] == {"observed_at": 0, "units": 1, "version": 1},
                "ASCII rules, zero units and positive versions are separate")
        require(report["column_stats"]["observed_at"]["distinct_nonblank_count"] == 2,
                "Raw distinct time is not normalized instant count")

        for name, fields, rows in [
            ("duplicate", FIELDS + ["units"], []),
            ("reordered", list(reversed(FIELDS)), []),
            ("extra", FIELDS, [["x"] * 7]),
            ("missing", FIELDS, [["x"] * 5]),
        ]:
            path = scratch / (name + ".csv")
            make_csv(path, rows, fields)
            invalid(path)
            checks += 1
        try:
            profile(scratch / "absent.csv")
        except FileNotFoundError:
            checks += 1
        else:
            raise AssertionError("Do not hide file-system failures as bad records")

        output = scratch / "nested/result.json"
        process = subprocess.run(
            [sys.executable, str(candidate_path), "--input", str(changed), "--output", str(output)],
            cwd=scratch, capture_output=True, text=True,
        )
        require(process.returncode == 0, "CLI must succeed from a different cwd: " + process.stderr)
        require(output.exists(), "CLI must create the output parent/file")
        require(json.loads(output.read_text(encoding="utf-8")) == profile(changed),
                "CLI publishes the measured dictionary as JSON")
        process = subprocess.run(
            [sys.executable, str(candidate_path), "--input", str(scratch / "missing.csv"),
             "--output", str(scratch / "bad.json")],
            cwd=scratch, capture_output=True, text=True,
        )
        require(process.returncode != 0, "Failed CLI must not report success")
    return checks


if __name__ == "__main__":
    print(f"checks passed: {run_checks(HERE / 'profile.py')}")
