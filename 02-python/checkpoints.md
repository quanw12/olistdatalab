# Independent Python checkpoints

[Course](README.md) · [Study method](../docs/study.md)

Use a blank scratch file with teaching examples/help closed. Syntax references are
allowed. Predict results, test a changed input and record hints/decisions.
These are transfer checks, not another daily course.

## Checkpoint 1 — after Chapter 3: usage receipt

Valid input: label="  backup job  ", seconds=125, price_per_started_minute=3.
Billing is per started minute, so a partial minute counts as a whole one.
Print a trimmed uppercase label, billed minutes and total cents.
Functions/conditions/exception architecture are not required yet.
Try 0, 60, 61 and 180 seconds, then change the price.

<details>
<summary>After an attempt — results</summary>

Main: BACKUP JOB, 3 minutes, 9 cents. At price 3, extra cases bill
0/1/2/3 minutes for 0/3/6/9 cents. Do not hard-code these totals.

</details>

## Checkpoint 2 — after Chapter 6: alarm state

A device starts armed. An armed reading >= 11 emits one alarm and disarms it.
A disarmed device rearms only when a reading <= 9 occurs. Other readings preserve
state. Scan [7, 12, 14, 8, 11, 10, 6]; print alarm count and final armed state.
All inputs are valid integers; no parsing exceptions/libraries are needed.
Try empty input, a long high run and each boundary. Explain why counting every
high reading would answer a different question.

<details>
<summary>After an attempt — results</summary>

Main: two alarms, armed True. Empty: zero/True. [11,12,14]: one/False.
[11,9,11]: two/False. Choose the state variables and control flow yourself.

</details>

## Checkpoint 3 — after Chapter 8: shipment preparation

Implement prepare_shipments(rows). Every input dictionary has event_id, sku and
units. IDs/SKUs are nonblank strings normalized with strip; units is an exact int
>= 0 (bool is invalid). Do not mutate input. Validate before deduplicating.
Keep the first valid event_id; reject later valid repeats with reason "duplicate".
An invalid row has reason "invalid".

Return a dictionary containing accepted (new normalized rows in input order),
rejected (index/reason dictionaries, zero-based) and totals (sku-to-units dictionary).
totals sums units from accepted rows only; rejected/duplicate rows contribute nothing.
Empty input returns three empty collections.
Create your own fixtures: interleaved SKUs, a normalized duplicate, an invalid row
followed by a valid row with its ID, zero units, True units and empty input.
Explain helper boundaries, return values and independent group state.

<details>
<summary>One hint after an attempt</summary>

Separate validation from collection/reporting. Trace two rows sharing an ID where
only the second is valid. Choose the implementation and helper interfaces yourself.

</details>

## Checkpoint 4 — after Chapter 14

Complete [Gate A](../docs/assessment.md#gate-a--python-independence-90120-minutes)
on a new CSV from a blank implementation. A retail fixture pass does not replace
this check. Include a meaningful regression and run from another cwd.

## Save and commit your attempt

Create checkpoint-work when saving attempted code and sanitized notes. On your
current feature/... branch, stage only the attempt you actually completed:

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "02-python/checkpoint-work"
git diff --cached
git commit -m "feat(python): record independent checkpoint evidence"
git push -u origin HEAD
~~~

Review previously staged files too. There is no supplied checkpoint solution.
