# LE20 assignment

Implement project/compose.yaml: batch builds '.', mounts ../data:/data:ro and artifacts:/output, command is --input /data/events.csv --output /output. web uses python:3.12-slim, mounts artifacts:/output:ro, runs python -m http.server 8000 --bind 0.0.0.0 --directory /output, publishes 127.0.0.1:8765:8000, and depends on batch service_completed_successfully. Declare named volume artifacts. No version field, credentials, database, restart policy or privileged mode is required. Validate config; bring up; retrieve manifest; rerun batch once; stop with down; start again and explain the retained volume. Do not use down -v.

## Deliverables

compose.yaml and notes.md with successful batch exit, report response, rerun and retained data evidence.

## Reflection

Does depends_on guarantee that web always sees a coherent new set of files during reruns?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
