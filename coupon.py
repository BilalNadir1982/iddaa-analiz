def format_coupon(selected_matches):
    if not selected_matches: return "⚠️ Analiz edilecek maç bulunamadı."
    
    message = "🤖 İDDAA ANALİZ BOTU SİNYALİ 🤖\n📊 Günün Tüm Maç Analizleri:\n\n"
    
    for match in selected_matches:
        message += f"⚽ {match['home']} - {match['away']} ({match['league']})\n"
        message += f"📝 Analiz: {match['detail']}\n"
        message += f"📈 Güven: %{match['confidence']}\n\n"
        
    message += "🎫 **HAZIR KUPON LİSTESİ** 🎫\n"
    for i, match in enumerate(selected_matches):
        message += f"{i+1}️⃣ {match['home']} - {match['away']} ➔ **{match['prediction']}**\n"
        
    message += "\n💰 **Bol Şanslar!**"
    return message
