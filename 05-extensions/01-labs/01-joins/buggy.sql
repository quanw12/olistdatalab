-- Deliberately faulty reproduction; this is not the student answer.
SELECT p.product_id, COALESCE(SUM(m.units), 0) AS total_units,
       COUNT(m.event_id) AS event_count
FROM products p
LEFT JOIN movements m ON m.product_id = p.product_id
LEFT JOIN audits a ON a.event_id = m.event_id
GROUP BY p.product_id ORDER BY p.product_id;
