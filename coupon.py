def format_coupon(matches):
    msg = "🤖 BOT ÇALIŞIYOR 🤖\n\n"
    for m in matches:
        msg += f"⚽ {m['home']} - {m['away']}\n📈 Tahmin: {m['prediction']} (%{m['confidence']})\n\n"
    return msg
