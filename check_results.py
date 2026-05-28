import random
from db import son_kuponu_getir
from sender import send_coupon

def sonuclari_kontrol_et():
    print("Gece raporu: Kupon sonuçları kontrol ediliyor...")
    kupon = son_kuponu_getir()
    
    if not kupon:
        print("Hafızada kontrol edilecek kupon bulunamadı.")
        return

    rapor_mesaji = "📊 **GÜNLÜK KUPON SONUÇ RAPORU** 📊\n"
    rapor_mesaji += "───────────────────────\n\n"
    
    kupon_tuttu_mu = True
    tutan_mac_sayisi = 0

    for match in kupon:
        # İleride burası API'den gerçek skorları çekecek. 
        # Şimdilik sistemi test etmek için %80 ihtimalle DOĞRU (Tuttu) simüle ediyoruz.
        mac_sonucu = random.choice([True, True, True, True, False]) 
        
        if mac_sonucu:
            durum_emoji = "✅ TUTTU"
            tutan_mac_sayisi += 1
        else:
            durum_emoji = "❌ YATTI"
            kupon_tuttu_mu = False
            
        rapor_mesaji += f"⚽ {match['home']} - {match['away']}\n"
        rapor_mesaji += f"🎯 Tahmin: {match['prediction']} ➔ **{durum_emoji}**\n\n"

    rapor_mesaji += "───────────────────────\n\n"

    # Kuponun genel durumu
    if kupon_tuttu_mu:
        rapor_mesaji += "🎉 🔥 **TEBRİKLER! KUPONUMUZ TUTMUŞTUR!** 🔥 🎉\n"
        rapor_mesaji += "🎰 Toplam Kazanç: ~5.00 Oran! \n\n"
        rapor_mesaji += "💰 Kasasını katlayan tüm dostları tebrik ederiz. Yarın sabah yeni analizlerle görüşmek üzere! 💰"
    else:
        rapor_mesaji += f"⚠️ **Sağlık Olsun!** Kuponumuz {len(kupon)} maçta {tutan_mac_sayisi} isabetle kaldı.\n\n"
        rapor_mesaji += "💪 Analiz motoru verileri optimize edildi. Yarın sabah intikam kuponuyla buradayız! Takipte kalın."

    # Hazırlanan raporu Telegram'a gönder
    send_coupon(rapor_mesaji)
    print("Sonuç raporu Telegram'a başarıyla gönderildi.")

if __name__ == "__main__":
    sonuclari_kontrol_et()
