def analyze_matches(matches):
    analyses = []
    for match in matches:
        # Basit kural: home favori, tahmin "1"
        # Sonraki aşamada form, gol ortalaması vs eklenebilir
        analyses.append({
            "match": f"{match['home']} - {match['away']}",
            "prediction": "1",  # MS1 = ev sahibi galibiyeti
            "confidence": 70    # Basit sabit değer
        })
    return analyses

if __name__ == "__main__":
    sample = [
        {"home": "Galatasaray", "away": "Fenerbahçe", "league": "Süper Lig"}
    ]
    print(analyze_matches(sample))
