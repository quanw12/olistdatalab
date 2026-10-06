# DE08 assignment

Implement choose_latest(current, incoming) in exercise.py. Inputs are canonical DE04 records; current may be None. Different IDs raise ValueError. Higher version wins, lower loses, equal version with identical seven-field content is replay, equal version with any conflicting canonical field raises ValueError. Return a shallow copy of the winner, never mutate either input. Keep deletes. Fold b1 then b2 then stale replay to current state; document the single-source version assumption.

## Deliverables

exercise.py, notes.md, and your own delete-then-stale test.

## Reflection

Why keep B in state after its deletion?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

