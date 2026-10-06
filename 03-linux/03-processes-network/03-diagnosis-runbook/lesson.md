# Logs, resource checks and a useful runbook

## Concept and purpose

Diagnose from evidence: exact command, timestamp/run identity, exit status, inputs, interpreter, permissions, logs and resource state. A symptom is not automatically its cause.

head/tail inspect bounded log output. df -h shows filesystem capacity, du -sh shows directory usage and free -h shows memory. These observe different resources. Logs must include actionable context without secrets. A runbook specifies a symptom, read-only checks, likely causes, a scoped repair and a verification step.

Do not paper over a missing source with an empty file or blindly retry validation failures. Reproduce a single failure and make one change. Keep generated output separate from versioned documentation.

## Syntax example — Bash in Ubuntu

~~~bash
df -h "$LE_LAB_ROOT"
du -sh "$LE_LAB_ROOT"
free -h
tail -n 10 "$LE_LAB_ROOT/python-run/manifest.json"
~~~

## Trace the example

Capacity and memory readings are machine-dependent. The manifest has deterministic fixture totals. None of these commands repairs a failed job.

## Apply it to Data Engineering

An internship deliverable should tell the next operator how to distinguish and recover common failures.

[Reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). These explanations and exercises are original course material.
