"""Cardiff Airport (CWL) destinations."""

DESTINATIONS = {
    "CWL": {
        "name": "Cardiff",
        "routes": {
            "AGP": "Malaga",
            "ALC": "Alicante",
            "ACE": "Lanzarote",
            "AYT": "Antalya",
            "BCN": "Barcelona",
            "CFU": "Corfu",
            "DLM": "Dalaman",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "FAO": "Faro",
            "FUE": "Fuerteventura",
            "HER": "Heraklion",
            "LPA": "Gran Canaria",
            "PMI": "Palma",
            "TFS": "Tenerife",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
