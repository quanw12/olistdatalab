-- In pgAdmin Query Tool, highlight and execute one SELECT at a time.
-- Expected: city_count = 2, observation_count = 3.
SELECT COUNT(*) AS city_count FROM cities;
SELECT COUNT(*) AS observation_count FROM weather_observations;

-- Expected: 0 for both counts.
SELECT COUNT(*) AS bad_temperature_count
FROM weather_observations
WHERE temperature_c NOT BETWEEN -50 AND 60;

SELECT COUNT(*) AS bad_humidity_count
FROM weather_observations
WHERE humidity_pct NOT BETWEEN 0 AND 100;

-- Timestamps may display in UTC depending on the connection's session timezone.
SELECT city_id, observed_at, temperature_c, humidity_pct, source
FROM weather_observations
ORDER BY city_id, observed_at;
