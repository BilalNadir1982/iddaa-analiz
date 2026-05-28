```python
# stats.py

import requests
from config import API_KEY

BASE_URL = "https://api.football-data.org/v4"

HEADERS = {
    "X-Auth-Token": API_KEY
}

# =========================================
# TEAM LAST MATCHES
# =========================================

def get_team_stats(team_id):

    url = f"{BASE_URL}/teams/{team_id}/matches?limit=5"

    response = requests.get(
        url,
        headers=HEADERS
    )

    data = response.json()

    matches = data.get("matches", [])

    wins = 0
    goals = 0

    for match in matches:

        home_goals = match["score"]["fullTime"]["home"]
        away_goals = match["score"]["fullTime"]["away"]

        if home_goals is None:
            continue

        goals += home_goals + away_goals

        winner = match["score"]["winner"]

        if winner == "HOME_TEAM":
            wins += 1

    avg_goals = goals / 5 if goals else 0

    return {
        "wins_last5": wins,
        "goals_avg": round(avg_goals, 2)
    }
```
