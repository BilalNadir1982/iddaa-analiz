import requests
from config import API_KEY

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

# Premier League örnek (39)
def get_fixtures(league=39, season=2024):

    url = f"{BASE_URL}/fixtures?league={league}&season={season}&next=20"

    r = requests.get(url, headers=HEADERS)
    data = r.json()

    return data["response"]
