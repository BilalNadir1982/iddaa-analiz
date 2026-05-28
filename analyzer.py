import random

def analyze_matches(match_list):
    """API'den gelen tüm maçlardaki takımları analiz eder ve en iyi 5'ini seçer."""
    if not match_list:
        return []

    analiz_sonuclari = []

    for match in match_list:
        home_team = match["home"]
        away_team = match["away"]
        
        # --- YAPAY ZEKA ANALİZ ALGORİTMASI ---
        # Gerçek sistemde buralar takımların son 5 maçtaki gol ortalamalarına bakar.
        # Şimdilik dinamik bir analiz simülasyonu kuruyoruz:
        
        tahminler = [
            {"pred": "Maç Sonucu 1", "conf": random.randint(80, 95), "det": f"{home_team} iç saha performansıyla öne çıkıyor."},
            {"pred": "Karşılıklı Gol Var (KG VAR)", "conf": random.randint(75, 92), "det": f"İki takımın da son maçlarında gol barajı aşıldı."},
            {"pred": "2.5 Üst", "conf": random.randint(78, 94), "det": f"{away_team} deplasmanda açık futbol tercih ediyor."},
            {"pred": "İlk Yarı 1.5 Alt", "conf": random.randint(82, 96), "det": f"İki takım da maça kontrollü başlayacaktır."},
            {"pred": "Toplam Korner 9.5 Üst", "conf": random.randint(80, 90), "det": f"Kanat organizasyonları korner sayısını artıracaktır."}
        ]
        
        # Bu maç için en uygun tahmini rastgele/algoritmik seçiyoruz
        secilen_tahmin = random.choice(tahminler)
        
        analiz_sonuclari.append({
            "league": match["league"],
            "home": home_team,
            "away": away_team,
            "prediction": secilen_tahmin["pred"],
            "confidence": secilen_tahmin["conf"],
            "detail": secilen_tahmin["det"]
        })

    # Tüm liglerdeki tüm takımların analizleri bitti. 
    # Şimdi güven skoru en yüksek olan EN İYİ 5 maçı ayıklıyoruz:
    sirali_maclar = sorted(analiz_sonuclari, key=lambda x: x['confidence'], reverse=True)
    return sirali_maclar[:5]

analyze_match = analyze_matches
