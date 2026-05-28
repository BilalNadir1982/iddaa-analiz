import requests
from config import API_KEY

BASE_URL = "https://api.football-data.org/v4"

HEADERS = {
    "X-Auth-Token": API_KEY
}

LEAGUES = ["PL", "SA", "BL1", "PD", "FL1", "CL"]

def get_matches():

    matches = []

    for league in LEAGUES:

        url = f"{BASE_URL}/competitions/{league}/matches"

        try:
            r = requests.get(url, headers=HEADERS)
            data = r.json()

            for m in data.get("matches", []):

                if m["status"] != "TIMED":
                    continue

                matches.append({
                    "home": m["homeTeam"]["name"],
                    "away": m["awayTeam"]["name"]
                })

        except:
            pass

    return matches
