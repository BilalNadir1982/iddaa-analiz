import os
from telegram import Bot

# ENV değişkenleri
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Güvenlik kontrolü (crash yerine net hata verir)
if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN bulunamadı! GitHub Secrets kontrol et.")

if not CHAT_ID:
    raise Exception("❌ CHAT_ID bulunamadı! GitHub Secrets kontrol et.")

# Bot başlat
bot = Bot(token=BOT_TOKEN)


def send_message(text):
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=text,
            parse_mode="HTML"
        )
    except Exception as e:
        print("Telegram mesaj hatası:", e)
