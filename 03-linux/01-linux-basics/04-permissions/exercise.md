# LE04 assignment

1. Create a disposable directory $LE_LAB_ROOT/permissions, owned by your current user.
2. Make a text file private with chmod 600; inspect it using stat -c '%a %n'.
3. Write a tiny script yourself that prints ready. Save it with LF and test bash script.sh.
4. Remove its owner execute bit and observe direct execution failing. Add u+x and repeat successfully.
5. Explain what 700 on the lab directory means. Apply it only to that exact directory.
6. Record the current umask without changing global configuration.

## Deliverables

notes.md with observed modes, interpreter path, failure/success status and your small script in this lesson folder.

## Reflection

Why can bash script.sh work while ./script.sh reports Permission denied?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
