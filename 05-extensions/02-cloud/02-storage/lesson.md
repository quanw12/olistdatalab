# CL02 — Learn

## An object is identified by bucket and key

Cloud Storage is object storage, not a shared local filesystem. Slashes in an object name organize names; they do not grant filesystem transaction semantics. Build a deterministic key from a stable batch ID. Do not use the current clock to identify a replayed batch.

## Syntax — Python SDK boundary

~~~python
from google.cloud import storage
bucket = storage.Client().bucket(bucket_name)
blob = bucket.blob(key)
blob.upload_from_filename(local_path, if_generation_match=0)
~~~
The zero generation precondition requests create-only behavior. If the object exists, verify identity/content or fail; do not blindly overwrite raw data. An object generation identifies a stored version. [Upload documentation](https://docs.cloud.google.com/storage/docs/uploading-objects).

The offline function only validates/builds a name. It proves no remote permissions, checksum or upload behavior. Live evidence adds those boundaries. Keep an input digest in your manifest and compare it on replay.

[Assignment](exercise.md) · [Hints](help.md)
