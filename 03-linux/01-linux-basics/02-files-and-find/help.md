# Help — Files, directories, inspection and scoped cleanup

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

The shell can expand a wildcard before find receives it.

</details>

<details>
<summary>Detailed approach</summary>

Use mkdir -p for the two directories, then cp -- "$LE_COURSE_ROOT/data/events.csv" "$LE_LAB_ROOT/files-practice/raw/input batch.csv". Use cp and mv for the processed copy. cmp exits 0 when files have identical bytes; inspect its status immediately. find "$LE_LAB_ROOT/files-practice" -type f -name '*.csv' -print should return exactly two paths. Use head -n 1 and tail -n 2 instead of opening a huge file blindly.

For cleanup, first ls the exact disposable file, then rm -- that path. -- ends options, so a filename starting with a dash is treated as a path.

</details>

<details>
<summary>Troubleshooting</summary>

Several unexpected find arguments mean the shell expanded an unquoted glob. cp errors involving separate words usually mean a space-containing path was unquoted.

</details>
