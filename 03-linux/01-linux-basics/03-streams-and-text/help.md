# Help — Standard streams, pipes and text inspection

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Filter by the exact level token and inspect the file before assuming the delimiter.

</details>

<details>
<summary>Detailed approach</summary>

Use grep 'level=ERROR' "$LE_COURSE_ROOT/data/runs.log" > "$LE_LAB_ROOT/errors.txt". wc -l counts newline-terminated lines, not semantic records. For this fixture only, cut -d' ' -f2 selects level=...; then LC_ALL=C sort | uniq -c. Use ls ... 2> "$LE_LAB_ROOT/ls-error.txt" and save $? immediately, because the next command changes it.

</details>

<details>
<summary>Troubleshooting</summary>

uniq counts duplicates only after adjacent grouping. A status saved after cat describes cat, not the earlier ls. An empty grep result uses exit 1 and needs interpretation.

</details>
