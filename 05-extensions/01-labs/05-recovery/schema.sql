CREATE TABLE items(item_id TEXT PRIMARY KEY, units INTEGER NOT NULL CHECK(units >= 0));
CREATE TABLE ledger(batch_id TEXT PRIMARY KEY, payload_sha TEXT NOT NULL);
