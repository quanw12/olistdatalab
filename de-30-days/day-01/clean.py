# Day 01: Python and CSV cleaning
# Read lesson.md, then exercise.md. Detailed guidance: help.md.
# Read weather.csv using csv.DictReader. Implement clean_row(row), a loop over input rows, and a
# main entry point. Trim city; require a real date written exactly YYYY-MM-DD; convert finite
# temperature in [-50,60] and integer humidity in [0,100]. Reject malformed rows with one clear
# reason. Deduplicate only valid rows by (city, observed_at), keeping the first. Write the four
# columns to output/clean.csv and print accepted/rejected totals and counts by reason. Create
# the output directory yourself. Use standard-library Python only.
# Write your own implementation below. No solution is supplied here.
