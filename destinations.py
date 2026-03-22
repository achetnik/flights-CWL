"""Cardiff Airport (CWL) destinations — verified March 2026."""

DESTINATIONS = {
    "CWL": {
        "name": "Cardiff",
        "routes": {
            "ACE": "Lanzarote",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "AYT": "Antalya",
            "BGI": "Barbados",
            "BHD": "Belfast",
            "BOJ": "Bourgas",
            "CFU": "Corfu",
            "CMF": "Chambery",
            "CUN": "Cancun",
            "DBV": "Dubrovnik",
            "DLM": "Dalaman",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "EFL": "Kefalonia",
            "ENF": "Enontekio",
            "FAO": "Faro",
            "FUE": "Fuerteventura",
            "HER": "Heraklion",
            "IBZ": "Ibiza",
            "IVL": "Ivalo",
            "KGS": "Kos",
            "LCA": "Larnaca",
            "LPA": "Gran Canaria",
            "MAH": "Menorca",
            "NBE": "Enfidha",
            "PFO": "Paphos",
            "PJA": "Pajala",
            "PMI": "Palma",
            "REU": "Reus",
            "RHO": "Rhodes",
            "TFS": "Tenerife",
            "ZTH": "Zakynthos",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
