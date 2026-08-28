import numpy as np
import pandas as pd

def yearly_summary(df):
    out = (
        df.groupby("year", as_index=False)
        .agg(
            incidents=("eventid", "count"),
            fatalities=("nkill", "sum"),
            injuries=("nwound", "sum"),
            casualties=("casualties", "sum"),
            success_rate=("success", "mean"),
        )
        .sort_values("year")
    )
    out["success_rate"] *= 100
    return out

def country_summary(df):
    out = (
        df.groupby("country_txt", as_index=False)
        .agg(
            incidents=("eventid", "count"),
            fatalities=("nkill", "sum"),
            injuries=("nwound", "sum"),
            avg_casualties=("casualties", "mean"),
            success_rate=("success", "mean"),
        )
    )
    out["success_rate"] *= 100
    return out.sort_values("incidents", ascending=False)

def attack_summary(df, col):
    return (
        df.groupby(col, as_index=False)
        .agg(incidents=("eventid", "count"), casualties=("casualties", "sum"))
        .sort_values("incidents", ascending=False)
    )

def normalize_series(s):
    s = s.astype(float)
    lo, hi = s.min(), s.max()
    if hi == lo:
        return pd.Series(np.full(len(s), 50.0), index=s.index)
    return (s - lo) / (hi - lo) * 100

def historical_exposure_index(df):
    """Explainable historical index; not a real-time threat score."""
    recent_cut = max(int(df["year"].max()) - 4, int(df["year"].min()))
    all_counts = df.groupby("country_txt").size()
    recent = df[df["year"] >= recent_cut]
    recent_counts = recent.groupby("country_txt").size()

    grouped = df.groupby("country_txt").agg(
        incidents=("eventid", "count"),
        fatalities=("nkill", "sum"),
        avg_casualties=("casualties", "mean"),
        success_rate=("success", "mean"),
    )
    grouped["recent_activity"] = grouped.index.map(recent_counts).fillna(0)
    grouped["frequency_component"] = normalize_series(np.log1p(grouped["incidents"]))
    grouped["severity_component"] = normalize_series(grouped["avg_casualties"])
    grouped["recent_component"] = normalize_series(np.log1p(grouped["recent_activity"]))
    grouped["success_component"] = grouped["success_rate"] * 100

    grouped["exposure_index"] = (
        0.35 * grouped["frequency_component"]
        + 0.30 * grouped["severity_component"]
        + 0.20 * grouped["recent_component"]
        + 0.15 * grouped["success_component"]
    ).round(2)

    def level(x):
        if x >= 75:
            return "High"
        if x >= 50:
            return "Moderate"
        return "Lower"

    grouped["exposure_level"] = grouped["exposure_index"].map(level)
    return grouped.reset_index().sort_values("exposure_index", ascending=False)
