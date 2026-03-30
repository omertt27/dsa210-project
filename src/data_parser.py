"""
data_parser.py
--------------
Parses Apple Health XML export (export.xml) and extracts:
- Sleep duration per night
- Step count per day
- Exercise minutes per day
- Resting heart rate per day

Usage:
    python src/data_parser.py --input data/raw/export.xml --output data/processed/health_data.csv
"""

import xml.etree.ElementTree as ET
import pandas as pd
import argparse
from datetime import datetime


def parse_health_export(xml_path: str) -> pd.DataFrame:
    """Parse Apple Health export.xml and return a daily summary DataFrame."""
    print(f"Parsing Apple Health export: {xml_path}")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    records = []
    for record in root.findall("Record"):
        rec_type = record.attrib.get("type", "")
        value = record.attrib.get("value", None)
        start_date = record.attrib.get("startDate", None)

        if rec_type in (
            "HKCategoryTypeIdentifierSleepAnalysis",
            "HKQuantityTypeIdentifierStepCount",
            "HKQuantityTypeIdentifierAppleExerciseTime",
            "HKQuantityTypeIdentifierRestingHeartRate",
        ):
            records.append({
                "type": rec_type,
                "value": value,
                "start_date": start_date,
            })

    df = pd.DataFrame(records)
    if df.empty:
        print("No relevant records found in the XML.")
        return pd.DataFrame()

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["date"] = df["start_date"].dt.date
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Pivot into daily summaries
    sleep_df = (
        df[df["type"] == "HKCategoryTypeIdentifierSleepAnalysis"]
        .groupby("date")["value"]
        .sum()
        .rename("sleep_hours") / 3600  # seconds → hours
    )

    steps_df = (
        df[df["type"] == "HKQuantityTypeIdentifierStepCount"]
        .groupby("date")["value"]
        .sum()
        .rename("steps")
    )

    exercise_df = (
        df[df["type"] == "HKQuantityTypeIdentifierAppleExerciseTime"]
        .groupby("date")["value"]
        .sum()
        .rename("exercise_min")
    )

    hr_df = (
        df[df["type"] == "HKQuantityTypeIdentifierRestingHeartRate"]
        .groupby("date")["value"]
        .mean()
        .rename("resting_hr")
    )

    daily = pd.concat([sleep_df, steps_df, exercise_df, hr_df], axis=1).reset_index()
    daily["date"] = pd.to_datetime(daily["date"])
    print(f"Parsed {len(daily)} daily records.")
    return daily


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Apple Health XML export")
    parser.add_argument("--input", required=True, help="Path to export.xml")
    parser.add_argument("--output", required=True, help="Output CSV path")
    args = parser.parse_args()

    df = parse_health_export(args.input)
    if not df.empty:
        df.to_csv(args.output, index=False)
        print(f"Saved to {args.output}")
