def format_coupon(matches):
    if not matches:
        return "⚠️ Kupon oluşturulacak yeterli maç bulunamadı."
    
    # Kombine için en fazla 3 maç seçelim (Gereksiz uzamasın)
    kombine_list = matches[:3]
    
    msg = "🔥 *GÜNÜN ALTIN KOMBİNE KUPONU* 🔥\n"
    msg += "⚡ _Yapay Zeka Tarafından Optimize Edildi_\n\n"
    
    total_odds = 1.0
    
    for i, m in enumerate(kombine_list, 1):
        msg += f"📍 *{i}. MAÇ:* {m['home']} - {m['away']}\n"
        msg += f"🏆 Lig: {m['league']}\n"
        msg += f"🎯 Tahmin: *{m['prediction']}*\n"
        msg += f"📈 Oran: `{m['odd']}` | Güven: %{m['confidence']}\n"
        msg += f"📊 Skor Analizi: {m['score']}\n"
        msg += "───────────────────\n"
        total_odds *= m['odd']
    
    # Toplam oranı virgülden sonra 2 basamak olacak şekilde hesapla
    clean_total_odds = round(total_odds, 2)
    
    msg += f"\n💰 *TOPLAM ORAN: {clean_total_odds}*\n"
    msg += "🚀 *Kupon Güven Derecesi:* 🌟🌟🌟🌟☆\n"
    msg += "🔔 _Bol Şanslar! Kuponumuz Hazır._"
    return msg
