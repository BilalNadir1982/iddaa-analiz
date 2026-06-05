import os
import requests
from datetime import datetime, timedelta

def get_live_matches():
    api_key = os.getenv("FOOTBALL_API_KEY")
    headers = {"X-Auth-Token": api_key}
    allowed = ["BSA", "ARG"] 
    
    matches = []
    for days in range(2): # Bugün ve yarın
        date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        url = f"https://api.football-data.org/v4/matches?date={date}"
        try:
            response = requests.get(url, headers=headers).json()
            for m in response.get('matches', []):
                if m['competition']['code'] in allowed:
                    matches.append({
                        "league": m['competition']['name'],
                        "home": m['homeTeam']['name'],
                        "away": m['awayTeam']['name']
                    })
        except: continue
    return matches[:5]
