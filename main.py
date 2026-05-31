import os, requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon, get_poll_data

def main():
    matches = get_live_matches()
    if not matches: return
    
    analizler = analyze_matches(matches)
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    # Mesaj
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id, "text": format_coupon(analizler), "parse_mode": "Markdown"
    })
    
    # Anket
    poll = get_poll_data()
    requests.post(f"https://api.telegram.org/bot{token}/sendPoll", data={
        "chat_id": chat_id, "question": poll["question"], "options": poll["options"]
    })

if __name__ == "__main__":
    main()
