# LE01 assignment

1. Complete setup.md and record wsl --list --verbose from PowerShell.
2. In Ubuntu record whoami, uname -s, pwd, command -v bash and the value of $LE_LAB_ROOT.
3. Navigate to the course root using its quoted /mnt/c path; then navigate to your native lab directory.
4. Find data/events.csv with ls. Explain the difference between its repository path and your scratch directory.
5. Use cd .. and return. Try ls on one nonexistent path and record its exit status immediately with printf '%s\n' "$?".

## Deliverables

Create notes.md containing the two shell contexts, observed paths, one successful command and one failed command. Do not copy another user's username or version as your result.

## Reflection

Why can a valid Windows path fail when pasted into Bash?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
