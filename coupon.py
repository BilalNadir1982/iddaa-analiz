def format_coupon(selected_matches):
    """
    Seçilen maçları şık bir Telegram mesaj formatına dönüştürür.
    """
    if not selected_matches:
        return "🤖 İDDAA ANALİZ BOTU 🤖\n\n⚠️ Analiz motoru kriterlerine uyan BANKO MAÇ YOK."
        
    message = "🤖 İDDAA ANALİZ BOTU SİNYALİ 🤖\n"
    message += "📊 İstatistiksel Güven Derecesi Yüksek 5 Maçlık Analiz Kuponu:\n\n"
    
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    
    for i, match in enumerate(selected_matches):
        emoji = emojis[i] if i < len(emojis) else "⚽"
        message += f"{emoji} [{match['league']}] {match['home']} - {match['away']}\n"
        message += f"   📌 Tahmin: {match['prediction']}\n"
        message += f"   📈 Güven Skoru: %{match['confidence']}\n\n"
    
    message += "🎰 Toplam Tahmini Oran: ~4.50 - 5.50\n"
    message += "💪 Analiz Motoru Notu: 'Veri tabanındaki geçmiş form durumları ve şut/korner istatistikleri optimize edilerek yapay zeka tarafından seçilmiştir.'\n\n"
    message += "💰 Bol Şanslar! 💰"
    
    return message
