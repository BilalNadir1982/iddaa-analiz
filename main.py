```python
# main.py

from analyzer import analyze_match
from coupon import create_coupon
from sender import send_coupon

# =========================================
# SAMPLE DATA
# API'DEN GELECEK
# =========================================

matches_data = [

    {
        "home": {
            "name": "Galatasaray",
            "wins_last5": 4,
            "points_last5": 12,
            "home_winrate": 80,
            "goals_scored_avg": 2.3,
            "first_half_goal_rate": 75,
            "h2h_winrate": 70,
            "missing_players": 0,
            "motivation": "title",
            "clean_sheet_rate": 60
        },

        "away": {
            "name": "Kasımpaşa",
            "wins_last5": 1,
            "points_last5": 4,
            "away_lossrate": 65,
            "goals_scored_avg": 1.1,
            "missing_players": 3
        }
    }

]

# =========================================
# ANALYZE
# =========================================

analyzed_matches = []

for match in matches_data:

    result = analyze_match(match)

    analyzed_matches.append(result)

# =========================================
# CREATE COUPON
# =========================================

coupon = create_coupon(analyzed_matches)

# =========================================
# SEND TELEGRAM
# =========================================

send_coupon(coupon)
```
