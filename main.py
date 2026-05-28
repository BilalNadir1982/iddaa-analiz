from api import fetch_daily_matches
from analyzer import analyze_matches
from coupon import format_coupon
from sender import send_coupon
from db import son_kuponu_kaydet  # Yeni ekledik

def main():
    print("Bot çalıştırıldı, analiz süreci başlıyor...")
    raw_matches = fetch_daily_matches()
    analyzed_matches = analyze_matches(raw_matches)
    
    if not analyzed_matches or len(analyzed_matches) < 5:
        print("Kriterlere uygun yeterli maç bulunamadı.")
        return 
    
    # Kuponu gönder
    coupon_text = format_coupon(analyzed_matches)
    send_coupon(coupon_text)
    
    # Gece kontrolü için bu kuponu hafızaya yazıyoruz
    son_kuponu_kaydet(analyzed_matches)
    print("İşlem başarıyla tamamlandı!")

if __name__ == "__main__":
    main()
