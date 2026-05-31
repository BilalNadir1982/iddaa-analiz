import os
import requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon, get_poll_data

def main():
    # 1. Veri Çek
    matches = get_live_matches()
    if not matches:
        print("Bugün maç yok veya API hatası.")
        return

    # 2. Analiz Et
    analizler = analyze_matches(matches)

    # 3. Mesajı Gönder
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    msg_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(msg_url, json={
        "chat_id": chat_id,
        "text": format_coupon(analizler),
        "parse_mode": "Markdown"
    })

    # 4. Anketi Gönder
    poll = get_poll_data()
    poll_url = f"https://api.telegram.org/bot{bot_token}/sendPoll"
    requests.post(poll_url, data={
        "chat_id": chat_id,
        "question": poll["question"],
        "options": poll["options"]
    })

if __name__ == "__main__":
    main()
