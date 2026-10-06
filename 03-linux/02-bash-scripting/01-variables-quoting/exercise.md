# LE05 assignment

Implement exercise.sh: require exactly one argument. On valid arity print exactly batch=<argument> and newline, status 0. Wrong arity -> stderr usage, empty stdout, exit 64. A single empty argument is valid. Preserve wildcard/dollar/percent characters literally; never execute input.

## Deliverables

exercise.sh and notes.md explaining "$1" versus "$@".

## Reflection

Why use printf 'batch=%s\n' "$1" rather than printf "$1"?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
