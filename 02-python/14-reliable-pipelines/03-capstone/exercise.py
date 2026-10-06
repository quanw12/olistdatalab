# C14-L03 — Capstone: reproducible retail ingestion
# Implement your own solution below these problem statements.
#
# Implement run_pipeline(csv_path, db_path, output_dir) -> manifest dict. See contract.md for the full contract.
# Use the shared raw data files, strict header validation, city normalization, Decimal-to-cents conversion and aware UTC timestamps.
# Quarantine invalid rows; apply newest-version rules and detect equal-version conflicts.
# Persist orders and a successful-batch ledger in SQLite in one transaction.
# Write rejected.jsonl, report.json and manifest.json under output_dir.
# All artifact writes are individually atomic, with manifest last. Rerun must rebuild artifacts even if the batch already succeeded.
# Do not mutate input files. Use only the standard library. No network, scheduler, Docker or AI service is needed.
# Provide a main-guard CLI using argparse with --input, --database and --output, calling run_pipeline and printing its result.
# Complete the rehearsal checklist in contract.md after the checker passes.
# See help.md for hints and expected.md for cases.
