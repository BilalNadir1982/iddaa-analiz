def format_coupon(selected_matches):
    if not selected_matches: return "⚠️ Analiz kriterlerine uyan maç yok."
    
    # 1. Analiz Bölümü
    message = "🤖 İDDAA ANALİZ BOTU SİNYALİ 🤖\n📊 Detaylı Analizler:\n\n"
    for match in selected_matches:
        message += f"⚽ {match['home']} - {match['away']}\n📝 {match['detail']}\n📈 %{match['confidence']}\n\n"
        
    message += "───────────────────────\n\n🎫 **HAZIR KUPON ŞABLONU**\n\n"
    
    # 2. Dinamik Liste (Sınırsız Numaralandırma)
    for i, match in enumerate(selected_matches):
        message += f"{i+1}️⃣ {match['home']} - {match['away']} ➔ **{match['prediction']}**\n"
        
    message += "\n💰 **Bol Şanslar!**"
    return message
