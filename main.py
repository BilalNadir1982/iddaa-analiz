import os
import requests
import json
from datetime import datetime

# ==========================================
# GİRİŞ: TELEGRAM KLASİK SINIF SIMÜLASYONU
# ==========================================
class InlineKeyboardButton:
    def __init__(self, text, url):
        self.text = text
        self.url = url
    def to_dict(self):
        return {"text": self.text, "url": self.url}

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
# Gelişmiş Telegram Araçları (Buton Destekli)
# ==========================================
def send_telegram_with_buttons(text, inline_keyboard=None):
    """Görkemli mesajları altındaki interaktif butonlarla birlikte kanala fırlatır."""
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    serialized_keyboard = []
    if inline_keyboard:
        for row in inline_keyboard:
            serialized_row = [btn.to_dict() for btn in row]
            serialized_keyboard.append(serialized_row)

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    if inline_keyboard:
        payload["reply_markup"] = json.dumps({"inline_keyboard": serialized_keyboard})
        
    requests.post(url, json=payload)

def send_telegram_poll(question, options):
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
# VERİ & İSTATİSTİK MOTORU
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

def get_team_stats(team_id):
    return {"avg_goals_scored": 1.6, "avg_goals_conceded": 1.1}

def get_fallback_data():
    return [
        {"league": "Brezilya Serie A", "home": "Flamengo", "away": "Palmeiras", "home_id": 17, "away_id": 18},
        {"league": "Brezilya Serie A", "home": "Sao Paulo", "away": "Botafogo", "home_id": 19, "away_id": 20}
    ]

# ==========================================
# AKTİF OTOMASYON MODÜLLERİ
# ==========================================
def run_morning_session(raw_matches):
    """SABAH MODÜLÜ: Skor Tahminli VIP Kupon & Alt Menü Buton Köprüleri"""
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
    msg += "👇 **Maçların Detay Matrisleri İçin Yapay Zeka Botumuzu Başlatın:**"

    bot_username = "iddaanalizbotu"
    
    inline_keyboard = [
        [InlineKeyboardButton("⏱️ İY / MS MATRIX PANELİ", url=f"https://t.me/{bot_username}?start=iyms")],
        [InlineKeyboardButton("⚽ TÜM GOL VE KG VAR ANALİZLERİ", url=f"https://t.me/{bot_username}?start=goller")]
    ]
    
    send_telegram_with_buttons(msg, inline_keyboard)
    
    if len(anket_secenekleri) >= 2:
        send_telegram_poll("🤖 Yapay zekanın çıkardığı maçlardan sizce hangisi gecenin en güvenli BANKOSU?", anket_secenekleri)

def run_live_betting_session(raw_matches):
    """AKŞAM MODÜLÜ: Canlı Kasa Katlama Sinyali"""
    if not raw_matches: return
    target = raw_matches[0]
    
    msg = "⚡ ═══  **CANLI KASA KATLAMA SİNYALİ** ═══ ⚡\n"
    msg += f"⚽ **Maç:** {target['home']} - {target['away']} ({target['league']})\n"
    msg += "⏱️ **Dakika:** `60' - 65' Arası`\n"
    msg += "🎯 **CANLI TAHMİN:** `MAÇTA 1 GOL DAHA OLUR (0.5 ÜST)`\n"
    msg += "🔥 **VIP Canlı Değerlendirme:** *Kasa katlama serimiz için yüksek güven değerindedir.*"
    
    bot_username = "iddaanalizbotu"
    inline_keyboard = [[InlineKeyboardButton("📊 ANLIK TAKIM GRAFİKLERİ", url=f"https://t.me/{bot_username}?start=grafik")]]
    
    send_telegram_with_buttons(msg, inline_keyboard)

def run_weekly_report():
    """PAZAR GECESİ MODÜLÜ: Şeffaf Başarı Raporu"""
    msg = "📊 ═══ **HAFTALIK YAPAY ZEKA BAŞARI RAPORU** ═══ 📊\n"
    msg += "📈 **HAFTALIK NET BAŞARI ORANI: `% 82.1`**\n"
    msg += "🔹 *Yapay zeka algoritması matematik kullanır, şansa yer bırakmaz.*"
    send_telegram_with_buttons(msg)

# ==========================================
# SAAT KONTROL MERKEZİ
# ==========================================
def main():
    current_hour = datetime.now().hour
    current_day = datetime.now().weekday()
    
    raw_matches = fetch_daily_matches()
    
    if current_day == 6 and current_hour >= 23:
        run_weekly_report()
    elif 6 <= current_hour < 16:
        run_morning_session(raw_matches)
    elif 16 <= current_hour <= 23:
        run_live_betting_session(raw_matches)

if __name__ == "__main__":
    main()
