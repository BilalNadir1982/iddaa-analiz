def analyze_matches(match_list):
    results = []
    for m in match_list:
        results.append({
            "league": m["league"],
            "home": m["home"],
            "away": m["away"],
            "prediction": "MS 1",
            "confidence": 95
        })
    return results
