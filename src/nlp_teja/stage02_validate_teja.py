"""
stage02_validate_teja.py

Source: raw JSON object
Sink: validated JSON object

Purpose

  Inspect and validate the JSON structure from the ISS Now API.

Analytical Questions

- What is the top-level structure of the JSON data?
- What keys are present in the response?
- What data types are associated with each field?
- Are latitude and longitude within valid geographic ranges?
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any

# ============================================================
# Section 2. Define Run Validate Function
# ============================================================


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> dict[str, Any]:
    """Inspect and validate JSON structure.

    Args:
        json_data (Any): The raw JSON data from the Extract stage.
        LOG (logging.Logger): The logger instance.

    Returns:
        dict[str, Any]: The validated JSON data.
    """
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting...")
    LOG.info("========================")

    # ============================================================
    # INSPECT JSON STRUCTURE
    # ============================================================

    LOG.info("JSON STRUCTURE INSPECTION:")
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if isinstance(json_data, dict):
        LOG.info(f"Top-level keys: {list(json_data.keys())}")
        for key, value in json_data.items():
            LOG.info(f"{key}: {type(value).__name__}")

    elif isinstance(json_data, list) and len(json_data) > 0:
        first_record = json_data[0]
        LOG.info(f"Keys in first record: {list(first_record.keys())}")
        LOG.info("Field types:")
        for key, value in first_record.items():
            LOG.info(f"{key}: {type(value).__name__}")

    # ============================================================
    # VALIDATE EXPECTATIONS
    # ============================================================

    if not isinstance(json_data, dict):
        raise ValueError(
            f"Expected a dict from ISS API, got {type(json_data).__name__}."
        )

    required_keys = {"message", "timestamp", "iss_position"}
    if not required_keys.issubset(json_data.keys()):
        raise ValueError(
            f"Missing required keys. Expected {required_keys}, got {set(json_data.keys())}"
        )

    if not isinstance(json_data["iss_position"], dict):
        raise ValueError("Expected 'iss_position' to be a dictionary.")

    position_keys = {"latitude", "longitude"}
    if not position_keys.issubset(json_data["iss_position"].keys()):
        raise ValueError(
            f"Missing position keys. Expected {position_keys}, got {set(json_data['iss_position'].keys())}"
        )

    lat = float(json_data["iss_position"]["latitude"])
    lon = float(json_data["iss_position"]["longitude"])
    if not (-90.0 <= lat <= 90.0):
        raise ValueError(f"Latitude out of valid range [-90, 90]: {lat}")
    if not (-180.0 <= lon <= 180.0):
        raise ValueError(f"Longitude out of valid range [-180, 180]: {lon}")

    LOG.info("ISS position JSON validation passed.")
    LOG.info("Sink: validated JSON object")
    return json_data
