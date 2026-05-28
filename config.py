import os

# Telegram Ayarları
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Football-Data.org API Ayarları (Ücretsiz API Key'ini buraya koyacaksınız)
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "BURAYA_API_KEY_GELECEK")
API_BASE_URL = "https://api.football-data.org/v4/"

# Takip edilecek tüm liglerin kodları (Ücretsiz planda açık olan en popüler ligler)
TAKIP_EDILEN_LIGLER = {
    "BL1": "Almanya Bundesliga",
    "PL": "İngiltere Premier Lig",
    "PD": "İspanya La Liga",
    "SA": "İtalya Serie A",
    "FL1": "Fransa Ligue 1",
    "DED": "Hollanda Eredivisie",
    "PPL": "Portekiz Premier Lig"
    # Not: Ücretsiz planda Türkiye Süper Lig (TSL) bazen kısıtlı olabiliyor. 
    # Eğer API paketini yükseltirsen "TR" kodunu da ekleyebilirsin.
}
