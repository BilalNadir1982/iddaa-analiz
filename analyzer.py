# =========================================
# analyzer.py
# PRO AI BETTING ENGINE
# =========================================

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

    confidence = 50
    market = "NO BET"
    prediction = "Riskli"

    # ===================================
    # FAVORI LIG BONUS
    # ===================================

    if league in FAVORITE_LEAGUES:
        confidence += 10

    # ===================================
    # OVER ANALIZ
    # ===================================

    if total >= 2 and minute < 70:

        market = "OVER 2.5"
        prediction = "2.5 ÜST güçlü ihtimal"
        confidence += 25

    # ===================================
    # KG VAR
    # ===================================

    if hg > 0 and ag > 0:

        market = "BTTS"
        prediction = "KG VAR güçlü ihtimal"
        confidence += 20

    # ===================================
    # ILK YARI ANALIZ
    # ===================================

    if minute < 35 and total >= 1:

        confidence += 15

    # ===================================
    # BANKO FILTRE
    # ===================================

    if confidence >= 85:

        coupon = True

    else:

        coupon = False

    # ===================================
    # AI SKOR TAHMIN
    # ===================================

    predicted_home = random.randint(1, 3)
    predicted_away = random.randint(0, 2)

    score_prediction = f"{predicted_home}-{predicted_away}"

    return {
        "home": home,
        "away": away,
        "league": league,
        "prediction": prediction,
        "market": market,
        "confidence": confidence,
        "coupon": coupon,
        "score_prediction": score_prediction
    }
