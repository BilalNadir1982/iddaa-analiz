import os, requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon
from news_scraper import get_latest_news # Yeni import

def main():
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    # 1. Haberleri Çek
    haberler = "\n\n".join(get_latest_news())
    
    # 2. Maçları Çek
    matches = get_live_matches()
    
    # Mesajı Birleştir
    full_message = f"☀️ GÜNAYDIN! Bugünün Gündemi:\n\n{haberler}\n\n"
    
    if matches:
        analizler = analyze_matches(matches)
        full_message += f"\n{format_coupon(analizler)}"
    else:
        full_message += "\n⚽ Bugün bültende maç bulunamadı."

    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id, "text": full_message, "parse_mode": "Markdown"
    })

if __name__ == "__main__":
    main()
