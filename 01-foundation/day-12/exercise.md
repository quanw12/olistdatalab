# Day 12 assignment

1. Complete model.md before writing SQL. The grain is one city at one instant for this single-provider fixture.
2. Complete schema.sql using its column specifications: create day12_mart, dim_city, dim_date, fact_weather. Use a transaction and keep public tables unchanged.
3. Run the provided fixture.sql once to load your empty model. It maps source_city_id to an independent city_key.
4. Run checks.sql A1–A6, then complete all questions in queries.sql.
5. Explain why UNIQUE(city_key, observation_date) is wrong when several observations occur on one day.

Continue your current schema.sql and model.md. Your unfinished work is preserved; this revision does not reset your implementation.
