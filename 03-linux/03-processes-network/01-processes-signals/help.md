# Help — Processes, jobs and graceful stopping

## First hint

Use a requested termination before a forced termination.

## Detailed approach

Capture practice_pid=$! immediately after starting sleep. Never target a guessed PID or all Python processes. A cleanup function can check that its known temporary directory exists and call rmdir -- "$temporary_dir"; only an empty directory is removed. Register trap cleanup EXIT. Test one process and one directory at a time. A normal shell exit runs the EXIT handler; an uncatchable signal cannot run it.

## Troubleshooting

jobs from another terminal does not show the first shell's job list. A variable captured after another background launch identifies a different PID. A trap using a broad path can remove unrelated work; keep ownership exact.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
