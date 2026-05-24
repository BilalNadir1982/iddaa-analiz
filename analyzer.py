import random

def analyze_match(match):

    try:

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        league = match["league"]["name"]

        status = match["fixture"]["status"]["short"]

        allowed = [
            "NS",
            "1H",
            "HT",
            "2H",
            "LIVE"
        ]

        if status not in allowed:
            return None

        score = 0

        # =====================================
        # CANLI BONUS
        # =====================================

        if status in ["1H", "2H", "LIVE"]:
            score += 30

        # =====================================
        # GOL BONUS
        # =====================================

        goals_home = match["goals"]["home"]
        goals_away = match["goals"]["away"]

        if goals_home is not None and goals_away is not None:

            total = goals_home + goals_away

            if total >= 2:
                score += 25

        # =====================================
        # TAHMİN
        # =====================================

        if score >= 40:
            prediction = "ÜST 2.5"
            emoji = "🔥"

        else:
            prediction = "KG VAR"
            emoji = "⚽"

        return f"""
{emoji} MAÇ ANALİZİ

🏆 {league}

⚔️ {home} vs {away}

📊 Tahmin: {prediction}

📈 Skor: {score}

⏱ Durum: {status}
"""

    except Exception as e:

        print("ANALYZER ERROR:", e)

        return None
