-- Supplied controlled mutation. NEW SOURCE ONLY, after making the archive.
BEGIN;
INSERT INTO restore_lab.batches VALUES
    ('b2', repeat('b',64), 2, '2026-10-01T07:00:00+00:00');
UPDATE restore_lab.current_items
SET units=99, version=3, batch_id='b2' WHERE item_id='A';
INSERT INTO restore_lab.current_items VALUES ('Z',7,1,FALSE,'b2');
COMMIT;
