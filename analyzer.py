def analyze_match(match):

    home = match["home"]
    away = match["away"]

    score = 50
    reasons = []

    # FORM
    if home["form"] > away["form"]:
        score += 12
        reasons.append("Form üstünlüğü")

    # GOL
    if home["avg_goals"] > 2:
        score += 10
        reasons.append("Yüksek gol ortalaması")

    # İÇ SAHA
    if home["home_strength"] > 70:
        score += 10
        reasons.append("İç saha güçlü")

    # DEPLASMAN ZAYIF
    if away["away_weak"] > 60:
        score += 8
        reasons.append("Deplasman zayıf")

    # H2H
    if home["h2h"] > 60:
        score += 10
        reasons.append("H2H üstünlük")

    if score > 100:
        score = 100

    if score >= 85:
        signal = "BANKO"
    elif score >= 70:
        signal = "IDEAL"
    else:
        signal = "RISK"

    return {
        "home": home["name"],
        "away": away["name"],
        "score": score,
        "signal": signal,
        "reasons": reasons
    }
