CREATE TABLE entity_state(
 event_id TEXT PRIMARY KEY, sku TEXT NOT NULL, observed_at TEXT NOT NULL,
 version INTEGER NOT NULL, units INTEGER NOT NULL, op TEXT NOT NULL
);
CREATE TABLE message_ledger(
 topic TEXT NOT NULL, partition_id INTEGER NOT NULL, offset_id INTEGER NOT NULL,
 payload_sha TEXT NOT NULL, PRIMARY KEY(topic, partition_id, offset_id)
);
