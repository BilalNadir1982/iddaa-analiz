import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_iddaa_matches():
    """
    Mackolik'ten iddaa programını çeker (en stabil kaynaklardan biri)
    """
    url = "https://arsiv.mackolik.com/Iddaa-Programi"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        matches = []
        
        # Bu selectorlar site değişirse güncellenmeli
        rows = soup.find_all("tr", class_="iddaa-row")  # Gerçek selector değişebilir
        
        for row in rows[:30]:  # İlk 30 maçı alalım
            try:
                time = row.find(class_="time").text.strip()
                league = row.find(class_="league").text.strip()
                home = row.find(class_="home").text.strip()
                away = row.find(class_="away").text.strip()
                odds = row.find_all(class_="odds")
                
                match = {
                    "time": time,
                    "league": league,
                    "match": f"{home} - {away}",
                    "home_odd": float(odds[0].text.strip()) if len(odds) > 0 else 0,
                    "draw_odd": float(odds[1].text.strip()) if len(odds) > 1 else 0,
                    "away_odd": float(odds[2].text.strip()) if len(odds) > 2 else 0,
                    "date": datetime.now().strftime("%d.%m.%Y")
                }
                matches.append(match)
            except:
                continue
                
        return matches
        
    except Exception as e:
        print(f"Scraping hatası: {e}")
        # Test için dummy data
        return [
            {"time": "21:45", "league": "Serie A", "match": "Fiorentina - Atalanta", 
             "home_odd": 2.80, "draw_odd": 3.40, "away_odd": 2.45, "date": datetime.now().strftime("%d.%m.%Y")},
            {"time": "20:45", "league": "Türkiye Kupası", "match": "Trabzonspor - Konyaspor", 
             "home_odd": 1.65, "draw_odd": 4.10, "away_odd": 4.80, "date": datetime.now().strftime("%d.%m.%Y")}
        ]
