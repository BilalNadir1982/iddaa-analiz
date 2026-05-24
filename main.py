from sender import send_panel
send_message("🚀 PRO IDDAA ANALİZ BOT AKTİF")
send_panel()
import time

from api import get_matches
from analyzer import analyze_match
from sender import send_message

# =========================================
# GÖNDERİLEN MAÇLAR
# =========================================

sent_matches = set()

# =========================================
# MAX MESAJ
# =========================================

MAX_MATCHES = 15

# =========================================
# ANA BOT
# =========================================

def main():

    send_message("🚀 PRO IDDAA ANALİZ BOT AKTİF")

    while True:

        try:

            # =====================================
            # MAÇLARI ÇEK
            # =====================================

            matches = get_matches()

            print(f"TOPLAM ÇEKİLEN MAÇ: {len(matches)}")

            if len(matches) == 0:

                print("MAÇ BULUNAMADI")

                time.sleep(60)

                continue

            # =====================================
            # SAYAÇ
            # =====================================

            count = 0

            # =====================================
            # MAÇ DÖNGÜSÜ
            # =====================================

            for match in matches:

                try:

                    # =================================
                    # MAX MESAJ LİMİTİ
                    # =================================

                    if count >= MAX_MATCHES:
                        break

                    fixture_id = match["fixture"]["id"]

                    # =================================
                    # AYNI MAÇI TEKRAR GÖNDERME
                    # =================================

                    if fixture_id in sent_matches:
                        continue

                    # =================================
                    # ANALİZ
                    # =================================

                    result = analyze_match(match)

                    if result:

                        send_message(result)

                        print("MESAJ GÖNDERİLDİ")

                        sent_matches.add(fixture_id)

                        count += 1

                        time.sleep(3)

                except Exception as e:

                    print("MATCH ERROR:", e)

            # =====================================
            # TEMİZLEME
            # =====================================

            if len(sent_matches) > 500:

                sent_matches.clear()

                print("SENT MATCHES TEMİZLENDİ")

            # =====================================
            # DÖNGÜ BEKLEME
            # =====================================

            print("10 DAKİKA BEKLENİYOR...")

            time.sleep(600)

        except Exception as e:

            print("MAIN ERROR:", e)

            time.sleep(30)

# =========================================
# START
# =========================================

if __name__ == "__main__":
    main()
