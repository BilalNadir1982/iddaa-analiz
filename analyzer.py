def analyze_matches(matches):
    """
    Basit analiz mantığı
    """
    good_bets = []
    
    for m in matches:
        # Basit value bet mantığı
        if m["home_odd"] > 2.0 and m["home_odd"] < 3.0:
            tip = "1 (Ev Sahibi)"
            confidence = "Orta"
            reason = "Ev sahibi avantajı + makul oran"
        elif m["away_odd"] > 2.5:
            tip = "2 (Deplasman)"
            confidence = "Orta-Yüksek"
            reason = "Deplasman takımı iyi formda"
        elif abs(m["home_odd"] - m["away_odd"]) < 0.3:
            tip = "X (Beraberlik)"
            confidence = "Düşük-Orta"
            reason = "Takımlar dengeli"
        else:
            continue
            
        good_bets.append({
            "match": m["match"],
            "league": m["league"],
            "time": m["time"],
            "tip": tip,
            "odds": m["home_odd"] if "1" in tip else m["away_odd"] if "2" in tip else m["draw_odd"],
            "reason": reason,
            "confidence": confidence
        })
    
    return good_bets[:8]  # Maksimum 8 öneri
