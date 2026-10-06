# LE09 assignment

Implement project/run_batch.sh. Exactly two arguments: input CSV and output directory; wrong arity ->64. Locate sibling app.py from the runner path. Use ${LE_PYTHON:-python3} as executable; missing executable ->127. Create the output directory, failing visibly on error. Invoke the app with quoted paths. Overwrite output/run.log with stdout and output/error.log with stderr. Exit with the app's exact status. Work from any cwd and with space-containing paths.

## Deliverables

project/run_batch.sh and lesson notes.md with success/failure evidence.

## Reflection

Why is using pwd to locate app.py unreliable?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
