import time

from telegram.ext import Updater, CallbackQueryHandler

from api import get_matches
from analyzer import analyze_match
from sender import send_message, send_panel
from panel import handle_buttons

sent_matches = set()


def main():

    send_message("🚀 PRO BOT AKTİF")

    send_panel()

    updater = Updater("TELEGRAM_BOT_TOKEN", use_context=True)

    dp = updater.dispatcher

    # 🔥 BUTONLAR AKTİF
    dp.add_handler(CallbackQueryHandler(handle_buttons))

    updater.start_polling()

    while True:

        try:

            matches = get_matches()

            count = 0

            for m in matches:

                if count >= 15:
                    break

                mid = m["fixture"]["id"]

                if mid in sent_matches:
                    continue

                result = analyze_match(m)

                if result:

                    send_message(result)

                    sent_matches.add(mid)

                    count += 1

                    time.sleep(3)

            time.sleep(600)

        except Exception as e:
            print(e)
            time.sleep(30)


if __name__ == "__main__":
    main()
