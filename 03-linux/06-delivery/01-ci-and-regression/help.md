# Help — CI and regression evidence

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

What observable defect does your additional test detect that the supplied tests do not?
Check that at least one test was collected before interpreting a passing command.

</details>

<details>
<summary>Syntax pointer</summary>

The lesson shows multiline run: | syntax. The guide/setup contains the environment
and invocation commands. For a fresh fixture, use tempfile.TemporaryDirectory;
unittest discovery runs test-prefixed methods in TestCase classes.
For Bash-dependent steps, declare shell: bash and use repository-relative paths.

</details>

<details>
<summary>Stronger hint</summary>

Read the existing app contract and tests, then choose a missing boundary. First prove
your test passes on the supplied app in an isolated copy. Change only that behavior
in the copied app and verify an assertion failure; restore the copy and pass again.
An import or syntax failure does not prove your behavior test works.
Keep network/Docker operations out of the default offline suite.

</details>

<details>
<summary>Troubleshooting</summary>

A workflow outside .github/workflows is a draft. Inspect paths, indentation and
collected-test counts before activation. Record local evidence separately from a
real GitHub run; do not claim a workflow draft executed.

</details>
