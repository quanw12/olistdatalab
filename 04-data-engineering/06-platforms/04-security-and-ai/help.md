# Help — Credentials, privacy and verified AI assistance

## First hint

Schema-valid is not necessarily factually correct.

## Detailed approach

Compare set(payload) to {'id','label'}, then check exact value types and allowlists. Reject extra keys such as command/sql/url. Never execute model-returned code or SQL just because JSON parses. Evaluate a mislabeled but valid object separately with ground truth; the schema checker cannot judge semantic truth. If no AI access remains, evaluate provided simulated responses and record that boundary honestly. For actual secret exposure, revoke/rotate it; deleting a file alone does not remove Git history.

Check that label is a string before set membership. A list/dict label is invalid input and must produce your deliberate ValueError; letting Python raise TypeError from hashing is not the promised validation contract.

## Troubleshooting

A response with priority label can satisfy schema yet be wrong. Mock fixture evaluation is not evidence of a live model's accuracy. Do not build an agent framework for this task.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

