def format_coupon(matches):
    msg = ""
    for m in matches:
        # Daha kısa bir format
        msg += f"🏆 {m['league']}\n⚽ {m['home']} vs {m['away']}\n🎯 Skor Tahmini: {m['score']}\n📊 %{m['confidence']} ➔ {m['prediction']}\n────────\n"
    return msg
