"""Provided reproduction: intentionally incorrect grouping. Preserve this file."""
import json
from pathlib import Path

def build_report(rows):
    """Two logic defects are intentional; inspect them before writing the repair."""
    totals = {}
    for row in rows:
        customer_id = row["customer_id"]
        totals[customer_id] = row["amount_cents"]
    return totals

if __name__ == "__main__":
    rows = json.loads(Path(__file__).with_name("data.json").read_text(encoding="utf-8"))
    print(build_report(rows))
