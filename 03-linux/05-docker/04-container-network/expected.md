# Checking your work

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Host and sibling probe both retrieve the correct manifest. Host uses 8765, sibling uses service name/container port 8000. Container-local localhost is explained accurately.

## Reflection answer — reveal after your attempt

<details>
<summary>Show the explanation</summary>

The sibling reaches the target through their shared Docker network. Its localhost refers to itself; 8765 is a mapping on the host, not the sibling's listening port.

</details>

Completion requires your own work and an explanation. Creating materials does not mark the lesson complete.

</details>
