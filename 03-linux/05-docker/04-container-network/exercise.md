# LE19 assignment

1. Create/reuse le-network. Start only le-web with python:3.12-slim, network le-network, le-storage mounted read-only at /output, host binding 127.0.0.1:8765:8000, and python -m http.server 8000 --bind 0.0.0.0 --directory /output.
2. Fetch /manifest.json from Ubuntu using the published endpoint and confirm counts.
3. From a disposable Python container on le-network, fetch http://le-web:8000/manifest.json using urllib.request.
4. Explain why http://localhost:8765 from that second container points to the wrong place.
5. Stop/remove only le-web after recording evidence; retain le-storage.

## Deliverables

notes.md with the two addresses, actual responses and scoped cleanup commands.

## Reflection

Why does a sibling container use le-web:8000 rather than localhost:8765?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
