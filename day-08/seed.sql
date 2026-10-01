-- Run once after completing schema.sql, on a fresh weather_day08 database.
INSERT INTO cities (city_name, timezone_name)
VALUES
    ('Hanoi', 'Asia/Ho_Chi_Minh'),
    ('Da Nang', 'Asia/Ho_Chi_Minh');

-- On the fresh database above, identity values are Hanoi=1, Da Nang=2.
INSERT INTO weather_observations
    (city_id, observed_at, requested_at, temperature_c, humidity_pct, source)
VALUES
    (1, '2026-09-18T11:30:00+07:00', '2026-09-18T04:31:14+00:00', 30.7, 72, 'open-meteo'),
    (1, '2026-09-18T12:30:00+07:00', '2026-09-18T05:31:14+00:00', 31.2, 70, 'open-meteo'),
    (2, '2026-09-18T11:30:00+07:00', '2026-09-18T04:31:14+00:00', 29.8, 79, 'open-meteo');
