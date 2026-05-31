def analyze_matches(match_list):
    if not match_list: return []
    analiz_sonuclari = []
    
    for match in match_list:
        # ... (API verisi çekme ve hesaplama mantığın aynı kalıyor) ...
        # (Tahmin mantığın burada çalışıyor)
        analiz_sonuclari.append({
            "league": match["league"], "home": match["home"], "away": match["away"],
            "prediction": prediction, "confidence": confidence, "detail": detail
        })
    
    # Kısıtlama yok, tüm maçları döndürüyoruz
    return sorted(analiz_sonuclari, key=lambda x: x['confidence'], reverse=True)
