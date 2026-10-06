# 03 — Linux

[Home](../README.md) · [Overall roadmap](../roadmap.md) · [Study guide](../docs/study.md)

**After Python, read [setup.md](setup.md), then begin [LE01](01-linux-basics/01-shell-navigation/guide.md).** Complete 22 lessons in order. No Linux knowledge is assumed. This course teaches execution, diagnosis, collaboration and delivery around a supplied batch application.

## Modules

| Module | Lessons | Checkpoint |
|---|---|---|
| [Linux basics](01-linux-basics/README.md) | LE01–LE04 | Navigate, inspect streams and understand native permissions. |
| [Bash scripting and execution](02-bash-scripting/README.md) | LE05–LE09 | Quote arguments, validate inputs, select Python and propagate job statuses. |
| [Processes, networking and diagnosis](03-processes-network/README.md) | LE10–LE12 | Own process cleanup, classify HTTP failures and write a recovery runbook. |
| [Git collaboration](04-git-collaboration/README.md) | LE13–LE15 | Review staging, resolve conflicts and simulate collaboration with local remotes. |
| [Docker and Compose](05-docker/README.md) | LE16–LE20 | Package the batch, persist artifacts and explain service networking. |
| [CI and delivery capstone](06-delivery/README.md) | LE21–LE22 | Reject a real regression and rehearse delivery/recovery. |

Docker starts at LE16 after shells, scripts, processes and networking. A lesson may take several sessions. No cloud account, Kubernetes or paid API is needed.

## Practice and evidence

Each guide links lesson, assignment, help, expected observations and commit commands. The [shared study guide](../docs/study.md) explains the learning cycle; [progress](progress.md) tracks your work.

Four Bash contracts have executable checks: LE05 variables, LE07 status, LE08 loops and LE09 runner. The supplied app has behavior tests; the capstone has a local HTTP report checker. Permission, process, Git and container labs require actual observations. A syntax check or workflow draft is not proof that a live lab ran.

The [delivery capstone](06-delivery/02-capstone/contract.md) combines your wrapper, Docker/Compose and CI work. Demonstrate success, missing-input failure, preserved outputs and recovery, then continue to [Data Engineering](../04-data-engineering/README.md).

Author reference checks used Windows Python, Git Bash and isolated Git repositories. Native Ubuntu, Docker engine and live GitHub execution must be demonstrated in your environment; read [sources and boundaries](sources.md). Bash labs use the scoped lab directory described in setup; Git conflict experiments use separate repositories.

Use the guide's manual commit commands and your feature/... convention. See [workspace conventions](../docs/workspace.md) for branch naming and staging rules.
