import os
import requests
from scraper import get_live_matches
from analyzer import analyze_matches
from coupon import format_coupon
from news_scraper import get_latest_news

def main():
    # GitHub Secrets üzerinden gelen Telegram ve API bilgileri
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    # 1. Güncel spor haberlerini çek
    haber_text = get_latest_news()
    
    # 2. Bültendeki aktif maçları çek
    matches = get_live_matches()
    
    # 3. Resim altına yazılacak ana metni oluştur (Gündem başlığı)
    msg = f"☀️ *GÜNÜN SPOR GÜNDEMİ*\n\n{haber_text}\n\n"
    
    # 4. Maç varsa kombine kuponu oluştur ve metne ekle
    if matches:
        analizler = analyze_matches(matches)
        msg += f"{format_coupon(analizler)}"
    else:
        msg += "⚽ *Bugün ve yarın bültende kombine kupon için yeterli maç bulunamadı.*"

    # 5. Gönderilecek şık kapak görseli (Futbol temalı yüksek kalite görsel)
    image_url = "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?q=80&w=600&auto=format&fit=crop"
    
    # 6. Telegram API bağlantısı (sendPhoto)
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": image_url,
        "caption": msg,
        "parse_mode": "Markdown"
    }
    
    # Mesajı Telegram kanalına tek seferde gönder
    try:
        response = requests.post(url, json=payload, timeout=15)
        if not response.ok:
            print(f"Telegram API Hatası: {response.text}")
    except Exception as e:
        print(f"İstek gönderilirken bir bağlantı hatası oluştu: {e}")

if __name__ == "__main__":
    main()
