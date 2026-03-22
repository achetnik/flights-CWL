"""Cardiff Airport (CWL) destinations — verified via Google Flights."""

DESTINATIONS = {
    "CWL": {
        "name": "Cardiff",
        "routes": {
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "BHD": "Belfast City",
            "DUB": "Dublin",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
