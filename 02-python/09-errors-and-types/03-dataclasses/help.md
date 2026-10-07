# Help — Type hints, dataclasses, and simple objects

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Type hints and validation solve different problems.

</details>

<details>
<summary>Detailed approach</summary>

Import dataclass and use a frozen decorator. In __post_init__, inspect self.order_id and self.amount_cents. Use type(self.amount_cents) is int to reject bool. Build order_dict with ordinary field access or dataclasses.asdict; both produce a new mapping here.

</details>

<details>
<summary>Troubleshooting</summary>

If invalid input constructs successfully, annotations alone did not check it. If assignment after construction works, frozen=True is missing.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.

</details>

<details>
<summary>Read class syntax slowly</summary>

This separate example shows validation after automatic initialization:

~~~python
from dataclasses import dataclass

@dataclass(frozen=True)
class BatchSize:
    value: int

    def __post_init__(self):
        if type(self.value) is not int or self.value <= 0:
            raise ValueError("positive integer required")

size = BatchSize(3)
print(size.value)
~~~

class introduces a new type. The annotated field tells dataclass what to include in its generated initializer. self refers to the object being constructed. __post_init__ runs after its fields have been assigned. A raised exception prevents the constructor from returning a valid object.

To return a dictionary, use ordinary field access: {"value": size.value}. This is a fresh dictionary; changing that dictionary does not reassign the object's field. Apply that reasoning to your Order contract, checking each condition explicitly.

</details>
