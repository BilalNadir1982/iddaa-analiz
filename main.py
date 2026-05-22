import asyncio
import sys
from datetime import datetime

from config import BOT_TOKEN, CHANNEL_ID
from scraper import get_iddaa_matches
from analyzer import analyze_matches
from sender import send_to_channel

async def run_analysis():
    print(f"[{datetime.now()}] İddaa analizi başlatılıyor...")
    
    matches = get_iddaa_matches()
    good_bets = analyze_matches(matches)
    
    if not good_bets:
        message = "🔍 Bugün kaliteli bahis önerisi bulunamadı."
    else:
        message = f"🔥 **Günün İddaa Analizi** 🔥\n"
        message += f"📅 {datetime.now().strftime('%d %B %Y, %A')}\n\n"
        
        for bet in good_bets:
            message += f"⏰ **{bet['time']}** | {bet['league']}\n"
            message += f"⚽ {bet['match']}\n"
            message += f"💡 **{bet['tip']}** @ **{bet['odds']:.2f}**\n"
            message += f"📌 {bet['reason']}\n\n"
        
        message += "⚠️ Bu sadece analizdir. Sorumlu oynayınız."

    await send_to_channel(BOT_TOKEN, CHANNEL_ID, message)
    print("✅ Analiz tamamlandı ve kanala gönderildi.")

if __name__ == "__main__":
    if "--run-once" in sys.argv:
        # GitHub Actions için tek seferlik çalıştırma
        asyncio.run(run_analysis())
    else:
        # Yerel makinede test etmek için
        print("Yerel modda çalıştırıyorsun. Scheduler devre dışı.")
        asyncio.run(run_analysis())
        print("RUN ONCE STARTED")
        import os

if os.path.exists("sent.txt"):
    print("Already sent today, exiting")
    exit()

open("sent.txt", "w").write("sent")
