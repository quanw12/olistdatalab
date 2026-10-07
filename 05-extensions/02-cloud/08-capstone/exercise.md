# CL08 — Assignment

Complete worker.py from CL03 and the pipeline CLI here. Process b1 then b2 from data/batches.json: create-only raw upload, deterministic warehouse load request, checked latest-state/MERGE, active report and immutable per-batch publication evidence. Preserve delete markers in current. Use runtime permissions from CL05 and bounds from CL03/CL07.

Run an identical replay and an altered-content replay; the latter must fail before corrupting history/current/report. Inject failure after warehouse work but before report publication, then recover. Demonstrate a failed job and real logs. Test Scheduler once, then pause it. Provide a README, diagram, data contract, tests, sanitized evidence, recovery and cleanup runbook.

If you choose local-only mode, implement the equivalent local pipeline and label the result local; cloud deployment evidence remains incomplete. Follow [live-lab.md](../live-lab.md) for owned resource setup and the exact service sequence.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
