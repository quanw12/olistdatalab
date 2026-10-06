"""Day 6: fetch current weather from a public HTTP API through a CLI."""

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests


API_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_OUTPUT_PATH = Path("output") / "weather_api_response.json"


def parse_args():
    """Read CLI flags and return parsed arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch current weather from Open-Meteo.",
    )
    parser.add_argument("--city", default="Ho Chi Minh City")
    parser.add_argument("--latitude", type=float, default=10.8231)
    parser.add_argument("--longitude", type=float, default=106.6297)
    parser.add_argument("--timezone", default="Asia/Ho_Chi_Minh")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def fetch_current_weather(args):
    """Fetch current weather JSON and return it with request parameters."""
    # TODO 1: make a params dictionary for latitude, longitude, current and timezone.
    params = {
        "latitude": args.latitude,
        "longitude": args.longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": args.timezone,
    }
    # TODO 2: read WEATHER_TIMEOUT_SECONDS; use 10 seconds if it is missing.
    timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
    # TODO 3: request API_URL with requests.get, params and timeout.
    # Call response.raise_for_status(). Convert request errors to RuntimeError.
    try: 
        response =  requests.get(API_URL, params= params, timeout= timeout_seconds)
        response.raise_for_status()
    except requests.exceptions.RequestException as error: 
        raise RuntimeError(f"Weather request failed: {error}") from error
    # TODO 4: convert the response to JSON, check that current exists,
    # then return payload, params.
    payload = response.json()
    if "current" not in payload:
        raise ValueError("response has no current weather")
    return payload, params


def write_json(path, data):
    """Write raw API data and its request metadata to JSON."""
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=2)
        output_file.write("\n")


def main():
    args = parse_args()
    payload, params = fetch_current_weather(args)

    record = {
        "city": args.city,
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "request": params,
        "response": payload,
    }
    write_json(args.output, record)

    print(f"city: {args.city}")
    print(f"current weather: {payload['current']}")
    print(f"wrote: {args.output}")


if __name__ == "__main__":
    main()
