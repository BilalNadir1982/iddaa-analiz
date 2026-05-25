def analyze_match(match):

    hg = match["home_goals"]
    ag = match["away_goals"]

    total = hg + ag

    minute = match["minute"]

    prediction = ""
    confidence = 0
    market = ""

    # ==========================
    # OVER ANALIZ
    # ==========================

    if total >= 2 and minute < 70:

        prediction = "2.5 ÜST güçlü ihtimal"

        confidence = 82

        market = "OVER 2.5"

    elif hg > 0 and ag > 0:

        prediction = "KG VAR uygun"

        confidence = 76

        market = "BTTS"

    elif total == 0 and minute > 60:

        prediction = "ALT bahis uygun"

        confidence = 71

        market = "UNDER 2.5"

    else:

        prediction = "Temkinli maç"

        confidence = 55

        market = "NO BET"

    return {
        "prediction": prediction,
        "confidence": confidence,
        "market": market
    }
