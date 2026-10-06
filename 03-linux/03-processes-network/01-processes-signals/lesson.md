# Processes, jobs and graceful stopping

## Concept and purpose

A process has a PID and a parent. ps reports processes; a shell job is a shell-managed foreground/background task. & starts a command asynchronously. $! captures the most recent background PID. jobs reports jobs owned by the current shell, while ps inspects OS processes.

wait collects a child's result. kill sends a signal; its default TERM requests termination and allows cleanup. Ctrl+C normally sends INT to the foreground process group. KILL prevents graceful cleanup, so first understand why normal termination failed.

A trap registers a handler for signals or shell exit. Cleanup should target only resources your program created. Starting background work without collecting its status can hide failures. WSL behavior differs from a full always-on server; do not assume a background shell job is a deployment service.

## Syntax example — Bash in Ubuntu

~~~bash
sleep 60 &
practice_pid=$!
ps -p "$practice_pid" -o pid,ppid,comm
kill -TERM "$practice_pid"
if wait "$practice_pid"; then
    printf 'completed\n'
else
    result=$?
    printf 'child status=%s\n' "$result"
fi
~~~

## Trace the example

A sleep process exists, receives TERM, and normally exits with a signal-related nonzero status. Exact display text may vary.

## Apply it to Data Engineering

Stopping a pipeline cleanly matters when it owns temporary files, database transactions or child jobs.

[Reference](https://www.gnu.org/software/bash/manual/bash.html#Job-Control). These explanations and exercises are original course material.
