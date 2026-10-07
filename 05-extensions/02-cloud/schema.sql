-- Supplied infrastructure for YOUR OWN learning dataset.
-- Replace YOUR_PROJECT_ID in your copy before running in BigQuery.
CREATE TABLE IF NOT EXISTS `YOUR_PROJECT_ID.p5_inventory.history` (
 event_id STRING NOT NULL,
 sku STRING NOT NULL,
 observed_at TIMESTAMP NOT NULL,
 version INT64 NOT NULL,
 units INT64 NOT NULL,
 op STRING NOT NULL
);
CREATE TABLE IF NOT EXISTS `YOUR_PROJECT_ID.p5_inventory.current` (
 event_id STRING NOT NULL,
 sku STRING NOT NULL,
 observed_at TIMESTAMP NOT NULL,
 version INT64 NOT NULL,
 units INT64 NOT NULL,
 op STRING NOT NULL
);
