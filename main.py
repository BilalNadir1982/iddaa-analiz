import os
import requests
import json
from datetime import datetime

# Ayarlar
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def get_matches():
    # Buraya maçları manuel ekle, sistem her zaman çalışır!
    return [
        {"league": "PREMIER LİG", "home": "Arsenal", "away": "Chelsea", "home_id": 10, "away_id": 20},
        {"league": "LA LIGA", "home": "Real Madrid", "away": "Barcelona", "home_id": 30, "away_id": 40},
        {"league": "BUNDESLIGA", "home": "Bayern", "away": "Dortmund", "home_id": 50, "away_id": 60},
        {"league": "SERIE A", "home": "Juventus", "away": "Milan", "home_id": 70, "away_id": 80},
        {"league": "LIGUE 1", "home": "PSG", "away": "Monaco", "home_id": 90, "away_id": 100}
    ]

def main():
    raw_matches = get_matches()
    
    # Analizleri al (analyzer.py'dan)
    from analyzer import analyze_matches
    analizler = analyze_matches(raw_matches)
    
    # Kupon formatına getir (coupon.py'dan)
    from coupon import format_coupon
    mesaj = format_coupon(analizler)
    
    # Gönder
    send_telegram_message(mesaj)

if __name__ == "__main__":
    main()
