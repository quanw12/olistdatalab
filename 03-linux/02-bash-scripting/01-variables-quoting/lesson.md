# Variables, quoting and arguments

## Concept and purpose

Bash assignment has no spaces around =. Expand a variable using "$name". Double quotes permit variable expansion while keeping spaces in one argument; single quotes preserve literal text. An unquoted expansion may undergo word splitting and filename expansion.

$1 is the first positional argument; $# is the number of arguments. "$@" preserves each argument separately. Use printf with a fixed format string, rather than treating arbitrary input as the format. export makes a variable available to child programs; it does not turn it into a persistent configuration file.

Command substitution $(command) captures stdout and removes trailing newlines. Quote it when using the result as one path. Arrays store separate values; "${array[@]}" passes each element separately. Never use eval to reconstruct a command from user input.

## Syntax example — Bash in Ubuntu

~~~bash
label='batch with spaces'
printf 'label=%s\n' "$label"
args=('one file.csv' 'second.csv')
printf '<%s>\n' "${args[@]}"
~~~

## Trace the example

The first output preserves spaces. The array prints two lines, one per element.

## Apply it to Data Engineering

Quoting preserves valid paths and prevents unintended extra arguments.

[Reference](https://www.gnu.org/software/bash/manual/bash.html#Quoting). These explanations and exercises are original course material.
