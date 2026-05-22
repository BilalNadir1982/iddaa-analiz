import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://v3.football.api-sports.io"

headers = {
    "x-apisports-key": API_KEY
}

def get_todays_matches():
    url = f"{BASE_URL}/fixtures?date=2026-05-22"
    response = requests.get(url, headers=headers)
    return response.json()
