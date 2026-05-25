# =========================================
# main.py
# =========================================

import time
from api import get_matches
from analyzer import analyze_match
from sender import send_telegram

send_telegram("🚀 PRO İDDIA AI ENGINE AKTİF")

while True:

    try:

        matches = get_matches()

        coupons = []

        for match in matches:

            analysis = analyze_match(match)

            if analysis["coupon"]:

                coupons.append(analysis)

                msg = f"""
🔥 BANKO MAÇ

🏆 Lig:
{analysis['league']}

🏠 {analysis['home']}
🆚
🚩 {analysis['away']}

📊 Market:
{analysis['market']}

🧠 AI Analiz:
{analysis['prediction']}

🎯 Güven:
%{analysis['confidence']}

⚽ AI Skor Tahmini:
{analysis['score_prediction']}
"""

                send_telegram(msg)

                time.sleep(3)

        # =================================
        # OTOMATIK 3'LU KUPON
        # =================================

        if len(coupons) >= 3:

            c1 = coupons[0]
            c2 = coupons[1]
            c3 = coupons[2]

            coupon_msg = f"""
💎 OTOMATIK 3'LÜ KUPON

1️⃣ {c1['home']} vs {c1['away']}
➡️ {c1['market']}

2️⃣ {c2['home']} vs {c2['away']}
➡️ {c2['market']}

3️⃣ {c3['home']} vs {c3['away']}
➡️ {c3['market']}

🔥 AI GÜVENLİ KUPON
"""

            send_telegram(coupon_msg)

        else:

            send_telegram("⚠️ Yeterli BANKO maç bulunamadı")

        time.sleep(600)

    except Exception as e:

        send_telegram(f"❌ HATA: {e}")

        print(e)

        time.sleep(60)
