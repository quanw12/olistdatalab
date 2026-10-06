# Day 18 — Docker and Linux CLI from the beginning


1. If docker is unrecognized, finish installation and reopen the terminal. If only the client is reachable, open Docker Desktop and wait for its engine.
2. Run the small Alpine shell exercise first; exit returns to PowerShell. A Windows C:\ path is not an absolute Linux path.
3. Open a new .env in capstone and type only the three POSTGRES variables. Confirm git check-ignore .env reports it ignored.
4. Run the single-line docker run command. If the name exists, inspect docker ps -a and docker logs de30-pg; do not blindly create a second DB. If5433 is occupied, inspect the existing service before choosing another port and document any change.
5. Wait until pg_isready reports accepting connections. Register a NEW pgAdmin server on5433; do not silently edit your native server's settings.
6. Bootstrap the empty database, set host Python PG variables, then run the loader. A missing table means SQL bootstrap was skipped.
7. Run docker stop de30-pg, then docker start de30-pg. Reconnect and count. The same named volume retains data.
8. Changing a port changes how you reach a server, not what is stored in it. Show current_database() and server port if you accidentally query the wrong one.
