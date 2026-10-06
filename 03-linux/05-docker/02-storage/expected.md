# Checking your work

persistent survives container replacement. The bind-mounted CSV is readable; attempted writes fail. Host fixture bytes remain unchanged and the named volume still exists.

## Reflection answer — reveal after your attempt

<details>
<summary>Show the explanation</summary>

The explicitly named volume is a separate managed resource. Removing a container does not imply deleting that resource and its data.

</details>

Completion requires your own work and an explanation. Creating materials does not mark the lesson complete.
