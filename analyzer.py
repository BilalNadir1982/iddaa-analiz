import random

def analyze_match(match):

    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    # basit ama stabil model
    base = random.randint(45, 60)

    # MS tahmini
    if base > 55:
        ms = "1"
    elif base < 48:
        ms = "2"
    else:
        ms = "X"

    # KG
    kg = "VAR" if random.random() > 0.5 else "YOK"

    # 2.5
    over25 = "ÜST" if random.random() > 0.5 else "ALT"

    # ilk yarı
    first_half = "ÜST" if random.random() > 0.55 else "ALT"

    return {
        "ms": ms,
        "kg": kg,
        "over25": over25,
        "first_half": first_half
    }
