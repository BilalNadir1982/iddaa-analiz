import os
import requests

def get_live_matches():
    api_key = os.getenv("FOOTBALL_API_KEY")
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": api_key}
    
    # Senin istediğin ligler
    allowed = ["WC", "CL", "BL1", "DED", "BSA", "PD", "FL1", "ELC", "PPL", "EC", "SA", "PL", "ARG", "SD"]
    
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
        return matches[:5] # En iyi 5 maç
    except:
        return []
