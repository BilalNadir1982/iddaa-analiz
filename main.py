def run_morning_session(raw_matches):
    # 1. Tüm maçları analiz et
    tum_analizler = analyze_matches(raw_matches)
    
    # 2. Kupon formatına dök
    mesaj = format_coupon(tum_analizler)
    
    # 3. Telegram'a gönder
    send_telegram_message(mesaj)
