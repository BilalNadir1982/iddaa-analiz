import os, requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon

def main():
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    matches = get_live_matches()
    
    if not matches:
        # Mesajı yoruma alabilirsin, sessiz kalsın istiyorsan burayı sil:
        # requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={"chat_id": chat_id, "text": "Bugün maç yok."})
        return
    
    analizler = analyze_matches(matches)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id, "text": format_coupon(analizler), "parse_mode": "Markdown"
    })

if __name__ == "__main__":
    main()
