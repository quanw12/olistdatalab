# LE06 assignment

1. Install python3-venv in Ubuntu if needed; setup.md gives commands.
2. Create $LE_LAB_ROOT/venv and export LE_PYTHON="$LE_LAB_ROOT/venv/bin/python".
3. Run supplied project/app.py --help.
4. Run it with data/events.csv and output $LE_LAB_ROOT/python-run.
5. Run "$LE_PYTHON" -m unittest discover -s "$LE_COURSE_ROOT/project" -p 'test_app.py' -v.
6. Inspect artifacts and compare data/README.md. Do not change supplied code just to alter counts.

## Deliverables

notes.md: interpreter path/version, exact invocation, counts, tests.

## Reflection

Why use an explicit interpreter path in a scheduled job?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
