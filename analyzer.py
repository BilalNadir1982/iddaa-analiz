import random

FAVORITE_LEAGUES = [
    "Super Lig",
    "Premier League",
    "La Liga",
    "Serie A",
    "Bundesliga",
    "Ligue 1",
    "Champions League"
]

def analyze_match(match):

    home = match["home"]
    away = match["away"]

    hg = match["home_goals"]
    ag = match["away_goals"]

    minute = match["minute"]

    league = match["league"]

    total = hg + ag

    # =================================
    # BASE AI SCORE
    # =================================

    confidence = random.randint(55, 75)

    market = "NO BET"
    prediction = "Temkinli"

    # =================================
    # FAVORI LIG BONUS
    # =================================

    if league in FAVORITE_LEAGUES:
        confidence += 10

    # =================================
    # GOL ANALIZ
    # =================================

    if total >= 1:
        confidence += 8

    if total >= 2:
        confidence += 12

    # =================================
    # KG VAR
    # =================================

    if hg > 0 and ag > 0:

        market = "BTTS"

        prediction = "KG VAR güçlü"

        confidence += 15

    # =================================
    # OVER ANALIZ
    # =================================

    elif total >= 2:

        market = "OVER 2.5"

        prediction = "2.5 ÜST güçlü"

        confidence += 18

    # =================================
    # ILK YARI GOL
    # =================================

    elif minute < 35 and total >= 1:

        market = "İY 0.5 ÜST"

        prediction = "İlk yarı gol uygun"

        confidence += 15

    else:

        market = "UNDER 3.5"

        prediction = "Düşük risk"

        confidence += 5

    # =================================
    # LIMIT
    # =================================

    if confidence > 99:
        confidence = 99

    # =================================
    # BANKO FILTRE
    # =================================

    coupon = confidence >= 75

    # =================================
    # AI SCORE PREDICTION
    # =================================

    ph = random.randint(1, 3)
    pa = random.randint(0, 2)

    return {
        "home": home,
        "away": away,
        "league": league,
        "market": market,
        "prediction": prediction,
        "confidence": confidence,
        "coupon": coupon,
        "score_prediction": f"{ph}-{pa}"
    }
