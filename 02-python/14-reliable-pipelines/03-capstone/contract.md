# Capstone contract and rehearsal

## Inputs

Shared fixtures: [base](../../data/orders.csv), [next batch](../../data/orders_next.csv), [data definitions](../../data/README.md).

Exactly four distinct CSV headers: order_id, city, amount, updated_at, in any order. Missing/extra cells or invalid headers fail the whole run with ValueError before loading. All CSV values remain raw strings until cleaning.

Validate each row in this priority:
1. Strip order_id; blank -> reason id.
2. Collapse city whitespace and title-case; blank -> city.
3. Parse amount exactly as C10-L04: finite, nonnegative, at most 1000000 units, no fractional cent -> amount on failure.
4. Parse aware datetime and serialize UTC with fixed microseconds -> time on failure.

Accepted shape: order_id, city, amount_cents (int), updated_at (canonical UTC string).
Rejected shape: {"row_number": CSV record number including the header as record 1, "reason": one label, "raw": original dictionary}. The first data record is 2. Count parsed records, not physical newline characters inside quoted fields.
Each row has one outcome. accepted_rows includes exact duplicate source rows; stored_rows counts distinct latest orders.

## SQLite

Use db_path exactly as provided. Its parent exists.
Create if absent:
- orders: order_id TEXT PRIMARY KEY, city TEXT NOT NULL, amount_cents INTEGER NOT NULL CHECK(amount_cents >= 0), updated_at TEXT NOT NULL.
- batches: batch_id TEXT PRIMARY KEY. Additional count columns are optional.

batch_id is the SHA-256 of original CSV bytes. Apply the latest-version rule from C14-L01. Equal-version conflicting contents fail the entire batch. Insert the successful batch ID in the SAME transaction as its data.
A recognized batch does not change state. This includes replaying the original file after a correction file.

Only use this exercise's dedicated database path. Do not point it at another project's database.

## Files and return value

Under output_dir:
- rejected.jsonl: rejected rows for this input in source order; empty file when none.
- report.json: list of {"city": name, "total_cents": integer}, sorted by city, based on CURRENT stored state.
- manifest.json: same dictionary returned by run_pipeline.

Exactly these integer manifest fields:
input_rows, accepted_rows, rejected_rows, stored_rows, total_cents.

For no stored orders, total_cents is 0 and report is [].
Validate input before writing outputs. Commit the database, then publish each file through temporary-sibling replacement. Publish manifest last. A filesystem failure propagates as an OSError; a rerun must reconstruct outputs without duplicating data. This is a recoverable single-writer lab, not an atomic snapshot across all files.

## Demonstration commands

After implementing the argparse main guard:
~~~powershell
Set-Location "C:\DE Courses\02-python\14-reliable-pipelines\03-capstone"
New-Item -ItemType Directory -Force .\output
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\exercise.py --input ..\..\data\orders.csv --database .\output\state.sqlite --output .\output\published
~~~
The directory-creation command prepares the database parent. Then rerun with orders_next.csv and finally orders.csv again.

## Rehearsal

- [ ] Base counts reconcile: 8 = 4 accepted + 4 rejected; state 3, cents 3050.
- [ ] Base replay leaves state unchanged.
- [ ] Correction batch gives state 4, cents 3850.
- [ ] Old base replay does not undo corrections.
- [ ] A conflicting equal version fails without partial state or batch ledger progress.
- [ ] A failed output publication can be repaired by rerunning.
- [ ] Empty input works.
- [ ] CLI and README allow a fresh setup without Codex.
- [ ] Explain where memory grows, why this is single-writer, and what a production design would add.

Write a short portfolio.md in this folder: problem, row grain, data flow, run commands, evidence, recovery steps and limitations. Include a five-minute demo script. This is your written deliverable, not a supplied completed solution.
