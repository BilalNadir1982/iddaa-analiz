import os
import requests

def get_live_matches():
    api_key = os.getenv("FOOTBALL_API_KEY")
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": api_key}
    
    # Yazın da devam eden ligler dahil güncel liste
    allowed = ["BSA", "MLS", "J1", "WC", "CL", "BL1", "DED", "PD", "FL1", "ELC", "PPL", "SA", "PL", "ARG", "SD"]
    
    try:
        response = requests.get(url, headers=headers).json()
        matches = []
        for m in response.get('matches', []):
            if m['competition']['code'] in allowed:
                matches.append({
                    "league": m['competition']['name'],
                    "home": m['homeTeam']['name'],
                    "away": m['awayTeam']['name']
                })
        return matches[:5]
    except:
        return []
