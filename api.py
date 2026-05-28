```python
# api.py

import requests
from config import API_KEY

# =========================================
# API SETTINGS
# =========================================

BASE_URL = "https://api.football-data.org/v4"

HEADERS = {
    "X-Auth-Token": API_KEY
}

# =========================================
# LEAGUES
# =========================================

LEAGUES = [
    "WC",     # FIFA World Cup
    "CL",     # Champions League
    "BL1",    # Bundesliga
    "DED",    # Eredivisie
    "BSA",    # Brazil Serie A
    "PD",     # La Liga
    "FL1",    # Ligue 1
    "ELC",    # Championship
    "PPL",    # Portugal
    "EC",     # Euro
    "SA",     # Serie A
    "PL"      # Premier League
]

# =========================================
# GET MATCHES
# =========================================

def get_matches():

    all_matches = []

    for league in LEAGUES:

        url = f"{BASE_URL}/competitions/{league}/matches"

        try:

            response = requests.get(
                url,
                headers=HEADERS
            )

            data = response.json()

            matches = data.get("matches", [])

            for match in matches:

                # Sadece yaklaşan maçlar
                if match["status"] != "TIMED":
                    continue

                home = match["homeTeam"]["name"]
                away = match["awayTeam"]["name"]

                all_matches.append({
                    "league": league,
                    "home": home,
                    "away": away
                })

        except Exception as e:
            print(f"HATA: {league} -> {e}")

    return all_matches
```
