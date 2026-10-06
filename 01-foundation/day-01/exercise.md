# Day 01 assignment

Read weather.csv using csv.DictReader. Implement clean_row(row), a loop over input rows, and a main entry point. Trim city; require a real date written exactly YYYY-MM-DD; convert finite temperature in [-50,60] and integer humidity in [0,100]. Reject malformed rows with one clear reason. Deduplicate only valid rows by (city, observed_at), keeping the first. Write the four columns to output/clean.csv and print accepted/rejected totals and counts by reason. Create the output directory yourself. Use standard-library Python only.

## Deliverables

- Your implementation in `clean.py`.
- Output/report checked against [expected.md](expected.md).
- `reflection.md`: explain one decision, one bug you fixed, and one remaining question.

Do not overwrite supplied fixtures to make a failing check pass. [help.md](help.md) explains the implementation in smaller steps.

Function contract: clean_row(row) returns (clean_dictionary, None) on success or (None, reason_string) on rejection. main handles counts, duplicate keys and file output.
