# CL03 — Assignment

Implement validate_job_config(config) returning a new dictionary with exactly tasks, max_retries, timeout_seconds, memory_mib. Reject extra/missing keys, wrong types or invalid values with ValueError. All values are exact ints: tasks=1; max_retries 0–2; timeout_seconds 1–300; memory_mib one of 512,1024,2048. These are course limits, not the platform's universal limits.

Write worker.py and Dockerfile: bounded synthetic batch work, explicit configuration, structured start/success/failure logs and nonzero failure. Log batch ID and stage, never credentials. Locally build/run before deployment; follow live-lab.md. A minimal first worker may validate a batch and exit; CL08 integrates its actual data operations.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
