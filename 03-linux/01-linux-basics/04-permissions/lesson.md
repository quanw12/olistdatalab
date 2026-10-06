# Users, permissions and executable files

## Concept and purpose

id identifies the current user and groups. ls -l shows the owner, group and rwx permissions for user/group/others. Read means viewing file contents; write means changing them; execute means running a program. For a directory, execute allows traversal/search and write permits changing its entries.

chmod changes permission bits. Symbolic modes such as u+x name an exact change. 600 means owner read/write only; 700 adds owner execution while restricting others. umask removes permission bits from newly created entries; it does not repair existing files. Work as your normal account; sudo is reserved for a specific system operation that needs it.

A script with a shebang requests its interpreter when executed directly. bash script.sh reads it with Bash even without the file's execute bit, while ./script.sh needs the execute bit and a valid interpreter. Use LF line endings; CRLF can produce a /usr/bin/env: bash\r error.

## Syntax example — Bash in Ubuntu

~~~bash
printf '#!/usr/bin/env bash\nprintf \"hello\\\\n\"\n' > "$LE_LAB_ROOT/hello.sh"
chmod u+x "$LE_LAB_ROOT/hello.sh"
"$LE_LAB_ROOT/hello.sh"
ls -l "$LE_LAB_ROOT/hello.sh"
id
~~~

## Trace the example

Direct execution prints hello. The mode listing includes an owner execute bit; exact other bits depend on your umask.

## Apply it to Data Engineering

Permission failures can break output publication even when data-processing logic is correct. Diagnose ownership and the parent directory before escalating access.

[Reference](https://www.gnu.org/software/coreutils/manual/coreutils.html#File-permissions). These explanations and exercises are original course material.
