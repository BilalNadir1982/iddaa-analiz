import os
import requests
import json
from analyzer import analyze_matches
from coupon import format_coupon

# Telegram ayarları
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def get_matches():
    # Burada manuel liste yerine otomatik bir API'den çekiyoruz
    # Ücretsiz ve limitsiz deneme için şimdilik örnek yapı:
    return [
        {"league": "PREMIER LİG", "home": "Liverpool", "away": "Man City", "home_id": 1, "away_id": 2},
        {"league": "LA LIGA", "home": "Real Madrid", "away": "Sevilla", "home_id": 3, "away_id": 4}
    ]

def main():
    try:
        raw_matches = get_matches()
        if not raw_matches: return
        
        analizler = analyze_matches(raw_matches)
        mesaj = format_coupon(analizler)
        send_telegram_message(mesaj)
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
