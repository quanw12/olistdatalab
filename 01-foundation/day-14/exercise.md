# Day 14 — Mini-project 2: a reusable loader and SQL mart


Build the capstone package. Implement the load subcommand, load_records(connection, rows), and refresh_mart(connection, cities). Read city configuration from ../data/cities.csv. Load normalized input into staging and refresh dimensions/facts in one transaction.

Write bootstrap SQL for a fresh database. On existing weather_course, create only the missing mart objects; staging already exists. Add sql/report.sql for a city report retaining Hue. Repeat the load and prove no duplication. Document the package and bootstrap order in capstone/README.md.
