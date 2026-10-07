# DE28 acceptance

Require actual native-server evidence for backup, archive inspection, restoration,
value/constraint checks and measured duration. Syntax-only evidence is insufficient.

<details>
<summary>After an attempt — baseline and recovery point</summary>

The baseline has four items, three active items, 20 active units and one batch.
C remains a version-3 deletion marker. The restored target contains that baseline,
including units A=12. It excludes the later A=99/version-3 update, item Z and batch b2.
The mutated source has five items, four active items, 114 active units and two batches.

Primary keys, nonnegative units, positive versions and batch references still reject
invalid writes. A valid stock report runs after rolling back the constraint probes.
These totals apply to the supplied fixture, not your independent variation.

</details>

State that a logical single-database restore with --no-owner/--no-acl does not
recreate cluster roles/grants or supply continuous/PITR recovery. Report measured
duration honestly; no required universal timing target is imposed.
