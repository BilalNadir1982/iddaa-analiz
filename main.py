import os, requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon
from news_scraper import get_latest_news

def main():
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    haber_text = get_latest_news()
    matches = get_live_matches()
    
    msg = f"☀️ *GÜNÜN SPOR GÜNDEMİ*\n\n{haber_text}\n\n"
    
    if matches:
        analizler = analyze_matches(matches)
        msg += f"💎 *YAPAY ZEKA ANALİZİ*\n\n{format_coupon(analizler)}"
    else:
        msg += "⚽ *Bugün ve yarın bültende maç bulunamadı.*"

    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id, "text": msg, "parse_mode": "Markdown"
    })

if __name__ == "__main__":
    main()
