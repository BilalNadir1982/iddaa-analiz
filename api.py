import requests
from datetime import datetime
import pytz

from config import API_KEY, TIMEZONE

HEADERS = {
    "x-apisports-key": API_KEY
}

BASE_URL = "https://v3.football.api-sports.io"

# =========================================
# BUGÜNÜN MAÇLARI
# =========================================

def get_matches():

    try:

        turkey = pytz.timezone(TIMEZONE)

        today = datetime.now(turkey).strftime("%Y-%m-%d")

        url = f"{BASE_URL}/fixtures"

        params = {
            "date": today,
            "timezone": TIMEZONE
        }

        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=30
        )

        print("STATUS:", response.status_code)

        data = response.json()

        print("API RESPONSE:", data)

        # =====================================
        # RESPONSE YOKSA
        # =====================================

        if "response" not in data:
            print("RESPONSE YOK")
            return []

        matches = data["response"]

        print("TOPLAM MAÇ:", len(matches))

        return matches

    except Exception as e:

        print("API ERROR:", e)

        return []
