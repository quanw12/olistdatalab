# Files, directories, inspection and scoped cleanup

## Concept and purpose

mkdir creates directories; -p permits existing parents. cp copies, mv moves or renames, and rm removes a specified file. cat displays text; less lets you navigate longer text and q exits it. head/tail show a bounded beginning/end. find walks a directory tree and can match file names.

Globs such as *.txt are expanded by the shell. Quote a pattern passed to find so find, rather than the shell, interprets it. Separate data paths from operations and use -- before a path where the command supports it. Inspect the resolved scope with pwd and ls before cleanup.

The commands here operate only on a directory you created for this lesson. Re-running a command may behave differently if a file already exists. Keep source fixtures read-only in your workflow; produce copies in your lab.

## Syntax example — Bash in Ubuntu

~~~bash
mkdir -p "$LE_LAB_ROOT/files"
printf 'first\nsecond\n' > "$LE_LAB_ROOT/files/note.txt"
cp -- "$LE_LAB_ROOT/files/note.txt" "$LE_LAB_ROOT/files/copy.txt"
find "$LE_LAB_ROOT/files" -type f -name '*.txt' -print
tail -n 1 "$LE_LAB_ROOT/files/copy.txt"
~~~

## Trace the example

Two text files exist and the last printed line is second. The quoted *.txt reaches find unchanged.

## Apply it to Data Engineering

A pipeline should locate inputs deliberately and write artifacts to a documented destination.

[Reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). These explanations and exercises are original course material.
