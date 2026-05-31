import random

def analyze_matches(match_list):
    results = []
    for m in match_list:
        # Rastgele ama mantıklı skor tahminleri üretelim
        skor1 = random.randint(1, 3)
        skor2 = random.randint(0, 2)
        guven = random.randint(75, 92)
        
        results.append({
            "league": m["league"],
            "home": m["home"],
            "away": m["away"],
            "score": f"{skor1} - {skor2}",
            "prediction": "Maç Sonucu 1" if skor1 > skor2 else "2.5 Üst",
            "confidence": guven
        })
    return results
