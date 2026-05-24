import time
from api import get_matches
from analyzer import analyze_match
from sender import send_message

sent = set()

def main():

    send_message("🚀 İDDIA PRO BOT AKTİF")

    while True:

        try:
            matches = get_matches()

            for m in matches:

                mid = m["fixture"]["id"]

                if mid in sent:
                    continue

                result = analyze_match(m)

                if result:
                    send_message(result)
                    sent.add(mid)

            time.sleep(600)

        except Exception as e:
            print("ERROR:", e)
            time.sleep(30)


if __name__ == "__main__":
    main()
