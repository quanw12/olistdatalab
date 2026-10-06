# DE24 assignment

Implement build_features(changes,cutoff). Inputs are canonical source history with consistent equal versions; cutoff aware ISO string. Retain revisions with updated_at strictly before cutoff, choose highest version per id, then retain upserts with occurred_at strictly before cutoff. Return a customer_id-keyed dict of {'order_count': int,'total_cents': int}; omit empty customers. Do not mutate input. Raise ValueError on a naive timestamp. Write split-plan.md with train/validation/test time boundaries and future labels kept separate.

## Deliverables

exercise.py, split-plan.md and one late-availability test.

## Reflection

Why is old occurred_at insufficient to prove a correction was known earlier?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

