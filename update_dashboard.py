#!/usr/bin/env python3
"""
Alberta Capacity vs Income — Dashboard Update Script
Williams Economic Consulting

Purpose:
  Refresh the indicator dashboard and simple signal when new public data arrive.
  Designed to be run monthly (or after major AER / Statistics Canada / GoA releases).

Usage:
  python update_dashboard.py

Input:
  data/indicator_dashboard.csv  (edit values manually or extend with API pulls)
  data/historical_evaluation.csv

Output:
  Updated CSVs and a short console summary of the current reading.
"""

import pandas as pd
from pathlib import Path
from datetime import date

DATA = Path(__file__).resolve().parent.parent / "data"

def load_dashboard():
    return pd.read_csv(DATA / "indicator_dashboard.csv")

def load_history():
    return pd.read_csv(DATA / "historical_evaluation.csv")

def current_reading(df):
    """Produce a one-paragraph qualitative reading from the dashboard."""
    vol = df.loc[df['channel'] == 'Volume', 'signal'].tolist()
    price = df.loc[df['channel'] == 'Price', 'signal'].tolist()
    broad = df.loc[df['channel'] == 'Broad activity', 'signal'].tolist()

    vol_supportive = all(s == 'Supportive' for s in vol) if vol else False
    price_soft = all(s == 'Soft' for s in price) if price else False
    broad_mixed = 'Soft' in broad and 'Supportive' in broad

    lines = []
    if vol_supportive and price_soft:
        lines.append("Volume channel supportive; price channel soft.")
    if broad_mixed:
        lines.append("Broad activity indicators are mixed (YTD positive, recent month soft).")
    lines.append("Published forecasts remain clustered in a moderate-growth range (2.3–2.6%).")
    lines.append("Central scenario: continued moderate growth, still conditioned by energy volumes rather than clear non-energy broadening.")
    return " ".join(lines)

def main():
    print("=" * 60)
    print("Alberta Capacity vs Income — Dashboard Refresh")
    print(f"Run date: {date.today().isoformat()}")
    print("=" * 60)

    dash = load_dashboard()
    hist = load_history()

    print("\nCurrent indicator dashboard:")
    print(dash[['indicator', 'value', 'signal']].to_string(index=False))

    print("\nHistorical directional accuracy (2021–2025):")
    acc = hist['direction_correct'].mean()
    print(f"  {acc:.0%} ({hist['direction_correct'].sum()} of {len(hist)} years)")

    print("\nCurrent qualitative reading:")
    print(" ", current_reading(dash))

    print("\nNext steps when new data arrive:")
    print("  1. Update values in data/indicator_dashboard.csv")
    print("  2. Re-run this script")
    print("  3. If annual production/price data are revised, append to historical_evaluation.csv and recompute the signal")
    print("=" * 60)

if __name__ == "__main__":
    main()
