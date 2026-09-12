"""Clean a small weather CSV and write valid records to output/."""

import csv
from collections import Counter
from datetime import date
from pathlib import Path


INPUT_PATH = Path("weather.csv")
OUTPUT_DIR = Path("output")
OUTPUT_PATH = OUTPUT_DIR / "clean.csv"


def clean_row(raw_row: dict[str, str]) -> tuple[dict[str, object] | None, str | None]:
    """Return a clean row, or None plus the reason it was rejected."""
    # TODO 1: validate city and observed_at.
    city = raw_row["city"].strip()
    observed_at = raw_row["observed_at"].strip()

    if not city:
        return None, "city is empty"
    try:
        date.fromisoformat(observed_at)
    except ValueError:
        return None, "observed_at is not YYYY-MM-DD"

    # TODO 2: convert temperature_c and humidity_pct to numeric values.
    try:
        temperature_c = float(raw_row["temperature_c"])
        humidity_pct = int(raw_row["humidity_pct"])
    except ValueError:
        return None, "temperature_c or humidity_pct is not numeric"
    # TODO 3: validate the allowed ranges from README.md.
    if not -50 <= temperature_c <= 60:
        return None, "temperature is out of boudary"
    if not 0 <= humidity_pct <= 100:
        return None, "humidtiyt_pct is out of boudary"
    # TODO 4: return a dictionary with city, observed_at, temperature_c, humidity_pct
    cleaned = {
        "city": city,
        "observed_at": observed_at,
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
    }
    return cleaned, None

def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    accepted_rows: list[dict[str, object]] = []
    rejection_reasons: Counter[str] = Counter()
    seen_keys: set[tuple[str, str]] = set()

    with INPUT_PATH.open(newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)

        for raw_row in reader:
            clean, rejection_reason = clean_row(raw_row)

            # TODO 5: invalid row -> count its reason, then skip to the next CSV row.
            if clean is None:
                if rejection_reason is not None:
                    rejection_reasons[rejection_reason] += 1
                continue

            # TODO 6: valid row -> make its key. If the key already exists, count it as duplicate.
            key = (str(clean["city"]), str(clean["observed_at"]))
            if key in seen_keys:
                rejection_reasons["duplicate city and observed_at"] += 1
                continue
            # TODO 7: only after it is valid and non-duplicate: save the key, then save the row.
            seen_keys.add(key)
            accepted_rows.append(clean)
            pass

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=["city", "observed_at", "temperature_c", "humidity_pct"],
        )
        writer.writeheader()
        writer.writerows(accepted_rows)

    print(f"accepted: {len(accepted_rows)}")
    print(f"rejected: {sum(rejection_reasons.values())}")
    print("rejection reasons:")
    for reason, count in rejection_reasons.most_common():
        print(f"- {reason}: {count}")


if __name__ == "__main__":
    main()
