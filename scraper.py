import os
import requests
from datetime import datetime

def get_live_matches():
    api_key = os.getenv("FOOTBALL_API_KEY")
    today = datetime.now().strftime("%Y-%m-%d")
    # API'den tüm ligleri çekiyoruz
    url = f"https://api.football-data.org/v4/matches?date={today}"
    headers = {"X-Auth-Token": api_key}
    
    # Arjantin, Brezilya ve İspanya 2. Lig kodlarını ekledim
    # ARJANTİN (Primera Nacional): 'ARG'
    # BREZİLYA (Serie A): 'BSA'
    # İSPANYA 2. LİG (Segunda Division): 'SD'
    allowed_leagues = [
        "WC", "CL", "BL1", "DED", "BSA", "PD", "FL1", 
        "ELC", "PPL", "EC", "SA", "PL", "ARG", "SD"
    ]
    
    try:
        response = requests.get(url, headers=headers).json()
        matches = []
        for m in response.get('matches', []):
            if m['competition']['code'] in allowed_leagues:
                matches.append({
                    "league": m['competition']['name'],
                    "home": m['homeTeam']['name'],
                    "away": m['awayTeam']['name']
                })
        return matches[:10]
    except Exception as e:
        print(f"Scraper hatası: {e}")
        return []
