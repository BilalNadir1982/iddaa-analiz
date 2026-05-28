import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_coupon(text_message):
    """
    Hazırlanan mesaj metnini Telegram API üzerinden kanala veya gruba iletir.
    """
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("HATA: BOT_TOKEN veya CHAT_ID ortam değişkenleri (Secrets) eksik!")
    
    # Telegram API URL'si
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text_message,
        "parse_mode": "Markdown"  # Emojilerin ve kalın yazıların düzgün görünmesi için
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        print(f"Telegram'a mesaj gönderilirken hata oluştu: {response.text}")
    else:
        print("Mesaj Telegram'a başarıyla iletildi.")
