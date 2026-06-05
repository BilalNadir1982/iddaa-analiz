import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://www.hurriyet.com.tr/spor/"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []
        for h in soup.find_all('h3', limit=3):
            text = h.get_text().strip()
            # Başlığın sonundaki sayıları (örn: -43192684) temizler
            clean_text = text.split('-')[0]
            headlines.append(f"📰 {clean_text}")
        return "\n".join(headlines)
    except:
        return "📰 Şu an haber akışına bağlanılamıyor."
