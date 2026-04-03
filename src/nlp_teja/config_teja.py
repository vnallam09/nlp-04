"""
config_teja.py
(EDIT YOUR COPY OF THIS FILE)

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- What API endpoint should be used as the data source?
- What HTTP request headers are required?
- Where should raw and processed data be stored?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project,copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to change:
- API URL (source of the JSON data),
- the HTTP Request Headers (to show your app name in the user-agent header)
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================


API_URL: str = "http://api.open-notify.org/iss-now.json"

# to something that represents your app or project.
HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-teja-iss-location/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"


# to something that represents YOUR custom project.
RAW_JSON_PATH: Path = RAW_PATH / "iss_location_raw_teja.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "iss_location_processed_teja.csv"
