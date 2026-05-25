import requests
from config import API_KEY

def get_matches():

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    print(data)

    matches = []

    if "response" not in data:
        return matches

    for m in data["response"]:

        match = {
            "home": m["teams"]["home"]["name"],
            "away": m["teams"]["away"]["name"],
            "home_goals": m["goals"]["home"] or 0,
            "away_goals": m["goals"]["away"] or 0,
            "minute": m["fixture"]["status"]["elapsed"] or 0
        }

        matches.append(match)

    return matches
