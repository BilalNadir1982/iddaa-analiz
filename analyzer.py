IMPORTANT_LEAGUES = [

    "Super Lig",
    "Premier League",
    "La Liga",
    "Serie A",
    "Bundesliga",
    "Ligue 1",

    "Champions League",
    "Europa League",

    "Eredivisie",
    "Primeira Liga",

    "Championship",

    "Süper Lig"
]

def analyze_match(match):

    try:

        league = match["league"]["name"]

        # ====================================
        # SADECE ÖNEMLİ LİGLER
        # ====================================

        if not any(x.lower() in league.lower() for x in IMPORTANT_LEAGUES):
            return None

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        status = match["fixture"]["status"]["short"]

        goals_home = match["goals"]["home"] or 0
        goals_away = match["goals"]["away"] or 0

        total_goals = goals_home + goals_away

        score = 0

        # ====================================
        # CANLI MAÇ BONUS
        # ====================================

        if status in ["1H", "HT", "2H", "LIVE"]:
            score += 40

        # ====================================
        # GOL BONUS
        # ====================================

        if total_goals >= 1:
            score += 20

        if total_goals >= 2:
            score += 30

        if total_goals >= 3:
            score += 40

        # ====================================
        # TAHMİN
        # ====================================

        prediction = None
        emoji = "⚽"

        if score >= 70:
            prediction = "ÜST 2.5"
            emoji = "🔥"

        elif score >= 50:
            prediction = "KG VAR"

        else:
            return None

        # ====================================
        # MESAJ
        # ====================================

        return f"""
{emoji} CANLI MAÇ ANALİZİ

🏆 {league}

⚔️ {home} vs {away}

🥅 Skor: {goals_home} - {goals_away}

📊 Tahmin: {prediction}

📈 Güven Skoru: {score}

⏱ Durum: {status}
"""

    except Exception as e:

        print("ANALYZER ERROR:", e)

        return None
