import time
from api import get_matches
from analyzer import analyze_match
from sender import send_telegram

send_telegram("🚀 İDDIA PRO BOT AKTİF")

while True:

    try:

        matches = get_matches()

        print(matches)

        if not matches:
            send_telegram("⚠️ AKTİF MAÇ BULUNAMADI")
            time.sleep(300)
            continue

        for match in matches:

            analysis = analyze_match(match)

            if analysis is None:
                continue

            msg = f"""
🔥 CANLI MAÇ ANALİZİ

🏠 {match['home']}
🆚
🚩 {match['away']}

⚽ SKOR:
{match['home_goals']} - {match['away_goals']}

📊 ANALİZ:
{analysis['prediction']}

🎯 GÜVEN:
%{analysis['confidence']}

💎 MARKET:
{analysis['market']}
"""

            send_telegram(msg)

            time.sleep(5)

        time.sleep(300)

    except Exception as e:

        print(e)

        send_telegram(f"❌ HATA: {e}")

        time.sleep(60)
