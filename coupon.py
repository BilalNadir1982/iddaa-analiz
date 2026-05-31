def format_coupon(matches):
    msg = "💎 ═══  VIP YAPAY ZEKA ANALİZİ ═══ 💎\n"
    msg += "🔥 İstatistik Analizleriyle Gecenin Gold Bülteni Hazır!\n\n"
    
    for m in matches:
        msg += f"🏆 {m['league']}\n"
        msg += f"⚽ {m['home']} vs {m['away']}\n"
        msg += f"🎯 Yapay Zeka Skor Tahmini: {m['score']} 👈\n"
        msg += f"📊 Güven Skoru / Tahmin: % {m['confidence']} ➔ {m['prediction']}\n"
        msg += "🔸 ─────────────────────── 🔸\n\n"
        
    msg += "🔔 Bildirimleri açmayı ve kuponları takip etmeyi unutmayın!"
    return msg
