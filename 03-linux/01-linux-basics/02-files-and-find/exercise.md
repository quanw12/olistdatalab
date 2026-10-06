# LE02 assignment

1. Create $LE_LAB_ROOT/files-practice/raw and processed.
2. Copy the provided events.csv into raw/input batch.csv; preserve the shared source file.
3. Copy that lab input to processed/events-copy.csv, then rename only the copy to archived.csv.
4. Use find with a quoted '*.csv' pattern and record both matching paths.
5. Compare the lab source with the original using cmp. Inspect its header and final two lines.
6. Create and remove one disposable file with rm -- and its exact quoted path. Do not recursively delete the lab or repository.

## Deliverables

notes.md with paths and commands, a brief explanation of quoting and a count of the two remaining CSV files.

## Reflection

Why is find "$LE_LAB_ROOT" -name '*.csv' different from leaving *.csv unquoted?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
