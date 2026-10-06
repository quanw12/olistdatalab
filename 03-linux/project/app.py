"""Provided standard-library fixture app for engineering practice."""
import argparse
import csv
import json
import tempfile
from pathlib import Path


def atomic_text(path, content):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def run(input_path, output_dir):
    with Path(input_path).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        fields = reader.fieldnames
        if fields is None or len(fields) != 2 or set(fields) != {"event_id", "amount_cents"}:
            raise ValueError("expected event_id,amount_cents headers")
        rows = list(reader)
    events, rejected = {}, []
    accepted = 0
    for number, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"invalid CSV record shape at {number}")
        event_id = row["event_id"].strip()
        text = row["amount_cents"]
        reason = None
        if not event_id:
            reason = "id"
        elif not text or not text.isascii() or not text.isdecimal() or len(text) > 7 or int(text) > 1000000:
            reason = "amount"
        if reason is not None:
            rejected.append({"record_number": number, "reason": reason, "raw": row})
            continue
        value = int(text)
        if event_id in events and events[event_id] != value:
            raise ValueError(f"conflicting event: {event_id}")
        events[event_id] = value
        accepted += 1
    manifest = {"input_rows": len(rows), "accepted_rows": accepted, "rejected_rows": len(rejected),
                "event_count": len(events), "total_cents": sum(events.values())}
    report = {"event_count": len(events), "total_cents": sum(events.values())}
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    atomic_text(output / "rejected.jsonl", "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rejected))
    atomic_text(output / "report.json", json.dumps(report, indent=2) + "\n")
    atomic_text(output / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        manifest = run(args.input, args.output)
    except (OSError, ValueError, csv.Error, UnicodeError) as exc:
        print(json.dumps({"event": "run_failed", "message": str(exc)}), file=__import__("sys").stderr)
        return 2
    print(json.dumps({"event": "run_complete", "manifest": manifest}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
