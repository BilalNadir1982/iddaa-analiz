```python
# sender.py

from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

# =========================================
# TELEGRAM SEND
# =========================================

def send_coupon(coupon):

    if not coupon:
        bot.send_message(
            chat_id=CHAT_ID,
            text="⚠️ Uygun BANKO kupon bulunamadı"
        )
        return

    msg = "🏆 GÜNÜN BANKO KUPONU\n\n"

    for i, match in enumerate(coupon, start=1):

        msg += (
            f"{i}. ⚽ {match['home']} vs {match['away']}\n"
            f"🎯 Tahmin: {match['prediction']}\n"
            f"🔥 Güven: %{match['score']}\n"
            f"📊 Tip: {match['signal']}\n\n"
        )

        msg += "Analiz:\n"

        for reason in match["reasons"]:
            msg += f"• {reason}\n"

        msg += "\n"

    bot.send_message(
        chat_id=CHAT_ID,
        text=msg
    )
```
