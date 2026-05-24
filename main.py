import time

from api import get_matches
from analyzer import analyze_match
from sender import send_message, send_panel

sent_matches = set()

MAX_MATCHES = 15


def main():

    # 🔥 BURASI ÖNEMLİ
    send_message("🚀 PRO IDDAA BOT AKTİF")
    send_panel()

    while True:

        try:

            matches = get_matches()

            print(f"TOPLAM MAÇ: {len(matches)}")

            count = 0

            for match in matches:

                if count >= MAX_MATCHES:
                    break

                fixture_id = match["fixture"]["id"]

                if fixture_id in sent_matches:
                    continue

                result = analyze_match(match)

                if result:

                    send_message(result)

                    sent_matches.add(fixture_id)

                    count += 1

                    time.sleep(3)

            if len(sent_matches) > 500:
                sent_matches.clear()

            print("10 DK BEKLEME")

            time.sleep(600)

        except Exception as e:

            print("MAIN ERROR:", e)

            time.sleep(30)


if __name__ == "__main__":
    main()
