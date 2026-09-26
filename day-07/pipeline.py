"""Day 7: turn a raw weather API record into a validated clean record."""

import argparse
import json
from datetime import datetime
from pathlib import Path


DEFAULT_INPUT_PATH = Path("raw_weather.json")
DEFAULT_OUTPUT_PATH = Path("output") / "weather_clean.json"
CHECK_COUNT = 5


def parse_args():
    """Read input and output paths from the command line."""
    parser = argparse.ArgumentParser(
        description="Build a clean weather record from raw JSON.",
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def load_json(path):
    """Read one JSON file into a Python dictionary."""
    with path.open(encoding="utf-8") as source_file:
        return json.load(source_file)


def build_clean_record(raw):
    """Return a new clean weather record from raw API data."""
    # TODO 1: get response and current from nested raw JSON.
    response = raw["response"]
    current = response["current"]
    temperature_c = float(current["temperature_2m"])
    humidity_pct = int(current["relative_humidity_2m"])
    # TODO 2: return the seven fields in README.md's output contract.
    record = {
        "city": raw["city"],
        "requested_at": raw["requested_at"], 
        "observed_at": current["time"], 
        "timezone": response["timezone"],
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
        "source": "open-meteo",
    }
    return record


def validate_record(record):
    """Return all data-contract failures; return an empty list if valid."""
    # TODO 3: create errors and run the five quality checks from guide.md.
    errors = []

    if not record["city"]:
        errors.append("city is empty")
    
    try:
        datetime.fromisoformat(record["observed_at"])
    except ValueError:
        errors.append("observed_at is not ISO datetime")
    
    if not record["timezone"]:
        errors.append("timezone is empty")

    if not -50 <= record["temperature_c"] <= 60:
        errors.append("temperature_c is outside allowed range")
    if not 0 <= record["humidity_pct"] <= 100:
        errors.append("humidity_pct is outside allowed range")
    return errors


def write_json(path, data):
    """Write a validated clean record to JSON."""
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=2)
        output_file.write("\n")


def main():
    args = parse_args()
    raw = load_json(args.input)
    clean_record = build_clean_record(raw)
    errors = validate_record(clean_record)

    if errors:
        raise ValueError("; ".join(errors))

    write_json(args.output, clean_record)
    print(f"checks passed: {CHECK_COUNT}")
    print(f"wrote: {args.output}")


if __name__ == "__main__":
    main()
