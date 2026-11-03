---
tags: [decourse, security, governance]
module: 21
---

# Security and Governance

> [!info] Learning goals
> After this note you can: apply least privilege to pipeline principals; design and test a permission matrix with both allowed and denied actions; handle secrets safely; protect personal data (PII) with removal, masking and pseudonymisation, and know the limits of hashing; and describe the minimum governance a dataset needs (owner, definitions, retention, change process, lineage).

## 1. Why security belongs in the pipeline

Data platforms concentrate valuable information: customer addresses, payments, reviews. A leaked credential or an over-privileged account exposes everything. Security and governance are designed together with the pipeline, not added before an audit.

Principles:

- **Least privilege:** each principal (person, service account, tool) gets exactly the access it needs, nothing more.
- **Separation of duties:** the account that ingests raw data is not the one dashboards use.
- **Defence in depth:** network limits + authentication + authorisation + masking + monitoring.
- **Verify, don't assume:** "I ran the GRANT" is not evidence; a failed INSERT as the reader is.

## 2. Permission matrix

| Principal | Raw | Staging/Marts | DDL | Secrets |
|---|---|---|---|---|
| Ingest writer | write the needed sources | none | in its scope | source credentials |
| Transform writer (dbt) | read | write | transform schemas | warehouse credentials |
| BI reader | **none** | read allowed marts | none | read-only credential |
| Human analyst | none (or masked views) | read | none | personal login (SSO) |

```sql
-- PostgreSQL lab pattern; replace role names with the lab accounts you created. Run as an admin.
GRANT USAGE ON SCHEMA marts TO analyst_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA marts TO analyst_reader;
REVOKE ALL ON SCHEMA bronze FROM analyst_reader;
REVOKE ALL ON SCHEMA bronze FROM PUBLIC;
```

Gotchas:

- `REVOKE` from one role does not remove privileges the user inherits from another role or from `PUBLIC`.
- Grants on existing tables do not cover future tables; use default privileges and re-test after every publish (DROP/CREATE drops grants) — see [[Docker PostgreSQL and Serving]].
- Test with the real login: SELECT on the mart succeeds; INSERT, and SELECT on raw, fail. Keep both positive and negative tests in CI where possible.

In the cloud the same ideas use IAM: service accounts per pipeline, predefined roles such as BigQuery Data Viewer on a dataset (not project Owner), and no long-lived keys when workload identity is available ([[GCP BigQuery Terraform and Cost]]).

## 3. Secrets

- Credentials come from environment variables or a secret manager (GCP Secret Manager, Vault, GitHub Actions secrets), never from code.
- `.env` is in `.gitignore`; `.env.example` holds placeholders only.
- Never log a DSN or URL containing a password; redact headers.
- Terraform state can contain secrets: store it in a protected remote backend, never in Git.
- If a secret leaks (commit, log, screenshot), **rotate it immediately**; deleting the commit is not enough.
- Do not paste raw data or secrets into hosted AI tools just because the API works ([[Learning with AI]]).

## 4. Personal data (PII)

PII is anything that identifies a person directly (name, email, phone, CPF) or indirectly (zip code + birth date, free-text reviews mentioning names). Olist anonymised much of its data, but reviews are free text and can still contain personal details.

| Technique | What it does | Limits |
|---|---|---|
| Removal | Do not copy the column past raw | Best default if nobody needs it |
| Masking | `j***@mail.com`, last 4 digits | Partial data may still identify |
| Pseudonymisation | Replace with a token/keyed hash | Still personal data if re-linkable |
| Aggregation | Report counts, not rows | Small groups can still identify people |
| Access control | Restrict who sees raw PII | Requires discipline and audits |

```python
# runnable
import hashlib
import hmac

def pseudonymise(value: str, key: bytes) -> str:
    return hmac.new(key, value.strip().lower().encode(), hashlib.sha256).hexdigest()[:16]

key = b"load-from-a-secret-manager"      # never hard-code a real key
a = pseudonymise("Maria@Example.com", key)
assert a == pseudonymise(" maria@example.com", key)     # stable: joins still work
assert a != pseudonymise("maria@example.com", b"other-key")

# Why an unkeyed hash is weak: a dictionary of likely values reverses it.
plain = hashlib.sha256(b"maria@example.com").hexdigest()
guesses = {hashlib.sha256(e.encode()).hexdigest(): e for e in ["joao@example.com", "maria@example.com"]}
assert guesses[plain] == "maria@example.com"
```

Hashing does not make data anonymous: emails, phone numbers and CPFs come from small, guessable spaces. A keyed hash (HMAC) with a secret key resists dictionary attacks, but the result is still personal data under laws like the GDPR and Brazil's LGPD.

In the labs, use **fake PII**: add a fake email column to raw, then prove it is removed or masked before the mart, the logs and any AI calls.

## 5. Governance: the minimum

For each published dataset, record:

- name, **owner**, source, **grain**, metric definitions;
- schema version and **change process** (who approves, how consumers are notified, deprecation window);
- **retention** (how long raw and marts are kept, and deletion on request);
- freshness promise and quality checks;
- classification (public / internal / confidential / PII).

**Lineage** shows which downstream assets a change affects; it supports impact analysis but does not replace data tests. A schema change such as renaming a column needs an owner's decision, a notice to consumers, a transition period (both columns, or a view keeping the old name) and then removal.

## 6. Applying it to Olist

Module 21: reader/writer roles with positive and negative tests, fake PII removed before the mart and logs, secrets only from env/secret store, and permission tests re-run after each publish.

## 7. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| One admin credential everywhere | Total exposure on leak | Separate principals, least privilege |
| Testing only that access works | Over-privilege unnoticed | Negative tests (must fail) |
| Secrets in code, logs or state in Git | Leak | Secret manager, redaction, remote state |
| "It's hashed so it's anonymous" | Re-identification | Keyed hashes, minimisation, access control |
| Renaming columns without notice | Broken consumers | Change process with deprecation |
| PII flowing to AI tools | Compliance breach | Approved data only, minimise fields |

## 8. Exercises

1. Prove: the reader can SELECT a mart; INSERT and reading raw fail. Re-run after a publish.
2. Add a fake email column; show it never reaches the dashboard or the logs.
3. Write the change process for renaming `payment_total` to `payment_amount_brl`.
4. Find a secret in your shell history or logs (fake one) and describe the rotation steps.

## 9. Review questions

> [!question]- Why must permission tests include denied actions?
> Allowed-only tests cannot detect over-privilege; proving that writes and raw reads fail is what demonstrates least privilege.

> [!question]- Does hashing an email anonymise it?
> No. Unkeyed hashes of guessable values can be reversed with a dictionary; even keyed hashes remain personal data because they can be linked.

> [!question]- What should you do when a secret is committed?
> Rotate it immediately, then remove it from history if required, and check logs for misuse.

> [!question]- What is the minimum governance for a dataset?
> Owner, source, grain, definitions, schema version and change process, retention, freshness promise, quality checks and classification.

Related: [[Docker PostgreSQL and Serving]], [[LLM Caching Evaluation and Guardrails]], [[Delivery and Reproducibility]], [[Module 21 - Security and Delivery]]. Sources: [PostgreSQL privileges](https://www.postgresql.org/docs/current/ddl-priv.html), [GCP service account best practices](https://cloud.google.com/iam/docs/best-practices-service-accounts), [OWASP secrets management cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
