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
    # Canlı maçları scraper'dan çekiyoruz
    raw_matches = get_live_matches()
    
    if not raw_matches:
        print("Maç bulunamadı!")
        return
        
    # Analiz et
    analizler = analyze_matches(raw_matches)
    
    # Kupon hazırla
    mesaj = format_coupon(analizler)
    
    # Gönder
    send_telegram_message(mesaj)
    print("Mesaj başarıyla gönderildi.")

if __name__ == "__main__":
    main()
