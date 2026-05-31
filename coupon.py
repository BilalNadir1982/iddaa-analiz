def format_coupon(selected_matches):
    message = "🤖 GÜNCEL MAÇ ANALİZLERİ 🤖\n\n"
    for match in selected_matches:
        message += f"⚽ {match['home']} - {match['away']}\n📈 Güven: %{match['confidence']}\n\n"
    message += "💰 Bol Şanslar!"
    return message
