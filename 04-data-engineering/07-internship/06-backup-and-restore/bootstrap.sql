-- Supplied setup. Run ONCE on your NEW disposable source database only.
-- Existing restore_lab causes failure rather than silently modifying prior work.
BEGIN;
CREATE SCHEMA restore_lab;
CREATE TABLE restore_lab.batches (
    batch_id TEXT PRIMARY KEY,
    source_checksum TEXT NOT NULL CHECK (length(source_checksum) = 64),
    accepted_count INTEGER NOT NULL CHECK (accepted_count >= 0),
    applied_at TIMESTAMPTZ NOT NULL
);
CREATE TABLE restore_lab.current_items (
    item_id TEXT PRIMARY KEY,
    units INTEGER NOT NULL CHECK (units >= 0),
    version INTEGER NOT NULL CHECK (version > 0),
    is_deleted BOOLEAN NOT NULL,
    batch_id TEXT NOT NULL REFERENCES restore_lab.batches(batch_id)
);
INSERT INTO restore_lab.batches VALUES
    ('b1', repeat('a',64), 4, '2026-10-01T06:00:00+00:00');
INSERT INTO restore_lab.current_items VALUES
    ('A',12,2,FALSE,'b1'), ('B',3,1,FALSE,'b1'),
    ('C',0,3,TRUE,'b1'), ('D',5,1,FALSE,'b1');
COMMIT;
