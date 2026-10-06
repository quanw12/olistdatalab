# Setup: Windows -> Ubuntu -> Docker

This page establishes the environment; lessons teach the commands and syntax progressively. Prepare Ubuntu first. Docker is needed only at LE16.

## What is already on your machine

Read-only inventory during course preparation found:
- WSL registered docker-desktop using version 2; no Ubuntu learning distribution was listed.
- Docker client 29.8.1 was installed, but the configured Linux engine was unreachable.
- Windows Python 3.13.5 and Git were available.

This is an observed snapshot, not a guarantee about your next session. Docker's internal distribution is not the Ubuntu environment for these lessons. No distribution, package, Docker service or system setting was installed/changed while preparing the course.

## 1. Inspect from Windows PowerShell

~~~powershell
wsl --list --verbose
wsl --status
~~~

If Ubuntu is already present now, use its exact listed name. Otherwise install Ubuntu using an administrator PowerShell:

~~~powershell
wsl --install -d Ubuntu
~~~

Follow the installer, restart Windows if requested, and launch Ubuntu to create your own Linux username/password. Password input may show no characters. WSL/Ubuntu installation is your setup step, not part of running a lesson checker.

Confirm from PowerShell:

~~~powershell
wsl --list --verbose
wsl -d Ubuntu
~~~

The last command opens Ubuntu Bash. If your distribution is named Ubuntu-24.04 or another name, replace Ubuntu with that exact name. Use WSL version 2. If your actual Ubuntu entry shows version 1, Microsoft documents wsl --set-version <actual-name> 2; finish conversion before Docker integration.

[Microsoft installation reference](https://learn.microsoft.com/en-us/windows/wsl/install).

## 2. Install the small Ubuntu tool set

These commands run **inside Ubuntu**, not PowerShell:

~~~bash
sudo apt-get update
sudo apt-get install -y bash coreutils findutils grep procps iproute2 curl git python3 python3-venv
~~~

sudo applies to those package operations. Work on lessons as your ordinary Linux user. Installation needs network access; most subsequent labs use local fixtures.

Ubuntu's Python should be 3.10 or newer. The stable provided app uses no third-party packages. Record the actual versions:

~~~bash
uname -s
bash --version | head -n 1
git --version
python3 --version
curl --version | head -n 1
~~~

## 3. Define two locations in each new Ubuntu terminal

~~~bash
export LE_COURSE_ROOT='/mnt/c/DE Courses/03-linux'
export LE_LAB_ROOT="$HOME/de-labs/linux-engineering"
mkdir -p "$LE_LAB_ROOT"
cd "$LE_COURSE_ROOT"
ls data/events.csv
~~~

LE_COURSE_ROOT points to the existing Windows repository through WSL's drive mount. LE_LAB_ROOT is a separate native Linux location for temporary files, permissions, Git sandboxes and your Linux venv. $HOME is your existing Linux home; do not overwrite it.

The shared repository stays easy to edit on Windows. Native storage makes Unix permission and process labs meaningful; mounted Windows permissions behave differently. Larger development projects should use Linux-native checkouts. [Microsoft filesystem guidance](https://learn.microsoft.com/en-us/windows/wsl/filesystems).

These exports apply only to the current shell and its children. Repeat them in a new terminal. This course does not rewrite your shell profile automatically.

## 4. Editing and running Bash

Use VS Code or your editor; save .sh files with **LF** line endings. The folder's .gitattributes requests LF when Git handles Bash/container text. Running bash file.sh does not require an execute bit on the script. LE04 teaches direct execution on native lab files.

Do not run Windows environment activation commands inside Ubuntu. At LE06:

~~~bash
python3 -m venv "$LE_LAB_ROOT/venv"
export LE_PYTHON="$LE_LAB_ROOT/venv/bin/python"
"$LE_PYTHON" "$LE_COURSE_ROOT/project/app.py" --help
~~~

Use the full interpreter path. The Windows Python course's .venv-python-de environment is separate.

## 5. Docker setup — wait until LE16

Docker Desktop is already installed in the observed snapshot. Start it from Windows and wait for its engine to become ready. If absent on another machine, follow its [Windows installation guide](https://docs.docker.com/desktop/setup/install/windows-install/).

Use Linux containers and the WSL2 backend. Under Settings > Resources > WSL Integration, enable your actual Ubuntu distribution, then apply the change. Docker documents a minimum WSL application version 2.1.5; use wsl --version from PowerShell to inspect it and follow the official requirements if an update is needed. WSL application version and a distribution's WSL mode 1/2 are different values.

Do not install a second Docker Engine inside Ubuntu for this Desktop-based course. [Docker integration documentation](https://docs.docker.com/desktop/features/wsl/).

In Ubuntu:

~~~bash
docker context show
docker version
docker compose version
~~~

docker version must report a reachable server, not just a client. A missing pipe/socket is a setup/context failure. Do not reset Desktop or erase its existing data to fix it. Use the current error and official troubleshooting guidance.

The course uses python:3.12-slim as a teaching base. This tag is mutable; record its actual image ID/digest in your lab evidence. No image build/pull or live container run was performed during author preparation while the engine was unavailable.

## Terminal map

| Work | Shell and location |
|---|---|
| WSL inventory/install, main-course commits | Windows PowerShell; C:\DE Courses |
| Linux exercises and Bash checks | Ubuntu Bash; course files under /mnt/c, runtime under $LE_LAB_ROOT |
| Lab Git practice | Ubuntu Bash; isolated $LE_LAB_ROOT/git repositories |
| Docker/Compose after integration | Ubuntu Bash |
| Commands inside a container | Explicitly identified container command; its paths are Linux container paths |

Continue with [LE01](01-linux-basics/01-shell-navigation/guide.md).
