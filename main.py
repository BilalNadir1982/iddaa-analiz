import pandas as pd
import numpy as np
from scipy.stats import poisson

print("✅ İddaa Analiz Programı Başladı!\n")

# Takım Verileri
takimlar = {
    "Galatasaray": {"ev_gol": 2.1, "dep_gol": 1.8, "form": 4.2},
    "Fenerbahce": {"ev_gol": 2.3, "dep_gol": 1.6, "form": 3.8},
    "Besiktas": {"ev_gol": 1.7, "dep_gol": 1.4, "form": 3.5},
    "Trabzonspor": {"ev_gol": 1.9, "dep_gol": 1.5, "form": 3.9},
    "Sivasspor": {"ev_gol": 1.4, "dep_gol": 1.2, "form": 3.0}
}

def mac_analiz_et(ev_takimi, dep_takimi):
    if ev_takimi not in takimlar or dep_takimi not in takimlar:
        print("❌ Takım verisi eksik!")
        return
    
    ev = takimlar[ev_takimi]
    dep = takimlar[dep_takimi]
    
    ev_gol = (ev["ev_gol"] + dep["dep_gol"]) / 2 * 1.15
    dep_gol = (dep["dep_gol"] + ev["ev_gol"]) / 2 * 0.9
    
    ev_win = 0
    draw = 0
    dep_win = 0
    
    for h in range(0, 7):
        for a in range(0, 7):
            prob = poisson.pmf(h, ev_gol) * poisson.pmf(a, dep_gol)
            if h > a:
                ev_win += prob
            elif h == a:
                draw += prob
            else:
                dep_win += prob
    
    print(f"\n🏠 {ev_takimi} - {dep_takimi}")
    print(f"Ev Galibiyeti : %{ev_win*100:.1f}")
    print(f"Beraberlik    : %{draw*100:.1f}")
    print(f"Deplasman     : %{dep_win*100:.1f}")
    print(f"Beklenen Gol  : {ev_gol:.2f} - {dep_gol:.2f}")

# Test maçları
mac_analiz_et("Galatasaray", "Fenerbahce")
mac_analiz_et("Besiktas", "Trabzonspor")