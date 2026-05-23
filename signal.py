from analyzer import analyze_match

def generate_signal(match):
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    decision, score = analyze_match(home, away)

    if decision == "NO BET":
        return None

    return f"""
🔥 PRO ANALİZ MOTORU V2 🔥

⚽ {home} - {away}

📊 Sinyal: {decision}
📈 Güven: %{score}

⚠️ Bu analiz otomatik sistemdir
"""
