# CL05 — Assignment

Implement role_plan(actions). actions is a list containing only read_raw, write_output or load_warehouse strings; duplicate actions are allowed. Return a sorted, deduplicated list of {"resource":...,"role":...} dictionaries, sorted by resource then role.

Course mappings: read_raw → raw_bucket/roles/storage.objectViewer. write_output → output_bucket/roles/storage.objectCreator AND output_bucket/roles/storage.objectViewer (create output and verify replay). load_warehouse → project/roles/bigquery.jobUser AND dataset/roles/bigquery.dataEditor. Reject wrong types or unknown actions with ValueError. Empty list returns []. Do not modify the input.

In plan.md attach each symbolic scope to an actual owned resource and identity. Live: demonstrate raw read allowed and raw overwrite denied for the runtime; no project Owner shortcut.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
