"""Provided instrumentation. Run after implementing exercise.py."""
import time
import baseline
import exercise

products = [{'sku': f'p{i}', 'category': f'c{i % 8}'} for i in range(400)]
rows = [{'sku': f'p{i % 400}', 'units': i % 20} for i in range(20000)]
for label, function in [('baseline', baseline.enrich_movements), ('candidate', exercise.enrich_movements)]:
    start = time.perf_counter()
    result = function(rows, products)
    print(label, f'{time.perf_counter() - start:.6f}s', 'rows:', len(result))
