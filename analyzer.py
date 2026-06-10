import random

def analyze_matches(match_list):
    results = []
    # İddaa kuponlarında en çok tercih edilen kombine seçenekleri
    prediction_options = [
        {"pred": "Maç Sonucu 1", "odd": 1.65},
        {"pred": "2.5 Üst", "odd": 1.70},
        {"pred": "Karşılıklı Gol Var", "odd": 1.60},
        {"pred": "Maç Sonucu 2", "odd": 2.15},
        {"pred": "1.5 Üst", "odd": 1.35},
        {"pred": "Çifte Şans 1-X", "odd": 1.40}
    ]
    
    for m in match_list:
        option = random.choice(prediction_options)
        skor1 = random.randint(1, 3)
        skor2 = random.randint(0, 2)
        
        results.append({
            "league": m["league"],
            "home": m["home"],
            "away": m["away"],
            "score": f"{skor1} - {skor2}",
            "prediction": option["pred"],
            "odd": option["odd"],
            "confidence": random.randint(82, 96)
        })
    return results
