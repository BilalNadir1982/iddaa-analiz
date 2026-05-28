```python
# analyzer.py

from datetime import datetime

# =========================================
# AI MATCH ANALYZER ENGINE
# =========================================

def analyze_match(match):

    home = match["home"]
    away = match["away"]

    score = 50
    reasons = []

    # =========================================
    # FORM ANALIZI
    # =========================================

    if home["wins_last5"] > away["wins_last5"]:
        score += 10
        reasons.append("Ev sahibi daha formda")

    if home["points_last5"] > away["points_last5"]:
        score += 5
        reasons.append("Son 5 maç puan üstünlüğü")

    # =========================================
    # IC SAHA / DEPLASMAN
    # =========================================

    if home["home_winrate"] >= 70:
        score += 10
        reasons.append("İç saha performansı güçlü")

    if away["away_lossrate"] >= 60:
        score += 8
        reasons.append("Rakip deplasmanda kötü")

    # =========================================
    # GOL ANALIZI
    # =========================================

    avg_goals = (
        home["goals_scored_avg"] +
        away["goals_scored_avg"]
    ) / 2

    if avg_goals >= 2.5:
        score += 7
        reasons.append("Gol ortalaması yüksek")

    # =========================================
    # ILK YARI ANALIZI
    # =========================================

    if home["first_half_goal_rate"] >= 70:
        score += 5
        reasons.append("İlk yarı etkili takım")

    # =========================================
    # H2H ANALIZI
    # =========================================

    if home["h2h_winrate"] >= 60:
        score += 8
        reasons.append("H2H üstünlüğü mevcut")

    # =========================================
    # SAKAT / EKSİK
    # =========================================

    if away["missing_players"] >= 3:
        score += 6
        reasons.append("Rakip eksik kadro")

    # =========================================
    # MOTIVASYON
    # =========================================

    if home["motivation"] == "title":
        score += 7
        reasons.append("Şampiyonluk motivasyonu")

    if home["motivation"] == "europe":
        score += 5
        reasons.append("Avrupa hedefi")

    # =========================================
    # CLEAN SHEET
    # =========================================

    if home["clean_sheet_rate"] >= 50:
        score += 4
        reasons.append("Defans formu iyi")

    # =========================================
    # SONUC
    # =========================================

    if score > 100:
        score = 100

    # =========================================
    # MARKET SECIMI
    # =========================================

    prediction = "MS1"

    if avg_goals >= 3:
        prediction = "2.5 ÜST"

    if (
        home["goals_scored_avg"] >= 1.5 and
        away["goals_scored_avg"] >= 1.2
    ):
        prediction = "KG VAR"

    # =========================================
    # SIGNAL
    # =========================================

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
        "prediction": prediction,
        "reasons": reasons
    }
```
