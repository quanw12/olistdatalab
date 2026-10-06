# Type hints, dataclasses, and simple objects

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/dataclasses.html).

## Concept and purpose

A type hint documents an expected type and helps static analysis; it does not automatically validate runtime input. def double(value: int) -> int can still be called with a string unless you check it.

A class groups state and related behavior. Its methods receive self, the current instance. A dataclass can generate initialization, representation and equality methods from annotated fields. @dataclass is decorator syntax: it transforms the class definition. frozen=True prevents ordinary reassignment of fields, but does not recursively freeze nested lists.

Use __post_init__ for a small invariant check after generated initialization. Prefer a small record object or a plain dictionary over an elaborate inheritance tree. Composition means building larger behavior out of smaller objects/functions.

For this contract, amounts are already integer cents; parsing text into cents is a later lesson.

## Syntax example

~~~python
from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    city: str
    country: str = "VN"

location = Location("Hue")
print(location.city)
print(location == Location("Hue"))
~~~

## Trace the example

The generated initializer assigns the fields. Equality compares field values. The output is Hue then True.

## Apply it to DE

A typed record makes field names visible across pipeline stages. Runtime checks remain necessary at external-data boundaries.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.
