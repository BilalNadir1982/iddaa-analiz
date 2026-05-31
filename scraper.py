import requests

def get_live_matches():
    # Burası API'den güncel maçları çeken profesyonel kısımdır.
    # API_KEY kısmına kendi ücretsiz key'ini yazarsan maçlar otomatik güncellenir.
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": "BURAYA_FOOTBALL_DATA_API_KEY_YAZ"}
    
    try:
        response = requests.get(url, headers=headers).json()
        matches = []
        for m in response.get('matches', [])[:5]: # Sadece güncel 5 maç
            matches.append({
                "league": m['competition']['name'],
                "home": m['homeTeam']['name'],
                "away": m['awayTeam']['name'],
                "home_id": 99
            })
        return matches
    except:
        # Eğer API'ye bağlanamazsa, hata vermemesi için şimdilik boş döner
        return []
