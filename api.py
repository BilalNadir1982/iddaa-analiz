import requests
from config import ODDS_API_KEY

def get_matches():
    url = "https://api.the-odds-api.com/v4/sports/soccer/odds"

    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h,totals",
        "oddsFormat": "decimal"
    }

    r = requests.get(url, params=params)

    data = r.json()

    # ⚠️ güvenli dönüş
    if isinstance(data, list):
        return data

    return data.get("data", [])
