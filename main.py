from api import get_matches
from analyzer import analyze_match
from coupon import create_coupon
from sender import send_coupon

matches = get_matches()

analyzed = []

for m in matches:

    match_data = {
        "home": {
            "name": m["home"],
            "wins_last5": 4,
            "home_winrate": 75,
            "h2h_winrate": 60,
            "missing_players": 1
        },
        "away": {
            "name": m["away"],
            "wins_last5": 2,
            "missing_players": 3
        }
    }

    result = analyze_match(match_data)
    analyzed.append(result)

coupon = create_coupon(analyzed)

send_coupon(coupon)
