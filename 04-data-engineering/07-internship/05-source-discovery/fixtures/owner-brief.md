# Lab owner's clarification — read after listing your questions

Warehouse Operations owns this synthetic snapshot-change feed. One logical version
describes an item at a site. Identity is item_id + site_id; version increases for it.
A later version replaces stock, rather than adding it. Exact replay is allowed;
equal-version differing content requires investigation and blocks publication.
Deletion/completeness guarantees remain open questions; there is no deletion sample.

observed_at is the measurement instant with an offset. units is integer stock,
not money or a movement amount. Zero is valid. Malformed values require investigation/
quarantine, not zero substitution. The sample deliberately includes defects.

Refresh is intended daily, but delivery SLA and missing-file detection are unconfirmed.
Lab policy: retain raw data seven days with restricted engineering access. Omit
contact_email from reports. Confirm actual privacy/retention rules with the owner
in a real system; these lab decisions are not legal guidance.
