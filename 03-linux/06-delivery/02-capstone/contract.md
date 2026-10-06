# Capstone acceptance contract

## Stable application interface

The supplied [app](../../project/app.py) is provided infrastructure; do not replace its deterministic contract to make engineering checks pass.

- Python >=3.10; standard library.
- app.py --input <CSV> --output <directory>.
- Input columns: event_id, amount_cents. Values stay raw until validation.
- Valid ID: nonblank after trimming. Amount: 1–7 ASCII decimal digits, value <=1000000; leading zeros are allowed within that length.
- Equal repeated ID/amount is an accepted replay; conflicting repeated amounts fail the whole run.
- Bad ID or amount is quarantined with record number/reason/raw fields.
- Fixture: 6 input, 4 accepted, 2 rejected, 3 distinct events, total 3050 cents.
- Complete artifacts: manifest.json (five fields), report.json (event_count/total_cents), rejected.jsonl.
- stdout: JSON run_complete event with manifest; failure: JSON run_failed event on stderr and exit 2.
- Validate/aggregate before publication. Each artifact is replaced atomically, manifest last. There is no atomic transaction across all three files.
- Full-input replay overwrites aggregates; no database, watermark, live source or scheduler is involved.

## Your engineering interfaces

- run_batch.sh: LE09 argument, path, interpreter, log and status contract.
- Dockerfile: LE18 build context and executable interface.
- compose.yaml: LE20 batch/web/artifacts contract.
- workflow.yml: LE21 draft; activation and live results are optional separate evidence.

## Required evidence

- [ ] Native Ubuntu app and wrapper success.
- [ ] Bash contract checks and meaningful app tests.
- [ ] Actual image build and digest/ID recorded.
- [ ] Compose batch completed with exit 0 and report checker passed.
- [ ] Host/container addressing explained.
- [ ] Input bind is read-only and output volume survives ordinary down/up.
- [ ] Rerun does not inflate the total.
- [ ] Missing input fails visibly while old valid output is preserved.
- [ ] Corrected invocation succeeds with current status/log/data evidence.
- [ ] Runbook works from a fresh terminal.
- [ ] Five-minute demo and known limits recorded.

## Report validation

In Ubuntu, while the viewer is running:
~~~bash
python3 "$LE_COURSE_ROOT/checks/check_report.py" --url http://127.0.0.1:8765
~~~

This proves the supplied HTTP fixture response, not every Docker setting or all possible input behavior. Record runtime container evidence separately.

## Limits to explain

Single writer; individually atomic artifacts, not a coherent concurrent-reader snapshot; full-file aggregation held in memory; local-only teaching HTTP server; image tags can move; draft CI is not live CI; this is an engineering lab rather than production hosting.
