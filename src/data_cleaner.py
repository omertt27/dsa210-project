"""
data_cleaner.py
---------------
Loads, cleans and engineers features from the real smmh.csv survey dataset.

Raw columns (21 total):
    Timestamp, Age, Gender, Relationship Status, Occupation Status,
    Organization type, Do you use social media?, Platforms used,
    Daily usage time (categorical), Q9-Q20 (mental health indicators 1-5)

Output: data/processed/smmh_clean.csv

Usage:
    python src/data_cleaner.py
"""

import pandas as pd
import numpy as np
import os

RAW_PATH  = "data/raw/smmh.csv"
OUT_PATH  = "data/processed/smmh_clean.csv"

# Mapping of verbose question text → short column names
COL_RENAME = {
    "Timestamp": "timestamp",
    "1. What is your age?": "age",
    "2. Gender": "gender",
    "3. Relationship Status": "relationship_status",
    "4. Occupation Status": "occupation",
    "5. What type of organizations are you affiliated with?": "org_type",
    "6. Do you use social media?": "uses_social_media",
    "7. What social media platforms do you commonly use?": "platforms",
    "8. What is the average time you spend on social media every day?": "daily_usage",
    "9. How often do you find yourself using Social media without a specific purpose?": "purposeless_use",
    "10. How often do you get distracted by Social media when you are busy doing something?": "distraction_busy",
    "11. Do you feel restless if you haven't used Social media in a while?": "restlessness",
    "12. On a scale of 1 to 5, how easily distracted are you?": "easily_distracted",
    "13. On a scale of 1 to 5, how much are you bothered by worries?": "bothered_by_worries",
    "14. Do you find it difficult to concentrate on things?": "difficulty_concentrating",
    "15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?": "compare_to_others",
    "16. Following the previous question, how do you feel about these comparisons, generally speaking?": "feeling_about_comparisons",
    "17. How often do you look to seek validation from features of social media?": "seek_validation",
    "18. How often do you feel depressed or down?": "feel_depressed",
    "19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?": "interest_fluctuation",
    "20. On a scale of 1 to 5, how often do you face issues regarding sleep?": "sleep_issues",
}

# Ordinal mapping for daily usage (categorical → numeric hours midpoint)
USAGE_MAP = {
    "Less than an Hour":   0.5,
    "Between 1 and 2 hours": 1.5,
    "Between 2 and 3 hours": 2.5,
    "Between 3 and 4 hours": 3.5,
    "Between 4 and 5 hours": 4.5,
    "More than 5 hours":   6.0,
}

MENTAL_HEALTH_COLS = [
    "purposeless_use", "distraction_busy", "restlessness",
    "easily_distracted", "bothered_by_worries", "difficulty_concentrating",
    "compare_to_others", "feeling_about_comparisons", "seek_validation",
    "feel_depressed", "interest_fluctuation", "sleep_issues",
]


def load_and_rename(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Rename only columns that exist (handles partial matches)
    rename_map = {c: COL_RENAME[c] for c in df.columns if c in COL_RENAME}
    df = df.rename(columns=rename_map)
    print(f"Loaded {len(df)} rows, {df.shape[1]} columns from {path}")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Drop the 3 rows that answered "No" to social media use
    df = df[df["uses_social_media"].str.strip().str.lower() == "yes"].copy()

    # Standardise gender
    df["gender"] = df["gender"].str.strip().str.title()
    df["gender"] = df["gender"].replace({
        "Nb": "Non-binary", "Non-Binary": "Non-binary",
        "Nonbinary": "Non-binary", "Trans": "Other",
        "Unsure": "Other", "Nb": "Non-binary",
    })

    # Age: coerce to numeric, drop obvious outliers
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df = df[(df["age"] >= 13) & (df["age"] <= 75)].copy()

    # Encode daily usage to numeric
    df["daily_usage_hours"] = df["daily_usage"].map(USAGE_MAP)

    # All mental health scores should already be 1-5 integers
    for col in MENTAL_HEALTH_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=MENTAL_HEALTH_COLS + ["daily_usage_hours"]).copy()
    print(f"After cleaning: {len(df)} rows")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    # Composite mental health risk score (mean of all 12 indicators, range 1-5)
    df["mh_score"] = df[MENTAL_HEALTH_COLS].mean(axis=1).round(3)

    # Binary label: high mental health risk (above median)
    median_mh = df["mh_score"].median()
    df["high_mh_risk"] = (df["mh_score"] > median_mh).astype(int)

    # Anxiety sub-score (restlessness + bothered_by_worries + difficulty_concentrating)
    df["anxiety_score"] = df[["restlessness", "bothered_by_worries",
                               "difficulty_concentrating"]].mean(axis=1).round(3)

    # Depression sub-score (feel_depressed + interest_fluctuation + sleep_issues)
    df["depression_score"] = df[["feel_depressed", "interest_fluctuation",
                                  "sleep_issues"]].mean(axis=1).round(3)

    # Platform count
    df["platform_count"] = df["platforms"].str.split(",").apply(
        lambda x: len(x) if isinstance(x, list) else 0
    )

    # Student vs worker
    df["is_student"] = df["occupation"].str.strip().str.lower().str.contains(
        "student", na=False
    ).astype(int)

    # Usage group
    df["usage_group"] = pd.cut(
        df["daily_usage_hours"],
        bins=[0, 1, 3, 6],
        labels=["Low (<1h)", "Moderate (1-3h)", "High (>3h)"],
    )

    print(f"Engineered features. Median MH score: {median_mh:.2f}")
    print(f"High-risk label distribution:\n{df['high_mh_risk'].value_counts().to_dict()}")
    return df


def save(df: pd.DataFrame):
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"\nSaved cleaned dataset → {OUT_PATH}")
    print(df[["age", "daily_usage_hours", "mh_score", "anxiety_score",
              "depression_score"]].describe().round(2))


if __name__ == "__main__":
    df = load_and_rename(RAW_PATH)
    df = clean(df)
    df = engineer_features(df)
    save(df)
