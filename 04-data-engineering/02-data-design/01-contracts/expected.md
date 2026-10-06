# Expected — DE04

The first supplied batch's two records validate. An ID containing only spaces produces errors ['id']; a naive occurred_at and True version produce ['occurred_at', 'version']. Extra source metadata is omitted from the canonical record. Original dict remains unchanged.

## Reflection answer

<details>
<summary>Open after answering</summary>

Changing cents to currency units changes meaning without changing an integer column's type. Consumers need a coordinated migration and explicit version policy.

</details>

Passing a supplied fixture is one piece of evidence. Explain the result and show one changed-input or failure example before marking the lesson complete.

