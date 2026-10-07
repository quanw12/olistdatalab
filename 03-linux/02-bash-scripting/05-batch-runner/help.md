# Help — A reusable batch runner with logs

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

The caller controls pwd; the runner controls its own location.

</details>

<details>
<summary>Detailed approach</summary>

Resolve script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)". Store interpreter="${LE_PYTHON:-python3}" and verify it with command -v "$interpreter". Validate arity before $1/$2. Quote every path.

~~~bash
if "$interpreter" "$script_dir/app.py" --input "$input_path" --output "$output_dir" > "$output_dir/run.log" 2> "$output_dir/error.log"; then
    exit 0
else
    result=$?
    exit "$result"
fi
~~~
Define the variables, validate arguments and create the output directory before this invocation. Do not activate an environment interactively inside the wrapper.

</details>

<details>
<summary>Troubleshooting</summary>

A cwd-dependent runner often points to ./app.py. Missing input must return the app's 2, not a successful final print.

</details>
