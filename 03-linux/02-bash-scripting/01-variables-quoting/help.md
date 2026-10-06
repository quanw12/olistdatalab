# Help — Variables, quoting and arguments

## First hint

Keep the format fixed and quote the data.

## Detailed approach

Start with a shebang. Test [[ $# -ne 1 ]] before reading $1. Print usage with printf 'usage: ...\n' >&2 and exit 64. On success use a fixed %s conversion and "$1". Status 64 is this contract's chosen usage status. Do not add decorative output.

~~~bash
value='literal %s'
printf 'value=%s\n' "$value"
~~~
The input percent sequence remains data.

## Troubleshooting

Unquoted $1 can split a filename. printf "$1" interprets input as a format.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
