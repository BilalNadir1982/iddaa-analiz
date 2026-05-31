import requests
from bs4 import BeautifulSoup

def get_live_matches():
    # Güncel bülten sayfası
    url = "https://www.mackolik.com/canli-sonuclar"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        matches = []
        # Sayfadaki maç kutucuklarını bul
        for item in soup.select('.matches-list-item')[:5]: # Sadece ilk 5 maçı al
            home = item.select_one('.match-name-home').text.strip()
            away = item.select_one('.match-name-away').text.strip()
            league = item.select_one('.league-name').text.strip()
            
            matches.append({
                "league": league,
                "home": home,
                "away": away,
                "home_id": len(home) # Geçici ID
            })
        return matches
    except:
        return []
