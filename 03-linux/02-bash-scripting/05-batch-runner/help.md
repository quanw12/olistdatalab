# Help — A reusable batch runner with logs

## First hint

The caller controls pwd; the runner controls its own location.

## Detailed approach

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

## Troubleshooting

A cwd-dependent runner often points to ./app.py. Missing input must return the app's 2, not a successful final print.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
