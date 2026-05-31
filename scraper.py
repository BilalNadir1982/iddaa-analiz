import requests
from bs4 import BeautifulSoup

def get_live_matches():
    # Canlı sonuçlar sayfasından veriyi çek
    url = "https://www.mackolik.com/canli-sonuclar"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    matches = []
    # Site yapısına göre maçları bul (class isimleri değişebilir, mackolik yapısı baz alınmıştır)
    for match in soup.select('.match-item'): # Buradaki class ismi sitenin o anki yapısına göre düzeltilmelidir
        home = match.select_one('.home-team').text.strip()
        away = match.select_one('.away-team').text.strip()
        matches.append({"league": "Güncel Maç", "home": home, "away": away, "home_id": 111, "away_id": 222})
    
    return matches[:10] # En güncel 10 maçı döndür
