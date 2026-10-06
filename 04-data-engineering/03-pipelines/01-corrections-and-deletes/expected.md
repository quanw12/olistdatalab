# Expected — DE08

After b1: 2 active orders, 2500 cents. After b2: 2 active orders, 2000 cents; current state has A v2, B v2 delete, C v1. Replaying b1 leaves 2000 cents. Equal-version conflicting amount fails.

## Reflection answer

<details>
<summary>Open after answering</summary>

Its newer tombstone prevents an old B upsert from reappearing during replay or a delayed page.

</details>

Passing a supplied fixture is one piece of evidence. Explain the result and show one changed-input or failure example before marking the lesson complete.

