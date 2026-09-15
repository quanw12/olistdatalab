"""Day 3: transform an API-shaped JSON weather response into one clean record."""

import json
from datetime import datetime, timezone
from pathlib import Path


INPUT_PATH = Path("weather_response.json")
SETTINGS_PATH = Path("settings.json")
OUTPUT_PATH = Path("output") / "weather_snapshot.json"


def load_json(path):
    """Read a JSON file and return its Python dictionary."""
    with path.open(encoding="utf-8") as source_file:
        return json.load(source_file)


def write_json(path, data):
    """Write one dictionary to JSON, making its parent folder if necessary."""
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=2)
        output_file.write("\n")


def log_event(event, details):
    """Print one structured JSON log record."""
    record = {
        "event": event,
        "logged_at": datetime.now(timezone.utc).isoformat(),
        "details": details,
    }
    print(json.dumps(record, ensure_ascii=False))


def build_snapshot(payload, settings):
    """Return one clean weather record from a response and its configuration."""
    # TODO 1: get the nested current object from payload.
    current = payload["current"]
    # TODO 2: parse current["time"] with datetime.fromisoformat.
    observed_at = datetime.fromisoformat(current["time"]).isoformat()
    # TODO 3: extract temperature_c as float and humidity_pct as int.
    try: 
        temperature_c = float(current["temperature_2m"])
        humidity_pct = int(current["relative_humidity_2m"])
    except ValueError:
        raise ValueError("extract unsuccessfully")
    # TODO 4: raise ValueError if temperature_c is outside configured bounds.
    if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
        raise ValueError("temperature_c is outside configured range")
    # TODO 5: return a dictionary with city, observed_at, timezone,
    # temperature_c, humidity_pct and source.
    snapshot = {
        "city": settings["city"],
        "observed_at": observed_at,
        "timezone": payload["timezone"],
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
        "source": settings["source"]
    }
    return snapshot
  


def main():
    settings = load_json(SETTINGS_PATH)
    payload = load_json(INPUT_PATH)
    snapshot = build_snapshot(payload, settings)

    write_json(OUTPUT_PATH, snapshot)
    log_event(
        "snapshot_written",
        {
            "city": snapshot["city"],
            "observed_at": snapshot["observed_at"],
        },
    )


if __name__ == "__main__":
    main()
