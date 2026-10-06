# Provided checkers

check_scripts.py verifies the four Bash contracts: variables, status, loops, runner. It invokes your scripts with fixed normal/error inputs in temporary directories and rejects untouched prompt-only starters. Run it in Ubuntu for native Linux evidence. --script and --bash permit an explicitly chosen alternative lab implementation/interpreter.

project/test_app.py tests the supplied data app's counts, replay, empty input, shape errors, conflicting duplicates, preservation of prior artifacts and output failure. It is provided infrastructure, not your Python exercise answer.

check_report.py checks the fixed-fixture manifest/report over the local HTTP viewer. It cannot prove container configuration, volume persistence, networking layout or the latest run's status; collect that evidence separately.

Manual labs have exact expected observations and reflection keys. Do not edit checkers or hard-code fixture output to claim completion. Syntax checks, mocked behavior and live runtime evidence are different types of evidence.
