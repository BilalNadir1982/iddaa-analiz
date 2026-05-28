```python
# main.py

from api import get_matches
from analyzer import analyze_match
from coupon import create_coupon
from sender import send_coupon

# =========================================
# GET MATCHES
# =========================================

matches = get_matches()

analyzed = []

for m in matches:

    try:

        fake_match = {

            "home": {
                "name": m["home"],
                "wins_last5": 4,
                "points_last5": 11,
                "home_winrate": 75,
                "goals_scored_avg": 2.1,
                "first_half_goal_rate": 70,
                "h2h_winrate": 65,
                "missing_players": 1,
                "motivation": "title",
                "clean_sheet_rate": 55
            },

            "away": {
                "name": m["away"],
                "wins_last5": 1,
                "points_last5": 4,
                "away_lossrate": 65,
                "goals_scored_avg": 1.0,
                "missing_players": 3
            }
        }

        result = analyze_match(fake_match)

        analyzed.append(result)

    except Exception as e:
        print(e)

# =========================================
# CREATE COUPON
# =========================================

coupon = create_coupon(analyzed)

# =========================================
# SEND
# =========================================

send_coupon(coupon)
```
