from telegram import Bot
import asyncio

async def send_to_channel(bot_token, channel_id, message):
    bot = Bot(token=bot_token)
    try:
        await bot.send_message(
            chat_id=channel_id,
            text=message,
            parse_mode='Markdown'
        )
        print("✅ Mesaj kanala gönderildi")
    except Exception as e:
        print(f"❌ Gönderme hatası: {e}")
