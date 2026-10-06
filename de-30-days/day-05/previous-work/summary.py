"""Day 5: enrich clean weather data and summarize it by city."""

from pathlib import Path

import pandas as pd


WEATHER_PATH = Path("weather_clean.csv")
CITY_PATH = Path("city_lookup.csv")
OUTPUT_PATH = Path("output") / "city_weather_summary.csv"


def build_summary(weather_df, city_df):
    """Return a validated weather report grouped by region and city."""
    # TODO 1: merge weather_df and city_df on city.
    # Use how="left" and validate="many_to_one".
    enriched_df = weather_df.merge(
        city_df,
        on= "city",
        how= "left",
        validate= "many_to_one",
    )
    # TODO 2: detect and reject rows whose region is missing after merge.
    missing_region = enriched_df["region"].isna()
    if missing_region.any():
        unknown_cities = enriched_df.loc[missing_region, "city"].unique()
        raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
    # TODO 3: group by region and city, then aggregate:
    # observation_count, avg_temperature_c, min_temperature_c,
    # max_temperature_c and avg_humidity_pct.
    summary_df = ( enriched_df.groupby(["region", "city"], as_index=False)
        .agg(
            observation_count=("observed_at", "count"),
            avg_temperature_c=("temperature_c", "mean"),
            min_temperature_c=("temperature_c", "min"),
            max_temperature_c=("temperature_c", "max"),
            avg_humidity_pct=("humidity_pct", "mean"),
        )
    )

    # TODO 4: round averages, sort, validate total observation_count,
    summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
    summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)

    summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop = True)

    if summary_df["observation_count"].sum() != len(enriched_df):
        raise ValueError("summary observation count does not match input rows")
    # then return summary_df.
    return summary_df


def main():
    weather_df = pd.read_csv(WEATHER_PATH)
    city_df = pd.read_csv(CITY_PATH)
    summary_df = build_summary(weather_df, city_df)

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    summary_df.to_csv(OUTPUT_PATH, index=False)

    print(f"weather rows: {len(weather_df)}")
    print(f"city lookup rows: {len(city_df)}")
    print(f"summary rows: {len(summary_df)}")
    print(summary_df.to_string(index=False))


if __name__ == "__main__":
    main()
