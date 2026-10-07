# Help — Run Python in Linux with an explicit environment

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Inspect sys.executable from the interpreter actually running the program.

</details>

<details>
<summary>Detailed approach</summary>

~~~bash
export LE_PYTHON="$LE_LAB_ROOT/venv/bin/python"
"$LE_PYTHON" "$LE_COURSE_ROOT/project/app.py" --input "$LE_COURSE_ROOT/data/events.csv" --output "$LE_LAB_ROOT/python-run"
~~~
The first quoted word is the executable and the second is a script. --input and --output belong to this app. Use python -m json.tool to inspect manifest.json. The supplied app is engineering infrastructure, so no Python implementation is required here.

</details>

<details>
<summary>Troubleshooting</summary>

An ensurepip/venv failure may need Ubuntu's python3-venv package. A Windows .exe path means the wrong interpreter.

</details>
