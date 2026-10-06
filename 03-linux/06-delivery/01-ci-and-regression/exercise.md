# LE21 assignment

Complete project/workflow.yml as a DRAFT. Use ubuntu-24.04, Python 3.12, checkout@v6, setup-python@v5 and contents: read. Include workflow_dispatch and push/pull_request path filters for 03-linux/** and .github/workflows/linux-engineering.yml. Run the supplied unittest suite plus your own test_extra.py through -p 'test*.py'; run all four check_scripts modes in a Bash loop, failing on any nonzero result. Add bash -n on the final runner. Add one meaningful unittest in project/test_extra.py for a changed input or missing-file/duplicate conflict outcome. Prove your additional test fails with a relevant mutation in an isolated copy, then restore the copy. Optional activation: only after local checks pass, copy the finished draft to the root .github/workflows/linux-engineering.yml and deliberately commit/push it on a feature branch.

## Deliverables

workflow.yml draft, test_extra.py, notes.md with one genuine failing test followed by a repaired pass. A live Actions result is separate optional evidence.

## Reflection

Why is a test more useful when you can show which wrong behavior it rejects?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
