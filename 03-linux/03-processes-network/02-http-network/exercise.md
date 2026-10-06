# LE11 assignment

Use two Ubuntu terminals. In A, run python3 -m http.server 8765 --bind 127.0.0.1 --directory "$LE_COURSE_ROOT/data". In B, run bounded curl for /events.csv, then -i for /missing.csv, then -f for /missing.csv. Record HTTP statuses and shell statuses. Inspect ss -ltn. Stop A with Ctrl+C; retry curl and classify the new error. If 8765 is busy, identify the listener and choose another lab port rather than stopping an unrelated service.

## Deliverables

notes.md comparing successful HTTP, 404 and no listener; include the exact timeout options.

## Reflection

Why will retrying a stable 404 usually not repair the request?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
