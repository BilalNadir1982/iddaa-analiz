def analyze_matches(match_list):
    """
    Gelen maç havuzunu filtreler ve en güvenilir 5 maçı seçer.
    """
    if not match_list:
        return []
    
    # Güven skoruna göre büyükten küçüğe sırala
    sorted_matches = sorted(match_list, key=lambda x: x['confidence'], reverse=True)
    
    # En iyi 5 maçı seçerek kupon oluşturucuya gönder
    selected_predictions = sorted_matches[:5]
    return selected_predictions
