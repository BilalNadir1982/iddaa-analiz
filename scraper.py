import os
import requests
from datetime import datetime

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io/fixtures"

def get_today_matches():
    today = datetime.today().strftime("%Y-%m-%d")
    headers = {"x-apisports-key": API_KEY}
    params = {"date": today}

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        print(f"API Hatası: {response.status_code}")
        return []

    data = response.json()
    matches = []
    for match in data.get("response", []):
        matches.append({
            "home": match["teams"]["home"]["name"],
            "away": match["teams"]["away"]["name"],
            "league": match["league"]["name"]
        })
    return matches

if __name__ == "__main__":
    matches = get_today_matches()
    print(matches)
