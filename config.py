import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")          # Telegram bot token
CHANNEL_ID = os.getenv("CHANNEL_ID")        # @kanaladi veya -100xxxxxxxxxx

# Scraping ayarları
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
