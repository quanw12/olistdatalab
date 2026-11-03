---
tags: [decourse, template, incident]
status: template
---

# Incident Report

Blameless: describe systems and decisions, not people.

## Impact

Which dataset/metric/interval was wrong or missing, and how were users affected? If unknown, say so — do not guess numbers.

## Timeline

| Time and timezone | Event | Evidence |
|---|---|---|
| fill in | Detected | Log/query |
| fill in | Impact contained | Action |
| fill in | Recovered | Reconciliation query |

## Cause

Trigger, the wrong design assumption, and why tests/alerts did not catch it. Separate cause from symptom.

## Recovery

Input version, commands, backfill range, checkpoint, time to recover. Was data lost, and how do you know?

## Verification and actions

- [ ] Keys/counts/money/partitions match the reference.
- [ ] A test fails before the fix and passes after it.
- [ ] Each action has an owner, a deadline and a completion criterion.
