# Standard streams, pipes and text inspection

## Concept and purpose

Programs have standard input (stdin), standard output (stdout) and standard error (stderr). A pipe connects stdout to the next command's stdin. > truncates a destination; >> appends. 2> redirects stderr. Capture errors separately when successful data will be consumed by another program.

grep filters matching text, sort orders lines, uniq groups adjacent equal lines, wc counts, and cut selects simple delimited fields. Set LC_ALL=C when a deterministic byte-order sort is required. A shell text pipeline is not a general CSV parser: quoted commas and multiline fields need a real parser.

The status of a Bash pipeline normally follows its last command. A grep with no matches exits 1 even when no system failure occurred. Later lessons teach pipefail and intentional failure handling. Do not confuse an empty result with a broken source.

## Syntax example — Bash in Ubuntu

~~~bash
printf 'beta\nalpha\nalpha\n' | LC_ALL=C sort | uniq -c
printf 'ok\n' > "$LE_LAB_ROOT/stdout.txt"
printf 'problem\n' >&2
~~~

## Trace the example

Sorting puts the two alpha lines together, so uniq -c counts alpha twice and beta once. The success text is saved to a file; the problem text goes to stderr.

## Apply it to Data Engineering

Separate machine-readable pipeline output from diagnostic messages so downstream parsing remains dependable.

[Reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). These explanations and exercises are original course material.
