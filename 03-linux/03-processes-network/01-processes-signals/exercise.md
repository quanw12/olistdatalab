# LE10 assignment

1. Start a sleep child, save its PID, inspect ps and jobs, then stop only that PID with TERM and wait for it.
2. Write exercise.sh: create a uniquely named temporary directory with mktemp -d under your native lab directory. Register an EXIT trap to remove only that empty directory using rmdir. Print its path, start a short sleep and wait.
3. Demonstrate normal exit and Ctrl+C. Inspect whether the temporary directory is removed in both cases.
4. Explain why this demonstration does not guarantee cleanup after SIGKILL/power loss.

## Deliverables

exercise.sh and notes.md: owned PID, observed status, trap cleanup evidence.

## Reflection

Why is kill -9 a poor default for a process with unfinished writes?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
