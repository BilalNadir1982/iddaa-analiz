import requests
from bs4 import BeautifulSoup

def get_live_matches():
    url = "https://www.mackolik.com/canli-sonuclar"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        matches = []
        
        # Maçları bul
        items = soup.select('.matches-list-item')[:5]
        for item in items:
            home = item.select_one('.match-name-home').text.strip()
            away = item.select_one('.match-name-away').text.strip()
            league = item.select_one('.league-name').text.strip()
            
            matches.append({
                "league": league, "home": home, "away": away, "home_id": 10
            })
        return matches
    except Exception as e:
        print(f"Scraper hatası: {e}")
        return []
