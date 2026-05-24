import time

from api import get_matches
from analyzer import analyze_match
from sender import send_message

sent_matches = set()

def main():

    send_message("🚀 IDDAA BOT AKTİF")

    while True:

        try:

            matches = get_matches()

            print("ÇEKİLEN MAÇ:", len(matches))

            if len(matches) == 0:
                print("MAÇ YOK")

            for match in matches:

                fixture_id = match["fixture"]["id"]

                if fixture_id in sent_matches:
                    continue

                result = analyze_match(match)

                if result:

                    send_message(result)

                    sent_matches.add(fixture_id)

                    time.sleep(3)

            print("10 DK BEKLENİYOR")

            time.sleep(600)

        except Exception as e:

            print("MAIN ERROR:", e)

            time.sleep(30)

if __name__ == "__main__":
    main()
