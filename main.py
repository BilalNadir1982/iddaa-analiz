import os
import requests
from analyzer import analyze_matches
from coupon import format_coupon
from scraper import get_live_matches

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def main():
    raw_matches = get_live_matches()
    if not raw_matches:
        print("Maç bulunamadı, işlem durduruldu.")
        return
    analizler = analyze_matches(raw_matches)
    mesaj = format_coupon(analizler)
    send_telegram_message(mesaj)
    print("Mesaj gönderildi.")

if __name__ == "__main__":
    main()
