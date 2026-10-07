# Help — Native PostgreSQL with Psycopg

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

The lesson shows the SQL shape. Your task is binding the row data and managing contexts correctly.

</details>

<details>
<summary>Detailed approach</summary>

Enter with connection.transaction(): then with connection.cursor() as cursor:. Build [(row['order_id'], row['city'], row['amount_cents'], row['updated_at']) for row in rows]. Pass the SQL and that list as separate executemany arguments. Let errors escape the context. Native PostgreSQL supports TIMESTAMPTZ comparison, unlike arbitrary unnormalized timestamp text.

</details>

<details>
<summary>Troubleshooting</summary>

A missing psycopg import affects the live checker only. Authentication/connection errors are environment issues. A passing fake check does not verify SQL syntax or actual rollback.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>
