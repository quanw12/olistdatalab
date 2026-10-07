-- Supplied infrastructure; runs only when the owned source volume is first initialized.
CREATE TABLE public.stock (
 event_id TEXT PRIMARY KEY,
 sku TEXT NOT NULL CHECK(length(trim(sku)) > 0),
 units INTEGER NOT NULL CHECK(units >= 0)
);
INSERT INTO public.stock VALUES ('M1','p01',7),('M2','p01',3);
CREATE ROLE p5_cdc LOGIN REPLICATION PASSWORD 'p5_cdc_local_only';
GRANT CONNECT ON DATABASE p5_inventory TO p5_cdc;
GRANT USAGE ON SCHEMA public TO p5_cdc;
GRANT SELECT ON public.stock TO p5_cdc;
CREATE PUBLICATION p5_pub FOR TABLE public.stock;
