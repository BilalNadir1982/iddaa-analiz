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
    
    # Haber gelmediyse ve maç da yoksa mesaj atma
    if "Şu an haber akışına bağlanılamıyor" in haber_text and not matches:
        return 

    # RESİM ALTINA YAZILACAK METNİ OLUŞTURUYORUZ (CAPTION)
    msg = f"☀️ *GÜNÜN SPOR GÜNDEMİ*\n\n{haber_text}\n\n"
    
    if matches:
        analizler = analyze_matches(matches)
        # Karakter limiti için coupon.py'daki formatı sadeleştirebiliriz
        msg += f"💎 *YAPAY ZEKA ANALİZİ*\n\n{format_coupon(analizler)}"
    else:
        msg += "⚽ *Bugün bültende maç bulunamadı.*"

    # RESİMLİ MESAJ GÖNDERME (sendPhoto)
    # Örnek bir spor resmi. Kendi resim URL'ni de kullanabilirsin.
    image_url = "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?q=80&w=600&auto=format&fit=crop" # Örnek Futbol Topu Resmi
    
    payload = {
        "chat_id": chat_id,
        "photo": image_url,
        "caption": msg, # Metni buraya yazıyoruz
        "parse_mode": "Markdown"
    }

    response = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", json=payload)
    
    # Hata kontrolü için (GitHub Actions loglarında görmek için)
    if not response.ok:
        print(f"Hata: {response.text}")

if __name__ == "__main__":
    main()
