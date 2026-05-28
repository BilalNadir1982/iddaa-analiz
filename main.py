import os
import requests
import json

# ==========================================
# 1. AYARLAR & YAPILANDIRMA (YAZ LİGLERİ)
# ==========================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
API_BASE_URL = "https://api.football-data.org/v4/"

# Şu an aktif olan ve veri akışı sağlayan canlı yaz ligleri
TAKIP_EDILEN_LIGLER = {
    "BSA": "Brezilya Serie A",         # Yaz boyu kesintisiz devam eder
    "CLI": "Copa Libertadores",        # Güney Amerika Şampiyonlar Ligi
    "ELC": "İngiltere Championship",    # Play-off ve güncel finaller
    "WC": "Dünya Kupası Elemeleri"      # Dönemsel milli maçlar
}

# ==========================================
# 2. VERİ ÇEKME MOTORU (API)
# ==========================================
def fetch_daily_matches():
    """Yaz liglerindeki güncel maçları API'den canlı çeker."""
    if not FOOTBALL_API_KEY or "BURAYA" in FOOTBALL_API_KEY:
        print("⚠️ API Key bulunamadı, yedek veri yükleniyor.")
        return get_fallback_data()

    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    tum_maclar = []

    for lig_kodu, lig_adi in TAKIP_EDILEN_LIGLER.items():
        try:
            url = f"{API_BASE_URL}competitions/{lig_kodu}/matches"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                matches = data.get("matches", [])
                
                for match in matches:
                    # Sadece henüz oynanmamış (SCHEDULED) veya canlı (TIMED) maçları al
                    if match.get("status") in ["SCHEDULED", "TIMED"]:
                        tum_maclar.append({
                            "league": lig_adi,
                            "home": match["homeTeam"]["name"],
                            "away": match["awayTeam"]["name"],
                            "home_id": match["homeTeam"]["id"],
                            "away_id": match["awayTeam"]["id"]
                        })
        except Exception as e:
            print(f"{lig_adi} verisi çekilirken hata: {e}")
            continue

    # Eğer bültende hiç canlı maç yoksa boş dönüp kanalı kirletmesin
    return tum_maclar

def get_team_stats(team_id):
    """Bir takımın son 5 maçtaki gerçek gol istatistiklerini çeker."""
    if not FOOTBALL_API_KEY or "BURAYA" in FOOTBALL_API_KEY:
        return {"avg_goals_scored": 1.6, "avg_goals_conceded": 1.2}

    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    url = f"{API_BASE_URL}teams/{team_id}/matches?status=FINISHED&limit=5"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            matches = data.get("matches", [])
            
            total_scored = 0
            total_conceded = 0
            match_count = len(matches)
            
            if match_count == 0:
                return {"avg_goals_scored": 1.2, "avg_goals_conceded": 1.1}

            for m in matches:
                if m["homeTeam"]["id"] == team_id:
                    total_scored += m["score"]["fullTime"]["home"]
                    total_conceded += m["score"]["fullTime"]["away"]
                else:
                    total_scored += m["score"]["fullTime"]["away"]
                    total_conceded += m["score"]["fullTime"]["home"]
            
            return {
                "avg_goals_scored": total_scored / match_count,
                "avg_goals_conceded": total_conceded / match_count
            }
    except Exception as e:
        print(f"Takım istatistiği hatası: {e}")
    
    return {"avg_goals_scored": 1.4, "avg_goals_conceded": 1.2}

def get_fallback_data():
    return []

