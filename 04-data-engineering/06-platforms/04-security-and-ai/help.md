# Help — Credentials, privacy and verified AI assistance

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Schema-valid is not necessarily factually correct.

</details>

<details>
<summary>Detailed approach</summary>

Compare set(payload) to {'id','label'}, then check exact value types and allowlists. Reject extra keys such as command/sql/url. Never execute model-returned code or SQL just because JSON parses. Evaluate a mislabeled but valid object separately with ground truth; the schema checker cannot judge semantic truth. If no AI access remains, evaluate provided simulated responses and record that boundary honestly. For actual secret exposure, revoke/rotate it; deleting a file alone does not remove Git history.

Check that label is a string before set membership. A list/dict label is invalid input and must produce your deliberate ValueError; letting Python raise TypeError from hashing is not the promised validation contract.

</details>

<details>
<summary>Troubleshooting</summary>

A response with priority label can satisfy schema yet be wrong. Mock fixture evaluation is not evidence of a live model's accuracy. Do not build an agent framework for this task.

</details>
