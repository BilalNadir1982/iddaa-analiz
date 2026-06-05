import requests
import xml.etree.ElementTree as ET

def get_latest_news():
    url = "https://www.ntv.com.tr/spor.rss" # Spor haberleri kaynağı
    try:
        response = requests.get(url, timeout=10)
        root = ET.fromstring(response.content)
        news = []
        for item in root.findall('.//item'):
            title = item.find('title').text
            news.append(f"📰 {title}")
            if len(news) >= 3: break
        return "\n".join(news)
    except:
        return "📰 Güncel spor haberleri şu an alınamadı."
