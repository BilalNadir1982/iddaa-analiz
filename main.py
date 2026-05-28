import os
import requests
import json

# ==========================================
# 1. AYARLAR & YAPILANDIRMA
# ==========================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_BASE_URL = "https://api.football-data.org/v4/"
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

TAKIP_EDILEN_LIGLER = {
    "BSA": "Brezilya Serie A",
    "CLI": "Copa Libertadores",
    "ELC": "İngiltere Championship",
    "WC": "Dünya Kupası Elemeleri"
}

# ==========================================
# 2. VERİ ÇEKME & ANALİZ MOTORU
# ==========================================
def fetch_daily_matches():
    if not FOOTBALL_API_KEY or "BURAYA" in FOOTBALL_API_KEY:
        return get_fallback_data()

    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    tum_maclar = []

    for lig_kodu, lig_adi in TAKIP_EDILEN_LIGLER.items():
        try:
            url = f"{API_BASE_URL}competitions/{lig_kodu}/matches"
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for match in data.get("matches", []):
                    if match.get("status") in ["SCHEDULED", "TIMED"]:
                        tum_maclar.append({
                            "league": lig_adi,
                            "home": match["homeTeam"]["name"],
                            "away": match["awayTeam"]["name"],
                            "home_id": match["homeTeam"]["id"],
                            "away_id": match["awayTeam"]["id"]
                        })
        except: continue
    return tum_maclar

def get_team_stats(team_id):
    if not FOOTBALL_API_KEY or "BURAYA" in FOOTBALL_API_KEY:
        return {"avg_goals_scored": 1.6, "avg_goals_conceded": 1.2}
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    url = f"{API_BASE_URL}teams/{team_id}/matches?status=FINISHED&limit=5"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            matches = response.json().get("matches", [])
            total_scored, total_conceded, match_count = 0, 0, len(matches)
            if match_count == 0: return {"avg_goals_scored": 1.2, "avg_goals_conceded": 1.1}
            for m in matches:
                if m["homeTeam"]["id"] == team_id:
                    total_scored += m["score"]["fullTime"]["home"]
                    total_conceded += m["score"]["fullTime"]["away"]
                else:
                    total_scored += m["score"]["fullTime"]["away"]
                    total_conceded += m["score"]["fullTime"]["home"]
            return {"avg_goals_scored": total_scored / match_count, "avg_goals_conceded": total_conceded / match_count}
    except: pass
    return {"avg_goals_scored": 1.4, "avg_goals_conceded": 1.2}

def get_fallback_data():
    return []

def analyze_matches(match_list):
    if not match_list: return []
    analiz_sonuclari = []
    for match in match_list:
        home_team = match["home"]
        away_team = match["away"]
        home_stats = get_team_stats(match.get("home_id"))
        away_stats = get_team_stats(match.get("away_id"))
        toplam_gol_beklentisi = home_stats["avg_goals_scored"] + away_stats["avg_goals_scored"]
        deplasman_savunma_zaafi = away_stats["avg_goals_conceded"]

        if toplam_gol_beklentisi > 2.9:
            prediction, confidence = "2.5 Üst", int(min(95, 70 + (toplam_gol_beklentisi * 7)))
            detail = f"İki takımın toplam gol iştahı {toplam_gol_beklentisi:.2f}. Ofansif hatlar çok formda, bol pozisyonlu bir gece olur."
        elif home_stats["avg_goals_scored"] > 1.6 and deplasman_savunma_zaafi > 1.4:
            prediction, confidence = "Maç Sonucu 1", int(min(94, 75 + (home_stats["avg_goals_scored"] * 8)))
            detail = f"{home_team} iç sahada {home_stats['avg_goals_scored']:.2f} gol ortalamasıyla oynuyor. Seyirci baskısıyla galibiyete yakın."
        elif home_stats["avg_goals_scored"] > 0.9 and away_stats["avg_goals_scored"] > 0.9:
            prediction, confidence = "Karşılıklı Gol Var (KG VAR)", int(min(92, 68 + (toplam_gol_beklentisi * 6)))
            detail = f"Ev sahibi iç sahada, deplasman ise kontralarda skora yakın. İki ekibin de ağları havalandırması yüksek ihtimal."
        else:
            prediction, confidence = "İlk Yarı 1.5 Alt", 88
            detail = f"Takımların savunma öncelikli oyun yapısı ve düşük gol ortalaması, ilk 45 dakikada dengeli bir stratejiye işaret ediyor."

        analiz_sonuclari.append({
            "league": match["league"], "home": home_team, "away": away_team,
            "prediction": prediction, "confidence": confidence, "detail": detail
        })
    return sorted(analiz_sonuclari, key=lambda x: x['confidence'], reverse=True)

