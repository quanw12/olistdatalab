"""Deliberately incomplete coverage: reproduce before repairing in exercise.py."""
from datetime import datetime, timedelta

def full_chunks_only(start, end, days):
    cursor, stop = datetime.fromisoformat(start), datetime.fromisoformat(end)
    result = []
    while cursor + timedelta(days=days) <= stop:
        next_end = cursor + timedelta(days=days)
        result.append((cursor.isoformat(), next_end.isoformat()))
        cursor = next_end
    return result
