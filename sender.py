from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

def send_coupon(coupon):

    if not coupon:
        bot.send_message(CHAT_ID, "⚠️ BANKO MAÇ YOK")
        return

    text = "🏆 GÜNÜN BANKO KUPONU\n\n"

    for m in coupon:

        text += f"⚽ {m['home']} vs {m['away']}\n"
        text += f"🎯 Güven: %{m['score']}\n"
        text += f"📊 Tip: {m['signal']}\n"

        for r in m["reasons"]:
            text += f"• {r}\n"

        text += "\n"

    bot.send_message(CHAT_ID, text)
