# CL03 — Learn

## Own job behavior

A job receives arguments/configuration, does bounded work and exits. Success is an exit code of zero after required operations finish. Exceptions/nonzero exits make failed work visible to the scheduler. A retry repeats execution; it does not reverse a partial write.

## Syntax — CLI and container

~~~python
import os
batch_id = os.environ["BATCH_ID"]
~~~
~~~dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY worker.py .
ENTRYPOINT ["python", "worker.py"]
~~~
This shows the image recipe syntax, not the completed worker. Choose dependencies/interpreter deliberately; record the built image digest. Cloud job configuration is separate from environment variables. One task limits parallelism inside one execution; it does not lock out another execution. [Task/job behavior](https://docs.cloud.google.com/run/docs/create-jobs).

[Assignment](exercise.md) · [Hints](help.md)
