# Ubuntu, shells and path navigation

## Concept and purpose

An operating system manages programs, files and access. Linux is the kernel; Ubuntu packages it with tools and a user environment. WSL lets you run Ubuntu alongside Windows. A terminal is the window/interface; a shell interprets commands. This course uses Bash inside Ubuntu. PowerShell and Bash have different syntax even when they share a terminal window.

A command generally contains a program name, options and arguments. pwd prints your current directory. cd changes it; ls lists entries. Absolute Linux paths start with /. Relative paths start from the current directory. . means this directory, .. means its parent, and ~ represents your home directory when the shell expands it.

Paths containing spaces must be quoted. Windows C:\DE Courses maps to /mnt/c/DE Courses in WSL. The mounted repository holds learning files; permissions/process/runtime labs live in the native Linux filesystem at $LE_LAB_ROOT. Linux filenames may distinguish uppercase from lowercase. Use Tab completion, Up for command history, Ctrl+C to interrupt the current foreground command and exit to leave Bash.

## Syntax example — Bash in Ubuntu

~~~bash
pwd
printf 'shell=%s\n' "$SHELL"
ls -ld "$LE_LAB_ROOT"
cd "$LE_LAB_ROOT"
pwd
ls --help | head -n 5
~~~

## Trace the example

pwd and ls output depend on your username and filesystem. printf substitutes the shell variable into %s; \n ends the line. The final pipeline shows only the first five help lines.

## Apply it to Data Engineering

Many deployment failures begin with the wrong shell or working directory. Locate a file before diagnosing its contents.

[Reference](https://learn.microsoft.com/en-us/windows/wsl/filesystems). These explanations and exercises are original course material.
