# Run Python in Linux with an explicit environment

## Concept and purpose

Windows Python and Ubuntu Python are separate executables with separate packages. Windows .venv/Scripts/python.exe is not Linux venv/bin/python. command -v python3 locates the selected executable; python3 --version identifies it.

python3 -m venv creates an isolated Linux environment. Calling bin/python directly avoids reliance on activation. The provided app requires Python >=3.10 and only the standard library.

Keep the runtime environment under the native Linux lab directory. Small teaching code remains in the mounted repository for convenient editing. Larger projects benefit from a separate Linux-native checkout; clearly identify which checkout owns your changes.

## Syntax example — Bash in Ubuntu

~~~bash
command -v python3
python3 --version
python3 -m venv "$LE_LAB_ROOT/venv"
"$LE_LAB_ROOT/venv/bin/python" -c 'import sys; print(sys.executable); print(sys.prefix)'
~~~

## Trace the example

The final paths point into your native Linux lab venv, independent of Windows Python.

## Apply it to Data Engineering

An explicit interpreter makes scheduled and container runs easier to diagnose.

[Reference](https://docs.python.org/3/library/venv.html). These explanations and exercises are original course material.
