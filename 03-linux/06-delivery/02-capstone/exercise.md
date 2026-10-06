# LE22 assignment

1. Finish project/runbook.md and portfolio.md with architecture, shell contexts, prerequisites, exact native/container/Compose commands, tests and limitations.
2. From a new Ubuntu terminal, set the documented variables and run the native wrapper successfully. Compare artifacts with the fixture contract.
3. Start the Compose stack, verify report/manifest through check_report.py, and record the batch's exit status.
4. Rerun the batch; total remains 3050. Stop/remove the stack with down, start it again, and explain retained storage.
5. With web running, invoke a one-shot batch with /data/missing.csv; it must fail visibly and leave the previous valid report unchanged. Do not present that old report as proof of the failed invocation's success.
6. Restore the valid input invocation, rerun, and verify current logs/status/data.
7. Run app tests plus Bash checks and perform a five-minute demo. A reviewer should be able to follow the runbook without Codex.

## Deliverables

project/runbook.md, this lesson's portfolio.md, sanitized evidence/ and reflection.md. Keep actual usernames/versions when useful but exclude tokens, private logs and .env. Use contract.md for detailed acceptance.

## Reflection

What evidence proves recovery when old successful artifacts can survive a new failed run?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
