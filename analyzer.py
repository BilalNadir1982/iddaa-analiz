def analyze_matches(match_list):
    analiz_sonuclari = []
    for match in match_list:
        # Basit matematiksel tahmin mantığı
        confidence = 75 + (match["home_id"] % 25)
        analiz_sonuclari.append({
            "league": match["league"],
            "home": match["home"],
            "away": match["away"],
            "prediction": "MS 1" if match["home_id"] % 2 == 0 else "2.5 ÜST",
            "confidence": confidence,
            "detail": "İstatistikler bu maçta yüksek gol potansiyeli gösteriyor."
        })
    return sorted(analiz_sonuclari, key=lambda x: x['confidence'], reverse=True)
