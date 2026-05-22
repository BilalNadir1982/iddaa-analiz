import asyncio
import sys
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

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
        message += f"📅 {datetime.now().strftime('%d %B %Y')}\n\n"
        
        for bet in good_bets:
            message += f"**{bet['time']}** | {bet['league']}\n"
            message += f"{bet['match']}\n"
            message += f"💡 **{bet['tip']}** @ {bet['odds']:.2f}\n"
            message += f"📌 {bet['reason']}\n\n"
        
        message += "⚠️ Bu sadece analizdir. Sorumlu oynayınız."

    await send_to_channel(BOT_TOKEN, CHANNEL_ID, message)

if __name__ == "__main__":
    if "--run-once" in sys.argv:
        # GitHub Actions için tek seferlik çalıştırma
        asyncio.run(run_analysis())
    else:
        # Yerel geliştirme için sürekli çalışma
        scheduler = AsyncIOScheduler()
        scheduler.add_job(run_analysis, 'cron', hour=12, minute=0)
        scheduler.add_job(run_analysis, 'cron', hour=18, minute=30)
        print("🤖 Bot çalışıyor...")
        scheduler.start()
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
