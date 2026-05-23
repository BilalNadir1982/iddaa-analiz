import requests
import os
from datetime import date

API_KEY = os.getenv("FOOTBALL_API_KEY")

headers = {
    "x-apisports-key": API_KEY
}

def get_matches():
    today = str(date.today())

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    r = requests.get(url, headers=headers)

    data = r.json()

    return data["response"]
