import json
import os

KUPON_DOSYASI = "son_kupon.json"

def son_kuponu_kaydet(secilen_maclar):
    """Sabah paylaşılan kupon verilerini gece kontrol etmek için kaydeder."""
    with open(KUPON_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(secilen_maclar, f, ensure_ascii=False, indent=4)
    print("Son kupon gece kontrolü için hafızaya kaydedildi.")

def son_kuponu_getir():
    """Gece kontrol edilmek üzere hafızadaki kuponu okur."""
    if os.path.exists(KUPON_DOSYASI):
        with open(KUPON_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
