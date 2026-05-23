import random

def analyze_match(match):

    base = random.randint(45, 65)

    # MS
    if base > 58:
        ms = "1"
    elif base < 50:
        ms = "2"
    else:
        ms = "X"

    # KG
    kg = "VAR" if random.random() > 0.5 else "YOK"

    # 2.5
    over25 = "ÜST" if random.random() > 0.5 else "ALT"

    # İY
    first_half = "ÜST" if random.random() > 0.55 else "ALT"

    # güven skoru (kupon filtresi)
    confidence = base + random.randint(-5, 5)

    return {
        "ms": ms,
        "kg": kg,
        "over25": over25,
        "first_half": first_half,
        "confidence": confidence
    }
