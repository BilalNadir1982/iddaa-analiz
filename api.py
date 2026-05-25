# =========================================
# api.py
# =========================================

import requests
from datetime import datetime
from config import API_KEY

def get_matches():

    today = datetime.now().strftime("%Y-%m-%d")

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    matches = []

    if "response" not in data:
        return matches

    for m in data["response"]:

        try:

            matches.append({

                "home": m["teams"]["home"]["name"],
                "away": m["teams"]["away"]["name"],

                "home_goals": m["goals"]["home"] or 0,
                "away_goals": m["goals"]["away"] or 0,

                "minute": m["fixture"]["status"]["elapsed"] or 0,

                "league": m["league"]["name"]

            })

        except:
            pass

    return matches
