"""
visualizations.py
-----------------
Reusable plotting functions for the DSA 210 screen time analysis project.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np

# Consistent style across all notebooks
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
FIGURE_DIR = "figures/"


def save_fig(name: str):
    """Save the current figure to the figures/ directory."""
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    plt.savefig(f"{FIGURE_DIR}{name}.png", dpi=150, bbox_inches="tight")
    print(f"Saved: {FIGURE_DIR}{name}.png")


def plot_screen_time_over_time(df: pd.DataFrame):
    """Line chart of daily total screen time with 7-day rolling average."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(df["date"], df["total_screen_time_min"], color="steelblue", alpha=0.5, label="Daily")
    rolling = df["total_screen_time_min"].rolling(7, center=True).mean()
    ax.plot(df["date"], rolling, color="navy", linewidth=2, label="7-day avg")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45)
    ax.set_xlabel("Date")
    ax.set_ylabel("Screen Time (min)")
    ax.set_title("Daily Screen Time Over Time")
    ax.legend()
    plt.tight_layout()
    save_fig("screen_time_over_time")
    plt.show()


def plot_app_category_breakdown(df: pd.DataFrame):
    """Stacked bar chart of app category usage per day."""
    categories = ["social_min", "entertainment_min", "productivity_min", "other_min"]
    labels = ["Social", "Entertainment", "Productivity", "Other"]
    colors = ["#e74c3c", "#e67e22", "#2ecc71", "#95a5a6"]

    fig, ax = plt.subplots(figsize=(12, 5))
    bottom = np.zeros(len(df))
    for col, label, color in zip(categories, labels, colors):
        ax.bar(df["date"], df[col], bottom=bottom, label=label, color=color, alpha=0.85)
        bottom += df[col].values

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.xticks(rotation=45)
    ax.set_xlabel("Date")
    ax.set_ylabel("Minutes")
    ax.set_title("Daily App Category Breakdown")
    ax.legend(loc="upper right")
    plt.tight_layout()
    save_fig("app_category_breakdown")
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame):
    """Heatmap of Pearson correlations between numeric features."""
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    exclude = ["day_of_week", "workload_encoded", "high_screen_time"]
    cols = [c for c in numeric_cols if c not in exclude]

    corr = df[cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
        center=0, linewidths=0.5, ax=ax
    )
    ax.set_title("Feature Correlation Heatmap")
    plt.tight_layout()
    save_fig("correlation_heatmap")
    plt.show()


def plot_scatter_with_regression(df: pd.DataFrame, x: str, y: str, hue: str = None):
    """Scatter plot with regression line between two variables."""
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.regplot(data=df, x=x, y=y, ax=ax, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
    ax.set_title(f"{y} vs {x}")
    plt.tight_layout()
    save_fig(f"scatter_{x}_vs_{y}")
    plt.show()


def plot_weekday_vs_weekend(df: pd.DataFrame, col: str = "total_screen_time_min"):
    """Boxplot comparing weekday vs weekend for a given column."""
    df = df.copy()
    df["Day Type"] = df["is_weekend"].map({0: "Weekday", 1: "Weekend"})
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.boxplot(data=df, x="Day Type", y=col, palette="Set2", ax=ax)
    ax.set_title(f"{col} – Weekday vs Weekend")
    plt.tight_layout()
    save_fig(f"boxplot_weekday_weekend_{col}")
    plt.show()
