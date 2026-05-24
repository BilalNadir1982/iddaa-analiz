import requests
from config import API_KEY

URL = "https://v3.football.api-sports.io/fixtures"

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_matches():

    r = requests.get(URL, headers=HEADERS)

    if r.status_code != 200:
        return []

    return r.json().get("response", [])
