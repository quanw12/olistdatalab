# Help — Paths, context managers, and safe file replacement

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Do the potentially failing serialization before opening any output.

</details>

<details>
<summary>Detailed approach</summary>

Convert path with Path(path). Compute the JSON text. Use NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False), remember its Path, and exit its with block before temp_path.replace(path). A finally block can call unlink(missing_ok=True) on the temporary path you created. Never remove arbitrary sibling files.

</details>

<details>
<summary>Troubleshooting</summary>

PermissionError on Windows can mean the temporary file was still open during replacement. Truncated old output means the final destination was opened too early.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.

</details>

<details>
<summary>The syntax behind the steps</summary>

~~~python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    destination = Path(folder) / "nested" / "sample.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        handle.write("example")
    print(destination.read_text(encoding="utf-8"))
~~~

The / operator combines Path components. parent is the containing directory. parents=True creates missing ancestors; exist_ok=True permits an existing directory. A with block manages a resource's exit behavior, even when an exception leaves the block. For a file object, leaving with closes it.

This example teaches directory/file syntax, not atomic publication. In the exercise, serialize before opening a temporary file, close that file, and use its Path.replace(destination). Track only your own temporary path. finally is where cleanup belongs; never suppress the original failure.

</details>
