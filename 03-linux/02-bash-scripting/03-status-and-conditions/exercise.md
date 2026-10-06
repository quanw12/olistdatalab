# LE07 assignment

Implement exercise.sh accepting exactly one input path. Wrong arity -> usage on stderr, exit 64. Non-readable or non-regular file -> diagnostic on stderr, exit 66. Valid readable regular file -> stdout exactly ready and newline, status 0. Other stdout is forbidden. Do not alter the input or create a replacement; directories must fail.

## Deliverables

exercise.sh and notes.md describing each outcome.

## Reflection

How can an unconditional final printf hide a failed command?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
