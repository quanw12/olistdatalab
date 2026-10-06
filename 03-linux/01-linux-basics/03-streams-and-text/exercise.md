# LE03 assignment

1. Read data/runs.log. Find only lines containing level=ERROR and write them to $LE_LAB_ROOT/errors.txt.
2. Count all six log lines and the two error lines.
3. Extract the level tokens from this deliberately simple space-delimited fixture, sort them and count each distinct level.
4. Append a disposable note to a lab file and explain how >> differs from >.
5. Redirect the stderr of ls on a nonexistent lab path to a separate error file, recording the status.
6. Explain why cut -d, cannot reliably parse the CSV fixture in the Python course.

## Deliverables

notes.md with commands, exact level counts and stdout/stderr observations. Generated text stays in the ignored lab area.

## Reflection

Why should diagnostic text usually go to stderr when stdout contains JSON?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
