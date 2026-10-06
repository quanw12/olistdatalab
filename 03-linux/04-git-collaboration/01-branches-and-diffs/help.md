# Help — Git states, branches, diffs and scoped undo

## First hint

The index persists across staging commands.

## Detailed approach

~~~bash
mkdir -p "$LE_LAB_ROOT/git/basics"
cd "$LE_LAB_ROOT/git/basics"
git init -b main
git config user.name 'DE Student'
git config user.email 'student@example.test'
git config commit.gpgsign false
~~~
These settings affect only the newly created repository. Add one path at a time, inspect git diff --cached, then commit. git restore --staged keeps working edits. If experimenting with git restore -- README.md, first save the disposable edit's text in notes; that command discards it.

## Troubleshooting

'Not a git repository' means wrong cwd. A huge status list may mean you initialized at the wrong scope; stop and inspect the root with git rev-parse --show-toplevel.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
