# Help — Run Python in Linux with an explicit environment

## First hint

Inspect sys.executable from the interpreter actually running the program.

## Detailed approach

~~~bash
export LE_PYTHON="$LE_LAB_ROOT/venv/bin/python"
"$LE_PYTHON" "$LE_COURSE_ROOT/project/app.py" --input "$LE_COURSE_ROOT/data/events.csv" --output "$LE_LAB_ROOT/python-run"
~~~
The first quoted word is the executable and the second is a script. --input and --output belong to this app. Use python -m json.tool to inspect manifest.json. The supplied app is engineering infrastructure, so no Python implementation is required here.

## Troubleshooting

An ensurepip/venv failure may need Ubuntu's python3-venv package. A Windows .exe path means the wrong interpreter.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
