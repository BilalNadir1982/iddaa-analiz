import os
import requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon, get_poll_data

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def main():
    # 1. Veri Çek
    matches = get_live_matches()
    if not matches:
        print("Bugün maç bulunamadı.")
        return

    # 2. Analiz Et
    analizler = analyze_matches(matches)

    # 3. Mesajı Gönder
    msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(msg_url, json={
        "chat_id": CHAT_ID,
        "text": format_coupon(analizler),
        "parse_mode": "Markdown"
    }).json()

    # 4. Anketi Gönder (Mesajın hemen altına)
    poll = get_poll_data()
    poll_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"
    requests.post(poll_url, data={
        "chat_id": CHAT_ID,
        "question": poll["question"],
        "options": poll["options"]
    })

if __name__ == "__main__":
    main()
