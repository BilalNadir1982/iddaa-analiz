import json

def format_coupon(matches):
    msg = "💎 ═══  VIP YAPAY ZEKA ANALİZİ ═══ 💎\n🔥 İstatistik Analizleriyle Gecenin Gold Bülteni Hazır!\n\n"
    for m in matches:
        msg += f"🏆 {m['league']}\n⚽ {m['home']} vs {m['away']}\n🎯 Skor Tahmini: {m['score']}\n📊 Güven: %{m['confidence']} ➔ {m['prediction']}\n🔸 ─────────────────────── 🔸\n\n"
    msg += "🔔 Bildirimleri açmayı unutmayın!"
    return msg

def get_poll_data():
    return {"question": "Bu kupon tutar mı?", "options": json.dumps(["✅ Evet", "❌ Hayır"])}
