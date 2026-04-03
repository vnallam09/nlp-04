"""
stage03_transform_teja.py

Source: validated JSON object
Sink: Polars DataFrame

Purpose

  Transform validated ISS Now JSON data into a structured DataFrame.
  Flattens the nested iss_position dict and adds hemisphere derived fields.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

from datetime import UTC, datetime
import logging
from typing import Any

import polars as pl

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    json_data: Any,
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform JSON into a structured DataFrame.

    Args:
        json_data (Any): Validated JSON data.
        LOG (logging.Logger): The logger instance.

    Returns:
        pl.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    position = json_data["iss_position"]
    lat = float(position["latitude"])
    lon = float(position["longitude"])

    records: list[dict[str, Any]] = [
        {
            "timestamp": json_data["timestamp"],
            "timestamp_utc": datetime.fromtimestamp(
                json_data["timestamp"], tz=UTC
            ).isoformat(),
            "message": json_data.get("message"),
            "latitude": lat,
            "longitude": lon,
            "lat_hemisphere": "N" if lat >= 0 else "S",
            "lon_hemisphere": "E" if lon >= 0 else "W",
        }
    ]

    df: pl.DataFrame = pl.DataFrame(records)

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Polars DataFrame created")

    # Return the transformed DataFrame for use in the next stage.
    return df