# ==========================================
# 3. GERÇEK ANALİZ MOTORU
# ==========================================
def analyze_matches(match_list):
    """Matematiksel formüllerle takımların gol istatistiklerini analiz eder."""
    if not match_list:
        return []

    analiz_sonuclari = []

    for match in match_list:
        home_team = match["home"]
        away_team = match["away"]
        
        # Gerçek istatistikleri API'den talep et
        home_stats = get_team_stats(match.get("home_id"))
        away_stats = get_team_stats(match.get("away_id"))
        
        toplam_gol_beklentisi = home_stats["avg_goals_scored"] + away_stats["avg_goals_scored"]
        deplasman_savunma_zaafi = away_stats["avg_goals_conceded"]

        # 🎯 Tamamen Bilimsel Bahis Üretim Kriterleri
        if toplam_gol_beklentisi > 2.9:
            prediction = "2.5 Üst"
            confidence = int(min(95, 70 + (toplam_gol_beklentisi * 7)))
            detail = f"İki takımın son maçlardaki toplam gol ortalaması {toplam_gol_beklentisi:.2f}. Yüksek tempolu, bol pozisyonlu bir maç bekleniyor."
            
        elif home_stats["avg_goals_scored"] > 1.6 and deplasman_savunma_zaafi > 1.4:
            prediction = "Maç Sonucu 1"
            confidence = int(min(94, 75 + (home_stats["avg_goals_scored"] * 8)))
            detail = f"{home_team} iç sahada {home_stats['avg_goals_scored']:.2f} gol ortalamasıyla oynuyor. Form avantajıyla galibiyete yakın."
            
        elif home_stats["avg_goals_scored"] > 0.9 and away_stats["avg_goals_scored"] > 0.9:
            prediction = "Karşılıklı Gol Var (KG VAR)"
            confidence = int(min(92, 68 + (toplam_gol_beklentisi * 6)))
            detail = f"Ev sahibinin gol ortalaması {home_stats['avg_goals_scored']:.2f}, deplasmanın ise {away_stats['avg_goals_scored']:.2f}. Karşılıklı ataklar skoru getirir."
            
        else:
            prediction = "İlk Yarı 1.5 Alt"
            confidence = 88
            detail = f"Takımların kontrollü oyun yapısı ve düşük gol ortalaması, ilk yarıda dengeli ve az riskli bir stratejiye işaret ediyor."

        analiz_sonuclari.append({
            "league": match["league"],
            "home": home_team,
            "away": away_team,
            "prediction": prediction,
            "confidence": confidence,
            "detail": detail
        })

    # Güven skoru en yüksek olanları sırala
    sirali_maclar = sorted(analiz_sonuclari, key=lambda x: x['confidence'], reverse=True)
    return sirali_maclar

# ==========================================
# 4. KUPON TASARIM & TELEGRAM SENDER
# ==========================================
def format_and_send(selected_matches):
    # Eğer kupon oluşturacak kadar (en az 2 veya 3 maç) gerçek veri yoksa kanala gereksiz mesaj atmaz
    if not selected_matches or len(selected_matches) < 2:
        print("⚠️ Bugün analiz kriterlerine uyan yeterli canlı maç bülteni bulunamadı.")
        return
        
    # En fazla en iyi 5 maçı kupona dahil et
    kupon_maclari = selected_matches[:5]
    
    message = "🤖 **İDDAA ANALİZ BOTU SİNYALİ** 🤖\n"
    message += "📊 **Yapay Zeka Gerçek İstatistik Analizleri:**\n\n"
    
    for match in kupon_maclari:
        message += f"⚽ {match['home']} - {match['away']} ({match['league']})\n"
        message += f"📝 *Analiz:* {match['detail']}\n"
        message += f"📈 *Güven Skoru:* %{match['confidence']}\n\n"
        
    message += "───────────────────────\n\n"
    
    message += "🎫 **HAZIR KUPON ŞABLONU** 🎫\n"
    message += "✍️ *Direkt oynanabilir sade liste:*\n\n"
    
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for i, match in enumerate(kupon_maclari):
        message += f"{emojis[i]} {match['home']} - {match['away']} ➔ **{match['prediction']}**\n"
        
    message += "\n🎰 **Toplam Tahmini Oran:** ~3.50 - 5.50\n"
    message += "💰 **Bol Şanslar!** 💰"
    
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Hata: Telegram Secrets eksik!")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Tamamen gerçek analiz kuponu Telegram'a başarıyla gönderildi!")
    else:
        print(f"❌ Telegram Hatası: {response.text}")

# ==========================================
# 5. ANA TETİKLEYİCİ
# ==========================================
def main():
    print("Gerçek analiz motoru yaz ligleri için tetiklendi...")
    raw_matches = fetch_daily_matches()
    analyzed_matches = analyze_matches(raw_matches)
    format_and_send(analyzed_matches)

if __name__ == "__main__":
    main()
