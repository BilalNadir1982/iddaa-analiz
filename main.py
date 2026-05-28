from api import fetch_daily_matches
from analyzer import analyze_matches
from coupon import format_coupon
from sender import send_coupon

def main():
    print("Bot çalıştırıldı, analiz süreci başlıyor...")
    
    # 1. Adım: Maç verilerini havuzdan al
    raw_matches = fetch_daily_matches()
    
    # 2. Adım: En güvenilir olanları filtrele
    analyzed_matches = analyze_matches(raw_matches)
    
    # 3. Adım: Telegram mesaj formatına çevir
    coupon_text = format_coupon(analyzed_matches)
    
    # 4. Adım: Kanala gönder
    print("Kupon hazırlandı, Telegram'a gönderiliyor...")
    send_coupon(coupon_text)
    
    print("İşlem başarıyla tamamlandı!")

if __name__ == "__main__":
    main()
