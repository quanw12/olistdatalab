# C10-L02 — CSV, JSON, JSON Lines, and schema boundaries
# Implement your own solution below the problem statements.
#
# Implement read_orders_csv(path) -> list[dict].
# Require exactly these four distinct header names, in any order: order_id, city, amount, updated_at. Bad headers or rows with missing/extra columns raise ValueError.
# Open UTF-8 with newline="". Preserve all cell values as strings; do not validate business values yet.
# Implement write_jsonl(path, rows) -> None: write one JSON object per line in UTF-8, overwriting previous contents. Empty rows produce an empty file.
# Input files and parent output directory exist for this lesson.
#
# Read expected.md for concrete cases and help.md for graded hints.
