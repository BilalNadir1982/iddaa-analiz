import requests
import xml.etree.ElementTree as ET

def get_latest_news():
    # Örnek bir spor haber kaynağı (RSS)
    url = "https://www.ntv.com.tr/spor.rss"
    try:
        response = requests.get(url)
        root = ET.fromstring(response.content)
        news = []
        for item in root.findall('.//item'):
            title = item.find('title').text
            link = item.find('link').text
            news.append(f"📰 {title}\n🔗 {link}")
            if len(news) >= 3: break # İlk 3 haberi al
        return news
    except:
        return ["Haberler şu an güncellenemiyor."]
