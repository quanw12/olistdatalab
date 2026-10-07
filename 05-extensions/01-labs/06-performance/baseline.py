"""Provided slow baseline for valid, unique-dimension inputs only."""
def enrich_movements(rows, products):
    result = []
    for row in rows:
        copy = dict(row)
        copy['category'] = None
        for product in products:
            if row['sku'].strip() == product['sku'].strip():
                copy['category'] = product['category']
                break
        result.append(copy)
    return result
