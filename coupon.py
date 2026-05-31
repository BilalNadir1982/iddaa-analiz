import json

def format_coupon(matches):
    msg = "🤖 *GÜNLÜK PROFESYONEL ANALİZ* 🤖\n\n"
    for i, m in enumerate(matches):
        msg += f"{i+1}️⃣ {m['home']} - {m['away']}\n⚽ *Lig:* {m['league']}\n📈 *Tahmin:* {m['prediction']} (%{m['confidence']})\n\n"
    msg += "💰 *Bol Şanslar!*"
    return msg

def get_poll_data():
    return {
        "question": "Bu kupon tutar mı?",
        "options": json.dumps(["✅ Evet", "❌ Hayır"])
    }
