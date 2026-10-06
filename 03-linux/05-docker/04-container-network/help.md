# Help — Container networks, service names and published ports

## First hint

Distinguish host and container network contexts.

## Detailed approach

Use docker ps/docker logs to check the lab server before curl. Add --mount type=volume,src=le-storage,dst=/output,readonly to the run command and --directory /output to the server. From the probe, use python -c "import urllib.request; print(urllib.request.urlopen('http://le-web:8000/manifest.json', timeout=5).read().decode())". The network name resolves le-web inside that Docker network. Cleanup: docker stop le-web, then docker rm le-web. Do not remove the retained volume.

## Troubleshooting

Serving / instead of /output can return a 404 for existing artifacts. A name-resolution error differs from an HTTP 404. Port allocation failure may come from the earlier local server still running.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
