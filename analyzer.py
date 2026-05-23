import random

def analyze_match(match):

    prob = random.randint(55, 85)
    value = prob - random.randint(40, 65)

    ms = "1" if prob > 65 else "X" if prob > 55 else "2"
    kg = "VAR" if prob > 60 else "YOK"
    over25 = "ÜST" if prob > 62 else "ALT"
    iy = "ÜST" if prob > 60 else "ALT"

    return {
        "ms": ms,
        "kg": kg,
        "over25": over25,
        "iy": iy,
        "prob": prob,
        "value": value
    }
