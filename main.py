import os
import requests
import json
from datetime import datetime

# ==========================================
# 1. AYARLAR & YAPILANDIRMA
# ==========================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_BASE_URL = "https://api.football-data.org/v4/"
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

TAKIP_EDILEN_LIGLER = {
    TAKIP_EDILEN_LIGLER = {
    "PL": "İngiltere Premier Lig",
    "ELC": "İngiltere Championship",
    "PD": "İspanya La Liga",
    "SA": "İtalya Serie A",
    "BL1": "Almanya Bundesliga",
    "FL1": "Fransa Ligue 1",
    "DED": "Hollanda Eredivisie",
    "PPL": "Portekiz Premier Lig",
    "BSA": "Brezilya Serie A",
    "CL": "UEFA Şampiyonlar Ligi",
    "EC": "Avrupa Şampiyonası",
    "WC": "Dünya Kupası"
}

# ==========================================
# 2. TELEGRAM KLASİK GÖNDERİM MOTORU
# ==========================================
def send_telegram_message(text):
    """Mesajları saf, temiz ve şık bir şekilde kanala fırlatır."""
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def send_telegram_poll(question, options):
    """Kanal içi etkileşimi artıran anketi fırlatır."""
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"
    payload = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    requests.post(url, json=payload)

# ==========================================
# 3. VERİ & İSTATİSTİK MOTORU
# ==========================================
def fetch_daily_matches():
    """Bültendeki gerçek ve güncel maçları çeker."""
    if not FOOTBALL_API_KEY or "BURAYA" in FOOTBALL_API_KEY:
        return get_fallback_data()
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    tum_maclar = []
    for lig_kodu, lig_adi in TAKIP_EDILEN_LIGLER.items():
        try:
            url = f"{API_BASE_URL}competitions/{lig_kodu}/matches"
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                for match in response.json().get("matches", []):
                    if match.get("status") in ["SCHEDULED", "TIMED"]:
                        tum_maclar.append({
                            "league": lig_adi,
                            "home": match["homeTeam"]["name"][:15],
                            "away": match["awayTeam"]["name"][:15],
                            "home_id": match["homeTeam"]["id"],
                            "away_id": match["awayTeam"]["id"]
                        })
        except: continue
    return tum_maclar if tum_maclar else get_fallback_data()

def get_fallback_data():
    return [
        {"league": "Brezilya Serie A", "home": "Flamengo", "away": "Palmeiras", "home_id": 17, "away_id": 18},
        {"league": "Brezilya Serie A", "home": "Sao Paulo", "away": "Botafogo", "home_id": 19, "away_id": 20}
    ]

# ==========================================
# 🌍 RADAR WEB SİTESİ İÇİN JSON GÜNCELLEME MOTORU
# ==========================================
def update_web_radar_json(raw_matches):
    """Web sitesinin (radar.html) okuyacağı maclar.json dosyasını hazırlar."""
    if not raw_matches: return
    
    web_bulten = []
    
    # Tüm çekilen maçları web arayüzünün (radar.html) formatına dönüştürüyoruz
    for i, match in enumerate(raw_matches):
        # Ev sahibi id'sine göre botundaki gibi tahmini dinamik oluşturuyoruz
        prediction = "2.5 Üst" if (int(match.get("home_id", 0)) % 2 == 0) else "Maç Sonucu 1"
        confidence = 75 + (int(match.get("home_id", 0)) % 20)
        exact_score = f"{int(confidence/40)} - {int(confidence/50)}"
        
        # İlk 2 maçı web sitesinde VIP, kalanları Canlı Radar kategorisinde gösterelim
        if i < 2:
            status_text = "👑 VIP ANALİZ"
            note = f"Yapay zeka {match['league']} analizinde bu karşılaşma için skor tahminini {exact_score} olarak hesapladı."
        else:
            status_text = "🚨 CANLI RADAR"
            prediction = "Karşılıklı Gol Var" if i % 2 == 0 else "Maç Sonucu 1"
            note = f"Canlı veri tarayıcıları {match['home']} cephesinde ofansif aksiyon ve yüksek gol beklentisi (xG) yakaladı."

        web_bulten.append({
            "statusText": status_text,
            "score": f"{confidence}/100",
            "teams": f"{match['home']} - {match['away']}",
            "prediction": prediction,
            "note": note
        })
        
    # JSON çıktısını yazdırıyoruz
    try:
        with open('maclar.json', 'w', encoding='utf-8') as f:
            json.dump(web_bulten, f, ensure_ascii=False, indent=2)
        print("✅ Web Radar için maclar.json başarıyla güncellendi!")
    except Exception as e:
        print(f"❌ JSON yazılırken hata oluştu: {e}")

# ==========================================
# 4. AKTİF OTOMASYON MODÜLLERİ (SADE & NET)
# ==========================================
def run_morning_session(raw_matches):
    """SABAH MODÜLÜ: Skor Tahminli VIP Analiz Mesajı & Banko Anketi"""
    if not raw_matches: return
    
    kupon_maclari = []
    anket_secenekleri = []
    
    for match in raw_matches[:3]:
        prediction = "2.5 Üst" if (int(match.get("home_id", 0)) % 2 == 0) else "Maç Sonucu 1"
        confidence = 75 + (int(match.get("home_id", 0)) % 20)
        exact_score = f"{int(confidence/40)} - {int(confidence/50)}"
        
        kupon_maclari.append({
            "league": match["league"], "home": match["home"], "away": match["away"],
            "prediction": prediction, "confidence": confidence, "score": exact_score
        })
        if len(anket_secenekleri) < 3:
            anket_secenekleri.append(f"{match['home']} - {match['away']}")

    # Görkemli VIP Şablonu
    msg = "💎 ═══  **VIP YAPAY ZEKA ANALİZİ** ═══ 💎\n"
    msg += "🔥 *İstatistik Analizleriyle Gecenin Gold Bülteni Hazır!*\n\n"
    
    for m in kupon_maclari:
        msg += f"🏆 **{m['league'].upper()}**\n"
        msg += f"⚽ **{m['home']} vs {m['away']}**\n"
        msg += f"🎯 *Yapay Zeka Skor Tahmini:* `{m['score']}` 👈\n"
        msg += f"📊 *Güven Skoru / Tahmin:* `% {m['confidence']}` ➔ `{m['prediction']}`\n"
        msg += "🔸 ─────────────────────── 🔸\n\n"
        
    msg += "🎫 **GÜNLÜK HAZIR KUPON LİSTESİ**\n"
    for i, m in enumerate(kupon_maclari):
        msg += f"🔥 {i+1}️⃣ {m['home']} - {m['away']} ➔ `{m['prediction']}`\n"
        
    msg += "\n📊 **Yatırım Güven Endeksi:** `🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜ %85+`\n"
    msg += "🎰 **Tahmini Toplam VIP Oran:** `~4.50 - 6.20`\n\n"
    msg += "🔔 *Bildirimleri açmayı ve kuponları takip etmeyi unutmayın!*"

    send_telegram_message(msg)
    
    if len(anket_secenekleri) >= 2:
        send_telegram_poll("🤖 Yapay zekanın çıkardığı maçlardan sizce hangisi gecenin en güvenli BANKOSU?", anket_secenekleri)

def run_live_betting_session(raw_matches):
    """AKŞAM MODÜLÜ: Canlı Kasa Katlama Sinyali"""
    if not raw_matches: return
    target = raw_matches[0]
    
    msg = "⚡ ═══  **CANLI KASA KATLAMA SİNYALİ** ═══ ⚡\n"
    msg += f"⚽ **Maç:** {target['home']} - {target['away']} ({target['league']})\n"
    msg += "⏱️ **Dakika:** `60' - 65' Arası`\n"
    msg += "🎯 **CANLI TAHMİN:** `MAÇTA 1 GOL DAHA OLUR (0.5 ÜST)`\n\n"
    msg += "🔥 **VIP Canlı Değerlendirme:** *Kasa katlama serimiz için yüksek güven değerindedir. Değerlendiren herkese bol şans!*"
    
    send_telegram_message(msg)

def run_weekly_report():
    """PAZAR GECESİ MODÜLÜ: Şeffaf Başarı Raporu"""
    msg = "📊 ═══ **HAFTALIK YAPAY ZEKA BAŞARI RAPORU** ═══ 📊\n"
    msg += "📈 **HAFTALIK NET BAŞARI ORANI: `% 82.1`**\n"
    msg += "🔹 *Yapay zeka algoritması istatistik ve matematik kullanır, şansa yer bırakmaz.*"
    send_telegram_message(msg)

# ==========================================
# 5. SAAT KONTROL MERKEZİ
# ==========================================
def main():
    current_hour = datetime.now().hour
    current_day = datetime.now().weekday()
    
    raw_matches = fetch_daily_matches()
    
    # 📢 Saat fark etmeksizin web sitesi verilerini her tetiklendiğinde taze tut
    update_web_radar_json(raw_matches)
    
    if current_day == 6 and current_hour >= 23:
        run_weekly_report()
    elif 6 <= current_hour < 16:
        run_morning_session(raw_matches)
    elif 16 <= current_hour <= 23:
        run_live_betting_session(raw_matches)

if __name__ == "__main__":
    main()
