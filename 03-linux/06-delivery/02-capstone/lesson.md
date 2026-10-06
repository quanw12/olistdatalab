# Capstone: deliver and recover a Linux batch pipeline

## Concept and purpose

This capstone packages the skills into an operator-ready deliverable. The supplied data-processing app is the stable component; your work is execution, configuration, testing, inspection and recovery.

Define evidence for native Linux, container execution and service delivery separately. A manifest on disk may be old; combine exit status, logs and current response values. Distinguish a one-shot batch lifecycle from a long-running report viewer.

Use a runbook and a fresh-session rehearsal. Demonstrate correct replay, a visible input failure and recovery. The app rewrites deterministic aggregates from the full fixture; it is not an incremental database loader. Artifacts are individually atomic but not published as one concurrent snapshot. Document these limits rather than claiming production guarantees.

## Syntax example — Bash in Ubuntu

~~~bash
python3 "$LE_COURSE_ROOT/checks/check_report.py" --url http://127.0.0.1:8765
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" ps --all
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" logs batch
~~~

## Trace the example

The report checker verifies the locally served fixed-fixture results. Compose status/logs supply actual container evidence beyond an HTTP response.

## Apply it to Data Engineering

A portfolio should let someone else reproduce normal operation and recover a deliberate failure.

[Reference](https://docs.docker.com/compose/). These explanations and exercises are original course material.
