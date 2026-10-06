# DE11 assignment

Extend your DE06 loader with a run ledger and structured stderr/stdout events. State diagram must include received, data_committed, published and failed with enough detail to recover a publish error after commit. Inject missing input, invalid contract, database rollback and output-path-file collision. Repair each cause and rerun. Record the previous/new run IDs and which data/progress/artifacts changed. Write a runbook another person can follow.

## Deliverables

runbook.md, state-diagram.md, logging changes in your loader and sanitized evidence in notes.md.

## Reflection

Why must a successful last-run file not be reused as proof of a new run?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

