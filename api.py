import requests
import json
from config import FOOTBALL_API_KEY, API_BASE_URL, TAKIP_EDILEN_LIGLER

def fetch_daily_matches():
    """Belirlenen tüm liglerdeki güncel maçları ve takımları API'den çeker."""
    if FOOTBALL_API_KEY == "BURAYA_API_KEY_GELECEK" or not FOOTBALL_API_KEY:
        print("⚠️ Uyarı: API Key tanımlanmadığı için test verileri yükleniyor.")
        return get_fallback_data() # Key yoksa sistem çökmesin diye eski mantık çalışır

    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    tum_maclar = []

    # Tanımladığımız tüm ligleri tek tek dönerek o günkü maçları topluyoruz
    for lig_kodu, lig_adi in TAKIP_EDILEN_LIGLER.items():
        try:
            # Sadece o ligin güncel fikstürünü ve maçlarını istiyoruz
            url = f"{API_BASE_URL}competitions/{lig_kodu}/matches"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                matches = data.get("matches", [])
                
                for match in matches:
                    # Sadece henüz oynanmamış (SCHEDULED) veya canlı (TIMED) maçları al
                    if match.get("status") in ["SCHEDULED", "TIMED"]:
                        tum_maclar.append({
                            "league": lig_adi,
                            "home": match["homeTeam"]["name"],
                            "away": match["awayTeam"]["name"],
                            "home_id": match["homeTeam"]["id"],
                            "away_id": match["awayTeam"]["id"],
                            "match_id": match["id"]
                        })
        except Exception as e:
            print(f"{lig_adi} verisi çekilirken hata oluştu: {e}")
            continue

    return tum_maclar

def get_fallback_data():
    # API anahtarı henüz girilmediyse botun hata vermemesi için yedek havuz
    return [
        {"league": "Almanya Bundesliga", "home": "Bayern Münih", "away": "Eintracht Frankfurt"},
        {"league": "İngiltere Premier Lig", "home": "Arsenal", "away": "Aston Villa"},
        {"league": "Trendyol Süper Lig", "home": "Galatasaray", "away": "Beşiktaş"},
        {"league": "Trendyol Süper Lig", "home": "Fenerbahçe", "away": "Trabzonspor"},
        {"league": "İspanya La Liga", "home": "Real Madrid", "away": "Villarreal"}
    ]
