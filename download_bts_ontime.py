
"""
Download BTS TranStats On-Time Performance monthly files.

Run from the repo root:
    python download_bts_ontime.py
"""

import os
from pathlib import Path
import requests
import zipfile
from io import BytesIO

# ------------ CONFIGURE THESE ------------- #
YEARS = [2019]          # years you want
MONTHS = list(range(1, 13))   # 1–12

BASE_URL = (
    "https://transtats.bts.gov/PREZIP/"
    "On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"
)
# ----------------------------------------- #

# Use current working directory as the repo root
ROOT_DIR = Path.cwd()
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CSV_DIR = RAW_DIR / "csv"

print(f"Current working dir (ROOT_DIR): {ROOT_DIR}")

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)
CSV_DIR.mkdir(parents=True, exist_ok=True)

print(f"Ensured directory exists: {DATA_DIR}")
print(f"Ensured directory exists: {RAW_DIR}")
print(f"Ensured directory exists: {CSV_DIR}")


def download_and_extract(year: int, month: int) -> None:
    """Download and extract a single year/month file."""
    url = BASE_URL.format(year=year, month=month)
    filename = f"On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"
    zip_path = RAW_DIR / filename

    print(f"\n[{year}-{month:02d}] Downloading from {url}")

    try:
        resp = requests.get(url, timeout=60)
    except requests.RequestException as e:
        print(f"  ✗ Request failed: {e}")
        return

    if resp.status_code != 200:
        print(f"  ✗ HTTP {resp.status_code} – skipping. (status={resp.status_code})")
        return

    zip_path.write_bytes(resp.content)
    print(f"  ✓ Saved to {zip_path}")

    try:
        with zipfile.ZipFile(BytesIO(resp.content)) as zf:
            for member in zf.namelist():
                if member.lower().endswith(".csv"):
                    print(f"  → Extracting {member} to {CSV_DIR}")
                    zf.extract(member, path=CSV_DIR)
    except zipfile.BadZipFile:
        print("  ✗ Bad zip file – could not extract.")

def main():
    print("\nStarting BTS On-Time data download...\n")
    for year in YEARS:
        for month in MONTHS:
            download_and_extract(year, month)

    print("\nDone. Check the 'data/raw/csv' directory for extracted CSV files.")


if __name__ == "__main__":
    main()
