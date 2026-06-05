import os, requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon, get_poll_data

def main():
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    matches = get_live_matches()
    
    # EĞER MAÇ YOKSA BİLGİ VER, BÖYLECE BOTUN ÇALIŞTIĞINI ANLARSIN
    if not matches:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
            "chat_id": chat_id, "text": "🤖 Bot çalışıyor ancak bugün takip edilen liglerde maç bulunamadı."
        })
        return
    
    # MAÇ VARSA ANALİZ VE KUPON GÖNDER
    analizler = analyze_matches(matches)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id, "text": format_coupon(analizler), "parse_mode": "Markdown"
    })
    
    poll = get_poll_data()
    requests.post(f"https://api.telegram.org/bot{token}/sendPoll", data={
        "chat_id": chat_id, "question": poll["question"], "options": poll["options"]
    })

if __name__ == "__main__":
    main()
