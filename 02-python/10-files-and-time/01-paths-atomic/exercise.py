# C10-L01 — Paths, context managers, and safe file replacement
# Implement your own solution below the problem statements.
#
# Implement write_atomic_json(path, value) -> None.
# Accept a Path or string destination. Serialize using json.dumps(..., ensure_ascii=False, allow_nan=False) BEFORE touching the destination.
# Create missing parents. Write UTF-8 to a unique temporary sibling, close it, then replace the destination.
# Clean up your temporary file if an error occurs.
# Serialization failure must leave an existing destination byte-for-byte unchanged.
# This contract concerns one file; do not claim multi-file transactional guarantees.
#
# Read expected.md for concrete cases and help.md for graded hints.
