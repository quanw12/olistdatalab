# Help — CI that catches a real regression

## First hint

Choose a contract edge case; avoid assertions that only mirror an implementation detail.

## Detailed approach

For local tests:
~~~bash
"$LE_PYTHON" -m unittest discover -s "$LE_COURSE_ROOT/project" -p 'test*.py' -v
for mode in variables status loops runner; do
    python3 "$LE_COURSE_ROOT/checks/check_scripts.py" "$mode" || exit "$?"
done
~~~
In CI, use repository-relative paths such as 03-linux/project. The checker discovers course files from its own path, so LE_COURSE_ROOT is not required there; runner defaults to available python3. Give a step shell: bash when its command needs Bash syntax. A test can import app from its own project folder and use tempfile.TemporaryDirectory for outputs. Keep network/Docker operations out of the default CI test suite. Do not mutate the tracked app to simulate failure; make a lab copy and clearly record which copy you ran.

For YAML syntax, put your commands under a job's steps. A multiline step uses `run: |` and indents each command beneath it:

~~~yaml
      - name: Check application behavior
        shell: bash
        run: |
          python -m unittest discover -s 03-linux/project -p 'test*.py' -v
~~~

Add separate named steps for the four shell contracts and runner syntax. Declare path filters separately under push and pull_request; each paths value is a list of quoted patterns. Start from the lesson's toy workflow, replace its toy print, and check indentation before activation.

For your additional test, read test_app.py first. Choose a distinct edge case, create its CSV in a TemporaryDirectory, call app.run, and assert observable output or the expected exception. For example, leading zeros, a whitespace-only ID, or a value just above the numeric limit are meaningful cases. Keep assertions tied to the published contract.

To prove the test can catch an error, copy app.py and your test into a new isolated lab directory:

~~~bash
mutation_dir=$(mktemp -d "$LE_LAB_ROOT/mutation.XXXXXX")
cp "$LE_COURSE_ROOT/project/app.py" "$mutation_dir/app.py"
cp "$LE_COURSE_ROOT/project/test_extra.py" "$mutation_dir/test_extra.py"
"$LE_PYTHON" -m unittest discover -s "$mutation_dir" -p 'test_extra.py' -v
~~~

The baseline must pass and collect at least one test. In the copied app only, change the behavior your test targets, such as relaxing a numeric bound. Rerun the same command and record the genuine test failure. Restore the copied app from the provided app and rerun to pass. Leave this clearly named directory as evidence; do not change the tracked app or claim that an import/syntax error proves your behavior assertion.

## Troubleshooting

Files outside .github/workflows are not active workflows. YAML indentation is structural. A wrong -p pattern can collect zero tests and falsely look successful; inspect the test count.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
