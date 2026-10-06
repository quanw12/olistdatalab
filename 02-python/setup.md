# Setup for the Python companion course

Use PowerShell on Windows and your current editor. These lessons require only standard-library Python. Python 3.13 is available on this machine; your existing 3.14 installation is also suitable. Syntax uses Python 3.10+ features such as match and strict zip.

## Verify before changing anything

~~~powershell
Set-Location "C:\DE Courses"
python --version
python -c "import sys; print(sys.executable)"
~~~

The first command reports the version. The second identifies the interpreter used by python. Multiple installations can coexist; choose one consistently.

If python is not found, the interpreter verified while preparing this course is:

~~~powershell
& "C:\Users\DELL\AppData\Local\Programs\02-python\Python313\python.exe" --version
~~~

The & is PowerShell's call operator for an executable path in quotes. You do not need to reinstall Python or change execution policy. If that path later changes, select an installed interpreter in your editor.

## First run

~~~powershell
Set-Location "C:\DE Courses\02-python\01-fundamentals\01-run-print"
python .\exercise.py
~~~

Or use the full interpreter path:

~~~powershell
& "C:\Users\DELL\AppData\Local\Programs\02-python\Python313\python.exe" "C:\DE Courses\02-python\01-fundamentals\01-run-print\exercise.py"
~~~

The initial file contains comments only, so it prints nothing until you implement it. Save before running. Choose the same interpreter in your editor.

For input() exercises, run in the integrated terminal rather than a read-only output pane. Type each requested value and press Enter. The lesson specifies test inputs.

## Read code examples

Copy only the Python lines into scratch.py. Do not copy code-fence markers, expected output or the terminal prompt. Keep scratch code separate from your exercise.

~~~powershell
python .\scratch.py
~~~

The main example in every lesson is a complete runnable snippet. A syntax fragment mentioned in prose may need surrounding code. exercise.py is a problem statement, not a supplied solution.

## Common mistakes

| Symptom | Check |
|---|---|
| File not found | Folder and filename; quote paths containing spaces |
| No output | Comments-only exercise, unsaved file, or a function defined but never called |
| NameError | Spelling/case and whether assignment occurred before use |
| SyntaxError or IndentationError | Quotes, colon, parentheses and consistent four-space indentation |
| TypeError | Operation and operand types; input returns text |
| ValueError | Conversion/unpacking format and shape |
| IndexError or KeyError | Whether the position or dictionary key exists |
| Program keeps running | A while loop may not advance; press Ctrl+C and inspect its update paths |
| Extra output | Remove temporary diagnostic prints before exact output comparison |

Read the traceback's final line for the error category, then inspect your own file/line above it. Change one suspected cause and rerun.

## Environments and files

No virtual environment or dependency installation is necessary for these standard-library exercises. Later package lessons will teach environment isolation explicitly. Save text as UTF-8.

Exercise data is included in the problem statements. Use the original companion examples and your own implementation; do not copy the instructor's paid handbook or solutions into the repository.
