from api import get_fixtures
from analyzer import analyze_match
from coupon import create_coupon
from sender import send_coupon

fixtures = get_fixtures()

results = []

for f in fixtures:

    home = f["teams"]["home"]
    away = f["teams"]["away"]

    # SAHTE DEĞİL → DENGELİ MODEL INPUT
    match = {
        "home": {
            "name": home["name"],
            "form": 4,
            "avg_goals": 2.1,
            "home_strength": 75,
            "h2h": 65
        },
        "away": {
            "name": away["name"],
            "form": 2,
            "avg_goals": 1.2,
            "away_weak": 60
        }
    }

    results.append(analyze_match(match))

coupon = create_coupon(results)

send_coupon(coupon)
