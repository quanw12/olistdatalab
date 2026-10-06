# Day 18 — Docker and Linux CLI from the beginning


## What Docker adds

An image is a template containing a program and its dependencies. A container is an instance running from that image. A container has its own filesystem/network view; its writable layer is not your database backup. A named volume retains data separately from the container.

Docker Desktop runs Linux containers on Windows. Install it using [the Windows guide](https://docs.docker.com/desktop/setup/install/windows-install/) and its WSL2 prerequisites, start Desktop, then check docker version. A client-only response with a server connection error means the engine is not ready. Do not change your existing local PostgreSQL installation.

## First commands

~~~powershell
docker version
docker run --rm hello-world
docker run --rm -it alpine:3.22 sh
~~~

Inside the Alpine shell, type these one at a time:

~~~sh
pwd
ls
mkdir -p /tmp/practice
printf 'hello\n' > /tmp/practice/note.txt
cat /tmp/practice/note.txt
ls /tmp/practice | sort
exit
~~~

pwd shows your directory; ls lists entries; mkdir creates directories; cat reads a file. The slash is the Linux path separator. > redirects output into a file; | passes output to another program. --rm removes this disposable container after exit, so the practice file disappears. The terminal is now back in PowerShell. Do not assume PowerShell and Linux shell quoting are identical.

## Ports and persistence

PostgreSQL listens on5432 inside its container. We bind host127.0.0.1:5433 to container5432, leaving local PostgreSQL on5432. From pgAdmin/host Python use localhost:5433. A separate Compose app will later use db:5432.

For PostgreSQL 18, mount the data volume at /var/lib/postgresql. The image uses a version-specific data directory beneath it. Do not follow old version17 examples mounting only /var/lib/postgresql/data. Read [the PostgreSQL container guide](https://docs.docker.com/guides/postgresql/).

Create capstone/.env yourself, containing POSTGRES_DB=weather_course, POSTGRES_USER=de_student, and POSTGRES_PASSWORD with a password you choose. This file is ignored. It is passed explicitly by --env-file; ordinary Python does not automatically read it.

~~~powershell
docker volume create de30_pg18
docker run -d --name de30-pg --env-file .env -p 127.0.0.1:5433:5432 -v de30_pg18:/var/lib/postgresql postgres:18
docker logs de30-pg
docker exec de30-pg pg_isready -U de_student -d weather_course
~~~

These commands are executed from capstone after you create .env. The image initializes credentials/database only on a new empty volume; editing .env later does not change an existing database password.

## Connect and bootstrap

In pgAdmin register a new server label Course Docker; connection hostlocalhost, port 5433, userde_student, databaseweather_course, password from .env. Run your saved staging.sql and mart.sql (including ops state DDL) once in this fresh database.

In the host Python terminal set PGPORT=5433, PGDATABASE=weather_course, PGUSER=de_student and prompt for its password using setup.md. This is a new empty database, not an automatic copy of your native database.
