import requests
from bs4 import BeautifulSoup

def get_latest_news():
    # Hurriyet Spor sayfası
    url = "https://www.hurriyet.com.tr/spor/"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []
        for h in soup.find_all('h3', limit=3): # İlk 3 başlığı al
            headlines.append(f"📰 {h.get_text().strip()}")
        return "\n".join(headlines)
    except:
        return "📰 Şu an haber akışına bağlanılamıyor."
