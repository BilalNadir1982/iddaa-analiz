def analyze_matches(match_list):
    # İstatistiksel analiz katmanı
    for m in match_list:
        m['prediction'] = "MS 1"
        m['confidence'] = 85
    return match_list
