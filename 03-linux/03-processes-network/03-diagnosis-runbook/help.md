# Help — Logs, resource checks and a useful runbook

## First hint

Successful operation must satisfy the data contract, not merely stop complaining.

## Detailed approach

Use a known-good fixture as a control. For a path-occupied failure, create one disposable file under the lab root and request it as an output directory; do not alter existing outputs. For interpreter failure, override LE_PYTHON for one command. The wrapper must still propagate nonzero statuses. After repair confirm the manifest 6/4/2/3/3050. Record the observed failure type rather than guessing from the first word.

## Troubleshooting

Old output can remain from a previous success after a new failure. A manifest existing on disk alone does not prove that the latest invocation succeeded.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
