# Help — Ubuntu, shells and path navigation

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

First identify the shell. Then identify whether the path uses Windows or Linux notation.

</details>

<details>
<summary>Detailed approach</summary>

Open an Ubuntu tab after installing it; docker-desktop is Docker's internal environment. In Bash, run export LE_COURSE_ROOT='/mnt/c/DE Courses/03-linux' and export LE_LAB_ROOT="$HOME/de-labs/linux-engineering", then mkdir -p "$LE_LAB_ROOT". These variables name two separate locations. Run cd "$LE_COURSE_ROOT" and ls data/events.csv. Keep the quotation marks around each expanded path.

Use type pwd to see that a command may be a shell builtin. Use command -v python3 to locate an executable. If you used exit and see PS C:\..., you are back in PowerShell.

</details>

<details>
<summary>Troubleshooting</summary>

'export is not recognized' indicates PowerShell. 'Set-Location: command not found' indicates Bash. A missing /mnt/c path is a path/location problem, not a Python failure.

</details>
