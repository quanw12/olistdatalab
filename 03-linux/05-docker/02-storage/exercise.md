# LE17 assignment

1. Create/reuse the named lab volume le-storage and demonstrate one container writing a note and another reading it.
2. Mount $LE_COURSE_ROOT/data at /data read-only and display events.csv from a disposable Python container.
3. Attempt to write a NEW disposable file inside that read-only mount; expect failure. The shared fixture must remain unchanged.
4. Compare the bind source with the Docker volume's identity using inspect. Explain why the volume is not automatically a Windows file beside your source.
5. Retain le-storage until finishing the course; record its purpose.

## Deliverables

notes.md with mount commands, persistence/read-only evidence and ownership explanation.

## Reflection

Why does --rm not remove a separately named volume?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
