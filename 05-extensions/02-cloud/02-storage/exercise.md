# CL02 — Assignment

Implement object_key(batch_id, filename) returning raw/{batch_id}/{filename}.

batch_id must match ASCII [A-Za-z0-9_-]{1,64}. filename must match ASCII [A-Za-z0-9_-]+ followed by exactly one allowed suffix .jsonl, .json or .csv. Case-sensitive suffixes; no spaces, slashes, periods in the stem or directory traversal. Reject bad types/names with ValueError. Do not trim invalid input silently.

Then implement your own upload.py CLI: read one local synthetic input, build its key, upload with the create-only precondition and print only object identity/generation/digest. Use Application Default Credentials; no hard-coded service-account key.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
