# Build an image and control its command

## Concept and purpose

A Dockerfile is a build recipe. FROM selects a base; WORKDIR sets the working directory; COPY takes files from the build context; RUN executes at image build time. ENTRYPOINT names the executable contract, while CMD supplies default arguments that docker run can replace.

Exec-form JSON arrays pass arguments directly instead of invoking a shell. Shell variable expansion does not happen automatically there. The build context controls what files are eligible to copy; .dockerignore limits that context. Gitignore alone does not keep secrets out of images.

Rebuild after source changes. The image tag is a local name; record its ID/base digest. Use a small standard-library app so packaging can be understood before adding dependency management or image publishing.

## Syntax example — Dockerfile syntax; save only to a scratch file for the example

~~~dockerfile
FROM python:3.12-slim
WORKDIR /demo
RUN mkdir -p /results
ENTRYPOINT ["python", "-c"]
CMD ["print('image example')"]
~~~

## Trace the example

The default container runs a Python expression. Supplying a different final argument replaces CMD while keeping ENTRYPOINT.

## Apply it to Data Engineering

Package a known program and its interface so another machine can run the same fixture without your Windows venv.

[Reference](https://docs.docker.com/reference/dockerfile/). These explanations and exercises are original course material.
