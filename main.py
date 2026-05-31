import os
import json
import requests
from analyzer import analyze_matches
from coupon import format_coupon

# Telegram Ayarları
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def get_matches_from_json():
    try:
        with open('maclar.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON okuma hatası: {e}")
        return []

def main():
    raw_matches = get_matches_from_json()
    if not raw_matches:
        print("Maç listesi boş!")
        return
        
    analizler = analyze_matches(raw_matches)
    mesaj = format_coupon(analizler)
    send_telegram_message(mesaj)

if __name__ == "__main__":
    main()
