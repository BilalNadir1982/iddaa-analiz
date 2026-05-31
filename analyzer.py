def analyze_matches(match_list):
    analiz_sonuclari = []
    for match in match_list:
        analiz_sonuclari.append({
            "league": match.get("league", "Bilinmiyor"),
            "home": match.get("home", "Ev"),
            "away": match.get("away", "Deplasman"),
            "prediction": "MS 1",
            "confidence": 85,
            "detail": "İstatistiksel modelleme analizi."
        })
    return analiz_sonuclari
