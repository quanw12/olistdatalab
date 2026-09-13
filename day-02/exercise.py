"""Day 2: summarize weather rows that have already passed cleaning."""
import csv
from collections import Counter
from datetime import date
from pathlib import Path

WEATHER_ROWS = [
    {"city": "Hanoi", "observed_at": "2026-08-01", "temperature_c": 31.2},
    {"city": "Da Nang", "observed_at": "2026-08-01", "temperature_c": 30.1},
    {
        "city": "Ho Chi Minh City",
        "observed_at": "2026-08-01",
        "temperature_c": 32.0,
    },
    {"city": "Hanoi", "observed_at": "2026-08-02", "temperature_c": 33.4},
    {"city": "Da Nang", "observed_at": "2026-08-02", "temperature_c": 29.8},
]


def summarize_weather(rows):
    """Return a small report for already-clean weather rows."""
    # TODO 1: create an empty list named temperatures.
    temperatures = []
    # TODO 2: create an empty set named cities.
    cities = set()
    # TODO 3: loop through rows. In each loop, get city and temperature_c from row.
    # TODO 4: add the city to cities and temperature_c to temperatures.
    for row in rows: 
        cities.add(row["city"])
        temperatures.append(row["temperature_c"])
    # TODO 5: calculate lowest_temperature, highest_temperature and average_temperature.
    lowest_temperature = min(temperatures)
    highest_temperature = max(temperatures)
    average_temperature = round(sum(temperatures) / len(temperatures), 1) 

    # TODO 6: return one dictionary with these keys:
    # row_count, cities, temperature_min_c, temperature_max_c, temperature_avg_c.
    result = {
        "row_count": len(row), 
        "cities": sorted(cities), # sort lại vì set không đảm bảo thứ tự nên sắp xếp để output luôn ổn định
        "temperature_min_c": lowest_temperature, 
        "temperature_max_c": highest_temperature,
        "temperature_avg_c": average_temperature,
    }
    return result

def print_summary(summary):
    """Print a report dictionary in a readable format."""
    city_text = ", ".join(summary["cities"])
    print(f"rows: {summary['row_count']}")
    print(f"cities: {city_text}")
    print(f"temperature min: {summary['temperature_min_c']} C")
    print(f"temperature max: {summary['temperature_max_c']} C")
    print(f"temperature avg: {summary['temperature_avg_c']} C")


def main():
    summary = summarize_weather(WEATHER_ROWS)
    print_summary(summary)


if __name__ == "__main__":
    main()
