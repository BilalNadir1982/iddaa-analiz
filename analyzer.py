def analyze_match(match):

    home = match["home"]
    away = match["away"]

    score = 50
    reasons = []

    if home["wins_last5"] > away["wins_last5"]:
        score += 10
        reasons.append("Form üstünlüğü")

    if home["home_winrate"] > 70:
        score += 10
        reasons.append("İç saha güçlü")

    if away["missing_players"] >= 3:
        score += 8
        reasons.append("Rakip eksik")

    if home["h2h_winrate"] > 60:
        score += 8
        reasons.append("H2H avantaj")

    if score > 100:
        score = 100

    if score >= 85:
        signal = "BANKO"
    elif score >= 70:
        signal = "IDEAL"
    else:
        signal = "RISKLI"

    return {
        "home": home["name"],
        "away": away["name"],
        "score": score,
        "signal": signal,
        "reasons": reasons
    }
