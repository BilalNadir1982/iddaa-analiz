import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID") # Eğer kanala atıyorsan kanal id'si, gruba atıyorsan grup id'si

def send_coupon(text_message):
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN eksik!")
        
    bot = Bot(token=BOT_TOKEN)
    
    # Not: GitHub Actions'ta async yapısı sorun çıkarmasın diye telegram kütüphanesinin 
    # sürümüne göre direkt ya da bot.send_message şeklinde çağrılır.
    # Eğer mevcut kodun zaten çalışıyorsa buradaki mantığı hiç bozma, sadece gelen 'text_message'ı ilet.
    bot.send_message(chat_id=CHAT_ID, text=text_message)
