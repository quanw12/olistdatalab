# Help — Users, permissions and executable files

## First hint

One command opens the script as data; the other asks the OS to execute that file.

## Detailed approach

Use stat -c '%a %n' on the native lab files. chmod u-x removes owner execution and chmod u+x restores it. Run ./script.sh from its containing directory, saving $? immediately. Do not use chmod -R or 777 as a universal repair; identify which resource needs which permission. In VS Code, select LF in the status bar before saving a .sh file.

## Troubleshooting

Mode changes under /mnt/c may reflect Windows/DrvFS behavior rather than native Linux modes. A bash\r interpreter message means CRLF. A missing owner permission is different from a missing executable.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
