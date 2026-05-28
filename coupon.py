def format_coupon(selected_matches):
    """
    Seçilen maçları hem detaylı analiz hem de sadece oynanabilir 
    sade kupon formatında tek bir mesajda (veya bölünmüş olarak) hazırlar.
    """
    if not selected_matches:
        return "🤖 İDDAA ANALİZ BOTU 🤖\n\n⚠️ Analiz motoru kriterlerine uyan BANKO MAÇ YOK."
        
    # --- 1. BÖLÜM: DETAYLI ANALİZLER ---
    message = "🤖 İDDAA ANALİZ BOTU SİNYALİ 🤖\n"
    message += "📊 Yapay Zeka Detaylı Maç Analizleri:\n\n"
    
    for i, match in enumerate(selected_matches):
        message += f"⚽ {match['home']} - {match['away']} ({match['league']})\n"
        message += f"📝 **Analiz:** {match['detail']}\n"
        message += f"📈 **Güven Skoru:** %{match['confidence']}\n\n"
        
    message += "───────────────────────\n\n"
    
    # --- 2. BÖLÜM: SADECE KUPON SEKLİNDE GÖRÜNÜM ---
    message += "🎫 **HAZIR KUPON ŞABLONU** 🎫\n"
    message += "✍️ *Direkt oynanabilir sade liste:*\n\n"
    
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for i, match in enumerate(selected_matches):
        emoji = emojis[i] if i < len(emojis) else "🔹"
        message += f"{emoji} {match['home']} - {match['away']} ➔ **{match['prediction']}**\n"
        
    message += "\n🎰 **Toplam Tahmini Oran:** ~4.50 - 5.50\n"
    message += "💰 **Bol Şanslar!** 💰"
    
    return message
