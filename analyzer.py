def analyze_match(home, away):
    score = 50

    # basit güçlü takım mantığı (placeholder AI)
    strong_teams = [
        "Rangers", "Galatasaray", "Real Madrid",
        "Bayern", "Manchester City"
    ]

    if any(t in home for t in strong_teams):
        score += 20

    if any(t in away for t in strong_teams):
        score -= 10

    # rastgele varyasyon (maç çeşitliliği)
    import random
    score += random.randint(-10, 10)

    # tahmin seçimi
    if score >= 75:
        return "STRONG BUY", score
    elif score >= 60:
        return "BUY", score
    else:
        return "NO BET", score
