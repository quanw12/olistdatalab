# Help — Container networks, service names and published ports

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Distinguish host and container network contexts.

</details>

<details>
<summary>Detailed approach</summary>

Use docker ps/docker logs to check the lab server before curl. Add --mount type=volume,src=le-storage,dst=/output,readonly to the run command and --directory /output to the server. From the probe, use python -c "import urllib.request; print(urllib.request.urlopen('http://le-web:8000/manifest.json', timeout=5).read().decode())". The network name resolves le-web inside that Docker network. Cleanup: docker stop le-web, then docker rm le-web. Do not remove the retained volume.

</details>

<details>
<summary>Troubleshooting</summary>

Serving / instead of /output can return a 404 for existing artifacts. A name-resolution error differs from an HTTP 404. Port allocation failure may come from the earlier local server still running.

</details>
