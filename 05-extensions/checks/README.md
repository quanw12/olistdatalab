# Offline checks

check.py is supplied grading infrastructure. It imports one student function module or runs one student SQL statement against an isolated in-memory database. It never opens earlier lesson databases. It provides no finished solution. Keep the fixture and checker unchanged; write your own regressions alongside your implementation.

Run from the course root: python checks/check.py LAB01 (using the interpreter from setup). A fresh starter should FAIL. PASS proves that contract's supplied cases, not arbitrary correctness, a deployed cloud job, broker delivery, model quality or completion of a capstone. There are 25 offline contracts; seven concept/integration lessons have manual evidence checklists instead. See [verification](../verification.md) for author validation and limits.

Do not use python -O for checks: this checker deliberately uses assertions. The optional --file path checks an alternate implementation with the same contract. It is intended for a scratch revision; it does not relax acceptance rules. Fixtures are synthetic; databases are recreated in memory on each run.