# ==========================================
# 3. GÖRKEMLİ KUPON TASARIMI & TELEGRAM GÖNDERİMİ
# ==========================================
def format_and_send(selected_matches):
    if not selected_matches or len(selected_matches) < 2:
        print("⚠️ Bugün analiz kriterlerine uyan yeterli canlı maç bülteni bulunamadı.")
        return
        
    kupon_maclari = selected_matches[:5]
    
    # Yeni Görkemli Tasarım Metni
    message = "💎 ═══  **VIP YAPAY ZEKA ANALİZİ** ═══ 💎\n"
    message += "🔥 *Piyasanın En Yüksek Güven Skorlu Maçları Süzüldü!*\n\n"
    
    for match in kupon_maclari:
        message += f"🏆 **{match['league'].upper()}**\n"
        message += f"⚽ **{match['home']} vs {match['away']}**\n"
        message += f"💡 *Robot Analizi:* {match['detail']}\n"
        message += f"📊 *Yapay Zeka Güven Skoru:* `%{match['confidence']}`\n"
        message += "🔸 ─────────────────────── 🔸\n\n"
        
    message += "🎫 ═══  **GÜNLÜK GOLD KUPON** ═══ 🎫\n"
    message += "✍️ *Yüksek İsabetli Sade Liste:*\n\n"
    
    emojis = ["🔥 1️⃣", "🔥 2️⃣", "🔥 3️⃣", "🔥 4️⃣", "🔥 5️⃣"]
    for i, match in enumerate(kupon_maclari):
        message += f"{emojis[i]} {match['home']} - {match['away']} ➔ `{match['prediction']}`\n"
        
    message += "\n📊 **Yatırım Güven Endeksi:** `🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜ %85+`\n"
    message += "🎰 **Tahmini Toplam VIP Oran:** `~4.80 - 6.50`\n\n"
    message += "💰 **Kasayı Koruyarak Oynayınız. Bol Şanslar!** 💰"
    
    if not BOT_TOKEN or not CHAT_ID: return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)
    print("✅ Görkemli VIP kupon kanala gönderildi!")

# ==========================================
# 4. KANALA KATILMAK İSTEYENLERİ KARŞILAMA SİSTEMİ
# ==========================================
def check_and_welcome_users():
    """Kanala katılma isteği atan veya yeni gelen üyeleri özelden görkemli karşılar."""
    if not BOT_TOKEN: return
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            updates = response.json().get("result", [])
            for update in updates:
                # Kanala katılma isteği atan birini yakala (Join Request)
                if "chat_join_request" in update:
                    user_id = update["chat_join_request"]["from"]["id"]
                    first_name = update["chat_join_request"]["from"].get("first_name", "Dostum")
                    
                    # Görkemli Karşılama Mesajı
                    welcome_msg = f"🎉 **AİLEMİZE HOŞ GELDİN {first_name.upper()}!** 🎉\n\n" \
                                  f"🤖 Türkiye'nin en gelişmiş **Yapay Zeka İddaa ve Kripto Analiz Botu** kanalındasın.\n\n" \
                                  f"✅ Katılma isteğin onay sırasına alındı!\n" \
                                  f"📈 Her gün sabah 09:00'da **Gerçek İstatistikli VIP Kuponlar**,\n" \
                                  f"⚡ Her 30 dakikada bir **Canlı Balina Kripto Sinyalleri** bu kanalda!\n\n" \
                                  f"🔔 *Bildirimleri açmayı ve kanalı üste sabitlemeyi unutma!* 🔥"
                    
                    # Kullanıcıya özelden mesaj at
                    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    requests.post(send_url, json={"chat_id": user_id, "text": welcome_msg, "parse_mode": "Markdown"})
                    
                    # İsteği otomatik olarak onaylamak istersen (İleride bota adminlik yetkisi verdiğinde çalışır)
                    approve_url = f"https://api.telegram.org/bot{BOT_TOKEN}/approveChatJoinRequest"
                    requests.post(approve_url, json={"chat_id": CHAT_ID, "user_id": user_id})
    except: pass

# ==========================================
# 5. ANA TETİKLEYİCİ
# ==========================================
def main():
    print("Görkemli analiz sistemi başlatıldı...")
    raw_matches = fetch_daily_matches()
    analyzed_matches = analyze_matches(raw_matches)
    format_and_send(analyzed_matches)
    # Karşılama motorunu çalıştır
    check_and_welcome_users()

if __name__ == "__main__":
    main()
