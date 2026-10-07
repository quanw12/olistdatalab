# Help — Variables, quoting and arguments

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Keep the format fixed and quote the data.

</details>

<details>
<summary>Detailed approach</summary>

Start with a shebang. Test [[ $# -ne 1 ]] before reading $1. Print usage with printf 'usage: ...\n' >&2 and exit 64. On success use a fixed %s conversion and "$1". Status 64 is this contract's chosen usage status. Do not add decorative output.

~~~bash
value='literal %s'
printf 'value=%s\n' "$value"
~~~
The input percent sequence remains data.

</details>

<details>
<summary>Troubleshooting</summary>

Unquoted $1 can split a filename. printf "$1" interprets input as a format.

</details>
