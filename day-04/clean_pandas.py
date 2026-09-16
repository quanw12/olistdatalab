"""Day 4: clean a weather CSV with column-oriented pandas operations."""

from pathlib import Path

import pandas as pd


INPUT_PATH = Path("messy_weather.csv")
OUTPUT_PATH = Path("output") / "clean_weather.csv"


def clean_weather(raw_df):
    """Return clean rows plus counts for invalid and duplicate rows."""
    # TODO 1: copy raw_df and strip spaces from the city column.
    raw_df = raw_df.copy() # copy() giúp hàm an toàn hơn raw_df bên ngoài hàm vẫn giữ dữ liệu gốc để kiểm tra hoặc dùng tiếp.
    raw_df["city"] = raw_df["city"].str.strip()
    # TODO 2: convert observed_at, temperature_c and humidity_pct.
    # Use errors="coerce" so invalid values become missing values.
    raw_df["observed_at"] = pd.to_datetime(raw_df["observed_at"], format = "%Y-%m-%d" ,errors="coerce")
    raw_df["temperature_c"] = pd.to_numeric(raw_df["temperature_c"], errors="coerce")
    raw_df["humidity_pct"] = pd.to_numeric(raw_df["humidity_pct"], errors="coerce")
    # TODO 3: create valid_rows for city, date, temperature and humidity.
    # Count invalid rows and create candidate_df containing only valid rows.
    valid_rows = (
        raw_df["city"].notna()
        & raw_df["observed_at"].notna()
        & raw_df["temperature_c"].between(-50, 60)
        & raw_df["humidity_pct"].between(0, 100)
    )
    # TODO 4: remove duplicates by city + observed_at, format observed_at
    # back to YYYY-MM-DD text, then return clean_df, invalid_rows, duplicate_rows.
    invalid_rows = int((~valid_rows).sum())
    candidate_df = raw_df.loc[valid_rows].copy()
    before_deduplicate = len(candidate_df)
    clean_df = candidate_df.drop_duplicates(
        subset =["city", "observed_at"], 
        keep = "first",
    ).copy()
    duplicate_rows = before_deduplicate - len(clean_df)
    clean_df["observed_at"] = clean_df["observed_at"].dt.strftime("%Y-%m-%d")
    return clean_df, invalid_rows, duplicate_rows


def main():
    raw_df = pd.read_csv(INPUT_PATH)
    # print(raw_df.head())
    # print(raw_df.dtypes)
    # print(raw_df.info())

    clean_df, invalid_rows, duplicate_rows = clean_weather(raw_df)

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    clean_df.to_csv(OUTPUT_PATH, index=False)

    print(f"input rows: {len(raw_df)}")
    print(f"invalid rows: {invalid_rows}")
    print(f"duplicate rows: {duplicate_rows}")
    print(f"accepted rows: {len(clean_df)}")
  

if __name__ == "__main__":
    main()
