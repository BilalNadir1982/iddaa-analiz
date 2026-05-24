from telegram import Bot
from config import BOT_TOKEN

print("TOKEN:", BOT_TOKEN)

bot = Bot(token=BOT_TOKEN)

def send_message(text):

    try:

        bot.send_message(
            chat_id=CHAT_ID,
            text=text
        )

        print("MESAJ GÖNDERİLDİ")

    except Exception as e:

        print("TELEGRAM ERROR:", e)
