# Help — Users, permissions and executable files

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

One command opens the script as data; the other asks the OS to execute that file.

</details>

<details>
<summary>Detailed approach</summary>

Use stat -c '%a %n' on the native lab files. chmod u-x removes owner execution and chmod u+x restores it. Run ./script.sh from its containing directory, saving $? immediately. Do not use chmod -R or 777 as a universal repair; identify which resource needs which permission. In VS Code, select LF in the status bar before saving a .sh file.

</details>

<details>
<summary>Troubleshooting</summary>

Mode changes under /mnt/c may reflect Windows/DrvFS behavior rather than native Linux modes. A bash\r interpreter message means CRLF. A missing owner permission is different from a missing executable.

</details>
