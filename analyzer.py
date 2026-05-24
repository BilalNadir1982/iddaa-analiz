def calc_form(last5):
    return sum(last5) / len(last5)


ALLOWED_LEAGUES = {
    "Premier League",
    "Championship",
    "La Liga",
    "Bundesliga",
    "Serie A",
    "Ligue 1",
    "La Liga 2",
    "Serie B",
    "2. Bundesliga",
    "Eredivisie",
    "Primeira Liga",
    "Süper Lig",
    "1. Lig"
}


def analyze_match(match):

    league = match["league"]["name"]

    if league not in ALLOWED_LEAGUES:
        return None

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    # ---------------- demo stats (API bağlanınca gerçek olur)
    home_form = 0.8
    away_form = 0.6

    home_attack = 1.7
    away_attack = 1.2

    home_def = 1.0
    away_def = 1.3

    # ---------------- gol modeli
    home_exp = (home_attack + away_def) / 2
    away_exp = (away_attack + home_def) / 2

    total = home_exp + away_exp

    # ---------------- MS
    if home_form > away_form + 0.1:
        ms = "MS1"
    elif away_form > home_form + 0.1:
        ms = "MS2"
    else:
        ms = "MSX"

    # ---------------- KG
    if home_exp > 1 and away_exp > 0.8:
        kg = "KG VAR"
    else:
        kg = "KG YOK"

    # ---------------- gol
    if total >= 2.6:
        goal = "2.5 ÜST"
    else:
        goal = "2.5 ALT"

    # ---------------- confidence
    confidence = int(60 + (home_form - away_form) * 50)
    confidence = max(45, min(95, confidence))

    if confidence >= 80:
        risk = "🟢 BANKO"
    elif confidence >= 60:
        risk = "🟡 ORTA"
    else:
        risk = "🔴 RİSKLİ"

    return f"""
⚽ MAÇ ANALİZİ

🏆 {home} vs {away}
🏆 Lig: {league}

🎯 MS: {ms}
🎯 KG: {kg}
🎯 Gol: {goal}

📊 Güven: %{confidence}
📌 Seviye: {risk}
"""
