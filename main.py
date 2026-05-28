from api import fetch_daily_matches
from analyzer import analyze_matches
from coupon import format_coupon
from sender import send_coupon

def main():
    print("Bot çalıştırıldı, analiz süreci başlıyor...")
    
    # 1. Adım: Maç verilerini al
    raw_matches = fetch_daily_matches()
    
    # 2. Adım: Filtrele
    analyzed_matches = analyze_matches(raw_matches)
    
    # EĞER MAÇ YOKSA TELEGRAM'A MESAJ ATMA, SESSİZCE ÇIK
    if not analyzed_matches or len(analyzed_matches) < 5:
        print("Kriterlere uygun yeterli maç bulunamadı. Telegram'a mesaj gönderilmeyecek.")
        return # Programı burada bitirir, kanala gereksiz yazı atmaz.
    
    # 3. Adım: Maç varsa kuponu hazırla
    coupon_text = format_coupon(analyzed_matches)
    
    # 4. Adım: Kanala gönder
    print("Kupon hazırlandı, Telegram'a gönderiliyor...")
    send_coupon(coupon_text)
    
    print("İşlem başarıyla tamamlandı!")

if __name__ == "__main__":
    main()
