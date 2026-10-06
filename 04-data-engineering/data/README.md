# Original fixtures

b1 has A v1=1000 and B v1=1500. b2 has A v2=1200, B v2 tombstone and C v1=800. Source version is authoritative, with consistent equal-version content. updated_at is source availability/change time; occurred_at groups business events. b2's late C belongs to Sep 1 but arrives Sep 2. Preserve all_changes history for point-in-time reconstruction. No currency/PII or real transactions are represented.

Current active truth after b1: 2 orders/2500 cents. After b2: A and C, 2 orders/2000 cents. Keep B's tombstone in current state. Same timestamp ties use IDs under the DE09 source-order assumption. A real change feed can require another ordering key.

The dbt seed is the same five change rows. Parceled delivery fixtures use a different schema for the independent DE26 diagnostic; read its specification first.

