# Expected results — Type hints, dataclasses, and simple objects

Order('A1', 0) is valid. Blank IDs, -1 cents, True cents, and '10' cents fail. Reassigning order.amount_cents raises FrozenInstanceError. order_dict(Order('A1',100)) is {'order_id':'A1','amount_cents':100}.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Does frozen=True make every object reachable from a dataclass immutable?

<details>
<summary>Reveal the reasoning after answering</summary>

No. It blocks ordinary field reassignment. Mutable objects stored inside fields can still mutate unless independently protected. These fields are immutable scalar values.

</details>
